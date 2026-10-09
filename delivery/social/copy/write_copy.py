import json,pathlib
R=pathlib.Path(__file__).resolve().parent
copy={
'fr':{
 'whatsapp':{
  'description':'Valérie Migueres · Accompagnement personnel et professionnel à Nice. Confiance, stress, transitions de vie et évolution professionnelle. Un espace pour avancer.',
  'a-propos':'Accompagnement personnel & professionnel · Nice. Un espace pour avancer.',
  'accueil':'Bonjour et bienvenue. Merci pour votre message. Vous pouvez indiquer votre prénom et l’objet général de votre demande. Évitez de transmettre des informations médicales ou sensibles ici.',
  'absence':'Merci pour votre message. Je ne suis pas disponible pour échanger pour le moment. Votre demande sera consultée lorsque je pourrai vous répondre. Évitez de partager des informations médicales ou sensibles.',
  'reponses_rapides':{
   '/tarifs':'Les tarifs actuellement présentés sont provisoires, à confirmer avant tout engagement : séance individuelle 75 € ; confiance et estime de soi, 5 séances, 375 € ; transition de vie, 8 séances, 600 € ; préparation examens, 4 séances, 300 €. Bilan de compétences et entreprises : demande de renseignements.',
   '/acces':'L’accompagnement est présenté à Nice. Les coordonnées exactes et les modalités d’accès seront précisées avant tout rendez-vous confirmé.',
   '/rdv':'Pour une demande de rendez-vous, indiquez votre prénom et le type d’accompagnement recherché. Quelques mots sur votre demande suffisent ; évitez les informations médicales ou sensibles. Les modalités et langues de consultation sont à confirmer.'}},
 'instagram':{
  'piliers':['Comprendre une difficulté','Découvrir l’accompagnement','Faire connaissance avec Valérie Migueres','Trouver les informations pratiques'],
  'legendes':{
   'pedagogie':'Quand les examens approchent, les attentes peuvent prendre beaucoup de place. Identifier une seule prochaine étape peut aider à rendre la situation plus concrète. Ce repère ne remplace pas un accompagnement adapté à votre situation. Vous pouvez enregistrer ce visuel pour y revenir.',
   'carrousel':'Tout porter, tout le temps ? Ce carrousel propose quelques pistes pour nommer ce qui pèse et choisir un petit ajustement réaliste. Il ne s’agit pas d’une méthode universelle. Si vous souhaitez faire le point, découvrez l’accompagnement de Valérie Migueres à Nice.',
   'accompagnement':'Une évolution professionnelle peut soulever des questions sur vos compétences, vos aspirations et votre équilibre. Reconversion, prise de poste ou bilan de compétences : le cadre se définit selon votre demande. Découvrez la page dédiée sur le site.',
   'faq':'Vous n’avez pas besoin d’arriver avec une demande parfaitement formulée. Un premier échange permet de mettre des mots sur votre situation et de clarifier ce que vous souhaitez explorer. Découvrez mon approche sur le site.',
   'reel':'Par où commencer quand on souhaite retrouver confiance ? Cette vidéo ouvre une réflexion sur vos repères et les situations dans lesquelles le doute apparaît. À adapter au contenu réellement filmé avant diffusion.',
   'story':'Invitez à découvrir la page Contact avec le sticker Lien de l’application. Le bouton dessiné dans l’image n’est pas un lien cliquable.'},
  'stories_a_la_une':['À propos','Approche','Séances','Cabinet','FAQ','Contact']},
 'youtube':{
  'description_chaine':'Valérie Migueres, consultante en accompagnement et transformation personnelle et professionnelle à Nice. Un espace pour comprendre les périodes de stress, de doute et de transition, et découvrir un accompagnement personnalisé. Les vidéos proposent des repères généraux ; elles ne constituent ni un diagnostic ni un suivi individuel. Hypnose, thérapies brèves, approches issues des thérapies cognitives et comportementales, coaching, neurofeedback et bilan de compétences sont présentés selon les besoins. Les langues de consultation sont à confirmer. Informations et contact : https://ellistaieb.github.io/Site-beta/fr/',
  'description_video':'[TITRE]\n\nDans cette vidéo : [question abordée et 2–3 points réellement traités].\n\nRepères :\n[00:00 — introduction : ajuster aux durées réelles]\n[chapitres vérifiés après montage]\n\nPour découvrir l’accompagnement de Valérie Migueres à Nice : https://ellistaieb.github.io/Site-beta/fr/accompagnements/\nContact : https://ellistaieb.github.io/Site-beta/fr/contact/\n\nCes informations sont générales et ne remplacent pas un accompagnement personnalisé ou un suivi médical nécessaire. Évitez de publier des informations médicales ou sensibles dans les commentaires.\n[Crédits uniquement pour les ressources réellement utilisées et autorisées.]',
  'premieres_videos':[
   {'titre':'Stress des examens : quand la pression monte','angle':'Nommer les attentes, distinguer ce qui dépend de soi, choisir une prochaine étape réaliste.'},
   {'titre':'Confiance en soi : par où commencer ?','angle':'Explorer les situations de doute, repérer ses ressources, observer le discours intérieur sans jugement.'},
   {'titre':'Surcharge mentale : comment faire le point ?','angle':'Différencier tâches, attentes et besoins ; réfléchir aux limites et à la demande d’aide.'},
   {'titre':'Reconversion : quelles questions se poser ?','angle':'Clarifier motivations, valeurs et compétences ; expliquer le bilan de compétences sans financement ou résultat promis.'},
   {'titre':'Que se passe-t-il lors d’une première séance ?','angle':'Écoute, clarification de la demande et discussion du cadre ; aucune durée ou offre gratuite annoncée.'}]}
 },
'en':{
 'whatsapp':{
  'description':'Valérie Migueres · Personal and professional development in Nice. Support with confidence, stress, life changes and career direction. Space to move forward.',
  'a-propos':'Personal & professional development · Nice. Space to move forward.',
  'accueil':'Hello and welcome. Thank you for your message. Please share your first name and the general purpose of your enquiry. Please avoid medical or sensitive information here.',
  'absence':'Thank you for your message. I am not available to chat at the moment. I will read your enquiry when I am able to respond. Please avoid sharing medical or sensitive information.',
  'reponses_rapides':{
   '/fees':'The fees shown are provisional and will be confirmed before any commitment: individual session €75; confidence and self-esteem, 5 sessions, €375; life transition, 8 sessions, €600; exam preparation, 4 sessions, €300. Career review — bilan de compétences and workplace support: please enquire.',
   '/access':'The support is based in Nice. The exact contact details and access arrangements will be provided before a confirmed appointment.',
   '/appointment':'To enquire about an appointment, please share your first name and the area of support you are interested in. A few words are enough; avoid medical or sensitive information. Practical arrangements and consultation languages are to be confirmed.'}},
 'instagram':{
  'piliers':['Understand a difficulty','Explore the support','Get to know Valérie Migueres','Find practical information'],
  'legendes':{
   'pedagogie':'As exams approach, expectations can feel overwhelming. Identifying one realistic next step can make the situation more concrete. This reminder does not replace support tailored to your needs. Save it if you would like to come back to it.',
   'carrousel':'Carrying it all? This carousel offers ways to name what feels heavy and consider one small, realistic adjustment. It is not a universal method. To explore your situation, discover Valérie Migueres’s support in Nice.',
   'accompagnement':'A career transition can raise questions about your skills, aspirations and balance. Career change, a new role or career review — bilan de compétences: the framework is agreed around your enquiry. The French career review is not presented as an overseas qualification. Explore the relevant website page.',
   'faq':'You do not need a perfectly worded enquiry. An initial conversation can help put your experience into words and clarify what you would like to explore. Find out more about my approach on the website.',
   'reel':'Where could you begin when you want to build confidence? This video opens a reflection on your reference points and situations where self-doubt appears. Adapt this caption to the video actually filmed before sharing.',
   'story':'Add the application’s Link sticker to direct viewers to the Contact page. The button within the image is not clickable.'},
  'stories_a_la_une':['About','Approach','Sessions','Practice','FAQ','Contact']},
 'youtube':{
  'description_chaine':'Valérie Migueres, Personal & Professional Development Consultant in Nice. Space to understand periods of stress, uncertainty and change, and explore personalised support. These videos offer general perspectives, not a diagnosis or individual care. Hypnotherapy, brief therapies, CBT-informed approaches, coaching, neurofeedback and career review — bilan de compétences are introduced in relation to people’s needs. Consultation languages are to be confirmed; an English website does not imply sessions in English. Information and enquiries: https://ellistaieb.github.io/Site-beta/en/',
  'description_video':'[TITLE]\n\nIn this video: [the actual question explored and 2–3 points covered].\n\nChapters:\n[00:00 — introduction: adjust to the final edit]\n[chapters checked against the finished video]\n\nExplore Valérie Migueres’s support in Nice: https://ellistaieb.github.io/Site-beta/en/how-i-can-help/\nEnquiries: https://ellistaieb.github.io/Site-beta/en/contact/\n\nThis is general information and does not replace personalised support or medical care when needed. Please avoid medical or sensitive details in comments.\n[Credits for resources actually used, with the relevant permissions.]',
  'premieres_videos':[
   {'titre':'Exam stress: when pressure builds','angle':'Notice expectations, distinguish what is within your control and choose a realistic next step.'},
   {'titre':'Confidence: where could you begin?','angle':'Explore moments of self-doubt, recognise resources and notice inner dialogue without judgement.'},
   {'titre':'Mental overload: how can you take stock?','angle':'Separate tasks, expectations and needs; reflect on boundaries and asking for support.'},
   {'titre':'Career change: which questions matter?','angle':'Clarify motivations, values and skills; explain the French career review without promises of funding or outcomes.'},
   {'titre':'What happens in a first session?','angle':'Listening, understanding the enquiry and discussing the framework; no invented duration or free offer.'}]}
 }}
for lang,data in copy.items():
 (R/(lang+'.json')).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
 out=['# Textes prêts à adapter — '+lang.upper(),'','Les consultations en anglais ne sont pas confirmées. Aucun compte ni message n’a été créé ou envoyé.','']
 for platform,fields in data.items():
  out.extend(['## '+platform.capitalize(),''])
  for key,value in fields.items():
   out.extend(['### '+key.replace('_',' '),''])
   if isinstance(value,str):out.append(value)
   elif isinstance(value,dict):
    for label,text in value.items():out.extend(['**'+label+'**',text,''])
   elif isinstance(value,list):
    for item in value:out.append('- '+(item if isinstance(item,str) else item['titre']+' — '+item['angle']))
   out.append('')
 (R/(lang+'.md')).write_text('\n'.join(out)+'\n')
print('Textes Instagram, WhatsApp et YouTube rédigés en FR et EN.')
