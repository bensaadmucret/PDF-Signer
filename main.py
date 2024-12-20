import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout,
                           QWidget, QFileDialog, QLabel, QGroupBox, QLineEdit, QCheckBox,
                           QSpinBox, QScrollArea, QMessageBox)
from PyQt6.QtCore import Qt, QPoint
from PyQt6.QtGui import QPixmap, QPainter, QPen, QColor, QImage, QPainterPath
import fitz  # PyMuPDF
import os
from datetime import datetime
import traceback

class SignatureWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedSize(300, 150)
        self.setStyleSheet("background-color: white; border: 1px solid black;")
        self.signature_path = QPainterPath()
        self.drawing = False
        self.last_point = None
        self.signature_points = []

    def has_signature(self):
        return len(self.signature_points) > 0

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.drawing = True
            self.last_point = event.pos()
            self.signature_points.append([])
            self.signature_points[-1].append(event.pos())

    def mouseMoveEvent(self, event):
        if self.drawing:
            current_point = event.pos()
            self.signature_points[-1].append(current_point)
            self.update()
            self.last_point = current_point

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.drawing = False

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        
        # Fond blanc
        painter.fillRect(self.rect(), Qt.GlobalColor.white)
        
        # Dessiner la ligne de base
        painter.setPen(QPen(QColor(200, 200, 200), 1, Qt.PenStyle.DashLine))
        baseline_y = self.height() - 30
        painter.drawLine(10, baseline_y, self.width() - 10, baseline_y)
        
        # Dessiner la signature
        painter.setPen(QPen(Qt.GlobalColor.black, 2, Qt.PenStyle.SolidLine))
        for stroke in self.signature_points:
            if len(stroke) > 1:
                for i in range(len(stroke) - 1):
                    painter.drawLine(stroke[i], stroke[i + 1])

    def clear_signature(self):
        self.signature_points = []
        self.update()

    def get_signature_image(self):
        image = QImage(self.size(), QImage.Format.Format_ARGB32)
        image.fill(Qt.GlobalColor.white)
        painter = QPainter(image)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        
        # Dessiner la signature
        painter.setPen(QPen(Qt.GlobalColor.black, 2, Qt.PenStyle.SolidLine))
        for stroke in self.signature_points:
            if len(stroke) > 1:
                for i in range(len(stroke) - 1):
                    painter.drawLine(stroke[i], stroke[i + 1])
        
        painter.end()
        return image

class PDFSignerApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PDF Signer")
        self.setGeometry(100, 100, 1200, 800)
        
        # Create main widget and layout
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        main_layout = QHBoxLayout(main_widget)
        
        # Left panel for controls
        left_panel = QWidget()
        left_layout = QVBoxLayout(left_panel)
        left_panel.setMaximumWidth(400)
        
        # Create widgets
        self.status_label = QLabel("Aucun fichier sélectionné")
        self.select_button = QPushButton("Sélectionner un PDF")
        
        # Ajout des champs de signature
        self.signature_group = QGroupBox("Options de signature")
        signature_layout = QVBoxLayout()
        
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Votre nom")
        
        self.read_approved_checkbox = QCheckBox("Lu et approuvé")
        self.date_checkbox = QCheckBox("Ajouter la date")
        self.date_checkbox.setChecked(True)
        
        # Zone de signature manuscrite
        signature_label = QLabel("Signature manuscrite:")
        self.signature_widget = SignatureWidget()
        clear_signature_button = QPushButton("Effacer la signature")
        clear_signature_button.clicked.connect(self.signature_widget.clear_signature)
        
        # Position controls
        position_group = QGroupBox("Position de la signature")
        position_layout = QVBoxLayout()
        
        page_layout = QHBoxLayout()
        page_layout.addWidget(QLabel("Page:"))
        self.page_spin = QSpinBox()
        self.page_spin.setMinimum(1)
        self.page_spin.valueChanged.connect(self.update_preview)
        page_layout.addWidget(self.page_spin)
        
        position_layout.addLayout(page_layout)
        position_group.setLayout(position_layout)
        
        signature_layout.addWidget(QLabel("Nom :"))
        signature_layout.addWidget(self.name_input)
        signature_layout.addWidget(self.read_approved_checkbox)
        signature_layout.addWidget(self.date_checkbox)
        signature_layout.addWidget(signature_label)
        signature_layout.addWidget(self.signature_widget)
        signature_layout.addWidget(clear_signature_button)
        self.signature_group.setLayout(signature_layout)
        
        self.sign_button = QPushButton("Signer le PDF")
        self.sign_button.setEnabled(False)
        
        # Add widgets to left layout
        left_layout.addWidget(self.status_label)
        left_layout.addWidget(self.select_button)
        left_layout.addWidget(self.signature_group)
        left_layout.addWidget(position_group)
        left_layout.addWidget(self.sign_button)
        left_layout.addStretch()
        
        # Right panel for PDF preview
        right_panel = QWidget()
        right_layout = QVBoxLayout(right_panel)
        
        # Preview area
        self.preview_scroll = QScrollArea()
        self.preview_label = QLabel()
        self.preview_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.preview_scroll.setWidget(self.preview_label)
        self.preview_scroll.setWidgetResizable(True)
        right_layout.addWidget(self.preview_scroll)
        
        # Add panels to main layout
        main_layout.addWidget(left_panel)
        main_layout.addWidget(right_panel, stretch=1)
        
        # Connect buttons to functions
        self.select_button.clicked.connect(self.select_pdf)
        self.sign_button.clicked.connect(self.sign_pdf)
        
        self.pdf_path = None
        self.pdf_document = None
        self.signature_pos = None
        
        # Mouse tracking for signature placement
        self.preview_label.setMouseTracking(True)
        self.preview_label.mousePressEvent = self.on_preview_click
    
    def show_error(self, message, details=None):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Critical)
        msg.setText(message)
        if details:
            msg.setDetailedText(details)
        msg.setWindowTitle("Erreur")
        msg.exec()
    
    def select_pdf(self):
        try:
            file_name, _ = QFileDialog.getOpenFileName(
                self,
                "Sélectionner un PDF",
                "",
                "PDF Files (*.pdf)"
            )
            if file_name:
                try:
                    if self.pdf_document:
                        self.pdf_document.close()
                    self.pdf_document = fitz.open(file_name)
                    self.pdf_path = file_name
                    self.page_spin.setMaximum(len(self.pdf_document))
                    self.status_label.setText(f"Fichier sélectionné: {os.path.basename(file_name)}")
                    self.sign_button.setEnabled(True)
                    self.update_preview()
                except Exception as e:
                    self.show_error("Erreur lors de l'ouverture du PDF", str(e))
        except Exception as e:
            self.show_error("Erreur lors de la sélection du fichier", str(e))
    
    def update_preview(self):
        try:
            if not self.pdf_document:
                return
                
            page_num = self.page_spin.value() - 1
            page = self.pdf_document[page_num]
            
            # Render page to image
            pix = page.get_pixmap(matrix=fitz.Matrix(1, 1))
            img = QImage(pix.samples, pix.width, pix.height, pix.stride, QImage.Format.Format_RGB888)
            pixmap = QPixmap.fromImage(img)
            
            # Scale the pixmap to fit the preview area while maintaining aspect ratio
            scaled_pixmap = pixmap.scaled(
                self.preview_scroll.size(),
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation
            )
            
            # Draw signature position if set
            if self.signature_pos:
                painter = QPainter(scaled_pixmap)
                painter.setPen(QPen(QColor(255, 0, 0), 2))
                painter.drawRect(self.signature_pos[0]-100, self.signature_pos[1]-50, 200, 100)
                painter.end()
            
            self.preview_label.setPixmap(scaled_pixmap)
            
        except Exception as e:
            self.show_error("Erreur lors de la prévisualisation", traceback.format_exc())
    
    def on_preview_click(self, event):
        self.signature_pos = (event.pos().x(), event.pos().y())
        self.update_preview()
    
    def sign_pdf(self):
        if not self.pdf_path or not self.signature_pos:
            self.status_label.setText("Veuillez sélectionner un emplacement pour la signature")
            return
            
        try:
            # Open the original PDF
            output_pdf = fitz.open(self.pdf_path)
            page = output_pdf[self.page_spin.value() - 1]
            
            # Calculate signature position
            page_width = page.rect.width
            page_height = page.rect.height
            
            # Get the preview label's actual content rect (where the PDF is displayed)
            preview_pixmap = self.preview_label.pixmap()
            if preview_pixmap:
                preview_width = preview_pixmap.width()
                preview_height = preview_pixmap.height()
                
                # Calculate the scale factors
                scale_x = page_width / preview_width
                scale_y = page_height / preview_height
                
                # Convert click coordinates to PDF coordinates
                x = self.signature_pos[0] * scale_x
                y = self.signature_pos[1] * scale_y
                
                # Calculate signature box dimensions in PDF units
                box_width = 200 * scale_x
                box_height = 100 * scale_y
                
                # Create rectangle for signature area
                rect = fitz.Rect(
                    x - box_width/2,
                    y - box_height/2,
                    x + box_width/2,
                    y + box_height/2
                )
                
                # Add white background
                page.draw_rect(rect, color=(1, 1, 1), fill=(1, 1, 1))
                
                name = self.name_input.text().strip()
                
                if self.signature_widget.has_signature():
                    # Si une signature manuscrite existe, l'utiliser
                    signature_image = self.signature_widget.get_signature_image()
                    temp_image_path = "temp_signature.png"
                    signature_image.save(temp_image_path)
                    page.insert_image(rect, filename=temp_image_path)
                    os.remove(temp_image_path)
                elif name:
                    # Sinon, utiliser le nom comme signature avec une police élégante
                    font_size = min(20 * scale_x, 40)  # Taille de police adaptative
                    page.insert_text(
                        (x - box_width/3, y + box_height/4),
                        name,
                        fontname="Times-Italic",  # Police élégante
                        fontsize=font_size,
                        color=(0, 0, 0)
                    )
                
                # Add text below signature box
                text_y = y + box_height/2 + 15
                text_x = x - box_width/2
                font_size = min(11 * scale_x, 11)  # Taille de police pour le texte
                
                if self.read_approved_checkbox.isChecked():
                    page.insert_text(
                        (text_x, text_y),
                        "Lu et approuvé",
                        fontname="Helvetica",
                        fontsize=font_size,
                        color=(0, 0, 0)
                    )
                    text_y += 15 * scale_y
                
                if self.date_checkbox.isChecked():
                    current_date = datetime.now().strftime("%d/%m/%Y")
                    page.insert_text(
                        (text_x, text_y),
                        f"Date : {current_date}",
                        fontname="Helvetica",
                        fontsize=font_size,
                        color=(0, 0, 0)
                    )
                
                # Save the signed PDF
                output_path = os.path.splitext(self.pdf_path)[0] + '_signed.pdf'
                output_pdf.save(output_path)
                output_pdf.close()
                
                self.status_label.setText("PDF signé avec succès!")
                QMessageBox.information(self, "Succès", f"Le PDF a été signé avec succès et sauvegardé sous :\n{output_path}")
            else:
                raise Exception("Erreur: Impossible de déterminer la taille de la prévisualisation")
            
        except Exception as e:
            self.show_error("Erreur lors de la signature", traceback.format_exc())

def main():
    app = QApplication(sys.argv)
    window = PDFSignerApp()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
