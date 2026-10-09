# Audit du site — code de la version de travail

Date : 9 octobre 2026. Le contrôle porte sur `build.py`, `assets/site.js`, `assets/style.css`, `content/settings.json` et le workflow GitHub Pages. La consultation distante du site et des contrats prestataires reste non vérifiée à cause des restrictions réseau.

| Fonction | État observé | Conséquence pour les brouillons |
|---|---|---|
| Hébergement | GitHub Pages, déploiement par GitHub Actions | GitHub est identifié comme fournisseur technique ; entité contractuelle, coordonnées et traitements à confirmer |
| Formulaire | `contact_endpoint` vide ; bouton désactivé | Aucun envoi Formspree actif par le code |
| Champs prévus | prénom, e-mail, téléphone facultatif, accompagnement, message ; entreprise si demande entreprise ; langue, libellé et honeypot | À informer avant activation ; aucune donnée médicale demandée |
| Réservation / paiement | lien vide ; aucun paiement ou calendrier | Pas de vente ou réservation en ligne active |
| Compte utilisateur | absent | Pas d’identifiants ni de compte client |
| Cookies applicatifs | aucune API `document.cookie` | Pas de cookie de suivi dans le code ; contrôle hôte distant restant |
| Stockage navigateur | pas de localStorage/sessionStorage/IndexedDB | Pas de sauvegarde applicative des champs de contact |
| Statistiques / publicité | aucune intégration | Aucun consentement marketing à gérer dans cette version |
| Fonts du site | Georgia et Arial, polices de l’appareil | Aucun appel à Google Fonts ; les fonts du kit social sont des fichiers locaux, séparés du site |
| Images / scripts / styles | servis avec le site | Aucun CDN ou image distante dans les pages actuelles |
| Vidéo / réseaux | aucun embed | Les exports de ce dossier n’activent aucun réseau social sur le site |
| Journaux / transferts hébergement | GitHub Pages documente les logs IP de sécurité ; sa déclaration générale décrit des traitements internationaux | Rôles précis, autres données, bases, destinataires, conservation et garanties pour cette instance à documenter |

## Protection contre une politique périmée

`content/legal-settings.json` mémorise les fonctions examinées. Le build refuse une modification de l’endpoint de contact ou du lien de réservation tant que ces fonctions ne correspondent plus à cet audit. Avant activation : actualiser les textes et la notice, renseigner les champs juridiques et mettre à jour `audited_features` pour refléter les fonctions réellement revues. Ce mécanisme ne valide pas juridiquement les textes.

Les six pages de travail portent un bandeau de brouillon et des champs explicites. Les URLs françaises/anglaises existantes sont conservées pour mentions légales et confidentialité. Les CGU sont ajoutées à `/fr/conditions-utilisation/` et `/en/terms-of-use/`, avec le préfixe `/Site-beta/` lors du déploiement. Les trois liens figurent au pied de page ; le formulaire renvoie à la confidentialité.

Aucune publication sur `main`, aucun compte réseau social et aucun envoi de message n’ont été effectués pour cette livraison.

Les deux pages officielles GitHub citées dans la note de sources ont été consultées avec succès. Les conclusions relatives à la CNIL, aux textes publics et aux spécifications contemporaines des réseaux restent à revalider après résolution des refus réseau.
