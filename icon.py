import os
from PIL import Image, ImageDraw, ImageFont

def create_icon():
    # Create a new image with a white background
    size = (512, 512)
    image = Image.new('RGB', size, 'white')
    draw = ImageDraw.Draw(image)
    
    # Draw a stylized document
    margin = 100
    doc_coords = [(margin, margin), (size[0]-margin, size[1]-margin)]
    draw.rectangle(doc_coords, outline='#2196F3', width=20)
    
    # Draw a pen
    pen_width = 40
    pen_coords = [
        (size[0]-margin*1.5, size[1]-margin*1.5),
        (margin*1.5, margin*1.5)
    ]
    draw.line(pen_coords, fill='#2196F3', width=pen_width)
    
    # Save as PNG and ICO
    image.save('icon.png')
    image.save('icon.ico')

if __name__ == '__main__':
    create_icon()
