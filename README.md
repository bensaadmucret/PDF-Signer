# PDF Signer

Une application de bureau simple et élégante pour signer vos documents PDF. Développée avec Python et PyQt6.

## Avantages de la signature locale 🔒

- **Confidentialité maximale** : Vos documents restent sur votre ordinateur, aucun envoi vers des serveurs externes
- **Sécurité** : Pas de risque de fuite de données, tout est traité localement
- **Rapidité** : Pas besoin de connexion internet, signature instantanée
- **Gratuit** : Aucun abonnement ou frais cachés, contrairement aux services en ligne
- **Hors ligne** : Fonctionne sans connexion internet
- **Pas de limite** : Signez autant de documents que vous voulez
- **Protection des données** : Conforme RGPD car aucune donnée n'est collectée

![Capture d'écran de l'application](screenshot.png)

## Fonctionnalités

- 📝 Signature manuscrite ou textuelle
- 📄 Prévisualisation du PDF en temps réel
- 🖱️ Placement précis de la signature
- ✍️ Option "Lu et approuvé"
- 📅 Ajout automatique de la date
- 🎨 Interface utilisateur moderne et intuitive

## Installation

### Prérequis

- Python 3.9 ou supérieur
- pip (gestionnaire de paquets Python)

### Installation des dépendances

```bash
pip install -r requirements.txt
```

### Lancement de l'application

```bash
python main.py
```

### Installation comme application (macOS)

1. Installez PyInstaller :
```bash
pip install pyinstaller
```

2. Créez l'application :
```bash
pyinstaller PDF_Signer.spec
```

3. L'application se trouve dans le dossier `dist/PDF Signer`

## Utilisation

1. Lancez l'application
2. Cliquez sur "Sélectionner un PDF" pour ouvrir votre document
3. Entrez votre nom
4. Vous pouvez soit :
   - Dessiner votre signature dans la zone prévue
   - Utiliser votre nom comme signature (si aucune signature n'est dessinée)
5. Cochez les options souhaitées ("Lu et approuvé", date)
6. Cliquez sur le PDF à l'endroit où vous souhaitez placer la signature
7. Cliquez sur "Signer le PDF"
8. Le PDF signé sera sauvegardé avec le suffixe "_signed"

## Structure du projet

```
pdf_signer/
├── main.py           # Code principal de l'application
├── icon.py          # Générateur d'icône
├── requirements.txt  # Dépendances Python
├── PDF_Signer.spec  # Configuration PyInstaller
└── README.md        # Documentation
```

## Dépendances principales

- PyQt6 : Interface graphique
- PyMuPDF : Manipulation des PDF
- Pillow : Traitement d'images

## Contribution

Les contributions sont les bienvenues ! Voici comment contribuer :

1. Forkez le projet ([Cliquez ici pour fork](https://github.com/bensaadmucret/PDF-Signer/fork))
2. Clonez votre fork
   ```bash
   git clone https://github.com/votre-username/PDF-Signer.git
   cd PDF-Signer
   ```
3. Créez votre branche de fonctionnalité
   ```bash
   git checkout -b feature/ma-super-fonctionnalite
   ```
4. Committez vos changements
   ```bash
   git add .
   git commit -m 'feat: Ajout de ma super fonctionnalité'
   ```
5. Poussez vers la branche
   ```bash
   git push origin feature/ma-super-fonctionnalite
   ```
6. Ouvrez une Pull Request ([Créer une nouvelle Pull Request](https://github.com/bensaadmucret/PDF-Signer/compare))

### Convention de nommage des commits

Utilisez les préfixes suivants pour vos commits :
- `feat:` pour une nouvelle fonctionnalité
- `fix:` pour une correction de bug
- `docs:` pour la documentation
- `style:` pour le formatage du code
- `refactor:` pour une refactorisation du code
- `test:` pour l'ajout ou la modification de tests
- `chore:` pour la maintenance du code

### Guide de contribution

- Assurez-vous que votre code respecte les standards de codage Python (PEP 8)
- Ajoutez des commentaires pour le code complexe
- Mettez à jour la documentation si nécessaire
- Testez vos modifications avant de soumettre une PR

## Licence

Distribué sous la licence MIT. Voir `LICENSE` pour plus d'informations.

## Contact

Mohamed BENSAAD

Lien du projet : [https://github.com/bensaadmucret/PDF-Signer](https://github.com/bensaadmucret/PDF-Signer)
