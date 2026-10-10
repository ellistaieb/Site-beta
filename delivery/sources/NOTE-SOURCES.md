# Sources : mise à jour du 10 octobre 2026

L’accès réseau a évolué depuis la première livraison. `checks.json` conserve les nouveaux résultats, et `checks-2026-10-09.json` l’état initial. Un HTTP 200 n’est pas assimilé à la lecture du contenu : Instagram ne restitue que « Help Center », sans ses spécifications.

## Sources effectivement consultées aujourd’hui

- Service Public Entreprendre, F31228 : identité, statut selon la situation, adresse, e-mail, téléphone, immatriculation/TVA applicables et identité/adresse/téléphone de l’hébergeur. La page concerne l’entrepreneur individuel ; elle ne permet pas de déduire ce statut pour Valérie Migueres. Le statut, l’adresse et l’identité de publication restent à confirmer.
- EUR-Lex, RGPD : articles 5 et 6 (limitation, conservation justifiée et bases par finalité), 12–14 (information et droits), 15–22 et 44–49 (droits et transferts). Les coordonnées publiées ne déterminent ni les bases concrètes, ni les durées, ni les garanties contractuelles Gmail ou GitHub.
- YouTube, identité visuelle : https://support.google.com/youtube/answer/10456525?hl=fr ; bannière recommandée 2560 × 1440, minimum 2048 × 1152, zone texte/logo de 1235 × 338 au minimum, limite 6 Mo. Notre zone centrale 1546 × 423 à 2560 × 1440 est cohérente avec cette référence ; vérifier les crops dans Studio.
- YouTube, miniatures : la recommandation actuelle lue est 3840 × 2160 pour les vidéos (16:9), largeur minimale 640 ; JPG/PNG. Limite mobile 2 Mo pour les vidéos, ordinateur 50 Mo. Les modèles modifiables 1280 × 720 sont conservés ; six exports JPG supplémentaires `miniature-*-4k.jpg` en 3840 × 2160, sous 2 Mo, sont fournis.
- YouTube, écran de fin : vidéo d’au moins 25 secondes, éléments à ajouter dans Studio ; notre image ne crée pas de lien interactif.
- Les deux sources GitHub précédentes restent consultables ; journalisation IP de sécurité et contexte général des transferts confirmés, contrats/rôles/durées de cette instance non établis.

## Limites restantes

CNIL et Formspree répondent 403 ; WhatsApp Business reste bloqué à la connexion/redirection. Les pages Instagram accessibles ne livrent pas le contenu des spécifications. Les marges Instagram/WhatsApp demeurent des choix prudents à contrôler dans les applications. Formspree reste désactivé.

Le contrôle HTTP direct du site GitHub Pages et l’API Actions restent bloqués dans cet environnement. La page web Actions de GitHub est consultable pour suivre la publication. La publication sur le site a été expressément demandée le 10 octobre 2026 ; les informations juridiques non confirmées restent signalées dans les pages.

## Première note de livraison, conservée pour historique

# Sources et limites de vérification — 9 octobre 2026

Les sources officielles listées dans `checks.json` ont été demandées le 9 octobre 2026. Les deux pages GitHub ont été consultées avec succès (HTTP 200). Les sources CNIL, Service Public, EUR-Lex, plateformes et Formspree ont été refusées par le réseau (HTTP 403). Le fichier conserve le résultat exact ; aucun contenu des pages refusées n’a été lu. Les domaines nécessaires ont été ajoutés au brouillon de configuration réseau, sans activation automatique ni publication.

Hormis les deux pages GitHub explicitement consultées, les références ci-dessous sont des points de contrôle, pas des affirmations de consultation actuelle. Les formats livrés sont des choix de création compatibles avec les formats largement documentés ; leur validation contemporaine contre les plateformes reste à faire après ouverture de l’accès réseau. Les restrictions d’application, versions et recadrages peuvent varier.

## Formats de création livrés

| Usage | Export | Zone de création retenue | Statut |
|---|---|---|---|
| Instagram publication / carrousel | 1080 × 1350, 4:5 | x=90…990, y=90…1320 | Choix de format, pas une dimension maximale revendiquée |
| Instagram Reel / Story | 1080 × 1920, 9:16 | x=90…990, y=260…1650 ; titre Reel dans le carré central y=420…1500 | Marges prudentes, à contrôler dans l’application et sa grille |
| Instagram stories à la une | 1080 × 1080 | zone circulaire centrale ; nom de story également fourni séparément | Pas de garantie de tout recadrage |
| WhatsApp profil | 1080 × 1080 | monogramme au centre, marges pour le cercle | Format de création proposé, application peut réduire |
| WhatsApp statut | 1080 × 1920 | marges portrait identiques à la Story | Format de création proposé, pas une exigence technique revendiquée |
| WhatsApp fiche | 1080 × 1350 | publication verticale lisible, sans coordonnées inventées | Fichier à partager manuellement si souhaité |
| YouTube bannière | 2560 × 1440 | zone centrale 1546 × 423, x=507, y=508,5 | Valeurs usuelles de référence, à revalider avec l’aide actuelle |
| YouTube profil | 1080 × 1080 | zone circulaire centrale | Export haute définition, vérifier les limites de l’application |
| YouTube miniature | 1280 × 720, PNG et JPG | x=64…1216, y=36…684 ; éviter le coin bas droit | Valeurs usuelles de référence, à revalider |
| YouTube titre / fin / intro | 1920 × 1080 | marges 5–10 % ; emplacements interactifs de fin documentés | Visuels vidéo, pas des liens activés automatiquement |
| YouTube intro animée | MP4 H.264, 1920 × 1080, 25 fps, 3 s, sans audio | fondu vert doux de 350 ms au début et à la fin | Version PNG statique également fournie |

## Sources plateformes à vérifier

- Instagram, résolution des images : https://help.instagram.com/1631821640426723
- Instagram, dimensions des Reels : https://help.instagram.com/1038071743007909
- WhatsApp Business, application et profils : https://business.whatsapp.com/products/business-app ; https://faq.whatsapp.com/
- YouTube, identité de chaîne et bannière : https://support.google.com/youtube/answer/2972003?hl=fr
- YouTube, miniatures : https://support.google.com/youtube/answer/72431?hl=fr
- YouTube, écran de fin : https://support.google.com/youtube/answer/6388789?hl=fr

L’écran de fin graphique ne crée aucun élément cliquable : ces éléments doivent être ajoutés dans YouTube Studio. Prévoir une vidéo d’au moins 25 secondes pour les conditions usuelles d’éligibilité ; vérifier aussi les restrictions actuelles, notamment le contenu destiné aux enfants. Les miniatures évitent les promesses, les notes d’efficacité et les mots qui ne correspondent pas au contenu réellement filmé.

## Sources juridiques à vérifier avant finalisation

- CNIL, exemples de mentions d’information : https://www.cnil.fr/fr/rgpd-exemples-de-mentions-dinformation
- CNIL, cookies et traceurs : https://www.cnil.fr/fr/cookies-et-autres-traceurs/regles/cookies/que-dit-la-loi
- CNIL, durées de conservation : https://www.cnil.fr/fr/les-durees-de-conservation-des-donnees
- Service Public Entreprendre, mentions obligatoires d’un site professionnel : https://entreprendre.service-public.gouv.fr/vosdroits/F31228 (vérifier les éventuelles redirections et le statut applicable)
- RGPD, texte officiel EUR-Lex : https://eur-lex.europa.eu/eli/reg/2016/679/oj?locale=fr
- GitHub, politique de confidentialité et Pages : https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement ; https://docs.github.com/en/pages/getting-started-with-github-pages/about-github-pages
- Formspree, politique et informations contractuelles, uniquement avant activation : https://formspree.io/legal/privacy-policy/

## Choix des brouillons et fondement à contrôler

- Information transparente et champs explicites : RGPD articles 12–14 ; identité réelle à confirmer, aucun SIRET, responsable ou statut inventé.
- Bases par finalité : article 6 ; mesures précontractuelles envisagées pour une demande de rendez-vous, intérêt légitime possible pour une demande générale ou la sécurité, sous réserve d’analyse. Aucun consentement global imposé.
- Conservation : principe de limitation de l’article 5(1)(e), sans durée arbitraire. Les durées et justifications doivent être fournies selon les traitements réels et le contrat du prestataire.
- Droits : articles 15–22, avec leurs conditions ; réclamation auprès de la CNIL.
- Transferts : articles 44–49 ; localisation et garanties à vérifier, sans certification supposée.
- Pas de bandeau décoratif : aucun traceur non nécessaire n’est identifié dans le code, mais l’hébergement distant n’a pas pu être vérifié par requête. Refaire l’audit réseau/cookies avant finalisation.
- Les CGU concernent la présentation et les demandes. Une future vente, réservation engageante ou paiement nécessiterait des conditions et informations supplémentaires adaptées.

Les brouillons ne garantissent pas une conformité complète. Les sources actuelles, le statut, les contrats et le fonctionnement final doivent être examinés avant publication des pages comme finalisées.

## Résultats des sources GitHub consultées

Le 9 octobre 2026, la page officielle « About GitHub Pages » indique que l’adresse IP des visiteurs est enregistrée et stockée pour la sécurité, avec ou sans connexion à GitHub. La déclaration générale décrit des traitements dans plusieurs pays, dont les États-Unis, et le recours général aux clauses contractuelles types pour certains transferts. Ces éléments ne déterminent pas les rôles et garanties contractuels spécifiques de cette instance, ni une durée exacte de journalisation Pages.

La déclaration mentionne GitHub B.V., Prins Bernhardplein 200, Amsterdam 1097JB, The Netherlands, et GitHub, Inc., 88 Colin P. Kelly Jr. St., San Francisco, CA 94107, United States. Ces adresses sont sourcées ; l’entité applicable au contrat d’hébergement reste à confirmer avant finalisation des mentions légales. Aucune entité n’est sélectionnée automatiquement.
