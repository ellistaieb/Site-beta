# Valérie Migueres — Kit réseaux et brouillons juridiques

Livraison mise à jour le 10 octobre 2026. Palette et identité existantes conservées. Les éléments sont prêts à adapter. Les sources GitHub, Service Public, EUR-Lex et YouTube ont été consultées ; CNIL, Instagram, WhatsApp et Formspree restent partiellement ou entièrement inaccessibles. Les résultats exacts et références sont dans `sources`.

## Ouvrir les livrables

- `social/Guide-reseaux-Valerie-Migueres.pdf` : guide visuel de 13 pages, avec de vrais exemples exportés.
- `social/editor.html` : studio local pour modifier les titres, textes, signatures, photo et cadrage ; import/export JSON et export SVG.
- `social/exports/{plateforme}/{fr|en|commun}` : PNG haute définition, JPG des miniatures et MP4 des intros.
- `social/templates/{plateforme}/{fr|en|commun}` : SVG modifiables, polices intégrées pour un rendu autonome.
- `social/logos` : 9 SVG vectorisés et 9 PNG transparents ; monogramme commun, signatures FR et EN.
- `social/copy/fr.md` / `en.md` : messages WhatsApp, descriptions, réponses rapides, légendes, piliers et cinq premiers sujets YouTube.
- `legal/site/index.html` : prévisualisation navigable du site de travail avec ses six brouillons juridiques.
- `legal/*.md` : textes juridiques séparés ; `legal/AUDIT.md` : état actif/prévu.

Ouvrir `index.html` pour parcourir les exports, ou utiliser directement la galerie et le studio depuis la page Ressources du site. Pour une utilisation locale depuis le dossier décompressé, lancer :

```sh
python -m http.server 8004
```

Puis ouvrir le studio à `/social/editor.html` ou le site à `/legal/site/index.html` dans le navigateur sur le serveur local. L’éditeur nécessite ce serveur pour charger les modèles ; les SVG et PNG s’ouvrent aussi directement. L’éditeur ne transmet aucun fichier, ne crée aucun compte, n’envoie aucun message et ne publie rien. Les changements ne sont pas enregistrés automatiquement : télécharger le SVG ou le JSON avant de fermer.

## Inventaire

- **Instagram : 30 visuels** — six familles de modèles, dont un carrousel de quatre slides et six couvertures à la une, en FR/EN séparés.
- **WhatsApp Business : 9 visuels** — profil commun, trois statuts FR/EN et fiche d’accompagnements FR/EN.
- **YouTube : 15 visuels** — profil commun, bannière, trois miniatures, titre transparent, intro statique et fin, avec versions FR/EN séparées.
- **Deux intros animées** — MP4 H.264 1920 × 1080, 25 fps, 3 secondes, aucun flux audio ; fondu doux, PNG statique fourni.
- **Douze miniatures JPG** — six en 1280 × 720 et six supplémentaires en 3840 × 2160, chacune sous 2 Mo.
- **Neuf logos** — SVG et PNG transparents, noms et monogrammes cohérents.

Les boutons dessinés ne sont pas des liens. Ajouter manuellement un sticker Lien dans Instagram ou les éléments de fin dans YouTube Studio. Les visuels annoncent des sujets proposés : les descriptions et légendes doivent correspondre aux vidéos réellement filmées avant diffusion. Aucun portrait, cabinet, disponibilité, qualification, financement ou résultat n’est inventé.

## Modifier et exporter

1. Choisir plateforme, langue et modèle dans le studio. Les langues ne sont pas mélangées sur un même visuel.
2. Modifier les champs ; une alerte empêche l’export si le texte dépasse le nombre de lignes prévu.
3. Pour une photo réelle, utiliser le champ local sur les modèles qui le permettent, puis choisir un cadrage centre/haut/bas. Le modèle est complet sans photo.
4. Télécharger le SVG modifié et, si souhaité, les textes JSON pour reprendre la session. Les PNG liés dans le studio restent ceux de l’exemple original.
5. Exporter le SVG modifié en PNG dans Inkscape, avec la taille du canevas inchangée. Les SVG intègrent les polices ; installer les polices locales peut être nécessaire selon l’outil choisi. Licences fournies dans `social/shared`.

Alternative pour régénérer tous les modèles depuis les textes centralisés : modifier `social/content.json`, puis exécuter `python social/build_templates.py` (Python avec Pillow et fontTools). `make_content.py` rétablit les exemples d’origine : ne pas le relancer après vos modifications sans sauvegarde.

Pour les PNG avec Chromium et Playwright, après avoir lancé le serveur ci-dessus :

```sh
npm install --prefix /tmp/vm-social-tools --cache /tmp/vm-social-cache playwright
PLAYWRIGHT_MODULE=/tmp/vm-social-tools/node_modules/playwright node social/render.cjs
```

Le script utilise Chromium à `/usr/bin/chromium` et le serveur sur le port 8004. Il conserve la transparence des titres et logos. Pour une autre machine, utiliser `CHROMIUM_PATH` pour le navigateur et `DELIVERY_ORIGIN` pour l’URL du dossier social. Le guide HTML/CSS est également modifiable et imprimable en A4 paysage, arrière-plans activés, marges nulles et sans en-tête/pied du navigateur.

## Pages juridiques et informations manquantes

Les trois pages existent en français et anglais, avec un bandeau de brouillon, des correspondances de langues et trois liens de pied de page. La confidentialité est liée près du formulaire. Les brouillons reflètent le code examiné : formulaire et réservation inactifs, aucun traceur applicatif identifié, ressources servies avec le site. L’hébergement distant n’a pas pu être complètement contrôlé.

À confirmer :

- Entité qui édite le site, statut, immatriculation applicable et adresse. E-mail confirmé : migueresv@gmail.com ; téléphone : 06 63 83 44 50 ; Instagram : @valmigueres.
- Responsable de publication et, si applicable, informations TVA/professionnelles.
- Entité contractuelle d’hébergement, coordonnées légales, rôles, sous-traitants, journaux et localisation.
- Responsable de traitement ; finalités, bases légales, durées justifiées et garanties de transfert. Le contact des droits publié est migueresv@gmail.com ; les conditions exactes du compte Gmail restent à examiner.
- Pour un futur formulaire : destinataires et contrat du service, données nécessaires, base appropriée, conservation et garanties ; pour une réservation/vente, informations et conditions spécifiques.
- Langues de consultation, modalités et tarifs provisoires avant toute communication finale ; photos réelles et leurs droits si ajoutées.

Aucune durée de conservation, certification ou coordonnée inconnue n’est inventée. Aucun consentement global ni bandeau cookies décoratif n’a été ajouté. Les brouillons ne garantissent pas la conformité complète : valider les faits et les sources actuelles avant publication finale.

## Publication et réseau

La publication de cette livraison sur le site a été expressément demandée le 10 octobre 2026. Le workflow Pages déploie les pushes sur `main`. La page Ressources donne accès au guide, au ZIP, à la galerie et au studio. Les mentions légales, CGU et confidentialité restent explicitement à compléter ; aucun contenu n’est publié sur les réseaux sociaux.

Les domaines officiels ajoutés à l’environnement permettent désormais de consulter Service Public, EUR-Lex et YouTube. CNIL et Formspree renvoient toujours 403, Instagram ne fournit pas le contenu des spécifications et WhatsApp reste inaccessible. Consulter `sources/NOTE-SOURCES.md` pour les URLs et le statut exact des formats retenus.
