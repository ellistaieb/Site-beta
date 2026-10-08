# Valérie Migueres — Accompagnement personnel & professionnel à Nice

Site bilingue existant amélioré : 27 pages HTML, mêmes URLs françaises et anglaises, palette ivoire/vert, identité VM, composition abstraite légère et parcours vers une demande qualifiée. Python 3.12 suffit. Aucun framework, traçage, publicité ou dépendance applicative externe.

## Prévisualisation

Depuis `/workspace/Site-beta` :

```sh
SITE_BASE_PATH=/Site-beta python build.py
python dev.py --port 8001
```

Le serveur propose la page de choix de langue à `/Site-beta/` et les pages à `/Site-beta/fr/` et `/Site-beta/en/`. `dev.py` est réservé au développement. Le build sans `SITE_BASE_PATH` reste utilisable à la racine d’un autre hébergement.

Pour une prévisualisation navigable hors connexion :

```sh
python export_preview.py
```

Décompresser `review/valerie-migueres-preview.zip` puis ouvrir `index.html` dans un navigateur. Cette archive réécrit uniquement les liens locaux pour une consultation hors connexion ; le contenu de déploiement dans `dist` reste intact. Les captures des principaux écrans sont dans `review`.

## Éditer les contenus

- `content/settings.json` : nom confirmé, domaine, identité légale, coordonnées, tarifs, modalités, images et intégrations.
- `content/fr.json` / `content/en.json` : textes publics, offres, exemples, boutons, FAQ, messages de validation et métadonnées.
- `assets/style.css` : palette, mise en page, signature sculpturale en CSS, responsive.
- `assets/site.js` : menu, animations progressives, préselection d’offre, formulaire.
- Regénérer le site après chaque modification. Ne modifier directement ni `dist`, ni la copie dans `review/site`.

Deux familles de polices seulement (Georgia et Arial, disponibles localement). Les sections restent visibles sans JavaScript ; les animations progressives ne masquent jamais le contenu. Les deux formes de l’accueil utilisent uniquement CSS, avec une version statique sous 768 px et en réduction des mouvements. Le monogramme VM et les compositions graphiques n’imitent ni un portrait ni le cabinet.

## Remplacer les visuels par vos photos

Les chemins, textes alternatifs FR/EN et cadrages sont centralisés dans `settings.json` :

```json
"images": {
  "hero": {"src": "", "alt": {"fr": "", "en": ""}, "position": "50% 50%"},
  "portrait": {
    "src": "/assets/valerie.webp",
    "alt": {"fr": "Portrait de Valérie Migueres", "en": "Portrait of Valérie Migueres"},
    "position": "50% 35%"
  },
  "share": {"fr": "/assets/share-fr.jpg", "en": "/assets/share-en.jpg"}
}
```

Déposer des photos autorisées et optimisées dans `assets`. `hero.src` vide conserve la sculpture ; `portrait.src` vide conserve la composition VM. Le même portrait est utilisé sur l’accueil et À propos. `position` règle le cadrage horizontal/vertical en pourcentages. La galerie de vrais visuels est masquée tant que `gallery` est vide :

```json
"gallery": [{"src": "/assets/cabinet.webp", "alt": {"fr": "Description réelle du cabinet", "en": "Accurate description of the practice"}, "position": "50% 50%"}]
```

L’ancienne image d’ambiance reste conservée dans les sources mais n’est plus affichée. Aucun cadre vide ni mention « photo à venir » n’apparaît publiquement.

## Activer le contact sur GitHub Pages

GitHub Pages héberge les fichiers statiques et n’envoie pas d’e-mail. Le formulaire est prêt pour **Formspree**, service externe avec identifiant de formulaire public, sans secret dans le code.

1. Créer un compte sur `https://formspree.io`, créer un formulaire et confirmer l’adresse destinataire.
2. Copier son endpoint HTTPS `https://formspree.io/f/IDENTIFIANT` dans `contact_endpoint`. Garder `contact_provider: "formspree"`. Ne renseigner aucune clé API privée.
3. Configurer la protection anti-spam du service, ses domaines autorisés si disponibles et ses notifications. Le champ piège `_gotcha` complète cette protection ; la validation client ne remplace pas les contrôles du service.
4. Renseigner `email` (contact professionnel visible) et éventuellement `phone`, `booking_url`, `address`, `hours`, `consultation_languages`.
5. Compléter les mentions légales et la confidentialité avec le prestataire, le responsable, la base juridique, les destinataires, la conservation, les droits et les transferts éventuels avant activation publique.
6. Générer et déployer après autorisation, puis transmettre une demande de test et vérifier sa réception dans la boîte destinataire et le service. Les tests locaux simulent les réponses ; ils ne prouvent pas une livraison réelle.

Le formulaire transmet prénom, e-mail, téléphone facultatif, type et libellé d’accompagnement, message et langue. L’entreprise est affichée et transmise seulement pour une demande « Entreprises ». Un paramètre `?support=4` depuis cette offre la préselectionne, et le changement de langue conserve ce choix.

En JavaScript, le formulaire exige une réponse HTTP réussie et `{"ok":true}` de Formspree. Une erreur, un délai dépassé ou une réponse non confirmée produit une erreur traduite et conserve le message. L’intégration générique est également disponible via `contact_provider: "generic"`, avec un endpoint qui valide, limite les abus, autorise l’origine du site par CORS, transmet réellement la demande et renvoie `{"success":true}` seulement après acceptation réelle. Sans JavaScript, un endpoint renseigné reçoit un POST natif et gère sa propre confirmation. Tant que l’endpoint est vide, l’envoi est désactivé et aucun faux succès n’est affiché.

La réservation se configure avec un lien HTTPS vers votre service, sans calendrier ou créneaux inventés.

## Informations restant à confirmer

- Coordonnées, adresse et accès, horaires, langues de consultation.
- Biographie et formations exactes, portrait et photos réelles si souhaités.
- Tarifs provisoires : 75 €, 375 €, 600 €, 300 €. Mettre `prices_confirmed` à `true` seulement après confirmation.
- Durée, modalités, paiement et annulation.
- Identité légale, responsable de publication, hébergeur et politique de confidentialité complète.
- Compte/formulaire de contact et lien de réservation.

La version anglaise du site ne promet pas de consultations en anglais. Aucune certification, financement, remboursement, avis, qualification ou résultat n’est inventé.

## SEO et déploiement

Le domaine actuel est `https://ellistaieb.github.io/Site-beta`, configurable via `domain` ou `SITE_DOMAIN`. Chaque page dispose d’une canonique, de hreflang absolus réciproques FR/EN et x-default, d’un titre et d’une description, de métadonnées de partage et du favicon VM. Le sitemap comprend 27 URLs avec les alternatives bilingues. Les données structurées Person utilisent uniquement le nom et le titre professionnel fournis.

`indexing_enabled: false` bloque les robots pour cette prévisualisation, tout en fournissant les métadonnées absolues. L’activer une fois les données finales approuvées. Une adresse professionnelle à la racine nécessitera d’ajuster le domaine et de retirer `SITE_BASE_PATH` dans le workflow.

Le workflow GitHub Pages existant déploie `dist` à chaque push sur `main`. Dans GitHub, Pages doit avoir « GitHub Actions » pour source. La publication de cette version a été autorisée. Pour les prochaines modifications, vérifier le résultat local puis pousser les changements après autorisation de publication ; suivre le workflow et l’adresse fournie par le déploiement.

## Vérifier

Avec Chromium installé, dépendances de test uniquement hors du dépôt :

```sh
npm install --prefix /tmp/site-browser --cache /tmp/npm-cache playwright
PLAYWRIGHT_MODULE=/tmp/site-browser/node_modules/playwright node tests/browser.cjs
```

Le serveur de prévisualisation doit tourner sur le port 8001. `PREVIEW_ORIGIN`, `SITE_BASE_PATH` et `CHROMIUM_PATH` permettent d’adapter le test. Vérifications : 27 pages, 320/390/768/1024/1440 px, liens et métadonnées, menu et focus clavier, formulaires FR/EN et piège anti-spam, choix d’offre et langue, tablette portrait/paysage, réduction des mouvements et navigation sans JavaScript. Les captures sont générées dans `review`.
