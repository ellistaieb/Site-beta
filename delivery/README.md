# Valérie Migueres — Kit réseaux et brouillons juridiques

Livraison de travail du 9 octobre 2026. Palette et identité existantes conservées. Les éléments sont prêts à adapter. Deux sources officielles GitHub ont été consultées ; les spécifications actuelles des plateformes et les sources CNIL, publiques françaises et européennes restent à vérifier à cause de refus réseau 403. Les résultats exacts et références sont dans `sources`.

## Ouvrir les livrables

- `social/Guide-reseaux-Valerie-Migueres.pdf` : guide visuel de 13 pages, avec de vrais exemples exportés.
- `social/editor.html` : studio local pour modifier les titres, textes, signatures, photo et cadrage ; import/export JSON et export SVG.
- `social/exports/{plateforme}/{fr|en|commun}` : PNG haute définition, JPG des miniatures et MP4 des intros.
- `social/templates/{plateforme}/{fr|en|commun}` : SVG modifiables, polices intégrées pour un rendu autonome.
- `social/logos` : 9 SVG vectorisés et 9 PNG transparents ; monogramme commun, signatures FR et EN.
- `social/copy/fr.md` / `en.md` : messages WhatsApp, descriptions, réponses rapides, légendes, piliers et cinq premiers sujets YouTube.
- `legal/site/index.html` : prévisualisation navigable du site de travail avec ses six brouillons juridiques.
- `legal/*.md` : textes juridiques séparés ; `legal/AUDIT.md` : état actif/prévu.

Depuis le dossier décompressé, lancer :

```sh
python -m http.server 8004
```

Puis ouvrir le studio à `/social/editor.html` ou le site à `/legal/site/index.html` dans le navigateur sur le serveur local. L’éditeur nécessite ce serveur pour charger les modèles ; les SVG et PNG s’ouvrent aussi directement. L’éditeur ne transmet aucun fichier, ne crée aucun compte, n’envoie aucun message et ne publie rien. Les changements ne sont pas enregistrés automatiquement : télécharger le SVG ou le JSON avant de fermer.

## Inventaire

- **Instagram : 30 visuels** — six familles de modèles, dont un carrousel de quatre slides et six couvertures à la une, en FR/EN séparés.
- **WhatsApp Business : 9 visuels** — profil commun, trois statuts FR/EN et fiche d’accompagnements FR/EN.
- **YouTube : 15 visuels** — profil commun, bannière, trois miniatures, titre transparent, intro statique et fin, avec versions FR/EN séparées.
- **Deux intros animées** — MP4 H.264 1920 × 1080, 25 fps, 3 secondes, aucun flux audio ; fondu doux, PNG statique fourni.
- **Six miniatures JPG** — alternatives aux PNG, chacune sous 2 Mo.
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

- Entité qui édite le site, statut, immatriculation applicable, adresse et contacts professionnels.
- Responsable de publication et, si applicable, informations TVA/professionnelles.
- Entité contractuelle d’hébergement, coordonnées légales, rôles, sous-traitants, journaux et localisation.
- Responsable de traitement et contact des droits ; finalités, bases légales, durées justifiées et garanties de transfert.
- Pour un futur formulaire : destinataires et contrat du service, données nécessaires, base appropriée, conservation et garanties ; pour une réservation/vente, informations et conditions spécifiques.
- Langues de consultation, modalités et tarifs provisoires avant toute communication finale ; photos réelles et leurs droits si ajoutées.

Aucune durée de conservation, certification ou coordonnée inconnue n’est inventée. Aucun consentement global ni bandeau cookies décoratif n’a été ajouté. Les brouillons ne garantissent pas la conformité complète : valider les faits et les sources actuelles avant publication finale.

## Publication et réseau

Cette livraison est préparée sur une branche dédiée : elle ne modifie pas `main`, le workflow Pages existant ne déploie que les pushes sur `main`, et aucun contenu n’est publié sur les réseaux. Les brouillons peuvent être revus sans changer le site public.

Les domaines officiels nécessaires ont été enregistrés dans le brouillon réseau de l’environnement. Revoir et enregistrer ces changements dans les paramètres puis publier l’environnement pour permettre une nouvelle vérification des sources ; le simple enregistrement du brouillon par l’agent ne les active pas. Consulter `sources/NOTE-SOURCES.md` pour les URLs et le statut exact des formats retenus.
