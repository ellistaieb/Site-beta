# Un espace pour avancer — Nice

Site éditorial bilingue statique : 27 pages, contenu rendu en HTML, sans framework ni dépendance JavaScript externe. Python 3.12 suffit à générer et servir le site. Les polices Georgia et Arial utilisent les familles disponibles sur l’appareil, sans requête externe. Aucune mesure d’audience ni publicité.

## Prévisualiser et modifier

Depuis `/workspace/Site-beta` :

```sh
python build.py
python -m http.server 8000 --bind 0.0.0.0 --directory dist
```

Le serveur propose une page de choix de langue à la racine et les versions `/fr/` et `/en/`. Le serveur Python est réservé au développement. Déployer uniquement le dossier `dist` sur un hébergement statique HTTPS, après révision du contenu.

- `content/settings.json` : identité, coordonnées, tarifs, modalités, images, réservation, domaine et endpoint de contact.
- `content/fr.json` et `content/en.json` : tous les textes publics et les messages du formulaire.
- `assets/style.css` : palette, typographie, compositions et responsive.
- Après chaque modification, exécuter `python build.py` puis rafraîchir la page.
- Les champs vides sont masqués. Le portrait n’est jamais remplacé par une fausse praticienne. La composition abstraite est décorative.
- Pour un portrait, déposer une image optimisée dans `assets`, puis renseigner `portrait` avec `/assets/nom.webp`.
- `gallery` peut contenir des objets `{"src":"/assets/cabinet.webp","alt":{"fr":"Description réelle","en":"Accurate description"}}`. La galerie est masquée tant qu’elle est vide.

## À confirmer avant publication

- Nom, biographie et formations réelles ; titre professionnel.
- E-mail, téléphone, adresse exacte, accès et horaires.
- Langues effectivement proposées en consultation.
- Tarifs (actuellement provisoires : 75 €, 375 €, 600 €, 300 €). Après confirmation, mettre `prices_confirmed` à `true`.
- Durée, modalités, paiement et conditions d’annulation.
- Portrait et photos réelles du cabinet si souhaités.
- Identité légale complète, statut, responsable de publication et hébergeur.
- Politique de confidentialité : responsable, base juridique, destinataires, conservation, contact pour les droits, éventuels transferts et journaux de l’hébergeur. Les pages légales sont des projets à réviser, pas des textes juridiques finalisés.
- Domaine de production : `domain` sous la forme `https://votre-domaine.fr`. Cela active les canoniques, le sitemap bilingue et l’indexation. Sans domaine, `robots.txt` interdit l’indexation de la prévisualisation.

## Connecter les demandes

Le formulaire est visible, mais son envoi est désactivé tant que `contact_endpoint` est vide. Il n’affiche aucun faux succès. Vous pouvez déjà configurer un e-mail et un lien de réservation HTTPS : ils sont affichés seulement lorsqu’ils sont renseignés.

Le futur endpoint HTTPS doit accepter un POST JSON : `first_name`, `email`, `phone`, `company`, `support` (0 confiance, 1 transition, 2 professionnel, 3 jeunes, 4 entreprises), `message`, `language`. Il doit valider et limiter ces champs côté serveur, limiter les abus, autoriser l’origine du site par CORS, transmettre réellement le message et répondre avec un statut 2xx et `{"success":true}` seulement après acceptation réelle de la transmission. Toute erreur HTTP, réseau ou réponse sans `success: true` affiche une erreur. Ne placez jamais de secret de service dans les fichiers publics. Documentez le prestataire et la conservation dans la confidentialité avant activation.

La réservation est un lien externe configurable, sans calendrier ni créneaux inventés. Les langues de consultation restent à confirmer : la version anglaise ne promet pas de séances en anglais.

## Image d’ambiance

`assets/ambiance.webp` est une image générée pour illustrer l’atmosphère souhaitée. Elle ne représente pas le vrai cabinet. Cette distinction apparaît en légende et dans le texte alternatif. Remplacez-la si vous disposez d’une photographie autorisée. Aucune photo de faux client ou de fausse praticienne n’est utilisée.

## Vérifications

La livraison est vérifiée dans Chromium : parcours des 27 pages, liens internes, langues correspondantes, absence de débordement à 390, 768 et 1440 px, menu mobile et fermeture avec Échap, formulaire désactivé sans intégration, réponses simulées en erreur et en succès dans les deux langues. Les réponses simulées vérifient l’interface, pas une intégration de messagerie réelle. Aucun message réel n’a été envoyé.

Les captures `preview-390.png`, `preview-768.png` et `preview-1440.png` montrent l’accueil. Le contenu et les liens restent disponibles sans JavaScript ; l’envoi du formulaire nécessite JavaScript et l’endpoint configuré.

Pour répéter les tests de navigateur avec Chromium installé (dépendances de test hors du dépôt) :

```sh
npm install --prefix /tmp/site-browser --cache /tmp/npm-cache playwright
PLAYWRIGHT_MODULE=/tmp/site-browser/node_modules/playwright node tests/browser.cjs
```

Les tests utilisent le serveur de développement sur le port 8000 et recréent les trois captures. Le domaine peut être testé sans modifier le contenu : `SITE_DOMAIN=https://example.invalid python build.py`. Relancer ensuite `python build.py` pour revenir à la configuration enregistrée.

## Prévisualiser sur GitHub Pages

Le workflow `.github/workflows/pages.yml` déploie une prévisualisation à chaque push sur `main`. Dans le dépôt GitHub, ouvrir **Settings → Pages → Build and deployment → Source → GitHub Actions**. Puis ouvrir **Actions → Publish preview to GitHub Pages → Run workflow** si le premier passage a précédé l’activation de Pages. L’adresse est fournie par le déploiement réussi, généralement `https://ellistaieb.github.io/Site-beta/`.

Le workflow configure le préfixe `/Site-beta` pour les liens et les images. Cette version reste une prévisualisation : formulaire désactivé et indexation bloquée tant que les informations de publication ne sont pas renseignées. GitHub Pages nécessite une offre compatible avec la visibilité du dépôt. Un domaine personnalisé nécessitera d’ajuster `SITE_BASE_PATH` et le domaine de production.
