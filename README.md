# PDF Signer

[Version française](#version-française) | [English version](#english-version)

---

# Version française

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

1. Clonez le dépôt
```bash
git clone https://github.com/bensaadmucret/PDF-Signer.git
cd PDF-Signer
```

2. Installez les dépendances
```bash
pip install -r requirements.txt
```

3. Lancez l'application
```bash
python main.py
```

## Utilisation

1. Cliquez sur "Sélectionner un PDF" pour choisir votre document
2. Entrez votre nom dans le champ signature
3. Choisissez vos options :
   - Cochez "Lu et approuvé" pour ajouter cette mention
   - Cochez "Ajouter la date" pour inclure la date actuelle
4. Dessinez votre signature dans la zone prévue
5. Sélectionnez la page où vous souhaitez placer la signature
6. Cliquez sur "Signer le PDF" pour générer votre document signé

## Structure du projet

```
PDF-Signer/
│
├── main.py              # Fichier principal de l'application
├── requirements.txt     # Dépendances Python
├── icon.py             # Icône de l'application
└── README.md           # Documentation (FR/EN)
```

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

Ce projet est sous licence MIT - voir le fichier [LICENSE](LICENSE) pour plus de détails.

## Contact

Mohamed BENSAAD

Lien du projet : [https://github.com/bensaadmucret/PDF-Signer](https://github.com/bensaadmucret/PDF-Signer)

---

# English version

A simple and elegant desktop application for signing your PDF documents. Developed with Python and PyQt6.

## Advantages of Local Signing 🔒

- **Maximum Privacy**: Your documents stay on your computer, no upload to external servers
- **Security**: No risk of data leaks, everything is processed locally
- **Speed**: No internet connection needed, instant signing
- **Free**: No subscription or hidden fees, unlike online services
- **Offline**: Works without internet connection
- **No Limits**: Sign as many documents as you want
- **Data Protection**: GDPR compliant as no data is collected

## Features

- 📝 Handwritten or text signature
- 📄 Real-time PDF preview
- 🖱️ Precise signature placement
- ✍️ "Read and approved" option
- 📅 Automatic date addition
- 🎨 Modern and intuitive user interface

## Installation

1. Clone the repository
```bash
git clone https://github.com/bensaadmucret/PDF-Signer.git
cd PDF-Signer
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Run the application
```bash
python main.py
```

## Usage

1. Click "Select a PDF" to choose your document
2. Enter your name in the signature field
3. Choose your options:
   - Check "Read and approved" to add this mention
   - Check "Add date" to include the current date
4. Draw your signature in the designated area
5. Select the page where you want to place the signature
6. Click "Sign PDF" to generate your signed document

## Project Structure

```
PDF-Signer/
│
├── main.py              # Main application file
├── requirements.txt     # Python dependencies
├── icon.py             # Application icon
└── README.md           # Documentation (FR/EN)
```

## Contribution

Contributions are welcome! Here's how to contribute:

1. Fork the project ([Click here to fork](https://github.com/bensaadmucret/PDF-Signer/fork))
2. Clone your fork
   ```bash
   git clone https://github.com/your-username/PDF-Signer.git
   cd PDF-Signer
   ```
3. Create your feature branch
   ```bash
   git checkout -b feature/amazing-feature
   ```
4. Commit your changes
   ```bash
   git add .
   git commit -m 'feat: Add amazing feature'
   ```
5. Push to the branch
   ```bash
   git push origin feature/amazing-feature
   ```
6. Open a Pull Request ([Create new Pull Request](https://github.com/bensaadmucret/PDF-Signer/compare))

### Commit Convention

Use these prefixes for your commits:
- `feat:` for a new feature
- `fix:` for a bug fix
- `docs:` for documentation
- `style:` for code formatting
- `refactor:` for code refactoring
- `test:` for adding or modifying tests
- `chore:` for code maintenance

### Contribution Guidelines

- Ensure your code follows Python coding standards (PEP 8)
- Add comments for complex code
- Update documentation when necessary
- Test your changes before submitting a PR

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

Mohamed BENSAAD

Project Link: [https://github.com/bensaadmucret/PDF-Signer](https://github.com/bensaadmucret/PDF-Signer)
