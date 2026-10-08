# Valérie Migueres — Charte graphique premium

La palette et la direction méditerranéenne existantes sont conservées. Cette proposition renforce la hiérarchie, les compositions, la signature typographique et les applications de marque. Elle ne modifie pas le site public.

## Télécharger sur GitHub

- [Consulter la charte PDF](https://github.com/ellistaieb/Site-beta/blob/main/brand/Valerie-Migueres-Charte-graphique.pdf)
- [Télécharger le kit ZIP](https://github.com/ellistaieb/Site-beta/raw/refs/heads/main/brand/Valerie-Migueres-Kit-graphique.zip)

## Livrables

- `Valerie-Migueres-Charte-graphique.pdf` : 12 pages A4 paysage, identité et exemples d’applications.
- `charte.html` / `charte.css` : version modifiable, lisible en français sur ordinateur et mobile.
- `logos/` : 6 fichiers SVG vectorisés, monogramme et signature complète, en vert, ivoire et encre. Pas de police requise pour ouvrir les SVG.
- `tokens.json` : codes couleurs, typographies, espacements et paramètres de mise en page.
- `assets/` : polices Cormorant Garamond et Manrope hébergées localement, licences SIL Open Font License incluses.
- `apercu-charte.jpg` : aperçu de six pages du document.

## Lire et modifier

Ouvrir `charte.html` avec ses dossiers voisins. Pour une lecture servie localement : `python -m http.server 8003 --directory brand` depuis le dépôt. Modifier les textes dans le HTML et les styles dans le CSS. Utiliser « Imprimer », papier A4 paysage, marges nulles, sans en-têtes/pieds de page du navigateur, avec les arrière-plans graphiques activés pour régénérer le PDF. Le document possède déjà ses numéros de pages.

`create_logos.py` permet de régénérer les tracés des signatures ; il nécessite Python et `fontTools`, et utilise les sources WOFF fournies.

## Règles principales

- Ivoire `#F7F4EE`, encre `#26352F`, vert `#29483E`, sauge `#DEE5DB`, sable `#E8DDCB`, bronze `#947448`.
- L’impact repose sur le vert, les grands titres et l’espace ; le bronze demeure un détail.
- Deux familles de polices maximum. Les fonts supplémentaires Regular/Italic appartiennent aux mêmes familles.
- Ne pas altérer les proportions des logos. Respecter la zone de protection et les tailles minimales du guide.
- Les ratios de contraste sont calculés selon WCAG ; bronze/ivoire : 3,94:1, insuffisant pour le petit texte.
- Le PDF est un guide de référence en couleurs écran. Les exemples de cartes et posts sont des mises en situation, sans coordonnées inventées. Pour l’impression réelle, adapter les fonds perdus et le profil ICC à l’imprimeur, puis valider un BAT.

## Vérification de livraison

12 pages PDF A4 paysage, polices locales chargées, 6 SVG parsables, textes sans collision avec les pieds de page sur le format de référence, absence de débordement à 390 px et inspection visuelle des pages principales. La charte est disponible dans le dépôt GitHub ; les pages du site ne sont pas modifiées par ces fichiers.
