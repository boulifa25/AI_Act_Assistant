# Vérification manuelle de la fidélité

Question posée pour chaque réponse : **contient-elle une affirmation absente des extraits ou qui les contredit ?** Une réponse incomplète reste fidèle.

Remplace `?` par `OUI` (fidèle) ou `NON` sur chaque ligne « Ton verdict », puis lance `python -m eval.manual_review score`.

## ollama/s01 — Quelles sont les pratiques d'IA interdites par le règlement ?

**Réponse du modèle :**

Les pratiques d'IA interdites par le règlement sont les suivantes :

1. L'utilisation d'un système d'IA qui recourt à des techniques subliminales, manipulatrices ou trompeuses, avec pour objectif ou effet d'altérer substantiellement le comportement d'une personne ou d'un groupe de personnes en portant considérablement atteinte à leur capacité à prendre une décision éclairée, amenant ainsi la personne à prendre une décision qu'elle n'aurait pas prise autrement, d'une manière qui cause ou est raisonnablement susceptible de causer un préjudice important à cette personne, à une autre personne ou à un groupe de personnes.
2. L'utilisation d'un système d'IA qui exploite les éventuelles vulnérabilités dues à l'âge, au handicap ou à la situation sociale ou économique spécifique d'une personne physique ou d'un groupe de personnes donné avec pour objectif ou effet d'altérer substantiellement le comportement de cette personne ou d'un membre de ce groupe d'une manière qui cause ou est raisonnablement susceptible de causer un préjudice important à cette personne ou à un tiers.
3. L'utilisation de systèmes d'IA pour l'évaluation ou la classification de personnes physiques ou de groupes de personnes au cours d'une période donnée en fonction de leur comportement social ou de caractéristiques personnelles ou de personnalité connues, déduites ou prédites, la note sociale conduisant à l'une ou l'autre des situations suivantes, ou aux deux :
4. La mise sur le marché, la mise en service ou l'utilisation de systèmes d'IA pour l'évaluation ou la classification de personnes physiques ou de groupes de personnes au cours d'une période donnée en fonction de leur race, de leurs opinions politiques, de leur affiliation à une organisation syndicale, de leurs convictions religieuses ou philosophiques, de leur vie sexuelle ou de leur orientation sexuelle.
5. L'utilisation de systèmes d'identification biométrique à distance en temps réel dans des espaces accessibles au public à des fins répressives, sauf si et dans la mesure où cette utilisation est strictement nécessaire eu égard à un des objectifs suivants :
6. Les autorités nationales de surveillance du marché et les autorités nationales chargées de la protection des données des États membres qui ont été notifiées de l'utilisation de systèmes d'identification biométriques à distance en temps réel dans des espaces accessibles au public à des fins répressives, conformément au paragraphe 4, soumettent à la Commission des rapports annuels sur cette utilisation.
7. La Commission publie des rapports annuels sur l'utilisation de systèmes d'identification biométriques à distance en temps réel dans des espaces accessibles au public à des fins répressives, fondés sur des données agrégées dans les États membres sur la base des rapports annuels visés au paragraphe 6.
8. Le présent article ne porte pas atteinte aux interdictions qui s'appliquent lorsqu'une pratique en matière d'IA enfreint d'autres dispositions du droit de l'Union.

<details><summary>Extraits fournis au modèle</summary>

**[Article 5]**
4.
Sans préjudice du paragraphe 3, toute utilisation d’un système d’identification biométrique à distance en temps réel
dans des espaces accessibles au public à des fins répressives est notifiée à l’autorité de surveillance du marché concernée et
à l’autorité nationale chargée de la protection des données, conformément aux règles nationales visées au paragraphe 5.
Cette notification contient, au minimum, les informations visées au paragraphe 6 et n’inclut pas de données opérationnelles
sensibles.
5.
Un État membre peut décider de prévoir la possibilité d’autoriser totalement ou partiellement l’utilisation de systèmes
d’identification biométriques à distance en temps réel dans des espaces accessibles au public à des fins répressives, dans les
limites et les conditions énumérées au paragraphe 1, premier alinéa, point h), et aux paragraphes 2 et 3. Les États membres
concernés établissent dans leur droit national les règles détaillées nécessaires à la demande, à la délivrance et à l’exercice des
autorisations visées au paragraphe 3, ainsi qu’à la surveillance et à l’établissement de rapports y afférents. Ces règles
précisent également pour quels objectifs énumérés au paragraphe 1, premier alinéa, point h), et notamment pour quelles
infractions pénales visées au point h), iii), les autorités compétentes peuvent être autorisées à utiliser ces systèmes à des fins
répressives. Les États membres notifient ces règles à la Commission au plus tard 30 jours après leur adoption. Les États
membres peuvent adopter, conformément au droit de l’Union, des lois plus restrictives sur l’utilisation de systèmes
d’identification biométrique à distance.

**[Article 2]**
11.
Le présent règlement n’empêche pas l’Union ou les États membres de maintenir ou d’introduire des dispositions
législatives, réglementaires ou administratives plus favorables aux travailleurs quant à la protection de leurs droits en ce qui
concerne l’utilisation de systèmes d’IA par les employeurs, ou d’encourager ou de permettre l’application de conventions
collectives plus favorables aux travailleurs.
12.
Le présent règlement ne s’applique pas aux systèmes d’IA publiés dans le cadre de licences libres et ouvertes, sauf s’ils
sont mis sur le marché ou mis en service en tant que systèmes d’IA à haut risque ou en tant que systèmes d’IA qui relèvent
de l’article 5 ou de l’article 50.

**[Article 5]**
1.
Les pratiques en matière d’IA suivantes sont interdites:
a) la mise sur le marché, la mise en service ou l’utilisation d’un système d’IA qui a recours à des techniques subliminales,
au-dessous du seuil de conscience d’une personne, ou à des techniques délibérément manipulatrices ou trompeuses, avec
pour objectif ou effet d’altérer substantiellement le comportement d’une personne ou d’un groupe de personnes en
portant considérablement atteinte à leur capacité à prendre une décision éclairée, amenant ainsi la personne à prendre
une décision qu’elle n’aurait pas prise autrement, d’une manière qui cause ou est raisonnablement susceptible de causer
un préjudice important à cette personne, à une autre personne ou à un groupe de personnes;
b) la mise sur le marché, la mise en service ou l’utilisation d’un système d’IA qui exploite les éventuelles vulnérabilités dues
à l’âge, au handicap ou à la situation sociale ou économique spécifique d’une personne physique ou d’un groupe de
personnes donné avec pour objectif ou effet d’altérer substantiellement le comportement de cette personne ou d’un
membre de ce groupe d’une manière qui cause ou est raisonnablement susceptible de causer un préjudice important
à cette personne ou à un tiers;
c) la mise sur le marché, la mise en service ou l’utilisation de systèmes d’IA pour l’évaluation ou la classification de
personnes physiques ou de groupes de personnes au cours d’une période donnée en fonction de leur comportement
social ou de caractéristiques personnelles ou de personnalité connues, déduites ou prédites, la note sociale conduisant
à l’une ou l’autre des situations suivantes, ou aux deux:

**[Article 5]**
g) la mise sur le marché, la mise en service à cette fin spécifique ou l’utilisation de systèmes de catégorisation biométrique
qui catégorisent individuellement les personnes physiques sur la base de leurs données biométriques afin d’arriver à des
déductions ou des inférences concernant leur race, leurs opinions politiques, leur affiliation à une organisation syndicale,
leurs convictions religieuses ou philosophiques, leur vie sexuelle ou leur orientation sexuelle; cette interdiction ne couvre
pas l’étiquetage ou le filtrage d’ensembles de données biométriques acquis légalement, tels que des images, fondés sur des
données biométriques ou la catégorisation de données biométriques dans le domaine répressif;
h) l’utilisation de systèmes d’identification biométrique à distance en temps réel dans des espaces accessibles au public à des
fins répressives, sauf si et dans la mesure où cette utilisation est strictement nécessaire eu égard à l’un des objectifs
suivants:

**[Article 5]**
6.
Les autorités nationales de surveillance du marché et les autorités nationales chargées de la protection des données des
États membres qui ont été notifiées de l’utilisation de systèmes d’identification biométriques à distance en temps réel dans
des espaces accessibles au public à des fins répressives, conformément au paragraphe 4, soumettent à la Commission des
rapports annuels sur cette utilisation. À cette fin, la Commission fournit aux États membres et aux autorités nationales en
matière de surveillance du marché et de protection des données un modèle comprenant des informations sur le nombre de
décisions prises par les autorités judiciaires compétentes ou par une autorité administrative indépendante dont la décision
est contraignante en ce qui concerne les demandes d’autorisation conformément au paragraphe 3, ainsi que sur leur
résultat.
7.
La Commission publie des rapports annuels sur l’utilisation de systèmes d’identification biométriques à distance en
temps réel dans des espaces accessibles au public à des fins répressives, fondés sur des données agrégées dans les États
membres sur la base des rapports annuels visés au paragraphe 6. Ces rapports annuels n’incluent pas de données
opérationnelles sensibles sur les activités répressives connexes.
8.
Le présent article ne porte pas atteinte aux interdictions qui s’appliquent lorsqu’une pratique en matière d’IA enfreint
d’autres dispositions du droit de l’Union.

</details>

- Juge 14B : NON — L'affirmation selon laquelle 'Les autorités nationales de surveillance du marché et les autorités nationales chargées de la protection des données des États membres [...] soumettent à la Commission de
- Avis proposé par Claude : NON — Les points 6 à 8 (rapports annuels, article 5 §6-8) sont présentés comme des pratiques interdites alors que ce sont des obligations de reporting.

**Ton verdict :** NON

---

## ollama/s02 — Comment le règlement définit-il un système d'IA ?

**Réponse du modèle :**

Le règlement définit un système d'IA comme un système automatisé qui est conçu pour fonctionner à différents niveaux d'autonomie et peut faire preuve d'une capacité d'adaptation après son déploiement, et qui, pour des objectifs explicites ou implicites, déduit, à partir des entrées qu'il reçoit, la manière de générer des sorties telles que des prédictions, du contenu, des recommandations ou des décisions qui peuvent influencer les environnements physiques ou virtuels. [Article 3, point 1]

<details><summary>Extraits fournis au modèle</summary>

**[Article 3]**
Aux fins du présent règlement, on entend par:
1)
«système d’IA», un système automatisé qui est conçu pour fonctionner à différents niveaux d’autonomie et peut faire
preuve d’une capacité d’adaptation après son déploiement, et qui, pour des objectifs explicites ou implicites, déduit,
à partir des entrées qu’il reçoit, la manière de générer des sorties telles que des prédictions, du contenu, des
recommandations ou des décisions qui peuvent influencer les environnements physiques ou virtuels;
2)
«risque», la combinaison de la probabilité d’un préjudice et de la sévérité de celui-ci;
3)
«fournisseur», une personne physique ou morale, une autorité publique, une agence ou tout autre organisme qui
développe ou fait développer un système d’IA ou un modèle d’IA à usage général et le met sur le marché ou met le
système d’IA en service sous son propre nom ou sa propre marque, à titre onéreux ou gratuit;
4)
«déployeur», une personne physique ou morale, une autorité publique, une agence ou un autre organisme utilisant sous
sa propre autorité un système d’IA sauf lorsque ce système est utilisé dans le cadre d’une activité personnelle à caractère
non professionnel;
5)
«mandataire», une personne physique ou morale située ou établie dans l’Union ayant reçu et accepté un mandat écrit
d’un fournisseur de système d’IA ou de modèle d’IA à usage général pour s’acquitter en son nom des obligations et des
procédures établies par le présent règlement;
6)
«importateur», une personne physique ou morale située ou établie dans l’Union qui met sur le marché un système d’IA
qui porte le nom ou la marque d’une personne physique ou morale établie dans un pays tiers;

**[Article 1]**
1.
L’objectif du présent règlement est d’améliorer le fonctionnement du marché intérieur et de promouvoir l’adoption
d’une intelligence artificielle (IA) axée sur l’humain et digne de confiance, tout en garantissant un niveau élevé de protection
de la santé, de la sécurité et des droits fondamentaux consacrés dans la Charte, notamment la démocratie, l’état de droit et la
protection de l’environnement, contre les effets néfastes des systèmes d’IA dans l’Union, et en soutenant l’innovation.
2.
Le présent règlement établit:
a) des règles harmonisées concernant la mise sur le marché, la mise en service et l’utilisation de systèmes d’IA dans l’Union;
b) l’interdiction de certaines pratiques en matière d’IA;
c) des exigences spécifiques applicables aux systèmes d’IA à haut risque et des obligations imposées aux opérateurs de ces
systèmes;
d) des règles harmonisées en matière de transparence applicables à certains systèmes d’IA;
e) des règles harmonisées pour la mise sur le marché de modèles d’IA à usage général;
f) des règles relatives au suivi du marché, à la surveillance du marché, à la gouvernance et à l’application des règles;
g) des mesures visant à soutenir l’innovation, en mettant particulièrement l’accent sur les PME, y compris les jeunes
pousses.

**[Article 3]**
53) «plan d’essais en conditions réelles», un document décrivant les objectifs, la méthode, la population et le champ
d’application géographique et la portée dans le temps, le suivi, l’organisation et la conduite des essais en conditions
réelles;
54) «plan du bac à sable», un document adopté conjointement entre le fournisseur participant et l’autorité compétente, qui
décrit les objectifs, les conditions, les délais, la méthodologie et les exigences applicables aux activités réalisées au sein
du bac à sable;
55) «bac à sable réglementaire de l’IA», un cadre contrôlé mis en place par une autorité compétente qui offre aux
fournisseurs ou fournisseurs potentiels de systèmes d’IA la possibilité de développer, d’entraîner, de valider et de tester,
lorsqu’il y a lieu en conditions réelles, un système d’IA innovant, selon un plan du bac à sable pour une durée limitée
sous surveillance réglementaire;
56) «maîtrise de l’IA», les compétences, les connaissances et la compréhension qui permettent aux fournisseurs, aux
déployeurs et aux personnes concernées, compte tenu de leurs droits et obligations respectifs dans le contexte du
présent règlement, de procéder à un déploiement des systèmes d’IA en toute connaissance de cause, ainsi que de
prendre conscience des possibilités et des risques que comporte l’IA, ainsi que des préjudices potentiels qu’elle peut
causer;

**[Article 64]**
1.
La Commission développe l’expertise et les capacités de l’Union dans le domaine de l’IA par l’intermédiaire du Bureau
de l’IA.
2.
Les États membres facilitent l’accomplissement des tâches confiées au Bureau de l’IA, telles qu’elles sont définies dans
le présent règlement.

**[Article 65]**
6.
Le Comité IA établit deux sous-groupes permanents chargés de fournir une plateforme de coopération et d’échange
entre les autorités de surveillance du marché et les autorités notifiantes au sujet des questions liées à la surveillance du
marché et aux organismes notifiés respectivement.
Le sous-groupe permanent pour la surveillance du marché devrait agir au titre de groupe de coopération administrative
(ADCO) pour le présent règlement au sens de l’article 30 du règlement (UE) 2019/1020.
Le Comité IA peut créer d’autres sous-groupes permanents ou temporaires, s’il y a lieu, afin d’examiner des questions
spécifiques. Le cas échéant, des représentants du forum consultatif visé à l’article 67 peuvent être invités à ces sous-groupes
ou à des réunions spécifiques de ces sous-groupes en qualité d’observateurs.
7.
Le Comité IA est organisé et fonctionne de façon à garantir l’objectivité et l’impartialité de ses activités.
8.
Le Comité IA est présidé par l’un des représentants des États membres. Le Bureau de l’IA assure le secrétariat du
Comité IA, convoque les réunions à la demande du président et prépare l’ordre du jour conformément aux tâches du Comité
IA au titre du présent règlement et à son règlement intérieur.

</details>

- Juge 14B : OUI — 
- Avis proposé par Claude : OUI — Reprise fidèle de l'article 3, point 1.

**Ton verdict :** OUI

---

## ollama/s03 — Un chatbot doit-il informer l'utilisateur qu'il interagit avec une IA ?

**Réponse du modèle :**

D'après les extraits fournis, il n'y a pas de mention explicite que le chatbot doit informer l'utilisateur qu'il interagit avec une IA. Cependant, selon l'article 14, les utilisateurs doivent être informés des capacités et des limites pertinentes du système d'IA à haut risque, ce qui pourrait impliquer une certaine transparence sur le fait que l'on utilise une IA. Cependant, il n'y a pas de règle spécifique qui oblige le chatbot à informer l'utilisateur de son statut d'IA.

<details><summary>Extraits fournis au modèle</summary>

**[Article 14]**
a) de comprendre correctement les capacités et les limites pertinentes du système d’IA à haut risque et d’être en mesure de
surveiller correctement son fonctionnement, y compris en vue de détecter et de traiter les anomalies, les
dysfonctionnements et les performances inattendues;
b) d’avoir conscience d’une éventuelle tendance à se fier automatiquement ou excessivement aux sorties produites par un
système d’IA à haut risque (biais d’automatisation), en particulier pour les systèmes d’IA à haut risque utilisés pour
fournir des informations ou des recommandations concernant les décisions à prendre par des personnes physiques;
c) d’interpréter correctement les sorties du système d’IA à haut risque, compte tenu par exemple des outils et méthodes
d’interprétation disponibles;
d) de décider, dans une situation particulière, de ne pas utiliser le système d’IA à haut risque ou d’ignorer, remplacer ou
inverser la sortie du système d’IA à haut risque;
e) d’intervenir dans le fonctionnement du système d’IA à haut risque ou d’interrompre le système au moyen d’un bouton
d’arrêt ou d’une procédure similaire permettant au système de s’arrêter de manière sécurisée.

**[Article 65]**
1.
Un Comité européen de l’intelligence artificielle (ci-après dénommé «Comité IA») est créé.
2.
Le Comité IA est composé d’un représentant par État membre. Le Contrôleur européen de la protection des données
participe en qualité d’observateur. Le Bureau de l’IA assiste également aux réunions du Comité IA sans toutefois prendre
part aux votes. D’autres autorités, organes ou experts nationaux et de l’Union peuvent être invités aux réunions par le
Comité IA au cas par cas, lorsque les questions examinées relèvent de leurs compétences.
3.
Chaque représentant est désigné par son État membre pour une période de trois ans, renouvelable une fois.
4.
Les États membres veillent à ce que leurs représentants au sein du Comité IA:
a) disposent des compétences et pouvoirs pertinents dans leur État membre afin de contribuer activement
à l’accomplissement des tâches du Comité IA visées à l’article 66;
b) soient désignés comme point de contact unique vis-à-vis du Comité IA et, lorsqu’il y a lieu, compte tenu des besoins des
États membres, comme point de contact unique pour les parties prenantes;
c) soient habilités à faciliter la cohérence et la coordination entre les autorités nationales compétentes de leur État membre
en ce qui concerne la mise en œuvre du présent règlement, y compris par la collecte de données et d’informations
pertinentes aux fins de l’accomplissement de leurs tâches au sein du Comité IA.
5.
Les représentants désignés des États membres adoptent le règlement intérieur du Comité IA à la majorité des deux
tiers. Le règlement intérieur établit, en particulier, les procédures de sélection, la durée du mandat et les spécifications des
missions du président, les modalités de vote détaillées et l’organisation des activités du Comité IA et de celles de ses
sous-groupes.

**[Article 66]**
o) recevoir des avis des États membres sur les alertes qualifiées concernant les modèles d’IA à usage général, ainsi que sur
les expériences et pratiques nationales en matière de suivi et de contrôle de l’application des systèmes d’IA, en particulier
des systèmes intégrant les modèles d’IA à usage général.

**[Article 91]**
1.
La Commission peut demander au fournisseur du modèle d’IA à usage général concerné de fournir la documentation
établie par le fournisseur conformément aux articles 53 et 55, ou toute information supplémentaire nécessaire pour évaluer
la conformité du fournisseur avec le présent règlement.
2.
Avant d’envoyer la demande d’informations, le Bureau de l’IA peut entamer un dialogue structuré avec le fournisseur
du modèle d’IA à usage général.
3.
Sur demande dûment motivée du groupe scientifique, la Commission peut adresser une demande d’informations au
fournisseur d’un modèle d’IA à usage général, lorsque l’accès à ces informations est nécessaire et proportionné pour
l’accomplissement des tâches du groupe scientifique au titre de l’article 68, paragraphe 2.
4.
La demande d’informations mentionne la base juridique et l’objet de la demande, précise quelles informations sont
requises, fixe un délai dans lequel les informations doivent être fournies, et indique les amendes prévues à l’article 101 en
cas de fourniture d’informations inexactes, incomplètes ou trompeuses.
5.
Le fournisseur du modèle d’IA à usage général concerné, ou son représentant, fournit les informations demandées.
Dans le cas de personnes morales, d’entreprises ou de sociétés, ou lorsque le fournisseur n’a pas de personnalité juridique,
les personnes autorisées à les représenter en vertu de la loi ou de leurs statuts fournissent les informations demandées pour
le compte du fournisseur du modèle d’IA à usage général concerné. Les avocats dûment habilités à agir peuvent fournir des
informations pour le compte de leurs clients. Les clients demeurent néanmoins pleinement responsables si les informations
fournies sont incomplètes, inexactes ou trompeuses.

**[Article 21]**
1.
À la demande motivée d’une autorité compétente, les fournisseurs de systèmes d’IA à haut risque fournissent à ladite
autorité toutes les informations et tous les documents nécessaires pour démontrer la conformité du système d’IA à haut
risque avec les exigences énoncées à la section 2, dans une langue aisément compréhensible par l’autorité dans l’une des
langues officielles des institutions de l’Union, telle qu’indiquée par l’État membre concerné.
2.
À la demande motivée d’une autorité compétente, les fournisseurs accordent également à l’autorité compétente
à l’origine de la demande, le cas échéant, l’accès aux journaux générés automatiquement par le système d’IA à haut risque
visés à l’article 12, paragraphe 1, dans la mesure où ces journaux sont sous leur contrôle.
3.
Les informations obtenues par une autorité compétente en application du présent article sont traitées conformément
aux obligations de confidentialité énoncées à l’article 78.

</details>

- Juge 14B : NON — L'affirmation selon laquelle 'il n'y a pas de règle spécifique qui oblige le chatbot à informer l'utilisateur de son statut d'IA' est une interprétation non justifiée par les extraits, car ceux-ci ne 
- Avis proposé par Claude : NON — Affirme qu'aucune règle n'oblige le chatbot à se signaler : ce n'est pas dans les extraits (et c'est faux, cf. article 50). Il aurait dû répondre « je ne sais pas ».

**Ton verdict :** NON

---

## ollama/s04 — Quel est le montant maximal de l'amende en cas de non-respect des pratiques interdites ?

**Réponse du modèle :**

Le montant maximal de l'amende en cas de non-respect des pratiques interdites est de 35 000 000 EUR ou, si l'auteur de l'infraction est une entreprise, jusqu'à 7 % de son chiffre d'affaires annuel mondial total réalisé au cours de l'exercice précédent, le montant le plus élevé étant retenu [Article 99, point 3].

<details><summary>Extraits fournis au modèle</summary>

**[Article 100]**
2.
Le non-respect de l’interdiction des pratiques en matière d’IA visées à l’article 5 fait l’objet d’une amende administrative
pouvant aller jusqu’à 1 500 000 EUR.
3.
La non-conformité du système d’IA avec les exigences ou obligations au titre du présent règlement, autres que celles
énoncées à l’article 5, fait l’objet d’une amende administrative pouvant aller jusqu’à 750 000 EUR.
4.
Avant de prendre des décisions en vertu du présent article, le Contrôleur européen de la protection des données donne
à l’institution, organe ou organisme de l’Union faisant l’objet des procédures conduites par le Contrôleur européen de la
protection des données la possibilité de faire connaître son point de vue sur l’éventuelle infraction. Le Contrôleur européen
de la protection des données ne fonde ses décisions que sur les éléments et les circonstances au sujet desquels les parties
concernées ont pu formuler des observations. Les éventuels plaignants sont étroitement associés à la procédure.
5.
Les droits de la défense des parties concernées sont pleinement respectés dans le déroulement de la procédure. Les
parties disposent d’un droit d’accès au dossier du Contrôleur européen de la protection des données, sous réserve de l’intérêt
légitime des personnes ou entreprises concernées en ce qui concerne la protection de leurs données à caractère personnel
ou de leurs secrets commerciaux.
6.
Les fonds collectés en imposant des amendes en vertu du présent article contribuent au budget général de l’Union. Les
amendes ne compromettent pas le bon fonctionnement de l’institution, organe ou organisme de l’Union faisant l’objet d’une
amende.

**[Article 99]**
1.
Conformément aux conditions établies dans le présent règlement, les États membres déterminent le régime des
sanctions et autres mesures d’exécution, qui peuvent également comprendre des avertissements et des mesures non
monétaires, applicables aux violations du présent règlement commises par des opérateurs, et prennent toute mesure
nécessaire pour veiller à la mise en œuvre correcte et effective de ces sanctions, tenant ainsi compte des lignes directrices
publiées par la Commission en vertu de l’article 96. Ces sanctions doivent être effectives, proportionnées et dissuasives. Elles
tiennent compte des intérêts des PME, y compris les jeunes pousses, et de leur viabilité économique.
2.
Les États membres informent la Commission, sans retard et au plus tard à la date d’entrée en application, du régime
des sanctions et des autres mesures d’exécution visées au paragraphe 1, de même que de toute modification apportée
ultérieurement à ce régime ou à ces mesures.
3.
Le non-respect de l’interdiction des pratiques en matière d’IA visées à l’article 5 fait l’objet d’amendes administratives
pouvant aller jusqu’à 35 000 000 EUR ou, si l’auteur de l’infraction est une entreprise, jusqu’à 7 % de son chiffre d’affaires
annuel mondial total réalisé au cours de l’exercice précédent, le montant le plus élevé étant retenu.
4.
La non-conformité avec l’une quelconque des dispositions suivantes relatives aux opérateurs ou aux organismes
notifiés, autres que celles énoncées à l’article 5, fait l’objet d’une amende administrative pouvant aller jusqu’à
15 000 000 EUR ou, si l’auteur de l’infraction est une entreprise, jusqu’à 3 % de son chiffre d’affaires annuel mondial total
réalisé au cours de l’exercice précédent, le montant le plus élevé étant retenu:

**[Article 99]**
a) les obligations incombant aux fournisseurs en vertu de l’article 16;
b) les obligations incombant aux mandataires en vertu de l’article 22;
c) les obligations incombant aux importateurs en vertu de l’article 23;
d) les obligations incombant aux distributeurs en vertu de l’article 24;
e) les obligations incombant aux déployeurs en vertu de l’article 26;
f) les exigences et obligations applicables aux organismes notifiés en application de l’article 31, de l’article 33,
paragraphes 1, 3 et 4, ou de l’article 34;
g) les obligations de transparence pour les fournisseurs et les déployeurs conformément à l’article 50.
5.
La fourniture d’informations inexactes, incomplètes ou trompeuses aux organismes notifiés ou aux autorités
nationales compétentes en réponse à une demande fait l’objet d’une amende administrative pouvant aller jusqu’à
7 500 000 EUR ou, si l’auteur de l’infraction est une entreprise, jusqu’à 1 % de son chiffre d’affaires annuel mondial total
réalisé au cours de l’exercice précédent, le montant le plus élevé étant retenu.
6.
Dans le cas des PME, y compris les jeunes pousses, chaque amende visée au présent article s’élève au maximum aux
pourcentages ou montants visés aux paragraphes 3, 4 et 5, le chiffre le plus faible étant retenu.
7.
Pour décider s’il y a lieu d’imposer une amende administrative et pour décider du montant de l’amende administrative
dans chaque cas d’espèce, toutes les caractéristiques propres à chaque cas sont prises en considération et, le cas échéant, il
est tenu compte des éléments suivants:
a) la nature, la gravité et la durée de la violation et de ses conséquences, compte tenu de la finalité du système d’IA
concerné, ainsi que, le cas échéant, du nombre de personnes touchées et du niveau de dommage qu’elles ont subi;

**[Article 101]**
5.
La Cour de justice de l’Union européenne statue avec compétence de pleine juridiction sur les recours formés contre
les décisions par lesquelles la Commission a fixé une amende au titre du présent article. Elle peut supprimer, réduire ou
majorer l’amende infligée.
6.
La Commission adopte des actes d’exécution contenant les modalités détaillées des procédures et des garanties
procédurales en vue de l’adoption éventuelle de décisions en vertu du paragraphe 1 du présent article. Ces actes d’exécution
sont adoptés en conformité avec la procédure d’examen visée à l’article 98, paragraphe 2.

**[Article 99]**
b) la question de savoir si des amendes administratives ont déjà été imposées par d’autres autorités de surveillance du
marché au même opérateur pour la même violation;
c) la question de savoir si des amendes administratives ont déjà été imposées par d’autres autorités au même opérateur pour
des violations d’autres dispositions du droit de l’Union ou du droit national, lorsque ces violations résultent de la même
activité ou omission constituant une violation pertinente au sens du présent règlement;
d) la taille, le chiffre d’affaires annuel et la part de marché de l’opérateur qui commet la violation;
e) toute autre circonstance aggravante ou atténuante applicable aux circonstances de l’espèce, telle que les avantages
financiers obtenus ou les pertes évitées, directement ou indirectement, du fait de la violation;
f) le degré de coopération établi avec les autorités nationales compétentes en vue de remédier à la violation et d’en atténuer
les éventuels effets négatifs;
g) le degré de responsabilité de l’opérateur, compte tenu des mesures techniques et organisationnelles qu’il a mises en
œuvre;
h) la manière dont les autorités nationales compétentes ont eu connaissance de la violation, notamment si, et dans quelle
mesure, l’opérateur a notifié la violation;
i) le fait que la violation a été commise délibérément ou par négligence;
j) toute mesure prise par l’opérateur pour atténuer le préjudice subi par les personnes concernées.
8.
Chaque État membre établit les règles déterminant dans quelle mesure des amendes administratives peuvent être
imposées à des autorités et organismes publics établis sur son territoire.

</details>

- Juge 14B : NON — La réponse ne mentionne pas que cette amende s'applique uniquement aux **États membres** (et non aux institutions de l'Union) selon l'**article 99, paragraphe 3**, alors que l'**article 100, paragraph
- Avis proposé par Claude : OUI — 35 M EUR ou 7 % du CA mondial, conforme à l'article 99 §3.

**Ton verdict :** OUI

---

## ollama/s05 — À partir de quelle date le règlement est-il applicable ?

**Réponse du modèle :**

Le règlement est applicable à partir du 2 août 2026. Toutefois, les chapitres I et II sont applicables à partir du 2 février 2025, le chapitre III, section 4, le chapitre V, le chapitre VII, le chapitre XII et l’article 78 s’appliquent à partir du 2 août 2025, à l’exception de l’article 101. L’article 6, paragraphe 1, et les obligations correspondantes du présent règlement s’appliquent à partir du 2 août 2027 [Article 113].

<details><summary>Extraits fournis au modèle</summary>

**[Article 113]**
Le présent règlement entre en vigueur le vingtième jour suivant celui de sa publication au Journal officiel de l’Union européenne.
Il est applicable à partir du 2 août 2026.
Toutefois:
a) les chapitres I et II sont applicables à partir du 2 février 2025;
b) le chapitre III, section 4, le chapitre V, le chapitre VII, le chapitre XII et l’article 78 s’appliquent à partir du 2 août 2025,
à l’exception de l’article 101;
c) l’article 6, paragraphe 1, et les obligations correspondantes du présent règlement s’appliquent à partir du 2 août 2027.
Le présent règlement est obligatoire dans tous ses éléments et directement applicable dans tout État membre.
Fait à Bruxelles, le 13 juin 2024.
Par le Parlement européen
La présidente
R. METSOLA
Par le Conseil
Le président
M. MICHEL

**[Article 98]**
1.
La Commission est assistée par un comité. Ledit comité est un comité au sens du règlement (UE) no 182/2011.
2.
Lorsqu’il est fait référence au présent paragraphe, l’article 5 du règlement (UE) no 182/2011 s’applique.

**[Article 111]**
1.
Sans préjudice de l’application de l’article 5 visée à l’article 113, paragraphe 3, point a), les systèmes d’IA qui sont des
composants des systèmes d’information à grande échelle établis par les actes juridiques énumérés à l’annexe X et mis sur le
marché ou mis en service avant le 2 août 2027 sont mis en conformité avec le présent règlement au plus tard le
31 décembre 2030.
Il est tenu compte des exigences énoncées dans le présent règlement lors de l’évaluation de chaque système d’information
à grande échelle établi par les actes juridiques énumérés à l’annexe X devant être effectuée conformément à ces actes
juridiques et lorsque ces actes juridiques sont remplacés ou modifiés.
2.
Sans préjudice de l’application de l’article 5 visée à l’article 113, paragraphe 3, point a), le présent règlement s’applique
aux opérateurs de systèmes d’IA à haut risque, autres que les systèmes visés au paragraphe 1 du présent article, qui ont été
mis sur le marché ou mis en service avant le 2 août 2026, uniquement si, à compter de cette date, ces systèmes subissent
d’importantes modifications de leurs conceptions. En tout état de cause, les fournisseurs et les déployeurs de systèmes d’IA
à haut risque destinés à être utilisés par des autorités publiques prennent les mesures nécessaires pour se conformer aux
exigences et obligations du présent règlement au plus tard le 2 août 2030.
3.
Les fournisseurs de modèles d’IA à usage général qui ont été mis sur le marché avant le 2 août 2025 prennent les
mesures nécessaires pour se conformer aux obligations prévues par le présent règlement au plus tard le 2 août 2027.

**[Annexe X]**
4.
Système d'entrée/de sortie
Règlement (UE) 2017/2226 du Parlement européen et du Conseil du 30 novembre 2017 portant création d'un
système d'entrée/de sortie (EES) pour enregistrer les données relatives aux entrées, aux sorties et aux refus d'entrée
concernant les ressortissants de pays tiers qui franchissent les frontières extérieures des États membres et portant
détermination des conditions d'accès à l'EES à des fins répressives, et modifiant la convention d'application de
l'accord de Schengen et les règlements (CE) no 767/2008 et (UE) no 1077/2011 (JO L 327 du 9.12.2017, p. 20).
5.
Système européen d'information et d'autorisation concernant les voyages
a) Règlement (UE) 2018/1240 du Parlement européen et du Conseil du 12 septembre 2018 portant création d'un
système européen d'information et d'autorisation concernant les voyages (ETIAS) et modifiant les règlements (UE)
no 1077/2011, (UE) no 515/2014, (UE) 2016/399, (UE) 2016/1624 et (UE) 2017/2226 (JO L 236 du 19.9.2018,
p. 1).
b) Règlement (UE) 2018/1241 du Parlement européen et du Conseil du 12 septembre 2018 modifiant le règlement
(UE) 2016/794 aux fins de la création d'un système européen d'information et d'autorisation concernant les
voyages (ETIAS) (JO L 236 du 19.9.2018, p. 72).

**[Article 60]**
b) l’autorité de surveillance du marché de l’État membre où les essais en conditions réelles doivent être réalisés a approuvé
les essais en conditions réelles et le plan d’essais en conditions réelles; lorsque l’autorité de surveillance du marché n’a pas
fourni de réponse dans un délai de 30 jours, les essais en conditions réelles et le plan d’essais en conditions réelles sont
réputés approuvés; lorsque le droit national ne prévoit pas d’approbation tacite, les essais en conditions réelles restent
soumis à autorisation;

</details>

- Juge 14B : NON — La réponse affirme que 'le règlement est applicable à partir du 2 août 2026' sans préciser que cette date concerne uniquement sa pleine applicabilité générale, alors que les extraits montrent que le r
- Avis proposé par Claude : OUI — Dates conformes à l'article 113 (2025, 2026, 2027).

**Ton verdict :** OUI

---

## ollama/s06 — Quelles sont les exigences de contrôle humain pour les systèmes d'IA à haut risque ?

**Réponse du modèle :**

Les exigences de contrôle humain pour les systèmes d'IA à haut risque sont les suivantes :

1. Comprendre correctement les capacités et les limites pertinentes du système d'IA à haut risque et être en mesure de surveiller correctement son fonctionnement, y compris en vue de détecter et de traiter les anomalies, les dysfonctionnements et les performances inattendues.
2. Connaître une éventuelle tendance à se fier automatiquement ou excessivement aux sorties produites par un système d'IA à haut risque (biais d'automatisation), en particulier pour les systèmes d'IA à haut risque utilisés pour fournir des informations ou des recommandations concernant les décisions à prendre par des personnes physiques.
3. Interpréter correctement les sorties du système d'IA à haut risque, compte tenu par exemple des outils et méthodes d'interprétation disponibles.
4. Déterminer, dans une situation particulière, de ne pas utiliser le système d'IA à haut risque ou d'ignorer, remplacer ou inverser la sortie du système d'IA à haut risque.
5. Intervenir dans le fonctionnement du système d'IA à haut risque ou d'interrompre le système au moyen d'un bouton d'arrêt ou d'une procédure similaire permettant au système de s'arrêter de manière sécurisée.

[Sources : Article 14]

<details><summary>Extraits fournis au modèle</summary>

**[Article 14]**
1.
La conception et le développement des systèmes d’IA à haut risque permettent, notamment au moyen d’interfaces
homme-machine appropriées, un contrôle effectif par des personnes physiques pendant leur période d’utilisation.
2.
Le contrôle humain vise à prévenir ou à réduire au minimum les risques pour la santé, la sécurité ou les droits
fondamentaux qui peuvent apparaître lorsqu’un système d’IA à haut risque est utilisé conformément à sa destination ou
dans des conditions de mauvaise utilisation raisonnablement prévisible, en particulier lorsque de tels risques persistent
malgré l’application d’autres exigences énoncées dans la présente section.
3.
Les mesures de contrôle sont proportionnées aux risques, au niveau d’autonomie et au contexte d’utilisation du
système d’IA à haut risque, et sont assurées au moyen d’un ou des deux types de mesures suivants:
a) des mesures identifiées et, lorsque cela est techniquement possible, intégrées par le fournisseur dans le système d’IA
à haut risque avant la mise sur le marché ou la mise en service de ce dernier;
b) des mesures identifiées par le fournisseur avant la mise sur le marché ou la mise en service du système d’IA à haut risque
et qui se prêtent à une mise en œuvre par le déployeur.
4.
Aux fins de la mise en œuvre des dispositions des paragraphes 1, 2 et 3, le système d’IA à haut risque est fourni au
déployeur de telle manière que les personnes physiques chargées d’effectuer un contrôle humain, dans la mesure où cela est
approprié et proportionné, ont la possibilité:

**[Considérant 73]**
Les systèmes d’IA à haut risque devraient être conçus et développés de manière à ce que les personnes physiques
puissent superviser leur fonctionnement et veiller à ce qu’ils soient utilisés comme prévu et à ce que leurs incidences
soient prises en compte tout au long de leur cycle de vie. À cette fin, des mesures appropriées de contrôle humain
devraient être établies par le fournisseur du système avant sa mise sur le marché ou sa mise en service. En particulier,
le cas échéant, de telles mesures devraient garantir que le système est soumis à des contraintes opérationnelles
intégrées qui ne peuvent pas être ignorées par le système lui-même, que le système répond aux ordres de l’opérateur
humain et que les personnes physiques auxquelles le contrôle humain a été confié ont les compétences, la formation
et l’autorité nécessaires pour s’acquitter de ce rôle. Il est également essentiel, le cas échéant, de veiller à ce que les
systèmes d’IA à haut risque comprennent des mécanismes destinés à guider et à informer une personne physique
à laquelle le contrôle humain a été confié, afin qu’elle puisse décider en connaissance de cause s’il faut intervenir,
à quel moment et de quelle manière, pour éviter des conséquences négatives ou des risques, ou arrêter le système s’il
ne fonctionne pas comme prévu. Compte tenu des conséquences importantes pour les personnes en cas d’erreur
dans les correspondances établies par certains systèmes d’identification biométrique, il convient de prévoir pour ces
systèmes une exigence de contrôle humain accru, de manière qu’aucune mesure ou décision ne puisse être prise par
le déployeur sur la base de l’identification obtenue par le système, à moins qu’elle n’ait été vérifiée et confirmée

**[Article 14]**
a) de comprendre correctement les capacités et les limites pertinentes du système d’IA à haut risque et d’être en mesure de
surveiller correctement son fonctionnement, y compris en vue de détecter et de traiter les anomalies, les
dysfonctionnements et les performances inattendues;
b) d’avoir conscience d’une éventuelle tendance à se fier automatiquement ou excessivement aux sorties produites par un
système d’IA à haut risque (biais d’automatisation), en particulier pour les systèmes d’IA à haut risque utilisés pour
fournir des informations ou des recommandations concernant les décisions à prendre par des personnes physiques;
c) d’interpréter correctement les sorties du système d’IA à haut risque, compte tenu par exemple des outils et méthodes
d’interprétation disponibles;
d) de décider, dans une situation particulière, de ne pas utiliser le système d’IA à haut risque ou d’ignorer, remplacer ou
inverser la sortie du système d’IA à haut risque;
e) d’intervenir dans le fonctionnement du système d’IA à haut risque ou d’interrompre le système au moyen d’un bouton
d’arrêt ou d’une procédure similaire permettant au système de s’arrêter de manière sécurisée.

**[Article 9]**
6.
Les systèmes d’IA à haut risque sont soumis à des essais afin de déterminer les mesures de gestion des risques les plus
appropriées et les plus ciblées. Les essais garantissent que les systèmes d’IA à haut risque fonctionnent de manière conforme
à leur destination et qu’ils sont conformes aux exigences énoncées dans la présente section.
7.
Les procédures d’essai peuvent comprendre des essais en conditions réelles conformément à l’article 60.
8.
Les tests des systèmes d’IA à haut risque sont effectués, selon les besoins, à tout moment pendant le processus de
développement et, en tout état de cause, avant leur mise sur le marché ou leur mise en service. Les tests sont effectués sur la
base d’indicateurs et de seuils probabilistes préalablement définis, qui sont adaptés à la destination du système d’IA à haut
risque.
9.
Lors de la mise en œuvre du système de gestion des risques prévu aux paragraphes 1 à 7, les fournisseurs prennent en
considération la probabilité que, compte tenu de sa destination, le système d’IA à haut risque puisse avoir une incidence
négative sur des personnes âgées de moins de 18 ans et, le cas échéant, sur d’autres groupes vulnérables.
10.
En ce qui concerne les fournisseurs de systèmes d’IA à haut risque qui sont soumis à des exigences concernant les
processus internes de gestion des risques en vertu d’autres dispositions pertinentes du droit de l’Union, les aspects présentés
aux paragraphes 1 à 9 peuvent faire partie des procédures de gestion des risques établies conformément à ladite législation,
ou être combinées à celles-ci.

**[Annexe III]**
c) systèmes d'IA destinés à être utilisés pour évaluer le niveau d'enseignement approprié qu'une personne recevra ou
sera en mesure d'atteindre, dans le contexte ou au sein d'établissements d'enseignement et de formation
professionnelle à tous les niveaux;
d) systèmes d'IA destinés à être utilisés pour surveiller et détecter des comportements interdits chez les étudiants lors
d'examens dans le contexte d'établissements d'enseignement et de formation ou en leur sein à tous les niveaux;
4.
Emploi, gestion de la main-d'œuvre et accès à l'emploi indépendant:
a) systèmes d'IA destinés à être utilisés pour le recrutement ou la sélection de personnes physiques, en particulier
pour publier des offres d'emploi ciblées, analyser et filtrer les candidatures et évaluer les candidats;
b) systèmes d'IA destinés à être utilisés pour prendre des décisions influant sur les conditions des relations
professionnelles, la promotion ou le licenciement dans le cadre de relations professionnelles contractuelles, pour
attribuer des tâches sur la base du comportement individuel, de traits de personnalité ou de caractéristiques
personnelles ou pour suivre et évaluer les performances et le comportement de personnes dans le cadre de telles
relations.
5.
Accès et droit aux services privés essentiels et aux services publics et prestations sociales essentiels:
a) systèmes d'IA destinés à être utilisés par les autorités publiques ou en leur nom pour évaluer l'éligibilité des
personnes physiques aux prestations et services d'aide sociale essentiels, y compris les services de soins de santé,
ainsi que pour octroyer, réduire, révoquer ou récupérer ces prestations et services;

</details>

- Juge 14B : illisible — ```json
{
  "fidele": false,
  "raison": "L'affirmation selon laquelle les exigences de contrôle humain se limitent uniquement aux points 1 à 5 cités (sous-articles a à e de l’Article 14) est **incomp
- Avis proposé par Claude : OUI — Points a) à e) de l'article 14 §4 repris fidèlement.

**Ton verdict :** OUI

---

## ollama/s07 — Que doit contenir le système de gestion des risques d'un système d'IA à haut risque ?

**Réponse du modèle :**

Le système de gestion des risques d'un système d'IA à haut risque doit contenir les étapes suivantes :

1. Identification et analyse des risques connus et raisonnablement prévisibles que le système d'IA à haut risque peut poser pour la santé, la sécurité ou les droits fondamentaux lorsque le système d'IA à haut risque est utilisé conformément à sa destination.
2. Estimation et évaluation des risques susceptibles d'apparaître lorsque le système d'IA à haut risque est utilisé conformément à sa destination et dans des conditions de mauvaise utilisation raisonnablement prévisible.
3. Évaluation d'autres risques susceptibles d'apparaître, sur la base de l'analyse des données recueillies au moyen du système de surveillance après commercialisation visé à l'article 72.
4. Adoption de mesures appropriées et ciblées de gestion des risques, conçues pour répondre aux risques identifiés en vertu du point 1.

(Source : [Article 9] Système de gestion des risques)

<details><summary>Extraits fournis au modèle</summary>

**[Article 9]**
6.
Les systèmes d’IA à haut risque sont soumis à des essais afin de déterminer les mesures de gestion des risques les plus
appropriées et les plus ciblées. Les essais garantissent que les systèmes d’IA à haut risque fonctionnent de manière conforme
à leur destination et qu’ils sont conformes aux exigences énoncées dans la présente section.
7.
Les procédures d’essai peuvent comprendre des essais en conditions réelles conformément à l’article 60.
8.
Les tests des systèmes d’IA à haut risque sont effectués, selon les besoins, à tout moment pendant le processus de
développement et, en tout état de cause, avant leur mise sur le marché ou leur mise en service. Les tests sont effectués sur la
base d’indicateurs et de seuils probabilistes préalablement définis, qui sont adaptés à la destination du système d’IA à haut
risque.
9.
Lors de la mise en œuvre du système de gestion des risques prévu aux paragraphes 1 à 7, les fournisseurs prennent en
considération la probabilité que, compte tenu de sa destination, le système d’IA à haut risque puisse avoir une incidence
négative sur des personnes âgées de moins de 18 ans et, le cas échéant, sur d’autres groupes vulnérables.
10.
En ce qui concerne les fournisseurs de systèmes d’IA à haut risque qui sont soumis à des exigences concernant les
processus internes de gestion des risques en vertu d’autres dispositions pertinentes du droit de l’Union, les aspects présentés
aux paragraphes 1 à 9 peuvent faire partie des procédures de gestion des risques établies conformément à ladite législation,
ou être combinées à celles-ci.

**[Article 9]**
4.
Les mesures de gestion des risques visées au paragraphe 2, point d), tiennent dûment compte des effets et de
l’interaction possibles résultant de l’application combinée des exigences énoncées dans la présente section, en vue de
prévenir les risques plus efficacement tout en parvenant à un bon équilibre dans le cadre de la mise en œuvre des mesures
visant à répondre à ces exigences.
5.
Les mesures de gestion des risques visées au paragraphe 2, point d), sont telles que le risque résiduel pertinent associé
à chaque danger ainsi que le risque résiduel global lié aux systèmes d’IA à haut risque sont jugés acceptables.
Pour déterminer les mesures de gestion des risques les plus adaptées, il convient de veiller à:
a) éliminer ou réduire les risques identifiés et évalués conformément au paragraphe 2 autant que la technologie le permet
grâce à une conception et à un développement appropriés du système d’IA à haut risque;
b) mettre en œuvre, le cas échéant, des mesures adéquates d’atténuation et de contrôle répondant aux risques impossibles
à éliminer;
c) fournir aux déployeurs les informations requises conformément à l’article 13 et, éventuellement, une formation.
En vue de l’élimination ou de la réduction des risques liés à l’utilisation du système d’IA à haut risque, il est dûment tenu
compte des connaissances techniques, de l’expérience, de l’éducation et de la formation pouvant être attendues du
déployeur, ainsi que du contexte prévisible dans lequel le système est destiné à être utilisé.

**[Article 9]**
1.
Un système de gestion des risques est établi, mis en œuvre, documenté et tenu à jour en ce qui concerne les systèmes
d’IA à haut risque.
2.
Ce système de gestion des risques s’entend comme étant un processus itératif continu qui est planifié et se déroule sur
l’ensemble du cycle de vie d’un système d’IA à haut risque et qui doit périodiquement faire l’objet d’un examen et d’une mise
à jour méthodiques. Il comprend les étapes suivantes:
a) l’identification et l’analyse des risques connus et raisonnablement prévisibles que le système d’IA à haut risque peut poser
pour la santé, la sécurité ou les droits fondamentaux lorsque le système d’IA à haut risque est utilisé conformément à sa
destination;
b) l’estimation et l’évaluation des risques susceptibles d’apparaître lorsque le système d’IA à haut risque est utilisé
conformément à sa destination et dans des conditions de mauvaise utilisation raisonnablement prévisible;
c) l’évaluation d’autres risques susceptibles d’apparaître, sur la base de l’analyse des données recueillies au moyen du
système de surveillance après commercialisation visé à l’article 72;
d) l’adoption de mesures appropriées et ciblées de gestion des risques, conçues pour répondre aux risques identifiés en
vertu du point a).
3.
Les risques visés au présent article ne concernent que ceux qui peuvent être raisonnablement atténués ou éliminés
dans le cadre du développement ou de la conception du système d’IA à haut risque, ou par la fourniture d’informations
techniques appropriées.

**[Article 8]**
1.
Les systèmes d’IA à haut risque respectent les exigences énoncées dans la présente section, en tenant compte de leur
destination ainsi que de l’état de la technique généralement reconnu en matière d’IA et de technologies liées à l’IA. Pour
garantir le respect de ces exigences, il est tenu compte du système de gestion des risques prévu à l’article 9.
2.
Lorsqu’un produit contient un système d’IA auquel s’appliquent les exigences du présent règlement ainsi que les
exigences de la législation d’harmonisation de l’Union dont la liste figure à la section A de l’annexe I, les fournisseurs sont
chargés de veiller à ce que leur produit soit pleinement conforme à toutes les exigences en vertu de la législation
d’harmonisation de l’Union applicable. Pour garantir que les systèmes d’IA à haut risque visés au paragraphe 1 sont
conformes aux exigences énoncées dans la présente section, et afin d’assurer la cohérence, d’éviter les doubles emplois et de
réduire au minimum les charges supplémentaires, les fournisseurs ont le choix d’intégrer, le cas échéant, les processus d’essai
et de déclaration nécessaires, les informations et la documentation qu’ils fournissent concernant leur produit dans la
documentation et les procédures qui existent déjà et qui sont requises en vertu de la législation d’harmonisation de l’Union
dont la liste figure à la section A de l’annexe I.

**[Article 14]**
a) de comprendre correctement les capacités et les limites pertinentes du système d’IA à haut risque et d’être en mesure de
surveiller correctement son fonctionnement, y compris en vue de détecter et de traiter les anomalies, les
dysfonctionnements et les performances inattendues;
b) d’avoir conscience d’une éventuelle tendance à se fier automatiquement ou excessivement aux sorties produites par un
système d’IA à haut risque (biais d’automatisation), en particulier pour les systèmes d’IA à haut risque utilisés pour
fournir des informations ou des recommandations concernant les décisions à prendre par des personnes physiques;
c) d’interpréter correctement les sorties du système d’IA à haut risque, compte tenu par exemple des outils et méthodes
d’interprétation disponibles;
d) de décider, dans une situation particulière, de ne pas utiliser le système d’IA à haut risque ou d’ignorer, remplacer ou
inverser la sortie du système d’IA à haut risque;
e) d’intervenir dans le fonctionnement du système d’IA à haut risque ou d’interrompre le système au moyen d’un bouton
d’arrêt ou d’une procédure similaire permettant au système de s’arrêter de manière sécurisée.

</details>

- Juge 14B : OUI — 
- Avis proposé par Claude : OUI — Étapes a) à d) de l'article 9 §2 reprises fidèlement.

**Ton verdict :** OUI

---

## ollama/s08 — Quelles sont les obligations des fournisseurs de modèles d'IA à usage général ?

**Réponse du modèle :**

Les fournisseurs de modèles d'IA à usage général ont plusieurs obligations en vertu du règlement (UE) 2024/1689 sur l'intelligence artificielle (AI Act). Voici une liste non exhaustive de ces obligations :

1. Veiller au respect des obligations pertinentes prévues par le présent règlement [Considérant 106].
2. Élaborer et tenir à jour la documentation technique du modèle, y compris son processus d'entraînement et d'essai et les résultats de son évaluation, qui contient, au minimum, les informations énoncées à l'annexe XI aux fins de la fournir, sur demande, au Bureau de l'IA et aux autorités nationales compétentes [Article 53, point 1a].
3. Élaborer, tiennent à jour et mettent à disposition des informations et de la documentation à l'intention des fournisseurs de systèmes d'IA qui envisagent d'intégrer le modèle d'IA à usage général dans leurs systèmes d'IA [Article 53, point 1b].
4. Élaborer et mettent à la disposition du public un résumé suffisamment détaillé du contenu utilisé pour entraîner le modèle d'IA à usage général, conformément à un modèle fourni par le Bureau de l'IA [Article 53, point 1d].
5. Élaborer une politique visant à se conformer au droit de l'Union en matière de droit d'auteur et droits voisins, et notamment à identifier et à respecter, y compris au moyen de technologies de pointe, une réservation de droits exprimée conformément à l'article 4, paragraphe 3, de la directive (UE) 2019/790 [Article 53, point 1c].
6. Effectuer une évaluation des modèles sur la base de protocoles et d'outils normalisés reflétant l'état de la technique, y compris en réalisant et en documentant des essais contradictoires des modèles en vue d'identifier et d'atténuer les risques systémiques, si le modèle d'IA à usage général présente un risque systémique [Article 55, point 1a].
7. Évaluer et atténuer les risques systémiques éventuels au niveau de l'Union, y compris leurs origines, qui peuvent découler du développement, de la mise sur le marché ou de l'utilisation de modèles d'IA à usage général présentant un risque systémique, si le modèle d'IA à usage général présente un risque systémique [Article 55, point 1b].
8. Suivre, documenter et communiquer sans retard injustifié au Bureau de l'IA et, le cas échéant, aux autorités nationales compétentes les informations pertinentes concernant les incidents graves ainsi que les éventuelles mesures correctives pour y remédier, si le modèle d'IA à usage général présente un risque systémique [Article 55, point 1c].
9. Garantir un niveau approprié de protection en matière de cybersécurité pour le modèle d'IA à usage général présentant un risque systémique et l'infrastructure physique du modèle, si le modèle d'IA à usage général présente un risque systémique [Article 55, point 1d].

<details><summary>Extraits fournis au modèle</summary>

**[Considérant 106]**
Les fournisseurs qui mettent des modèles d’IA à usage général sur le marché de l’Union devraient veiller au respect
des obligations pertinentes prévues par le présent règlement. À cette fin, les fournisseurs de modèles d’IA à usage
général devraient mettre en place une politique visant à respecter la législation de l’Union sur le droit d’auteur et les
droits voisins, en particulier pour identifier et respecter la réservation de droits exprimées par les titulaires de droits
conformément à l’article 4, paragraphe 3, de la directive (UE) 2019/790. Tout fournisseur qui met un modèle d’IA
à usage général sur le marché de l’Union devrait se conformer à cette obligation, quelle que soit la juridiction dans
laquelle se déroulent les actes pertinents au titre du droit d’auteur qui sous-tendent l’entraînement de ces modèles
d’IA à usage général. Cela est nécessaire pour garantir des conditions de concurrence équitables entre les fournisseurs
de modèles d’IA à usage général, lorsqu’aucun fournisseur ne devrait pouvoir obtenir un avantage concurrentiel sur
le marché de l’Union en appliquant des normes en matière de droit d’auteur moins élevées que celles prévues dans
l’Union.

**[Article 53]**
6.
La Commission est habilitée à adopter des actes délégués conformément à l’article 97, paragraphe 2, pour modifier les
annexes XI et XII à la lumière des évolutions technologiques.
7.
Toute information ou documentation obtenue en vertu du présent article, y compris les secrets d’affaires, est traitée
conformément aux obligations de confidentialité énoncées à l’article 78.

**[Article 53]**
1.
Les fournisseurs de modèles d’IA à usage général:
a) élaborent et tiennent à jour la documentation technique du modèle, y compris son processus d’entraînement et d’essai et
les résultats de son évaluation, qui contient, au minimum, les informations énoncées à l’annexe XI aux fins de la fournir,
sur demande, au Bureau de l’IA et aux autorités nationales compétentes;
b) élaborent, tiennent à jour et mettent à disposition des informations et de la documentation à l’intention des fournisseurs
de systèmes d’IA qui envisagent d’intégrer le modèle d’IA à usage général dans leurs systèmes d’IA. Sans préjudice de la
nécessité d’observer et de protéger les droits de propriété intellectuelle et les informations confidentielles de nature
commerciale ou les secrets d’affaires conformément au droit de l’Union et au droit national, ces informations et cette
documentation:
i) permettent aux fournisseurs de systèmes d’IA d’avoir une bonne compréhension des capacités et des limites du
modèle d’IA à usage général et de se conformer aux obligations qui leur incombent en vertu du présent règlement; et
ii) contiennent, au minimum, les éléments énoncés à l’annexe XII;
c) mettent en place une politique visant à se conformer au droit de l’Union en matière de droit d’auteur et droits voisins, et
notamment à identifier et à respecter, y compris au moyen de technologies de pointe, une réservation de droits exprimée
conformément à l’article 4, paragraphe 3, de la directive (UE) 2019/790;
d) élaborent et mettent à la disposition du public un résumé suffisamment détaillé du contenu utilisé pour entraîner le
modèle d’IA à usage général, conformément à un modèle fourni par le Bureau de l’IA.

**[Article 55]**
2.
Les fournisseurs de modèles d’IA à usage général présentant un risque systémique peuvent s’appuyer sur des codes de
bonne pratique au sens de l’article 56 pour démontrer qu’ils respectent les obligations énoncées au paragraphe 1 du présent
article, jusqu’à la publication d’une norme harmonisée. Le respect des normes européennes harmonisées confère au
fournisseur une présomption de conformité dans la mesure où lesdites normes couvrent ces obligations. Les fournisseurs de
modèles d’IA à usage général présentant un risque systémique qui n’adhèrent pas à un code de bonnes pratiques approuvé
ou ne respectent pas une norme européenne harmonisée démontrent qu’ils disposent d’autres moyens appropriés de mise
en conformité et les soumettent à l’appréciation de la Commission.
3.
Toute information ou documentation obtenue en vertu du présent article, y compris les secrets d’affaires, est traitée
conformément aux obligations de confidentialité énoncées à l’article 78.

**[Article 55]**
1.
Outre les obligations énumérées aux articles 53 et 54, les fournisseurs de modèles d’IA à usage général présentant un
risque systémique:
a) effectuent une évaluation des modèles sur la base de protocoles et d’outils normalisés reflétant l’état de la technique, y
compris en réalisant et en documentant des essais contradictoires des modèles en vue d’identifier et d’atténuer les risques
systémiques;
b) évaluent et atténuent les risques systémiques éventuels au niveau de l’Union, y compris leurs origines, qui peuvent
découler du développement, de la mise sur le marché ou de l’utilisation de modèles d’IA à usage général présentant un
risque systémique;
c) suivent, documentent et communiquent sans retard injustifié au Bureau de l’IA et, le cas échéant, aux autorités nationales
compétentes les informations pertinentes concernant les incidents graves ainsi que les éventuelles mesures correctives
pour y remédier;
d) garantissent un niveau approprié de protection en matière de cybersécurité pour le modèle d’IA à usage général
présentant un risque systémique et l’infrastructure physique du modèle.

</details>

- Juge 14B : NON — L'affirmation selon laquelle les fournisseurs doivent 'veiller au respect des obligations pertinentes prévues par le présent règlement' (point 1) est formulée comme une obligation générale, alors que 
- Avis proposé par Claude : OUI — Considérant 106 et articles 53/55 bien présents dans les extraits.

**Ton verdict :** OUI

---

## ollama/s09 — Quand un modèle d'IA à usage général est-il considéré comme présentant un risque systémique ?

**Réponse du modèle :**

Un modèle d'IA à usage général est considéré comme présentant un risque systémique si il remplit l'une des conditions suivantes :

1. Il dispose de capacités à fort impact évaluées sur la base de méthodologies et d'outils techniques appropriés, y compris des indicateurs et des critères de référence (Article 51, point a).
2. Sur la base d'une décision de la Commission, d'office ou à la suite d'une alerte qualifiée du groupe scientifique, il possède des capacités ou un impact équivalents à ceux énoncés au point a), compte tenu des critères définis à l'annexe XIII (Article 51, point b).
3. Lorsque la quantité cumulée de calcul utilisée pour son entraînement mesurée en opérations en virgule flottante est supérieure à 1025 (Article 51, point 2).

La Commission peut également désigner un modèle d'IA à usage général comme présentant un risque systémique, d'office ou à la suite d'une alerte qualifiée du groupe scientifique, sur la base des critères énoncés à l'annexe XIII (Article 52, paragraphe 4).

<details><summary>Extraits fournis au modèle</summary>

**[Article 55]**
1.
Outre les obligations énumérées aux articles 53 et 54, les fournisseurs de modèles d’IA à usage général présentant un
risque systémique:
a) effectuent une évaluation des modèles sur la base de protocoles et d’outils normalisés reflétant l’état de la technique, y
compris en réalisant et en documentant des essais contradictoires des modèles en vue d’identifier et d’atténuer les risques
systémiques;
b) évaluent et atténuent les risques systémiques éventuels au niveau de l’Union, y compris leurs origines, qui peuvent
découler du développement, de la mise sur le marché ou de l’utilisation de modèles d’IA à usage général présentant un
risque systémique;
c) suivent, documentent et communiquent sans retard injustifié au Bureau de l’IA et, le cas échéant, aux autorités nationales
compétentes les informations pertinentes concernant les incidents graves ainsi que les éventuelles mesures correctives
pour y remédier;
d) garantissent un niveau approprié de protection en matière de cybersécurité pour le modèle d’IA à usage général
présentant un risque systémique et l’infrastructure physique du modèle.

**[Article 3]**
65) «risque systémique», un risque spécifique aux capacités à fort impact des modèles d’IA à usage général, ayant une
incidence significative sur le marché de l’Union en raison de leur portée ou d’effets négatifs réels ou raisonnablement
prévisibles sur la santé publique, la sûreté, la sécurité publique, les droits fondamentaux ou la société dans son
ensemble, pouvant être propagé à grande échelle tout au long de la chaîne de valeur;
66) «système d’IA à usage général», un système d’IA qui est fondé sur un modèle d’IA à usage général et qui a la capacité de
répondre à diverses finalités, tant pour une utilisation directe que pour une intégration dans d’autres systèmes d’IA;
67) «opération en virgule flottante», toute opération ou assignation mathématique impliquant des nombres en virgule
flottante, qui constituent un sous-ensemble des nombres réels généralement représentés sur un ordinateur par un
entier de précision fixe suivi d’un exposant entier d’une base fixe;
68) «fournisseur en aval», un fournisseur d’un système d’IA, y compris d’un système d’IA à usage général, qui intègre un
modèle d’IA, que le modèle d’IA soit fourni par lui-même ou non, et verticalement intégré ou fourni par une autre
entité sur la base de relations contractuelles.

**[Article 51]**
systémique
1.
Un modèle d’IA à usage général est classé comme modèle d’IA à usage général présentant un risque systémique s’il
remplit l’une des conditions suivantes:
a) il dispose de capacités à fort impact évaluées sur la base de méthodologies et d’outils techniques appropriés, y compris
des indicateurs et des critères de référence;
b) sur la base d’une décision de la Commission, d’office ou à la suite d’une alerte qualifiée du groupe scientifique, il possède
des capacités ou un impact équivalents à ceux énoncés au point a), compte tenu des critères définis à l’annexe XIII.
2.
Un modèle d’IA à usage général est présumé avoir des capacités à fort impact conformément au paragraphe 1,
point a), lorsque la quantité cumulée de calcul utilisée pour son entraînement mesurée en opérations en virgule flottante est
supérieure à 1025.
3.
La Commission adopte des actes délégués conformément à l’article 97 pour modifier les seuils énumérés aux
paragraphes 1 et 2 du présent article, ainsi que pour compléter les critères de référence et les indicateurs à la lumière des
évolutions technologiques, telles que les améliorations algorithmiques ou l’efficacité accrue du matériel informatique, si
nécessaire, afin que ces seuils reflètent l’état de la technique.

**[Article 52]**
4.
La Commission peut désigner un modèle d’IA à usage général comme présentant un risque systémique, d’office ou à la
suite d’une alerte qualifiée du groupe scientifique conformément à l’article 90, paragraphe 1, point a), sur la base des critères
énoncés à l’annexe XIII.
La Commission est habilitée à adopter des actes délégués conformément à l’article 97 pour modifier l’annexe XIII en
précisant et mettant à jour les critères énoncés à ladite annexe.
5.
Sur demande motivée d’un fournisseur dont le modèle a été désigné comme modèle d’IA à usage général présentant
un risque systémique en vertu du paragraphe 4, la Commission tient compte de la demande et peut décider de réévaluer si le
modèle d’IA à usage général peut encore être considéré comme présentant un risque systémique sur la base des critères
énoncés à l’annexe XIII. Une telle demande contient les éléments objectifs, détaillés et nouveaux qui sont apparus depuis la
décision de désignation. Les fournisseurs peuvent demander une réévaluation au plus tôt six mois après la décision de
désignation. Lorsque la Commission, à la suite de sa réévaluation, décide de maintenir la désignation en tant que modèle
d’IA à usage général présentant un risque systémique, les fournisseurs peuvent demander une réévaluation au plus tôt six
mois après cette décision.
6.
La Commission veille à ce qu’une liste des modèles d’IA à usage général présentant un risque systémique soit publiée
et tient cette liste à jour, sans préjudice de la nécessité de respecter et de protéger les droits de propriété intellectuelle et les
informations confidentielles de nature commerciale ou les secrets d’affaires conformément au droit de l’Union et au droit
national.

**[Article 52]**
1.
Lorsqu’un modèle d’IA à usage général remplit la condition visée à l’article 51, paragraphe 1, point a), le fournisseur
concerné en informe la Commission sans tarder et, en tout état de cause, dans un délai de deux semaines après la date
à laquelle ce critère est rempli ou après qu’il a été établi qu’il le sera. Cette notification comprend les informations
nécessaires pour démontrer que le critère pertinent a été rempli. Si la Commission apprend l’existence d’un modèle d’IA
à usage général présentant un risque systémique dont elle n’a pas été informée, elle peut décider de le désigner comme
modèle présentant un risque systémique.
2.
Le fournisseur d’un modèle d’IA à usage général qui remplit la condition visée à l’article 51, paragraphe 1, point a),
peut présenter, avec sa notification, des arguments suffisamment étayés pour démontrer que, exceptionnellement, bien qu’il
remplisse ce critère, le modèle d’IA à usage général ne présente pas, en raison de ses caractéristiques spécifiques, de risque
systémique et ne devrait donc pas être classé comme modèle d’IA à usage général présentant un risque systémique.
3.
Lorsque la Commission conclut que les arguments présentés conformément au paragraphe 2 ne sont pas
suffisamment étayés et que le fournisseur concerné n’a pas été en mesure de démontrer que le modèle d’IA à usage général
ne présente pas, en raison de ses caractéristiques spécifiques, de risque systémique, elle rejette ces arguments, et le modèle
d’IA à usage général est considéré comme un modèle d’IA à usage général présentant un risque systémique.

</details>

- Juge 14B : NON — L'affirmation selon laquelle 'la quantité cumulée de calcul utilisée pour son entraînement mesurée en opérations en virgule flottante est supérieure à 1025' est une **condition présumée** de risque sy
- Avis proposé par Claude : OUI — Conforme aux articles 51 et 52. « 1025 » est un artefact d'extraction du PDF (10^25).

**Ton verdict :** OUI

---

## ollama/s10 — Qu'est-ce qu'un bac à sable réglementaire de l'IA ?

**Réponse du modèle :**

Un bac à sable réglementaire de l'IA, selon les extraits fournis, est un cadre contrôlé mis en place par une autorité compétente qui offre aux fournisseurs ou fournisseurs potentiels de systèmes d'IA la possibilité de développer, d'entraîner, de valider et de tester, lorsqu'il y a lieu en conditions réelles, un système d'IA innovant, selon un plan du bac à sable pour une durée limitée sous surveillance réglementaire. [Article 57] Bacs à sable réglementaires de l'IA, point 55.

<details><summary>Extraits fournis au modèle</summary>

**[Article 57]**
1.
Les États membres veillent à ce que leurs autorités compétentes mettent en place au moins un bac à sable
réglementaire de l’IA au niveau national, qui est opérationnel au plus tard le 2 août 2026. Ce bac à sable peut également être
établi conjointement avec les autorités compétentes d’autres États membres. La Commission peut fournir un soutien
technique, des conseils et des outils pour la mise en place et l’exploitation de bacs à sable réglementaires de l’IA.
L’obligation visée au premier alinéa peut également être remplie en participant à un bac à sable existant, pour autant que
cette participation offre un niveau de couverture nationale équivalent pour les États membres participants.
2.
Des bacs à sable réglementaires de l’IA supplémentaires au niveau régional ou au niveau local, ou établis
conjointement avec les autorités compétentes d’autres États membres peuvent également être mis en place.
3.
Le Contrôleur européen de la protection des données peut également créer un bac à sable réglementaire de l’IA pour
les institutions, organes et organismes de l’Union, et peut exercer les rôles et les tâches des autorités nationales compétentes
conformément au présent chapitre.

**[Article 57]**
9.
La mise en place de bacs à sable réglementaires de l’IA vise à contribuer aux objectifs suivants:
a) améliorer la sécurité juridique afin d’assurer le respect réglementaire du présent règlement ou, le cas échéant, d’autres
dispositions applicables du droit de l’Union et du droit national;
b) soutenir le partage des bonnes pratiques par la coopération avec les autorités participant au bac à sable réglementaire de
l’IA;
c) favoriser l’innovation et la compétitivité et faciliter la mise en place d’un écosystème d’IA;
d) contribuer à l’apprentissage réglementaire fondé sur des données probantes;
e) faciliter et accélérer l’accès au marché de l’Union pour les systèmes d’IA, en particulier lorsqu’ils sont fournis par des
PME, y compris des jeunes pousses.
10.
Les autorités nationales compétentes veillent à ce que, dans la mesure où les systèmes d’IA innovants impliquent le
traitement de données à caractère personnel ou relèvent à d’autres titres de la surveillance d’autres autorités nationales ou
autorités compétentes assurant ou encadrant l’accès aux données, les autorités nationales chargées de la protection des
données et ces autres autorités nationales ou autorités compétentes soient associées à l’exploitation du bac à sable
réglementaire de l’IA et participent au contrôle des aspects qui relèvent de leurs tâches et pouvoirs respectifs.

**[Article 3]**
53) «plan d’essais en conditions réelles», un document décrivant les objectifs, la méthode, la population et le champ
d’application géographique et la portée dans le temps, le suivi, l’organisation et la conduite des essais en conditions
réelles;
54) «plan du bac à sable», un document adopté conjointement entre le fournisseur participant et l’autorité compétente, qui
décrit les objectifs, les conditions, les délais, la méthodologie et les exigences applicables aux activités réalisées au sein
du bac à sable;
55) «bac à sable réglementaire de l’IA», un cadre contrôlé mis en place par une autorité compétente qui offre aux
fournisseurs ou fournisseurs potentiels de systèmes d’IA la possibilité de développer, d’entraîner, de valider et de tester,
lorsqu’il y a lieu en conditions réelles, un système d’IA innovant, selon un plan du bac à sable pour une durée limitée
sous surveillance réglementaire;
56) «maîtrise de l’IA», les compétences, les connaissances et la compréhension qui permettent aux fournisseurs, aux
déployeurs et aux personnes concernées, compte tenu de leurs droits et obligations respectifs dans le contexte du
présent règlement, de procéder à un déploiement des systèmes d’IA en toute connaissance de cause, ainsi que de
prendre conscience des possibilités et des risques que comporte l’IA, ainsi que des préjudices potentiels qu’elle peut
causer;

**[Article 57]**
16.
Les autorités nationales compétentes présentent des rapports annuels au Bureau de l’IA et au Comité IA, dont le
premier est élaboré dans un délai d’un an à compter de la mise en place du bac à sable réglementaire de l’IA, puis tous les
ans jusqu’à son terme, et un rapport final. Ces rapports fournissent des informations sur les progrès et les résultats de la
mise en œuvre de ces bacs à sable, y compris les bonnes pratiques, les incidents, les enseignements et les recommandations
concernant leur mise en place et, le cas échéant, sur l’application et la révision éventuelle du présent règlement, y compris
ses actes délégués et actes d’exécution, et sur l’application d’autres dispositions législatives de l’Union contrôlés par les
autorités compétentes dans le cadre du bac à sable. Les autorités nationales compétentes publient ces rapports annuels ou
des résumés de ceux-ci en ligne. La Commission tient compte, s’il y a lieu, des rapports annuels dans l’exercice de ses tâches
au titre du présent règlement.
17.
La Commission développe une interface unique et spécifique contenant toutes les informations pertinentes relatives
aux bacs à sable réglementaires de l’IA pour permettre aux parties prenantes d’interagir avec les bacs à sable réglementaires
de l’IA et de s’informer auprès des autorités compétentes, ainsi que de demander des orientations non contraignantes sur la
conformité de produits, services et modèles commerciaux innovants intégrant les technologies de l’IA, conformément
à l’article 62, paragraphe 1, point c). La Commission assure une coordination proactive avec les autorités nationales
compétentes, le cas échéant.

**[Article 58]**
g) que les procédures, processus et exigences administratives applicables en matière de demande, de sélection, de
participation et de sortie dans le cadre du bac à sable réglementaires de l’IA sont simples, facilement compréhensibles et
clairement communiqués afin de faciliter la participation des PME, y compris des jeunes pousses, disposant de capacités
juridiques et administratives limitées, et sont rationalisés dans toute l’Union, afin d’éviter la fragmentation et de
permettre que la participation à un bac à sable réglementaire de l’IA mis en place par un État membre ou par le
Contrôleur européen de la protection des données soit mutuellement et uniformément reconnue et produise les mêmes
effets juridiques dans l’ensemble de l’Union;
h) que la participation au bac à sable réglementaire de l’IA est limitée à une période adaptée à la complexité et à l’envergure
du projet, qui peut être prolongée par l’autorité nationale compétente;
i) que les bacs à sable réglementaire de l’IA facilitent le développement d’outils et d’infrastructures pour la mise à l’essai,
l’étalonnage des performances, l’évaluation et l’explication des aspects des systèmes d’IA pertinents pour l’apprentissage
réglementaire, tels que la précision, la solidité et la cybersécurité, ainsi que les mesures d’atténuation des risques d’atteinte
aux droits fondamentaux et à la société au sens large.

</details>

- Juge 14B : OUI — 
- Avis proposé par Claude : OUI — Définition fidèle (article 3, point 55), même si la citation mélange articles 3 et 57.

**Ton verdict :** OUI

---

## ollama/s11 — Les contenus générés par hypertrucage (deepfakes) doivent-ils être signalés ?

**Réponse du modèle :**

Les contenus générés par hypertrucage (deepfakes) ne doivent pas être signalés si l'utilisation est autorisée par la loi à des fins de prévention ou de détection des infractions pénales, d'enquêtes ou de poursuites en la matière [Article 50].

<details><summary>Extraits fournis au modèle</summary>

**[Article 50]**
4.
Les déployeurs d’un système d’IA qui génère ou manipule des images ou des contenus audio ou vidéo constituant un
hypertrucage indiquent que les contenus ont été générés ou manipulés par une IA. Cette obligation ne s’applique pas
lorsque l’utilisation est autorisée par la loi à des fins de prévention ou de détection des infractions pénales, d’enquêtes ou de
poursuites en la matière. Lorsque le contenu fait partie d’une œuvre ou d’un programme manifestement artistique, créatif,
satirique, fictif ou analogue, les obligations de transparence énoncées au présent paragraphe se limitent à la divulgation de
l’existence de tels contenus générés ou manipulés d’une manière appropriée qui n’entrave pas l’affichage ou la jouissance de
l’œuvre.
Les déployeurs d’un système d’IA qui génère ou manipule des textes publiés dans le but d’informer le public sur des
questions d’intérêt public indiquent que le texte a été généré ou manipulé par une IA. Cette obligation ne s’applique pas
lorsque l’utilisation est autorisée par la loi à des fins de prévention ou de détection des infractions pénales, d’enquêtes ou de
poursuites en la matière, ou lorsque le contenu généré par l’IA a fait l’objet d’un processus d’examen humain ou de contrôle
éditorial et lorsqu’une personne physique ou morale assume la responsabilité éditoriale de la publication du contenu.
5.
Les informations visées aux paragraphes 1 à 4 sont fournies aux personnes physiques concernées de manière claire et
reconnaissable au plus tard au moment de la première interaction ou de la première exposition. Les informations sont
conformes aux exigences applicables en matière d’accessibilité.

**[Article 10]**
a) la détection et la correction des biais ne peuvent être satisfaites de manière efficace en traitant d’autres données, y
compris des données synthétiques ou anonymisées;
b) les catégories particulières de données à caractère personnel sont soumises à des limitations techniques relatives à la
réutilisation des données à caractère personnel, ainsi qu’aux mesures les plus avancées en matière de sécurité et de
protection de la vie privée, y compris la pseudonymisation;
c) les catégories particulières de données à caractère personnel font l’objet de mesures visant à garantir que les données
à caractère personnel traitées sont sécurisées, protégées et soumises à des garanties appropriées, y compris des contrôles
stricts et une documentation de l’accès, afin d’éviter toute mauvaise utilisation et de veiller à ce que seules les personnes
autorisées ayant des obligations de confidentialité appropriées aient accès à ces données à caractère personnel;
d) les catégories particulières de données à caractère personnel ne doivent pas être transmises, transférées ou consultées
d’une autre manière par d’autres parties;
e) les catégories particulières de données à caractère personnel sont supprimées une fois que le biais a été corrigé ou que la
période de conservation des données à caractère personnel a expiré, selon celle de ces deux échéances qui arrive en
premier;
f) les registres des activités de traitement visés dans les règlements (UE) 2016/679 et (UE) 2018/1725 et dans la directive
(UE) 2016/680 comprennent les raisons pour lesquelles le traitement des catégories particulières de données à caractère
personnel était strictement nécessaire pour détecter et corriger les biais, ainsi que la raison pour laquelle cet objectif n’a
pas pu être atteint par le traitement d’autres données.

**[Article 8]**
1.
Les systèmes d’IA à haut risque respectent les exigences énoncées dans la présente section, en tenant compte de leur
destination ainsi que de l’état de la technique généralement reconnu en matière d’IA et de technologies liées à l’IA. Pour
garantir le respect de ces exigences, il est tenu compte du système de gestion des risques prévu à l’article 9.
2.
Lorsqu’un produit contient un système d’IA auquel s’appliquent les exigences du présent règlement ainsi que les
exigences de la législation d’harmonisation de l’Union dont la liste figure à la section A de l’annexe I, les fournisseurs sont
chargés de veiller à ce que leur produit soit pleinement conforme à toutes les exigences en vertu de la législation
d’harmonisation de l’Union applicable. Pour garantir que les systèmes d’IA à haut risque visés au paragraphe 1 sont
conformes aux exigences énoncées dans la présente section, et afin d’assurer la cohérence, d’éviter les doubles emplois et de
réduire au minimum les charges supplémentaires, les fournisseurs ont le choix d’intégrer, le cas échéant, les processus d’essai
et de déclaration nécessaires, les informations et la documentation qu’ils fournissent concernant leur produit dans la
documentation et les procédures qui existent déjà et qui sont requises en vertu de la législation d’harmonisation de l’Union
dont la liste figure à la section A de l’annexe I.

**[Article 73]**
9.
Pour les systèmes d’IA à haut risque visés à l’annexe III qui sont mis sur le marché ou mis en service par des
fournisseurs qui sont soumis à des instruments législatifs de l’Union établissant des obligations de signalement équivalentes
à celles énoncées dans le présent règlement, la notification des incidents graves est limitée à ceux visés à l’article 3, point 49)
c).
10.
Pour les systèmes d’IA à haut risque qui sont des composants de sécurité de dispositifs, ou qui sont eux-mêmes des
dispositifs, relevant des règlements (UE) 2017/745 et (UE) 2017/746, la notification des incidents graves est limitée à ceux
qui sont visés à l’article 3, point 49) c), du présent règlement, et est adressée à l’autorité nationale compétente choisie à cette
fin par les États membres dans lesquels l’incident s’est produit.
11.
Les autorités nationales compétentes notifient immédiatement à la Commission tout incident grave, qu’elles aient ou
non pris des mesures à cet égard, conformément à l’article 20 du règlement (UE) 2019/1020.

**[Annexe III]**
d) systèmes d'IA destinés à être utilisés par les autorités répressives ou par les institutions, organes et organismes de
l'Union, ou en leur nom, en soutien aux autorités répressives pour évaluer le risque qu'une personne physique
commette une infraction ou récidive, sans se fonder uniquement sur le profilage des personnes physiques visé
à l'article 3, paragraphe 4, de la directive (UE) 2016/680, ou pour évaluer les traits de personnalité, les
caractéristiques ou les antécédents judiciaires de personnes physiques ou de groupes;
e) systèmes d'IA destinés à être utilisés par les autorités répressives ou par les institutions, organes et organismes de
l'Union, ou en leur nom, en soutien aux autorités répressives pour le profilage de personnes physiques visé
à l'article 3, paragraphe 4, de la directive (UE) 2016/680 dans le cadre de la détection d'infractions pénales,
d'enquêtes ou de poursuites en la matière ou de l'exécution de sanctions pénales.
7.
Migration, asile et gestion des contrôles aux frontières, dans la mesure où leur utilisation est autorisée par le droit de
l'Union ou le droit national applicable:
a) systèmes d'IA destinés à être utilisés par les autorités publiques compétentes ou par les institutions, organes ou
organismes de l'Union, ou en leur nom, en tant que polygraphes et outils similaires;
b) systèmes d'IA destinés à être utilisés par les autorités publiques compétentes ou par les institutions, organes ou
organismes de l'Union, ou en leur nom, pour évaluer un risque, y compris un risque pour la sécurité, un risque de
migration irrégulière ou un risque pour la santé, posé par une personne physique qui a l'intention d'entrer ou qui
est entrée sur le territoire d'un État membre;

</details>

- Juge 14B : NON — L'affirmation selon laquelle les contenus générés par hypertrucage *ne doivent pas être signalés* dans ces cas est incorrecte : le texte précise qu'**ils ne sont PAS soumis à l'obligation de signaleme
- Avis proposé par Claude : OUI — L'exception citée existe bien, mais la réponse est trompeuse par omission : elle tait la règle générale (signalement obligatoire). Incomplet, pas infidèle.

**Ton verdict :** OUI

---

## ollama/s12 — Quelle obligation de maîtrise de l'IA s'impose aux fournisseurs et aux déployeurs ?

**Réponse du modèle :**

Les fournisseurs et les déployeurs de systèmes d'IA sont tenus de prendre des mesures pour garantir un niveau suffisant de maîtrise de l'IA pour leur personnel et les autres personnes s'occupant du fonctionnement et de l'utilisation des systèmes d'IA pour leur compte, en tenant compte des personnes ou des groupes de personnes à l'égard desquels les systèmes d'IA sont destinés à être utilisés, en fonction de leurs connaissances techniques, leur expérience, leur éducation et leur formation, ainsi que du contexte dans lequel les systèmes d'IA sont destinés à être utilisés [Article 4].

<details><summary>Extraits fournis au modèle</summary>

**[Article 4]**
Les fournisseurs et les déployeurs de systèmes d’IA prennent des mesures pour garantir, dans toute la mesure du possible, un
niveau suffisant de maîtrise de l’IA pour leur personnel et les autres personnes s’occupant du fonctionnement et de
l’utilisation des systèmes d’IA pour leur compte, en prenant en considération leurs connaissances techniques, leur
expérience, leur éducation et leur formation, ainsi que le contexte dans lequel les systèmes d’IA sont destinés à être utilisés,
et en tenant compte des personnes ou des groupes de personnes à l’égard desquels les systèmes d’IA sont destinés à être
utilisés.

**[Article 74]**
b) les procédures d’essai ou d’audit et les vérifications fondées sur les données et la documentation communiquées par le
fournisseur ont été entièrement accomplies ou se sont révélées insuffisantes.
14.
Toute information ou documentation obtenue par les autorités de surveillance du marché est traitée conformément
aux obligations de confidentialité énoncées à l’article 78.

**[Article 50]**
2.
Les fournisseurs de systèmes d’IA, y compris de systèmes d’IA à usage général, qui génèrent des contenus de synthèse
de type audio, image, vidéo ou texte, veillent à ce que les sorties des systèmes d’IA soient marquées dans un format lisible
par machine et identifiables comme ayant été générées ou manipulées par une IA. Les fournisseurs veillent à ce que leurs
solutions techniques soient aussi efficaces, interopérables, solides et fiables que la technologie le permet, compte tenu des
spécificités et des limites des différents types de contenus, des coûts de mise en œuvre et de l’état de la technique
généralement reconnu, comme cela peut ressortir des normes techniques pertinentes. Cette obligation ne s’applique pas
dans la mesure où les systèmes d’IA remplissent une fonction d’assistance pour la mise en forme standard ou ne modifient
pas de manière substantielle les données d’entrée fournies par le déployeur ou leur sémantique, ou lorsque leur utilisation
est autorisée par la loi à des fins de prévention ou de détection des infractions pénales, d’enquêtes ou de poursuites en la
matière.

**[Article 62]**
a) fournit des modèles normalisés pour les domaines qui relèvent du présent règlement, comme précisé par le Comité IA
dans sa demande;
b) met au point et tient à jour une plateforme d’information unique fournissant des informations faciles à utiliser en
rapport avec le présent règlement pour tous les opérateurs dans l’ensemble de l’Union;
c) organise des campagnes de communication appropriées pour sensibiliser aux obligations découlant du présent
règlement;
d) évalue et promeut la convergence des bonnes pratiques en matière de procédures de passation de marchés publics en ce
qui concerne les systèmes d’IA.

**[Article 91]**
1.
La Commission peut demander au fournisseur du modèle d’IA à usage général concerné de fournir la documentation
établie par le fournisseur conformément aux articles 53 et 55, ou toute information supplémentaire nécessaire pour évaluer
la conformité du fournisseur avec le présent règlement.
2.
Avant d’envoyer la demande d’informations, le Bureau de l’IA peut entamer un dialogue structuré avec le fournisseur
du modèle d’IA à usage général.
3.
Sur demande dûment motivée du groupe scientifique, la Commission peut adresser une demande d’informations au
fournisseur d’un modèle d’IA à usage général, lorsque l’accès à ces informations est nécessaire et proportionné pour
l’accomplissement des tâches du groupe scientifique au titre de l’article 68, paragraphe 2.
4.
La demande d’informations mentionne la base juridique et l’objet de la demande, précise quelles informations sont
requises, fixe un délai dans lequel les informations doivent être fournies, et indique les amendes prévues à l’article 101 en
cas de fourniture d’informations inexactes, incomplètes ou trompeuses.
5.
Le fournisseur du modèle d’IA à usage général concerné, ou son représentant, fournit les informations demandées.
Dans le cas de personnes morales, d’entreprises ou de sociétés, ou lorsque le fournisseur n’a pas de personnalité juridique,
les personnes autorisées à les représenter en vertu de la loi ou de leurs statuts fournissent les informations demandées pour
le compte du fournisseur du modèle d’IA à usage général concerné. Les avocats dûment habilités à agir peuvent fournir des
informations pour le compte de leurs clients. Les clients demeurent néanmoins pleinement responsables si les informations
fournies sont incomplètes, inexactes ou trompeuses.

</details>

- Juge 14B : OUI — 
- Avis proposé par Claude : OUI — Reprise fidèle de l'article 4.

**Ton verdict :** OUI

---

## ollama/s13 — Qui doit réaliser une analyse d'impact sur les droits fondamentaux ?

**Réponse du modèle :**

Les déployeurs qui sont des organismes de droit public, des entités privées fournissant des services publics et les déployeurs de systèmes d'IA à haut risque visés à l'annexe III doivent réaliser une analyse d'impact sur les droits fondamentaux, selon [Article 27].

<details><summary>Extraits fournis au modèle</summary>

**[Article 27]**
2.
L’obligation établie au paragraphe 1 s’applique à la première utilisation du système d’IA à haut risque. Le déployeur
peut, dans des cas similaires, s’appuyer sur des analyses d’impact sur les droits fondamentaux effectuées précédemment ou
sur des analyses d’impact existantes réalisées par le fournisseur. Si, au cours de l’utilisation du système d’IA à haut risque, le
déployeur estime qu’un des éléments énumérés au paragraphe 1 a changé ou n’est plus à jour, il prend les mesures
nécessaires pour mettre à jour les informations.
3.
Une fois l’analyse visée au paragraphe 1 du présent article effectuée, le déployeur en notifie les résultats à l’autorité de
surveillance du marché, et soumet le modèle visé au paragraphe 5 du présent article, rempli, dans le cadre de la notification.
Dans le cas visé à l’article 46, paragraphe 1, les déployeurs peuvent être exemptés de cette obligation de notification.
4.
Si l’une des obligations prévues au présent article est déjà remplie au moyen de l’analyse d’impact relative à la
protection des données réalisée en application de l’article 35 du règlement (UE) 2016/679 ou de l’article 27 de la directive
(UE) 2016/680, l’analyse d’impact sur les droits fondamentaux visée au paragraphe 1 du présent article complète ladite
analyse d’impact relative à la protection des données.
5.
Le Bureau de l’IA élabore un modèle de questionnaire, y compris au moyen d’un outil automatisé, afin d’aider les
déployeurs à se conformer de manière simplifiée aux obligations qui leur incombent en vertu du présent article.

**[Article 5]**
b) les conséquences de l’utilisation du système sur les droits et libertés de toutes les personnes concernées, notamment la
gravité, la probabilité et l’ampleur de ces conséquences.
En outre, l’utilisation de systèmes d’identification biométriques à distance en temps réel dans des espaces accessibles au
public à des fins répressives en vue de la réalisation de l’un des objectifs énumérés au paragraphe 1, premier alinéa, point h),
du présent article respecte les garanties et conditions nécessaires et proportionnées en ce qui concerne cette utilisation,
conformément au droit national qui l’autorise, notamment eu égard aux limitations temporelles, géographiques et relatives
aux personnes. L’utilisation du système d’identification biométrique à distance en temps réel dans des espaces accessibles au
public n’est autorisée que si l’autorité répressive a réalisé une analyse d’impact sur les droits fondamentaux conformément
à l’article 27 et a enregistré le système dans la base de données de l’UE prévue par l’article 49. Toutefois, dans des cas
d’urgence dûment justifiés, il est possible de commencer à utiliser ces systèmes sans enregistrement dans la base de données
de l’UE, à condition que cet enregistrement soit effectué sans retard injustifié.
3.
Aux fins du paragraphe 1, premier alinéa, point h), et du paragraphe 2, chaque utilisation à des fins répressives d’un
système d’identification biométrique à distance en temps réel dans des espaces accessibles au public est subordonnée à une
autorisation préalable octroyée par une autorité judiciaire ou une autorité administrative indépendante dont la décision est
contraignante de l’État membre dans lequel cette utilisation doit avoir lieu, délivrée sur demande motivée et conformément

**[Article 27]**
1.
Avant le déploiement d’un système d’IA à haut risque visé à l’article 6, paragraphe 2, à l’exception des systèmes d’IA
à haut risque destinés à être utilisés dans le domaine visé à l’annexe III, point 2, les déployeurs qui sont des organismes de
droit public ou des entités privées fournissant des services publics et les déployeurs de systèmes d’IA à haut risque visés
à l’annexe III, points 5), b) et c), effectuent une analyse de l’impact sur les droits fondamentaux que l’utilisation de ce système
peut produire. À cette fin, les déployeurs effectuent une analyse comprenant:
a) une description des processus du déployeur dans lesquels le système d’IA à haut risque sera utilisé conformément à sa
destination;
b) une description de la période pendant laquelle et de la fréquence à laquelle chaque système d’IA à haut risque est destiné
à être utilisé;
c) les catégories de personnes physiques et les groupes susceptibles d’être concernés par son utilisation dans le contexte
spécifique;
d) les risques spécifiques de préjudice susceptibles d’avoir une incidence sur les catégories de personnes physiques ou
groupes de personnes identifiés en vertu du point c) du présent paragraphe, compte tenu des informations fournies par
le fournisseur conformément à l’article 13;
e) une description de la mise en œuvre des mesures de contrôle humain, conformément à la notice d’utilisation;
f) les mesures à prendre en cas de matérialisation de ces risques, y compris les dispositifs relatifs à la gouvernance interne et
aux mécanismes de plainte internes.

**[Article 77]**
1.
Les autorités ou organismes publics nationaux qui supervisent ou font respecter les obligations au titre du droit de
l’Union visant à protéger les droits fondamentaux, y compris le droit à la non-discrimination, en ce qui concerne l’utilisation
des systèmes d’IA à haut risque visés à l’annexe III sont habilités à demander toute documentation créée ou conservée en
vertu du présent règlement et à y avoir accès dans une langue et un format accessibles lorsque l’accès à cette documentation
est nécessaire à l’accomplissement effectif de leur mandat dans les limites de leurs compétences. L’autorité ou l’organisme
public concerné informe l’autorité de surveillance du marché de l’État membre concerné de toute demande de ce type.
2.
Au plus tard le 2 novembre 2024, chaque État membre identifie les autorités ou organismes publics visés au
paragraphe 1 et met la liste de ces autorités ou organismes à la disposition du public. Les États membres notifient la liste à la
Commission et aux autres États membres, et tiennent cette liste à jour.
3.
Lorsque la documentation visée au paragraphe 1 ne suffit pas pour déterminer s’il y a eu violation des obligations au
titre du droit de l’Union protégeant les droits fondamentaux, l’autorité ou l’organisme public visé au paragraphe 1 peut
présenter à l’autorité de surveillance du marché une demande motivée visant à organiser des tests du système d’IA à haut
risque par des moyens techniques. L’autorité de surveillance du marché organise les tests avec la participation étroite de
l’autorité ou organisme public ayant présenté la demande dans un délai raisonnable après celle-ci.

**[Article 86]**
1.
Toute personne concernée faisant l’objet d’une décision prise par un déployeur sur la base des sorties d’un système
d’IA à haut risque mentionné à l’annexe III, à l’exception des systèmes énumérés au point 2 de ladite annexe, et qui produit
des effets juridiques ou affecte significativement cette personne de façon similaire d’une manière qu’elle considère comme
ayant des conséquences négatives sur sa santé, sa sécurité ou ses droits fondamentaux a le droit d’obtenir du déployeur des
explications claires et pertinentes sur le rôle du système d’IA dans la procédure décisionnelle et sur les principaux éléments
de la décision prise.
2.
Le paragraphe 1 ne s’applique pas à l’utilisation de systèmes d’IA pour lesquels des exceptions ou des restrictions
à l’obligation prévue audit paragraphe découlent du droit de l’Union ou du droit national dans le respect du droit de l’Union.
3.
Le présent article ne s’applique que dans la mesure où le droit visé au paragraphe 1 n’est pas prévu par ailleurs dans le
droit de l’Union.

</details>

- Juge 14B : NON — L'affirmation selon laquelle **les déployeurs de systèmes d'IA à haut risque visés à l'annexe III** doivent systématiquement réaliser une analyse d'impact sur les droits fondamentaux est **partielleme
- Avis proposé par Claude : NON — Généralise à tous les systèmes de l'annexe III alors que l'article 27 ne vise que les points 5 b) et 5 c).

**Ton verdict :** NON

---

## ollama/c02 — Une banque peut-elle utiliser une IA pour évaluer la solvabilité de ses clients ? Quel niveau de risque ?

**Réponse du modèle :**

Oui, une banque peut utiliser une IA pour évaluer la solvabilité de ses clients. Selon l'Annexe III du règlement, les systèmes d'IA destinés à évaluer la solvabilité des personnes physiques sont considérés comme à haut risque.

<details><summary>Extraits fournis au modèle</summary>

**[Article 57]**
7.
Les autorités compétentes donnent aux fournisseurs et aux fournisseurs potentiels participant au bac à sable
réglementaire de l’IA des orientations sur les attentes réglementaires et la manière de satisfaire aux exigences et obligations
énoncées dans le présent règlement.
À la demande du fournisseur ou du fournisseur potentiel du système d’IA, l’autorité compétente fournit une preuve écrite
des activités menées avec succès dans le bac à sable. L’autorité compétente fournit également un rapport de sortie détaillant
les activités menées dans le bac à sable ainsi que les résultats et acquis d’apprentissage correspondants. Les fournisseurs
peuvent utiliser ces documents pour démontrer leur conformité avec le présent règlement au moyen de la procédure
d’évaluation de la conformité ou d’activités pertinentes de surveillance du marché. À cet égard, les rapports de sortie et la
preuve écrite fournie par l’autorité nationale compétente sont évalués de manière positive par les autorités de surveillance
du marché et les organismes notifiés, en vue d’accélérer les procédures d’évaluation de la conformité dans une mesure
raisonnable.
8.
Sous réserve des dispositions relatives à la confidentialité énoncées à l’article 78 et avec l’accord du fournisseur ou du
fournisseur potentiel, la Commission et le Comité IA sont autorisés à accéder aux rapports de sortie et en tiennent compte,
le cas échéant, dans l’exercice des tâches qui leur incombent en vertu du présent règlement. Si le fournisseur ou le
fournisseur potentiel et l’autorité nationale compétente y consentent explicitement, le rapport de sortie peut être mis à la
disposition du public par l’intermédiaire de la plateforme d’information unique visée au présent article.

**[Article 60]**
b) l’autorité de surveillance du marché de l’État membre où les essais en conditions réelles doivent être réalisés a approuvé
les essais en conditions réelles et le plan d’essais en conditions réelles; lorsque l’autorité de surveillance du marché n’a pas
fourni de réponse dans un délai de 30 jours, les essais en conditions réelles et le plan d’essais en conditions réelles sont
réputés approuvés; lorsque le droit national ne prévoit pas d’approbation tacite, les essais en conditions réelles restent
soumis à autorisation;

**[Article 74]**
6.
Pour les systèmes d’IA à haut risque mis sur le marché, mis en service ou utilisés par des établissements financiers
régis par la législation de l’Union sur les services financiers, l’autorité de surveillance du marché aux fins du présent
règlement est l’autorité nationale responsable de la surveillance financière de ces établissements en vertu de cette législation
dans la mesure où la mise sur le marché, la mise en service ou l’utilisation du système d’IA est directement liée à la
fourniture de ces services financiers.
7.
Par dérogation au paragraphe 6, dans des circonstances appropriées, et pour autant que la coordination soit assurée,
l’État membre peut désigner une autre autorité compétente comme autorité de surveillance du marché aux fins du présent
règlement.
Les autorités nationales de surveillance du marché surveillant les établissements de crédit réglementés régis par la directive
2013/36/UE, qui participent au mécanisme de surveillance unique institué par le règlement (UE) no 1024/2013, devraient
communiquer sans tarder à la Banque centrale européenne toute information identifiée dans le cadre de leurs activités de
surveillance du marché qui pourrait présenter un intérêt potentiel pour les missions de surveillance prudentielle de la
Banque centrale européenne définies dans ledit règlement.

**[Article 80]**
5.
Le fournisseur s’assure que toutes les mesures correctives appropriées sont prises pour tous les systèmes d’IA
concernés qu’il a mis à disposition sur le marché de l’Union.
6.
Lorsque le fournisseur du système d’IA concerné ne prend pas de mesures correctives adéquates dans le délai visé au
paragraphe 2 du présent article, l’article 79, paragraphe 5 à 9, s’applique.
7.
Lorsque, au cours de l’évaluation prévue au paragraphe 1 du présent article, l’autorité de surveillance du marché
établit que le système d’IA a été classé à tort par le fournisseur comme n’étant pas à haut risque afin de contourner
l’application des exigences figurant au chapitre III, section 2, le fournisseur fait l’objet d’amendes conformément
à l’article 99.
8.
Dans l’exercice de leur pouvoir de contrôle de l’application du présent article, et conformément à l’article 11 du
règlement (UE) 2019/1020, les autorités de surveillance du marché peuvent effectuer des contrôles appropriés, en tenant
compte notamment des informations stockées dans la base de données de l’UE visée à l’article 71 du présent règlement.

**[Annexe III]**
b) systèmes d'IA destinés à être utilisés pour évaluer la solvabilité des personnes physiques ou pour établir leur note
de crédit, à l'exception des systèmes d'IA utilisés à des fins de détection de fraudes financières;
c) systèmes d'IA destinés à être utilisés pour l'évaluation des risques et la tarification en ce qui concerne les
personnes physiques en matière d'assurance-vie et d'assurance maladie;
d) systèmes d'IA destinés à évaluer et hiérarchiser les appels d'urgence émanant de personnes physiques ou à être
utilisés pour envoyer ou établir des priorités dans l'envoi des services d'intervention d'urgence, y compris par la
police, les pompiers et l'assistance médicale, ainsi que pour les systèmes de tri des patients admis dans les services
de santé d'urgence.
6.
Répression, dans la mesure où leur utilisation est autorisée par le droit de l'Union ou le droit national applicable:
a) systèmes d'IA destinés à être utilisés par les autorités répressives ou par les institutions, organes et organismes de
l'Union, ou en leur nom, en soutien aux autorités répressives ou en leur nom pour évaluer le risque qu'une
personne physique devienne la victime d'infractions pénales;
b) systèmes d'IA destinés à être utilisés par les autorités répressives ou par les institutions, organes et organismes de
l'Union, ou en leur nom, en soutien aux autorités répressives, en tant que polygraphes ou outils similaires;
c) systèmes d'IA destinés à être utilisés par les autorités répressives ou par les institutions, organes et organismes de
l'Union, ou en leur nom, en soutien aux autorités répressives pour évaluer la fiabilité des preuves au cours
d'enquêtes ou de poursuites pénales;

</details>

- Juge 14B : NON — L'affirmation selon laquelle 'les systèmes d'IA destinés à évaluer la solvabilité des personnes physiques sont considérés comme à haut risque' est **partiellement inexacte** : l'Annexe III (point b) m
- Avis proposé par Claude : OUI — Annexe III, point 5 b) : la solvabilité est bien à haut risque.

**Ton verdict :** OUI

---

## ollama/c03 — Un employeur peut-il utiliser une IA de reconnaissance des émotions pour surveiller ses salariés ?

**Réponse du modèle :**

Non, un employeur ne peut pas utiliser une IA de reconnaissance des émotions pour surveiller ses salariés, sauf dans le cas où la loi autorise l'utilisation de cette IA à des fins de prévention ou de détection des infractions pénales ou d'enquêtes en la matière, sous réserve de garanties appropriées pour les droits et libertés des tiers et conformément au droit de l'Union [Article 50].

<details><summary>Extraits fournis au modèle</summary>

**[Article 50]**
3.
Les déployeurs d’un système de reconnaissance des émotions ou d’un système de catégorisation biométrique
informent les personnes physiques qui y sont exposées du fonctionnement du système et traitent les données à caractère
personnel conformément au règlement (UE) 2016/679, au règlement (UE) 2018/1725 et à la directive (UE) 2016/680,
selon le cas. Cette obligation ne s’applique pas aux systèmes d’IA utilisés pour la catégorisation biométrique et la
reconnaissance des émotions dont la loi autorise l’utilisation à des fins de prévention ou de détection des infractions pénales
ou d’enquêtes en la matière, sous réserve de garanties appropriées pour les droits et libertés des tiers et conformément au
droit de l’Union.

**[Annexe III]**
c) systèmes d'IA destinés à être utilisés pour évaluer le niveau d'enseignement approprié qu'une personne recevra ou
sera en mesure d'atteindre, dans le contexte ou au sein d'établissements d'enseignement et de formation
professionnelle à tous les niveaux;
d) systèmes d'IA destinés à être utilisés pour surveiller et détecter des comportements interdits chez les étudiants lors
d'examens dans le contexte d'établissements d'enseignement et de formation ou en leur sein à tous les niveaux;
4.
Emploi, gestion de la main-d'œuvre et accès à l'emploi indépendant:
a) systèmes d'IA destinés à être utilisés pour le recrutement ou la sélection de personnes physiques, en particulier
pour publier des offres d'emploi ciblées, analyser et filtrer les candidatures et évaluer les candidats;
b) systèmes d'IA destinés à être utilisés pour prendre des décisions influant sur les conditions des relations
professionnelles, la promotion ou le licenciement dans le cadre de relations professionnelles contractuelles, pour
attribuer des tâches sur la base du comportement individuel, de traits de personnalité ou de caractéristiques
personnelles ou pour suivre et évaluer les performances et le comportement de personnes dans le cadre de telles
relations.
5.
Accès et droit aux services privés essentiels et aux services publics et prestations sociales essentiels:
a) systèmes d'IA destinés à être utilisés par les autorités publiques ou en leur nom pour évaluer l'éligibilité des
personnes physiques aux prestations et services d'aide sociale essentiels, y compris les services de soins de santé,
ainsi que pour octroyer, réduire, révoquer ou récupérer ces prestations et services;

**[Article 12]**
1.
Les systèmes d’IA à haut risque permettent, techniquement, l’enregistrement automatique des événements (journaux)
tout au long de la durée de vie du système.
2.
Afin de garantir un degré de traçabilité du fonctionnement d’un système d’IA qui soit adapté à la destination du
système, les fonctionnalités de journalisation permettent l’enregistrement des événements pertinents pour:
a) repérer les situations susceptibles d’avoir pour effet que le système d’IA à haut risque présente un risque au sens de
l’article 79, paragraphe 1, ou d’entraîner une modification substantielle;
b) faciliter la surveillance après commercialisation visée à l’article 72; et
c) surveiller le fonctionnement du système d’IA à haut risque comme prévu à l’article 26, paragraphe 5.
3.
Pour les systèmes d’IA à haut risque visés à l’annexe III, point 1 a), les fonctionnalités de journalisation fournissent, au
minimum:
a) l’enregistrement de la période de chaque utilisation du système (date et heure de début et de fin pour chaque utilisation);
b) la base de données de référence utilisée par le système pour vérifier les données d’entrée;
c) les données d’entrée pour lesquelles la recherche a abouti à une correspondance;
d) l’identification des personnes physiques participant à la vérification des résultats, visées à l’article 14, paragraphe 5.

**[Article 60]**
i) les participants aux essais en conditions réelles ont donné leur consentement éclairé conformément à l’article 61 ou,
dans le cas des services répressifs, lorsque la recherche d’un consentement éclairé empêcherait de réaliser les essais du
système d’IA, les essais proprement dits et les résultats des essais en conditions réelles n’ont pas d’effet négatif sur les
participants, et leurs données à caractère personnel sont supprimées une fois les essais réalisés;
j) le fournisseur ou le fournisseur potentiel ainsi que les déployeurs ou les déployeurs potentiels effectuent un contrôle
effectif des essais en conditions réelles, par des personnes dûment qualifiées dans le domaine concerné et disposant des
capacités, de la formation et de l’autorité nécessaires pour accomplir leurs tâches;
k) les prévisions, recommandations ou décisions du système d’IA peuvent effectivement être infirmées et ignorées.
5.
Tout participant aux essais en conditions réelles, ou son représentant légal, selon le cas, peut, sans encourir de
préjudice et sans devoir se justifier, se retirer des essais à tout moment, en révoquant son consentement éclairé et peut
demander la suppression immédiate et définitive de ses données à caractère personnel. Le retrait du consentement éclairé
n’affecte pas les activités déjà menées.

**[Article 57]**
7.
Les autorités compétentes donnent aux fournisseurs et aux fournisseurs potentiels participant au bac à sable
réglementaire de l’IA des orientations sur les attentes réglementaires et la manière de satisfaire aux exigences et obligations
énoncées dans le présent règlement.
À la demande du fournisseur ou du fournisseur potentiel du système d’IA, l’autorité compétente fournit une preuve écrite
des activités menées avec succès dans le bac à sable. L’autorité compétente fournit également un rapport de sortie détaillant
les activités menées dans le bac à sable ainsi que les résultats et acquis d’apprentissage correspondants. Les fournisseurs
peuvent utiliser ces documents pour démontrer leur conformité avec le présent règlement au moyen de la procédure
d’évaluation de la conformité ou d’activités pertinentes de surveillance du marché. À cet égard, les rapports de sortie et la
preuve écrite fournie par l’autorité nationale compétente sont évalués de manière positive par les autorités de surveillance
du marché et les organismes notifiés, en vue d’accélérer les procédures d’évaluation de la conformité dans une mesure
raisonnable.
8.
Sous réserve des dispositions relatives à la confidentialité énoncées à l’article 78 et avec l’accord du fournisseur ou du
fournisseur potentiel, la Commission et le Comité IA sont autorisés à accéder aux rapports de sortie et en tiennent compte,
le cas échéant, dans l’exercice des tâches qui leur incombent en vertu du présent règlement. Si le fournisseur ou le
fournisseur potentiel et l’autorité nationale compétente y consentent explicitement, le rapport de sortie peut être mis à la
disposition du public par l’intermédiaire de la plateforme d’information unique visée au présent article.

</details>

- Juge 14B : NON — L'affirmation selon laquelle un employeur ne peut pas utiliser une IA de reconnaissance des émotions pour surveiller ses salariés est **partiellement inexacte** : les extraits ne mentionnent pas expli
- Avis proposé par Claude : NON — La conclusion (interdit) est juste dans la loi (article 5 §1 f), mais l'article 5 n'était pas dans les extraits : la justification s'appuie à tort sur une exception de l'article 50.

**Ton verdict :** NON

---

## mistral/s01 — Quelles sont les pratiques d'IA interdites par le règlement ?

**Réponse du modèle :**

Voici les pratiques interdites par le règlement (UE) 2024/1689, telles que définies dans les extraits fournis :

1. **Manipulation comportementale** :
   - Utilisation de systèmes d’IA recourant à des techniques subliminales, manipulatrices ou trompeuses pour altérer substantiellement le comportement d’une personne ou d’un groupe, causant ou risquant de causer un **préjudice important** [Article 5(1)(a)].

2. **Exploitation des vulnérabilités** :
   - Exploitation des vulnérabilités liées à l’âge, au handicap ou à la situation socio-économique pour altérer le comportement d’une personne ou d’un groupe, avec les mêmes conséquences [Article 5(1)(b)].

3. **Note sociale** :
   - Évaluation ou classification des personnes sur une période donnée en fonction de leur comportement social ou de caractéristiques personnelles, conduisant à une **note sociale** entraînant des discriminations ou des restrictions [Article 5(1)(c)].

4. **Catégorisation biométrique intrusive** :
   - Utilisation de systèmes de catégorisation biométrique pour déduire ou inférer des caractéristiques sensibles (race, opinions politiques, convictions religieuses, orientation sexuelle, etc.) [Article 5(1)(g)].

5. **Surveillance biométrique répressive non autorisée** :
   - Utilisation de **systèmes d’identification biométrique à distance en temps réel** dans des espaces publics à des fins répressives, **sauf exceptions strictement encadrées** [Article 5(1)(h)].
   *(Voir les conditions d’autorisation possibles dans [Article 5(3) et (5)].)*

---
*Note* : Ces interdictions ne couvrent pas certaines exceptions précisées dans le texte (ex. : filtrage de données biométriques légalement acquises dans un cadre répressif [Article 5(1)(g)]).

<details><summary>Extraits fournis au modèle</summary>

**[Article 5]**
4.
Sans préjudice du paragraphe 3, toute utilisation d’un système d’identification biométrique à distance en temps réel
dans des espaces accessibles au public à des fins répressives est notifiée à l’autorité de surveillance du marché concernée et
à l’autorité nationale chargée de la protection des données, conformément aux règles nationales visées au paragraphe 5.
Cette notification contient, au minimum, les informations visées au paragraphe 6 et n’inclut pas de données opérationnelles
sensibles.
5.
Un État membre peut décider de prévoir la possibilité d’autoriser totalement ou partiellement l’utilisation de systèmes
d’identification biométriques à distance en temps réel dans des espaces accessibles au public à des fins répressives, dans les
limites et les conditions énumérées au paragraphe 1, premier alinéa, point h), et aux paragraphes 2 et 3. Les États membres
concernés établissent dans leur droit national les règles détaillées nécessaires à la demande, à la délivrance et à l’exercice des
autorisations visées au paragraphe 3, ainsi qu’à la surveillance et à l’établissement de rapports y afférents. Ces règles
précisent également pour quels objectifs énumérés au paragraphe 1, premier alinéa, point h), et notamment pour quelles
infractions pénales visées au point h), iii), les autorités compétentes peuvent être autorisées à utiliser ces systèmes à des fins
répressives. Les États membres notifient ces règles à la Commission au plus tard 30 jours après leur adoption. Les États
membres peuvent adopter, conformément au droit de l’Union, des lois plus restrictives sur l’utilisation de systèmes
d’identification biométrique à distance.

**[Article 2]**
11.
Le présent règlement n’empêche pas l’Union ou les États membres de maintenir ou d’introduire des dispositions
législatives, réglementaires ou administratives plus favorables aux travailleurs quant à la protection de leurs droits en ce qui
concerne l’utilisation de systèmes d’IA par les employeurs, ou d’encourager ou de permettre l’application de conventions
collectives plus favorables aux travailleurs.
12.
Le présent règlement ne s’applique pas aux systèmes d’IA publiés dans le cadre de licences libres et ouvertes, sauf s’ils
sont mis sur le marché ou mis en service en tant que systèmes d’IA à haut risque ou en tant que systèmes d’IA qui relèvent
de l’article 5 ou de l’article 50.

**[Article 5]**
1.
Les pratiques en matière d’IA suivantes sont interdites:
a) la mise sur le marché, la mise en service ou l’utilisation d’un système d’IA qui a recours à des techniques subliminales,
au-dessous du seuil de conscience d’une personne, ou à des techniques délibérément manipulatrices ou trompeuses, avec
pour objectif ou effet d’altérer substantiellement le comportement d’une personne ou d’un groupe de personnes en
portant considérablement atteinte à leur capacité à prendre une décision éclairée, amenant ainsi la personne à prendre
une décision qu’elle n’aurait pas prise autrement, d’une manière qui cause ou est raisonnablement susceptible de causer
un préjudice important à cette personne, à une autre personne ou à un groupe de personnes;
b) la mise sur le marché, la mise en service ou l’utilisation d’un système d’IA qui exploite les éventuelles vulnérabilités dues
à l’âge, au handicap ou à la situation sociale ou économique spécifique d’une personne physique ou d’un groupe de
personnes donné avec pour objectif ou effet d’altérer substantiellement le comportement de cette personne ou d’un
membre de ce groupe d’une manière qui cause ou est raisonnablement susceptible de causer un préjudice important
à cette personne ou à un tiers;
c) la mise sur le marché, la mise en service ou l’utilisation de systèmes d’IA pour l’évaluation ou la classification de
personnes physiques ou de groupes de personnes au cours d’une période donnée en fonction de leur comportement
social ou de caractéristiques personnelles ou de personnalité connues, déduites ou prédites, la note sociale conduisant
à l’une ou l’autre des situations suivantes, ou aux deux:

**[Article 5]**
g) la mise sur le marché, la mise en service à cette fin spécifique ou l’utilisation de systèmes de catégorisation biométrique
qui catégorisent individuellement les personnes physiques sur la base de leurs données biométriques afin d’arriver à des
déductions ou des inférences concernant leur race, leurs opinions politiques, leur affiliation à une organisation syndicale,
leurs convictions religieuses ou philosophiques, leur vie sexuelle ou leur orientation sexuelle; cette interdiction ne couvre
pas l’étiquetage ou le filtrage d’ensembles de données biométriques acquis légalement, tels que des images, fondés sur des
données biométriques ou la catégorisation de données biométriques dans le domaine répressif;
h) l’utilisation de systèmes d’identification biométrique à distance en temps réel dans des espaces accessibles au public à des
fins répressives, sauf si et dans la mesure où cette utilisation est strictement nécessaire eu égard à l’un des objectifs
suivants:

**[Article 5]**
6.
Les autorités nationales de surveillance du marché et les autorités nationales chargées de la protection des données des
États membres qui ont été notifiées de l’utilisation de systèmes d’identification biométriques à distance en temps réel dans
des espaces accessibles au public à des fins répressives, conformément au paragraphe 4, soumettent à la Commission des
rapports annuels sur cette utilisation. À cette fin, la Commission fournit aux États membres et aux autorités nationales en
matière de surveillance du marché et de protection des données un modèle comprenant des informations sur le nombre de
décisions prises par les autorités judiciaires compétentes ou par une autorité administrative indépendante dont la décision
est contraignante en ce qui concerne les demandes d’autorisation conformément au paragraphe 3, ainsi que sur leur
résultat.
7.
La Commission publie des rapports annuels sur l’utilisation de systèmes d’identification biométriques à distance en
temps réel dans des espaces accessibles au public à des fins répressives, fondés sur des données agrégées dans les États
membres sur la base des rapports annuels visés au paragraphe 6. Ces rapports annuels n’incluent pas de données
opérationnelles sensibles sur les activités répressives connexes.
8.
Le présent article ne porte pas atteinte aux interdictions qui s’appliquent lorsqu’une pratique en matière d’IA enfreint
d’autres dispositions du droit de l’Union.

</details>

- Juge 14B : NON — L'affirmation selon laquelle 'la note sociale [...] entraînant des discriminations ou des restrictions' est une pratique interdite n'est pas explicitement mentionnée dans les extraits fournis. L'extra
- Avis proposé par Claude : OUI — Points a), b), c), g), h) de l'article 5 et l'exception de filtrage bien présents dans les extraits.

**Ton verdict :** OUI

---

## mistral/s02 — Comment le règlement définit-il un système d'IA ?

**Réponse du modèle :**

D'après le règlement, un **système d’IA** est défini comme suit :

*« un système automatisé qui est conçu pour fonctionner à différents niveaux d’autonomie et peut faire preuve d’une capacité d’adaptation après son déploiement, et qui, pour des objectifs explicites ou implicites, déduit, à partir des entrées qu’il reçoit, la manière de générer des sorties telles que des prédictions, du contenu, des recommandations ou des décisions qui peuvent influencer les environnements physiques ou virtuels ».*

[Article 3, point 1]

<details><summary>Extraits fournis au modèle</summary>

**[Article 3]**
Aux fins du présent règlement, on entend par:
1)
«système d’IA», un système automatisé qui est conçu pour fonctionner à différents niveaux d’autonomie et peut faire
preuve d’une capacité d’adaptation après son déploiement, et qui, pour des objectifs explicites ou implicites, déduit,
à partir des entrées qu’il reçoit, la manière de générer des sorties telles que des prédictions, du contenu, des
recommandations ou des décisions qui peuvent influencer les environnements physiques ou virtuels;
2)
«risque», la combinaison de la probabilité d’un préjudice et de la sévérité de celui-ci;
3)
«fournisseur», une personne physique ou morale, une autorité publique, une agence ou tout autre organisme qui
développe ou fait développer un système d’IA ou un modèle d’IA à usage général et le met sur le marché ou met le
système d’IA en service sous son propre nom ou sa propre marque, à titre onéreux ou gratuit;
4)
«déployeur», une personne physique ou morale, une autorité publique, une agence ou un autre organisme utilisant sous
sa propre autorité un système d’IA sauf lorsque ce système est utilisé dans le cadre d’une activité personnelle à caractère
non professionnel;
5)
«mandataire», une personne physique ou morale située ou établie dans l’Union ayant reçu et accepté un mandat écrit
d’un fournisseur de système d’IA ou de modèle d’IA à usage général pour s’acquitter en son nom des obligations et des
procédures établies par le présent règlement;
6)
«importateur», une personne physique ou morale située ou établie dans l’Union qui met sur le marché un système d’IA
qui porte le nom ou la marque d’une personne physique ou morale établie dans un pays tiers;

**[Article 1]**
1.
L’objectif du présent règlement est d’améliorer le fonctionnement du marché intérieur et de promouvoir l’adoption
d’une intelligence artificielle (IA) axée sur l’humain et digne de confiance, tout en garantissant un niveau élevé de protection
de la santé, de la sécurité et des droits fondamentaux consacrés dans la Charte, notamment la démocratie, l’état de droit et la
protection de l’environnement, contre les effets néfastes des systèmes d’IA dans l’Union, et en soutenant l’innovation.
2.
Le présent règlement établit:
a) des règles harmonisées concernant la mise sur le marché, la mise en service et l’utilisation de systèmes d’IA dans l’Union;
b) l’interdiction de certaines pratiques en matière d’IA;
c) des exigences spécifiques applicables aux systèmes d’IA à haut risque et des obligations imposées aux opérateurs de ces
systèmes;
d) des règles harmonisées en matière de transparence applicables à certains systèmes d’IA;
e) des règles harmonisées pour la mise sur le marché de modèles d’IA à usage général;
f) des règles relatives au suivi du marché, à la surveillance du marché, à la gouvernance et à l’application des règles;
g) des mesures visant à soutenir l’innovation, en mettant particulièrement l’accent sur les PME, y compris les jeunes
pousses.

**[Article 3]**
53) «plan d’essais en conditions réelles», un document décrivant les objectifs, la méthode, la population et le champ
d’application géographique et la portée dans le temps, le suivi, l’organisation et la conduite des essais en conditions
réelles;
54) «plan du bac à sable», un document adopté conjointement entre le fournisseur participant et l’autorité compétente, qui
décrit les objectifs, les conditions, les délais, la méthodologie et les exigences applicables aux activités réalisées au sein
du bac à sable;
55) «bac à sable réglementaire de l’IA», un cadre contrôlé mis en place par une autorité compétente qui offre aux
fournisseurs ou fournisseurs potentiels de systèmes d’IA la possibilité de développer, d’entraîner, de valider et de tester,
lorsqu’il y a lieu en conditions réelles, un système d’IA innovant, selon un plan du bac à sable pour une durée limitée
sous surveillance réglementaire;
56) «maîtrise de l’IA», les compétences, les connaissances et la compréhension qui permettent aux fournisseurs, aux
déployeurs et aux personnes concernées, compte tenu de leurs droits et obligations respectifs dans le contexte du
présent règlement, de procéder à un déploiement des systèmes d’IA en toute connaissance de cause, ainsi que de
prendre conscience des possibilités et des risques que comporte l’IA, ainsi que des préjudices potentiels qu’elle peut
causer;

**[Article 64]**
1.
La Commission développe l’expertise et les capacités de l’Union dans le domaine de l’IA par l’intermédiaire du Bureau
de l’IA.
2.
Les États membres facilitent l’accomplissement des tâches confiées au Bureau de l’IA, telles qu’elles sont définies dans
le présent règlement.

**[Article 65]**
6.
Le Comité IA établit deux sous-groupes permanents chargés de fournir une plateforme de coopération et d’échange
entre les autorités de surveillance du marché et les autorités notifiantes au sujet des questions liées à la surveillance du
marché et aux organismes notifiés respectivement.
Le sous-groupe permanent pour la surveillance du marché devrait agir au titre de groupe de coopération administrative
(ADCO) pour le présent règlement au sens de l’article 30 du règlement (UE) 2019/1020.
Le Comité IA peut créer d’autres sous-groupes permanents ou temporaires, s’il y a lieu, afin d’examiner des questions
spécifiques. Le cas échéant, des représentants du forum consultatif visé à l’article 67 peuvent être invités à ces sous-groupes
ou à des réunions spécifiques de ces sous-groupes en qualité d’observateurs.
7.
Le Comité IA est organisé et fonctionne de façon à garantir l’objectivité et l’impartialité de ses activités.
8.
Le Comité IA est présidé par l’un des représentants des États membres. Le Bureau de l’IA assure le secrétariat du
Comité IA, convoque les réunions à la demande du président et prépare l’ordre du jour conformément aux tâches du Comité
IA au titre du présent règlement et à son règlement intérieur.

</details>

- Juge 14B : OUI — 
- Avis proposé par Claude : OUI — Citation exacte de l'article 3, point 1.

**Ton verdict :** OUI

---

## mistral/s04 — Quel est le montant maximal de l'amende en cas de non-respect des pratiques interdites ?

**Réponse du modèle :**

En cas de **non-respect des pratiques interdites** visées à l’**article 5** par des **opérateurs** (entreprises ou autres acteurs privés), le montant maximal de l’amende administrative est de **35 000 000 EUR ou 7 % du chiffre d’affaires annuel mondial total** de l’entreprise concernée, le montant le plus élevé étant retenu.

Pour les **institutions, organes ou organismes de l’Union**, le montant maximal est de **1 500 000 EUR** [Article 100(2)].

[Article 99(3)] / [Article 100(2)].

<details><summary>Extraits fournis au modèle</summary>

**[Article 100]**
2.
Le non-respect de l’interdiction des pratiques en matière d’IA visées à l’article 5 fait l’objet d’une amende administrative
pouvant aller jusqu’à 1 500 000 EUR.
3.
La non-conformité du système d’IA avec les exigences ou obligations au titre du présent règlement, autres que celles
énoncées à l’article 5, fait l’objet d’une amende administrative pouvant aller jusqu’à 750 000 EUR.
4.
Avant de prendre des décisions en vertu du présent article, le Contrôleur européen de la protection des données donne
à l’institution, organe ou organisme de l’Union faisant l’objet des procédures conduites par le Contrôleur européen de la
protection des données la possibilité de faire connaître son point de vue sur l’éventuelle infraction. Le Contrôleur européen
de la protection des données ne fonde ses décisions que sur les éléments et les circonstances au sujet desquels les parties
concernées ont pu formuler des observations. Les éventuels plaignants sont étroitement associés à la procédure.
5.
Les droits de la défense des parties concernées sont pleinement respectés dans le déroulement de la procédure. Les
parties disposent d’un droit d’accès au dossier du Contrôleur européen de la protection des données, sous réserve de l’intérêt
légitime des personnes ou entreprises concernées en ce qui concerne la protection de leurs données à caractère personnel
ou de leurs secrets commerciaux.
6.
Les fonds collectés en imposant des amendes en vertu du présent article contribuent au budget général de l’Union. Les
amendes ne compromettent pas le bon fonctionnement de l’institution, organe ou organisme de l’Union faisant l’objet d’une
amende.

**[Article 99]**
1.
Conformément aux conditions établies dans le présent règlement, les États membres déterminent le régime des
sanctions et autres mesures d’exécution, qui peuvent également comprendre des avertissements et des mesures non
monétaires, applicables aux violations du présent règlement commises par des opérateurs, et prennent toute mesure
nécessaire pour veiller à la mise en œuvre correcte et effective de ces sanctions, tenant ainsi compte des lignes directrices
publiées par la Commission en vertu de l’article 96. Ces sanctions doivent être effectives, proportionnées et dissuasives. Elles
tiennent compte des intérêts des PME, y compris les jeunes pousses, et de leur viabilité économique.
2.
Les États membres informent la Commission, sans retard et au plus tard à la date d’entrée en application, du régime
des sanctions et des autres mesures d’exécution visées au paragraphe 1, de même que de toute modification apportée
ultérieurement à ce régime ou à ces mesures.
3.
Le non-respect de l’interdiction des pratiques en matière d’IA visées à l’article 5 fait l’objet d’amendes administratives
pouvant aller jusqu’à 35 000 000 EUR ou, si l’auteur de l’infraction est une entreprise, jusqu’à 7 % de son chiffre d’affaires
annuel mondial total réalisé au cours de l’exercice précédent, le montant le plus élevé étant retenu.
4.
La non-conformité avec l’une quelconque des dispositions suivantes relatives aux opérateurs ou aux organismes
notifiés, autres que celles énoncées à l’article 5, fait l’objet d’une amende administrative pouvant aller jusqu’à
15 000 000 EUR ou, si l’auteur de l’infraction est une entreprise, jusqu’à 3 % de son chiffre d’affaires annuel mondial total
réalisé au cours de l’exercice précédent, le montant le plus élevé étant retenu:

**[Article 99]**
a) les obligations incombant aux fournisseurs en vertu de l’article 16;
b) les obligations incombant aux mandataires en vertu de l’article 22;
c) les obligations incombant aux importateurs en vertu de l’article 23;
d) les obligations incombant aux distributeurs en vertu de l’article 24;
e) les obligations incombant aux déployeurs en vertu de l’article 26;
f) les exigences et obligations applicables aux organismes notifiés en application de l’article 31, de l’article 33,
paragraphes 1, 3 et 4, ou de l’article 34;
g) les obligations de transparence pour les fournisseurs et les déployeurs conformément à l’article 50.
5.
La fourniture d’informations inexactes, incomplètes ou trompeuses aux organismes notifiés ou aux autorités
nationales compétentes en réponse à une demande fait l’objet d’une amende administrative pouvant aller jusqu’à
7 500 000 EUR ou, si l’auteur de l’infraction est une entreprise, jusqu’à 1 % de son chiffre d’affaires annuel mondial total
réalisé au cours de l’exercice précédent, le montant le plus élevé étant retenu.
6.
Dans le cas des PME, y compris les jeunes pousses, chaque amende visée au présent article s’élève au maximum aux
pourcentages ou montants visés aux paragraphes 3, 4 et 5, le chiffre le plus faible étant retenu.
7.
Pour décider s’il y a lieu d’imposer une amende administrative et pour décider du montant de l’amende administrative
dans chaque cas d’espèce, toutes les caractéristiques propres à chaque cas sont prises en considération et, le cas échéant, il
est tenu compte des éléments suivants:
a) la nature, la gravité et la durée de la violation et de ses conséquences, compte tenu de la finalité du système d’IA
concerné, ainsi que, le cas échéant, du nombre de personnes touchées et du niveau de dommage qu’elles ont subi;

**[Article 101]**
5.
La Cour de justice de l’Union européenne statue avec compétence de pleine juridiction sur les recours formés contre
les décisions par lesquelles la Commission a fixé une amende au titre du présent article. Elle peut supprimer, réduire ou
majorer l’amende infligée.
6.
La Commission adopte des actes d’exécution contenant les modalités détaillées des procédures et des garanties
procédurales en vue de l’adoption éventuelle de décisions en vertu du paragraphe 1 du présent article. Ces actes d’exécution
sont adoptés en conformité avec la procédure d’examen visée à l’article 98, paragraphe 2.

**[Article 99]**
b) la question de savoir si des amendes administratives ont déjà été imposées par d’autres autorités de surveillance du
marché au même opérateur pour la même violation;
c) la question de savoir si des amendes administratives ont déjà été imposées par d’autres autorités au même opérateur pour
des violations d’autres dispositions du droit de l’Union ou du droit national, lorsque ces violations résultent de la même
activité ou omission constituant une violation pertinente au sens du présent règlement;
d) la taille, le chiffre d’affaires annuel et la part de marché de l’opérateur qui commet la violation;
e) toute autre circonstance aggravante ou atténuante applicable aux circonstances de l’espèce, telle que les avantages
financiers obtenus ou les pertes évitées, directement ou indirectement, du fait de la violation;
f) le degré de coopération établi avec les autorités nationales compétentes en vue de remédier à la violation et d’en atténuer
les éventuels effets négatifs;
g) le degré de responsabilité de l’opérateur, compte tenu des mesures techniques et organisationnelles qu’il a mises en
œuvre;
h) la manière dont les autorités nationales compétentes ont eu connaissance de la violation, notamment si, et dans quelle
mesure, l’opérateur a notifié la violation;
i) le fait que la violation a été commise délibérément ou par négligence;
j) toute mesure prise par l’opérateur pour atténuer le préjudice subi par les personnes concernées.
8.
Chaque État membre établit les règles déterminant dans quelle mesure des amendes administratives peuvent être
imposées à des autorités et organismes publics établis sur son territoire.

</details>

- Juge 14B : NON — L'affirmation selon laquelle les amendes s'appliquent aux 'opérateurs' (entreprises ou autres acteurs privés) en général est incorrecte : les montants de l’**article 99(3)** (35 000 000 EUR ou 7 % du 
- Avis proposé par Claude : OUI — Articles 99 §3 et 100 §2 corrects ; la glose « entreprises ou autres acteurs privés » est mineure.

**Ton verdict :** OUI

---

## mistral/s05 — À partir de quelle date le règlement est-il applicable ?

**Réponse du modèle :**

Le règlement (UE) 2024/1689 est applicable **à partir du 2 août 2026** dans son ensemble, sauf exceptions précisées à l’[Article 113].

<details><summary>Extraits fournis au modèle</summary>

**[Article 113]**
Le présent règlement entre en vigueur le vingtième jour suivant celui de sa publication au Journal officiel de l’Union européenne.
Il est applicable à partir du 2 août 2026.
Toutefois:
a) les chapitres I et II sont applicables à partir du 2 février 2025;
b) le chapitre III, section 4, le chapitre V, le chapitre VII, le chapitre XII et l’article 78 s’appliquent à partir du 2 août 2025,
à l’exception de l’article 101;
c) l’article 6, paragraphe 1, et les obligations correspondantes du présent règlement s’appliquent à partir du 2 août 2027.
Le présent règlement est obligatoire dans tous ses éléments et directement applicable dans tout État membre.
Fait à Bruxelles, le 13 juin 2024.
Par le Parlement européen
La présidente
R. METSOLA
Par le Conseil
Le président
M. MICHEL

**[Article 98]**
1.
La Commission est assistée par un comité. Ledit comité est un comité au sens du règlement (UE) no 182/2011.
2.
Lorsqu’il est fait référence au présent paragraphe, l’article 5 du règlement (UE) no 182/2011 s’applique.

**[Article 111]**
1.
Sans préjudice de l’application de l’article 5 visée à l’article 113, paragraphe 3, point a), les systèmes d’IA qui sont des
composants des systèmes d’information à grande échelle établis par les actes juridiques énumérés à l’annexe X et mis sur le
marché ou mis en service avant le 2 août 2027 sont mis en conformité avec le présent règlement au plus tard le
31 décembre 2030.
Il est tenu compte des exigences énoncées dans le présent règlement lors de l’évaluation de chaque système d’information
à grande échelle établi par les actes juridiques énumérés à l’annexe X devant être effectuée conformément à ces actes
juridiques et lorsque ces actes juridiques sont remplacés ou modifiés.
2.
Sans préjudice de l’application de l’article 5 visée à l’article 113, paragraphe 3, point a), le présent règlement s’applique
aux opérateurs de systèmes d’IA à haut risque, autres que les systèmes visés au paragraphe 1 du présent article, qui ont été
mis sur le marché ou mis en service avant le 2 août 2026, uniquement si, à compter de cette date, ces systèmes subissent
d’importantes modifications de leurs conceptions. En tout état de cause, les fournisseurs et les déployeurs de systèmes d’IA
à haut risque destinés à être utilisés par des autorités publiques prennent les mesures nécessaires pour se conformer aux
exigences et obligations du présent règlement au plus tard le 2 août 2030.
3.
Les fournisseurs de modèles d’IA à usage général qui ont été mis sur le marché avant le 2 août 2025 prennent les
mesures nécessaires pour se conformer aux obligations prévues par le présent règlement au plus tard le 2 août 2027.

**[Annexe X]**
4.
Système d'entrée/de sortie
Règlement (UE) 2017/2226 du Parlement européen et du Conseil du 30 novembre 2017 portant création d'un
système d'entrée/de sortie (EES) pour enregistrer les données relatives aux entrées, aux sorties et aux refus d'entrée
concernant les ressortissants de pays tiers qui franchissent les frontières extérieures des États membres et portant
détermination des conditions d'accès à l'EES à des fins répressives, et modifiant la convention d'application de
l'accord de Schengen et les règlements (CE) no 767/2008 et (UE) no 1077/2011 (JO L 327 du 9.12.2017, p. 20).
5.
Système européen d'information et d'autorisation concernant les voyages
a) Règlement (UE) 2018/1240 du Parlement européen et du Conseil du 12 septembre 2018 portant création d'un
système européen d'information et d'autorisation concernant les voyages (ETIAS) et modifiant les règlements (UE)
no 1077/2011, (UE) no 515/2014, (UE) 2016/399, (UE) 2016/1624 et (UE) 2017/2226 (JO L 236 du 19.9.2018,
p. 1).
b) Règlement (UE) 2018/1241 du Parlement européen et du Conseil du 12 septembre 2018 modifiant le règlement
(UE) 2016/794 aux fins de la création d'un système européen d'information et d'autorisation concernant les
voyages (ETIAS) (JO L 236 du 19.9.2018, p. 72).

**[Article 60]**
b) l’autorité de surveillance du marché de l’État membre où les essais en conditions réelles doivent être réalisés a approuvé
les essais en conditions réelles et le plan d’essais en conditions réelles; lorsque l’autorité de surveillance du marché n’a pas
fourni de réponse dans un délai de 30 jours, les essais en conditions réelles et le plan d’essais en conditions réelles sont
réputés approuvés; lorsque le droit national ne prévoit pas d’approbation tacite, les essais en conditions réelles restent
soumis à autorisation;

</details>

- Juge 14B : NON — L'affirmation selon laquelle le règlement est applicable **dans son ensemble** à partir du 2 août 2026 contredit les extraits, qui précisent que **seuls certains chapitres et articles sont applicables
- Avis proposé par Claude : OUI — « Applicable le 2 août 2026, sauf exceptions de l'article 113 » est exact. Le juge s'est trompé.

**Ton verdict :** OUI

---

## mistral/s06 — Quelles sont les exigences de contrôle humain pour les systèmes d'IA à haut risque ?

**Réponse du modèle :**

Voici les exigences de contrôle humain pour les systèmes d’IA à haut risque, conformément aux extraits fournis :

1. **Conception et développement** :
   - Les systèmes doivent permettre un **contrôle effectif par des personnes physiques** pendant leur utilisation, via des interfaces homme-machine appropriées [Article 14(1)].
   - Le contrôle humain vise à **prévenir ou réduire les risques** pour la santé, la sécurité ou les droits fondamentaux, même en cas de mauvaise utilisation raisonnablement prévisible [Article 14(2)].

2. **Mesures de contrôle proportionnées** :
   - Les mesures sont adaptées aux **risques, au niveau d’autonomie et au contexte d’utilisation** du système.
   - Elles peuvent être :
     a) **Intégrées par le fournisseur** dans le système avant sa mise sur le marché ou sa mise en service [Article 14(3)(a)].
     b) **Identifiées par le fournisseur** pour être mises en œuvre par le déployeur [Article 14(3)(b)].

3. **Capacités requises pour les opérateurs humains** :
   Les personnes chargées du contrôle doivent pouvoir :
   - Comprendre les **capacités et limites** du système et surveiller son fonctionnement [Article 14(4)(a)].
   - Éviter le **biais d’automatisation** (confiance excessive dans les sorties du système) [Article 14(4)(b)].
   - **Interpréter correctement** les sorties du système [Article 14(4)(c)].
   - **Décider de ne pas utiliser** le système ou d’ignorer/modifier ses sorties [Article 14(4)(d)].
   - **Intervenir ou arrêter** le système en cas de dysfonctionnement (ex. : bouton d’arrêt) [Article 14(4)(e)].

4. **Exigences spécifiques pour les systèmes d’identification biométrique** :
   - **Contrôle humain accru** : Aucune mesure ou décision ne peut être prise sur la base de l’identification par le système **sans vérification et confirmation humaine** [Considérant 73].

5. **Guidance et formation** :
   - Le système doit inclure des **mécanismes pour guider et informer** l’opérateur humain (ex. : outils d’interprétation, alertes) [Considérant 73].

---
*Source : [Article 14], [Considérant 73]*.

<details><summary>Extraits fournis au modèle</summary>

**[Article 14]**
1.
La conception et le développement des systèmes d’IA à haut risque permettent, notamment au moyen d’interfaces
homme-machine appropriées, un contrôle effectif par des personnes physiques pendant leur période d’utilisation.
2.
Le contrôle humain vise à prévenir ou à réduire au minimum les risques pour la santé, la sécurité ou les droits
fondamentaux qui peuvent apparaître lorsqu’un système d’IA à haut risque est utilisé conformément à sa destination ou
dans des conditions de mauvaise utilisation raisonnablement prévisible, en particulier lorsque de tels risques persistent
malgré l’application d’autres exigences énoncées dans la présente section.
3.
Les mesures de contrôle sont proportionnées aux risques, au niveau d’autonomie et au contexte d’utilisation du
système d’IA à haut risque, et sont assurées au moyen d’un ou des deux types de mesures suivants:
a) des mesures identifiées et, lorsque cela est techniquement possible, intégrées par le fournisseur dans le système d’IA
à haut risque avant la mise sur le marché ou la mise en service de ce dernier;
b) des mesures identifiées par le fournisseur avant la mise sur le marché ou la mise en service du système d’IA à haut risque
et qui se prêtent à une mise en œuvre par le déployeur.
4.
Aux fins de la mise en œuvre des dispositions des paragraphes 1, 2 et 3, le système d’IA à haut risque est fourni au
déployeur de telle manière que les personnes physiques chargées d’effectuer un contrôle humain, dans la mesure où cela est
approprié et proportionné, ont la possibilité:

**[Considérant 73]**
Les systèmes d’IA à haut risque devraient être conçus et développés de manière à ce que les personnes physiques
puissent superviser leur fonctionnement et veiller à ce qu’ils soient utilisés comme prévu et à ce que leurs incidences
soient prises en compte tout au long de leur cycle de vie. À cette fin, des mesures appropriées de contrôle humain
devraient être établies par le fournisseur du système avant sa mise sur le marché ou sa mise en service. En particulier,
le cas échéant, de telles mesures devraient garantir que le système est soumis à des contraintes opérationnelles
intégrées qui ne peuvent pas être ignorées par le système lui-même, que le système répond aux ordres de l’opérateur
humain et que les personnes physiques auxquelles le contrôle humain a été confié ont les compétences, la formation
et l’autorité nécessaires pour s’acquitter de ce rôle. Il est également essentiel, le cas échéant, de veiller à ce que les
systèmes d’IA à haut risque comprennent des mécanismes destinés à guider et à informer une personne physique
à laquelle le contrôle humain a été confié, afin qu’elle puisse décider en connaissance de cause s’il faut intervenir,
à quel moment et de quelle manière, pour éviter des conséquences négatives ou des risques, ou arrêter le système s’il
ne fonctionne pas comme prévu. Compte tenu des conséquences importantes pour les personnes en cas d’erreur
dans les correspondances établies par certains systèmes d’identification biométrique, il convient de prévoir pour ces
systèmes une exigence de contrôle humain accru, de manière qu’aucune mesure ou décision ne puisse être prise par
le déployeur sur la base de l’identification obtenue par le système, à moins qu’elle n’ait été vérifiée et confirmée

**[Article 14]**
a) de comprendre correctement les capacités et les limites pertinentes du système d’IA à haut risque et d’être en mesure de
surveiller correctement son fonctionnement, y compris en vue de détecter et de traiter les anomalies, les
dysfonctionnements et les performances inattendues;
b) d’avoir conscience d’une éventuelle tendance à se fier automatiquement ou excessivement aux sorties produites par un
système d’IA à haut risque (biais d’automatisation), en particulier pour les systèmes d’IA à haut risque utilisés pour
fournir des informations ou des recommandations concernant les décisions à prendre par des personnes physiques;
c) d’interpréter correctement les sorties du système d’IA à haut risque, compte tenu par exemple des outils et méthodes
d’interprétation disponibles;
d) de décider, dans une situation particulière, de ne pas utiliser le système d’IA à haut risque ou d’ignorer, remplacer ou
inverser la sortie du système d’IA à haut risque;
e) d’intervenir dans le fonctionnement du système d’IA à haut risque ou d’interrompre le système au moyen d’un bouton
d’arrêt ou d’une procédure similaire permettant au système de s’arrêter de manière sécurisée.

**[Article 9]**
6.
Les systèmes d’IA à haut risque sont soumis à des essais afin de déterminer les mesures de gestion des risques les plus
appropriées et les plus ciblées. Les essais garantissent que les systèmes d’IA à haut risque fonctionnent de manière conforme
à leur destination et qu’ils sont conformes aux exigences énoncées dans la présente section.
7.
Les procédures d’essai peuvent comprendre des essais en conditions réelles conformément à l’article 60.
8.
Les tests des systèmes d’IA à haut risque sont effectués, selon les besoins, à tout moment pendant le processus de
développement et, en tout état de cause, avant leur mise sur le marché ou leur mise en service. Les tests sont effectués sur la
base d’indicateurs et de seuils probabilistes préalablement définis, qui sont adaptés à la destination du système d’IA à haut
risque.
9.
Lors de la mise en œuvre du système de gestion des risques prévu aux paragraphes 1 à 7, les fournisseurs prennent en
considération la probabilité que, compte tenu de sa destination, le système d’IA à haut risque puisse avoir une incidence
négative sur des personnes âgées de moins de 18 ans et, le cas échéant, sur d’autres groupes vulnérables.
10.
En ce qui concerne les fournisseurs de systèmes d’IA à haut risque qui sont soumis à des exigences concernant les
processus internes de gestion des risques en vertu d’autres dispositions pertinentes du droit de l’Union, les aspects présentés
aux paragraphes 1 à 9 peuvent faire partie des procédures de gestion des risques établies conformément à ladite législation,
ou être combinées à celles-ci.

**[Annexe III]**
c) systèmes d'IA destinés à être utilisés pour évaluer le niveau d'enseignement approprié qu'une personne recevra ou
sera en mesure d'atteindre, dans le contexte ou au sein d'établissements d'enseignement et de formation
professionnelle à tous les niveaux;
d) systèmes d'IA destinés à être utilisés pour surveiller et détecter des comportements interdits chez les étudiants lors
d'examens dans le contexte d'établissements d'enseignement et de formation ou en leur sein à tous les niveaux;
4.
Emploi, gestion de la main-d'œuvre et accès à l'emploi indépendant:
a) systèmes d'IA destinés à être utilisés pour le recrutement ou la sélection de personnes physiques, en particulier
pour publier des offres d'emploi ciblées, analyser et filtrer les candidatures et évaluer les candidats;
b) systèmes d'IA destinés à être utilisés pour prendre des décisions influant sur les conditions des relations
professionnelles, la promotion ou le licenciement dans le cadre de relations professionnelles contractuelles, pour
attribuer des tâches sur la base du comportement individuel, de traits de personnalité ou de caractéristiques
personnelles ou pour suivre et évaluer les performances et le comportement de personnes dans le cadre de telles
relations.
5.
Accès et droit aux services privés essentiels et aux services publics et prestations sociales essentiels:
a) systèmes d'IA destinés à être utilisés par les autorités publiques ou en leur nom pour évaluer l'éligibilité des
personnes physiques aux prestations et services d'aide sociale essentiels, y compris les services de soins de santé,
ainsi que pour octroyer, réduire, révoquer ou récupérer ces prestations et services;

</details>

- Juge 14B : NON — L'affirmation selon laquelle 'Les systèmes doivent permettre un **contrôle effectif par des personnes physiques** pendant leur utilisation, via des interfaces homme-machine appropriées' est **partiell
- Avis proposé par Claude : NON — « Aucune décision sans vérification et confirmation humaine » ne figure pas dans les extraits : le modèle l'a tiré de sa mémoire (c'est l'article 14 §5).

**Ton verdict :** NON

---

## mistral/s07 — Que doit contenir le système de gestion des risques d'un système d'IA à haut risque ?

**Réponse du modèle :**

D'après les extraits fournis, le système de gestion des risques d'un système d'IA à haut risque doit contenir les éléments suivants :

1. **Un processus itératif continu** couvrant tout le cycle de vie du système, incluant des examens et mises à jour périodiques [Article 9(1)].

2. **Les étapes suivantes** :
   - **Identification et analyse** des risques raisonnablement prévisibles pour la santé, la sécurité ou les droits fondamentaux, lors d'une utilisation conforme à la destination [Article 9(2)(a)].
   - **Estimation et évaluation** des risques liés à une utilisation conforme et à une mauvaise utilisation raisonnablement prévisible [Article 9(2)(b)].
   - **Évaluation** des risques émergents, basée sur les données recueillies via le système de surveillance après commercialisation [Article 9(2)(c)].
   - **Adoption de mesures appropriées** pour gérer les risques identifiés [Article 9(2)(d)].

3. **Des mesures de gestion des risques** visant à :
   - Éliminer ou réduire les risques identifiés, dans la mesure du possible, par une conception et un développement adaptés [Article 9(5)(a)].
   - Mettre en œuvre des mesures d’atténuation et de contrôle pour les risques non éliminables [Article 9(5)(b)].
   - Fournir aux déployeurs les informations requises (conformément à l’[Article 13]) et, le cas échéant, une formation [Article 9(5)(c)].

4. **Une prise en compte** des effets combinés des exigences du règlement et des connaissances attendues des déployeurs (compétences, contexte d’utilisation) [Article 9(4) et (5)].

5. **Une documentation** formalisée et mise à jour régulièrement [Article 9(1)].

<details><summary>Extraits fournis au modèle</summary>

**[Article 9]**
6.
Les systèmes d’IA à haut risque sont soumis à des essais afin de déterminer les mesures de gestion des risques les plus
appropriées et les plus ciblées. Les essais garantissent que les systèmes d’IA à haut risque fonctionnent de manière conforme
à leur destination et qu’ils sont conformes aux exigences énoncées dans la présente section.
7.
Les procédures d’essai peuvent comprendre des essais en conditions réelles conformément à l’article 60.
8.
Les tests des systèmes d’IA à haut risque sont effectués, selon les besoins, à tout moment pendant le processus de
développement et, en tout état de cause, avant leur mise sur le marché ou leur mise en service. Les tests sont effectués sur la
base d’indicateurs et de seuils probabilistes préalablement définis, qui sont adaptés à la destination du système d’IA à haut
risque.
9.
Lors de la mise en œuvre du système de gestion des risques prévu aux paragraphes 1 à 7, les fournisseurs prennent en
considération la probabilité que, compte tenu de sa destination, le système d’IA à haut risque puisse avoir une incidence
négative sur des personnes âgées de moins de 18 ans et, le cas échéant, sur d’autres groupes vulnérables.
10.
En ce qui concerne les fournisseurs de systèmes d’IA à haut risque qui sont soumis à des exigences concernant les
processus internes de gestion des risques en vertu d’autres dispositions pertinentes du droit de l’Union, les aspects présentés
aux paragraphes 1 à 9 peuvent faire partie des procédures de gestion des risques établies conformément à ladite législation,
ou être combinées à celles-ci.

**[Article 9]**
4.
Les mesures de gestion des risques visées au paragraphe 2, point d), tiennent dûment compte des effets et de
l’interaction possibles résultant de l’application combinée des exigences énoncées dans la présente section, en vue de
prévenir les risques plus efficacement tout en parvenant à un bon équilibre dans le cadre de la mise en œuvre des mesures
visant à répondre à ces exigences.
5.
Les mesures de gestion des risques visées au paragraphe 2, point d), sont telles que le risque résiduel pertinent associé
à chaque danger ainsi que le risque résiduel global lié aux systèmes d’IA à haut risque sont jugés acceptables.
Pour déterminer les mesures de gestion des risques les plus adaptées, il convient de veiller à:
a) éliminer ou réduire les risques identifiés et évalués conformément au paragraphe 2 autant que la technologie le permet
grâce à une conception et à un développement appropriés du système d’IA à haut risque;
b) mettre en œuvre, le cas échéant, des mesures adéquates d’atténuation et de contrôle répondant aux risques impossibles
à éliminer;
c) fournir aux déployeurs les informations requises conformément à l’article 13 et, éventuellement, une formation.
En vue de l’élimination ou de la réduction des risques liés à l’utilisation du système d’IA à haut risque, il est dûment tenu
compte des connaissances techniques, de l’expérience, de l’éducation et de la formation pouvant être attendues du
déployeur, ainsi que du contexte prévisible dans lequel le système est destiné à être utilisé.

**[Article 9]**
1.
Un système de gestion des risques est établi, mis en œuvre, documenté et tenu à jour en ce qui concerne les systèmes
d’IA à haut risque.
2.
Ce système de gestion des risques s’entend comme étant un processus itératif continu qui est planifié et se déroule sur
l’ensemble du cycle de vie d’un système d’IA à haut risque et qui doit périodiquement faire l’objet d’un examen et d’une mise
à jour méthodiques. Il comprend les étapes suivantes:
a) l’identification et l’analyse des risques connus et raisonnablement prévisibles que le système d’IA à haut risque peut poser
pour la santé, la sécurité ou les droits fondamentaux lorsque le système d’IA à haut risque est utilisé conformément à sa
destination;
b) l’estimation et l’évaluation des risques susceptibles d’apparaître lorsque le système d’IA à haut risque est utilisé
conformément à sa destination et dans des conditions de mauvaise utilisation raisonnablement prévisible;
c) l’évaluation d’autres risques susceptibles d’apparaître, sur la base de l’analyse des données recueillies au moyen du
système de surveillance après commercialisation visé à l’article 72;
d) l’adoption de mesures appropriées et ciblées de gestion des risques, conçues pour répondre aux risques identifiés en
vertu du point a).
3.
Les risques visés au présent article ne concernent que ceux qui peuvent être raisonnablement atténués ou éliminés
dans le cadre du développement ou de la conception du système d’IA à haut risque, ou par la fourniture d’informations
techniques appropriées.

**[Article 8]**
1.
Les systèmes d’IA à haut risque respectent les exigences énoncées dans la présente section, en tenant compte de leur
destination ainsi que de l’état de la technique généralement reconnu en matière d’IA et de technologies liées à l’IA. Pour
garantir le respect de ces exigences, il est tenu compte du système de gestion des risques prévu à l’article 9.
2.
Lorsqu’un produit contient un système d’IA auquel s’appliquent les exigences du présent règlement ainsi que les
exigences de la législation d’harmonisation de l’Union dont la liste figure à la section A de l’annexe I, les fournisseurs sont
chargés de veiller à ce que leur produit soit pleinement conforme à toutes les exigences en vertu de la législation
d’harmonisation de l’Union applicable. Pour garantir que les systèmes d’IA à haut risque visés au paragraphe 1 sont
conformes aux exigences énoncées dans la présente section, et afin d’assurer la cohérence, d’éviter les doubles emplois et de
réduire au minimum les charges supplémentaires, les fournisseurs ont le choix d’intégrer, le cas échéant, les processus d’essai
et de déclaration nécessaires, les informations et la documentation qu’ils fournissent concernant leur produit dans la
documentation et les procédures qui existent déjà et qui sont requises en vertu de la législation d’harmonisation de l’Union
dont la liste figure à la section A de l’annexe I.

**[Article 14]**
a) de comprendre correctement les capacités et les limites pertinentes du système d’IA à haut risque et d’être en mesure de
surveiller correctement son fonctionnement, y compris en vue de détecter et de traiter les anomalies, les
dysfonctionnements et les performances inattendues;
b) d’avoir conscience d’une éventuelle tendance à se fier automatiquement ou excessivement aux sorties produites par un
système d’IA à haut risque (biais d’automatisation), en particulier pour les systèmes d’IA à haut risque utilisés pour
fournir des informations ou des recommandations concernant les décisions à prendre par des personnes physiques;
c) d’interpréter correctement les sorties du système d’IA à haut risque, compte tenu par exemple des outils et méthodes
d’interprétation disponibles;
d) de décider, dans une situation particulière, de ne pas utiliser le système d’IA à haut risque ou d’ignorer, remplacer ou
inverser la sortie du système d’IA à haut risque;
e) d’intervenir dans le fonctionnement du système d’IA à haut risque ou d’interrompre le système au moyen d’un bouton
d’arrêt ou d’une procédure similaire permettant au système de s’arrêter de manière sécurisée.

</details>

- Juge 14B : NON — L'affirmation selon laquelle le système de gestion des risques doit inclure 'une prise en compte des effets combinés des exigences du règlement' (point 4) n'est pas directement appuyée par les extrait
- Avis proposé par Claude : OUI — Tous les éléments sont dans l'article 9 (§1, §2, §4, §5).

**Ton verdict :** OUI

---

## mistral/s08 — Quelles sont les obligations des fournisseurs de modèles d'IA à usage général ?

**Réponse du modèle :**

Voici les obligations des fournisseurs de modèles d’IA à usage général selon les extraits fournis :

1. **Documentation technique** :
   - Élaborer et tenir à jour une documentation technique du modèle, incluant son processus d’entraînement, d’essai et les résultats de son évaluation, conformément à l’**[Annexe XI]**.
   - La fournir sur demande au **Bureau de l’IA** et aux autorités nationales compétentes **[Article 53(1)(a)]**.

2. **Transparence envers les fournisseurs de systèmes d’IA** :
   - Mettre à disposition des informations et de la documentation pour les fournisseurs de systèmes d’IA intégrant leur modèle, incluant :
     - Une compréhension claire des **capacités et limites** du modèle **[Article 53(1)(b)(i)]**.
     - Les éléments minimaux énoncés à l’**[Annexe XII]**, tout en protégeant les droits de propriété intellectuelle et les secrets d’affaires **[Article 53(1)(b)]**.

3. **Respect du droit d’auteur et des droits voisins** :
   - Mettre en place une **politique de conformité** avec le droit de l’Union en matière de droit d’auteur, notamment pour identifier et respecter les **réservations de droits** (ex. : opt-out conformément à l’**article 4(3) de la directive (UE) 2019/790**) **[Article 53(1)(c) et Considérant 106]**.
   - Utiliser des **technologies de pointe** pour détecter ces réservations de droits.

4. **Transparence sur les données d’entraînement** :
   - Publier un **résumé détaillé** du contenu utilisé pour entraîner le modèle, selon un modèle fourni par le **Bureau de l’IA** **[Article 53(1)(d)]**.

---
**Pour les modèles présentant un risque systémique** (en plus des obligations ci-dessus) :
- Réaliser des **évaluations et essais contradictoires** pour identifier/atténuer les risques systémiques **[Article 55(1)(a)]**.
- **Surveiller, documenter et signaler** les incidents graves au **Bureau de l’IA** et aux autorités compétentes **[Article 55(1)(c)]**.
- Garantir un **niveau approprié de cybersécurité** pour le modèle et son infrastructure **[Article 55(1)(d)]**.
- Pouvoir s’appuyer sur des **codes de bonne pratique** ou des **normes harmonisées** pour démontrer la conformité **[Article 55(2)]**.

<details><summary>Extraits fournis au modèle</summary>

**[Considérant 106]**
Les fournisseurs qui mettent des modèles d’IA à usage général sur le marché de l’Union devraient veiller au respect
des obligations pertinentes prévues par le présent règlement. À cette fin, les fournisseurs de modèles d’IA à usage
général devraient mettre en place une politique visant à respecter la législation de l’Union sur le droit d’auteur et les
droits voisins, en particulier pour identifier et respecter la réservation de droits exprimées par les titulaires de droits
conformément à l’article 4, paragraphe 3, de la directive (UE) 2019/790. Tout fournisseur qui met un modèle d’IA
à usage général sur le marché de l’Union devrait se conformer à cette obligation, quelle que soit la juridiction dans
laquelle se déroulent les actes pertinents au titre du droit d’auteur qui sous-tendent l’entraînement de ces modèles
d’IA à usage général. Cela est nécessaire pour garantir des conditions de concurrence équitables entre les fournisseurs
de modèles d’IA à usage général, lorsqu’aucun fournisseur ne devrait pouvoir obtenir un avantage concurrentiel sur
le marché de l’Union en appliquant des normes en matière de droit d’auteur moins élevées que celles prévues dans
l’Union.

**[Article 53]**
6.
La Commission est habilitée à adopter des actes délégués conformément à l’article 97, paragraphe 2, pour modifier les
annexes XI et XII à la lumière des évolutions technologiques.
7.
Toute information ou documentation obtenue en vertu du présent article, y compris les secrets d’affaires, est traitée
conformément aux obligations de confidentialité énoncées à l’article 78.

**[Article 53]**
1.
Les fournisseurs de modèles d’IA à usage général:
a) élaborent et tiennent à jour la documentation technique du modèle, y compris son processus d’entraînement et d’essai et
les résultats de son évaluation, qui contient, au minimum, les informations énoncées à l’annexe XI aux fins de la fournir,
sur demande, au Bureau de l’IA et aux autorités nationales compétentes;
b) élaborent, tiennent à jour et mettent à disposition des informations et de la documentation à l’intention des fournisseurs
de systèmes d’IA qui envisagent d’intégrer le modèle d’IA à usage général dans leurs systèmes d’IA. Sans préjudice de la
nécessité d’observer et de protéger les droits de propriété intellectuelle et les informations confidentielles de nature
commerciale ou les secrets d’affaires conformément au droit de l’Union et au droit national, ces informations et cette
documentation:
i) permettent aux fournisseurs de systèmes d’IA d’avoir une bonne compréhension des capacités et des limites du
modèle d’IA à usage général et de se conformer aux obligations qui leur incombent en vertu du présent règlement; et
ii) contiennent, au minimum, les éléments énoncés à l’annexe XII;
c) mettent en place une politique visant à se conformer au droit de l’Union en matière de droit d’auteur et droits voisins, et
notamment à identifier et à respecter, y compris au moyen de technologies de pointe, une réservation de droits exprimée
conformément à l’article 4, paragraphe 3, de la directive (UE) 2019/790;
d) élaborent et mettent à la disposition du public un résumé suffisamment détaillé du contenu utilisé pour entraîner le
modèle d’IA à usage général, conformément à un modèle fourni par le Bureau de l’IA.

**[Article 55]**
2.
Les fournisseurs de modèles d’IA à usage général présentant un risque systémique peuvent s’appuyer sur des codes de
bonne pratique au sens de l’article 56 pour démontrer qu’ils respectent les obligations énoncées au paragraphe 1 du présent
article, jusqu’à la publication d’une norme harmonisée. Le respect des normes européennes harmonisées confère au
fournisseur une présomption de conformité dans la mesure où lesdites normes couvrent ces obligations. Les fournisseurs de
modèles d’IA à usage général présentant un risque systémique qui n’adhèrent pas à un code de bonnes pratiques approuvé
ou ne respectent pas une norme européenne harmonisée démontrent qu’ils disposent d’autres moyens appropriés de mise
en conformité et les soumettent à l’appréciation de la Commission.
3.
Toute information ou documentation obtenue en vertu du présent article, y compris les secrets d’affaires, est traitée
conformément aux obligations de confidentialité énoncées à l’article 78.

**[Article 55]**
1.
Outre les obligations énumérées aux articles 53 et 54, les fournisseurs de modèles d’IA à usage général présentant un
risque systémique:
a) effectuent une évaluation des modèles sur la base de protocoles et d’outils normalisés reflétant l’état de la technique, y
compris en réalisant et en documentant des essais contradictoires des modèles en vue d’identifier et d’atténuer les risques
systémiques;
b) évaluent et atténuent les risques systémiques éventuels au niveau de l’Union, y compris leurs origines, qui peuvent
découler du développement, de la mise sur le marché ou de l’utilisation de modèles d’IA à usage général présentant un
risque systémique;
c) suivent, documentent et communiquent sans retard injustifié au Bureau de l’IA et, le cas échéant, aux autorités nationales
compétentes les informations pertinentes concernant les incidents graves ainsi que les éventuelles mesures correctives
pour y remédier;
d) garantissent un niveau approprié de protection en matière de cybersécurité pour le modèle d’IA à usage général
présentant un risque systémique et l’infrastructure physique du modèle.

</details>

- Juge 14B : OUI — 
- Avis proposé par Claude : OUI — Articles 53 et 55 repris fidèlement, y compris les technologies de pointe (53 §1 c).

**Ton verdict :** OUI

---

## mistral/s09 — Quand un modèle d'IA à usage général est-il considéré comme présentant un risque systémique ?

**Réponse du modèle :**

Un modèle d’IA à usage général est considéré comme présentant un **risque systémique** dans les cas suivants :

1. **Capacités à fort impact** :
   - S’il dispose de capacités à fort impact évaluées sur la base de méthodologies et d’outils techniques appropriés (incluant indicateurs et critères de référence) **[Article 51, paragraphe 1, point a)]**.
   - **Présomption de risque systémique** si la quantité cumulée de calcul utilisée pour son entraînement dépasse **10²⁵ opérations en virgule flottante** **[Article 51, paragraphe 2]**.

2. **Décision de la Commission** :
   - Sur la base des critères de l’**Annexe XIII**, la Commission peut le désigner comme présentant un risque systémique, d’office ou après une alerte qualifiée du groupe scientifique **[Article 51, paragraphe 1, point b) et Article 52, paragraphe 4]**.

---
*Définition du risque systémique* :
Un risque lié aux capacités à fort impact du modèle, ayant une incidence significative sur le marché de l’UE, la santé publique, la sécurité, les droits fondamentaux ou la société **[Article 3, point 65]**.

<details><summary>Extraits fournis au modèle</summary>

**[Article 55]**
1.
Outre les obligations énumérées aux articles 53 et 54, les fournisseurs de modèles d’IA à usage général présentant un
risque systémique:
a) effectuent une évaluation des modèles sur la base de protocoles et d’outils normalisés reflétant l’état de la technique, y
compris en réalisant et en documentant des essais contradictoires des modèles en vue d’identifier et d’atténuer les risques
systémiques;
b) évaluent et atténuent les risques systémiques éventuels au niveau de l’Union, y compris leurs origines, qui peuvent
découler du développement, de la mise sur le marché ou de l’utilisation de modèles d’IA à usage général présentant un
risque systémique;
c) suivent, documentent et communiquent sans retard injustifié au Bureau de l’IA et, le cas échéant, aux autorités nationales
compétentes les informations pertinentes concernant les incidents graves ainsi que les éventuelles mesures correctives
pour y remédier;
d) garantissent un niveau approprié de protection en matière de cybersécurité pour le modèle d’IA à usage général
présentant un risque systémique et l’infrastructure physique du modèle.

**[Article 3]**
65) «risque systémique», un risque spécifique aux capacités à fort impact des modèles d’IA à usage général, ayant une
incidence significative sur le marché de l’Union en raison de leur portée ou d’effets négatifs réels ou raisonnablement
prévisibles sur la santé publique, la sûreté, la sécurité publique, les droits fondamentaux ou la société dans son
ensemble, pouvant être propagé à grande échelle tout au long de la chaîne de valeur;
66) «système d’IA à usage général», un système d’IA qui est fondé sur un modèle d’IA à usage général et qui a la capacité de
répondre à diverses finalités, tant pour une utilisation directe que pour une intégration dans d’autres systèmes d’IA;
67) «opération en virgule flottante», toute opération ou assignation mathématique impliquant des nombres en virgule
flottante, qui constituent un sous-ensemble des nombres réels généralement représentés sur un ordinateur par un
entier de précision fixe suivi d’un exposant entier d’une base fixe;
68) «fournisseur en aval», un fournisseur d’un système d’IA, y compris d’un système d’IA à usage général, qui intègre un
modèle d’IA, que le modèle d’IA soit fourni par lui-même ou non, et verticalement intégré ou fourni par une autre
entité sur la base de relations contractuelles.

**[Article 51]**
systémique
1.
Un modèle d’IA à usage général est classé comme modèle d’IA à usage général présentant un risque systémique s’il
remplit l’une des conditions suivantes:
a) il dispose de capacités à fort impact évaluées sur la base de méthodologies et d’outils techniques appropriés, y compris
des indicateurs et des critères de référence;
b) sur la base d’une décision de la Commission, d’office ou à la suite d’une alerte qualifiée du groupe scientifique, il possède
des capacités ou un impact équivalents à ceux énoncés au point a), compte tenu des critères définis à l’annexe XIII.
2.
Un modèle d’IA à usage général est présumé avoir des capacités à fort impact conformément au paragraphe 1,
point a), lorsque la quantité cumulée de calcul utilisée pour son entraînement mesurée en opérations en virgule flottante est
supérieure à 1025.
3.
La Commission adopte des actes délégués conformément à l’article 97 pour modifier les seuils énumérés aux
paragraphes 1 et 2 du présent article, ainsi que pour compléter les critères de référence et les indicateurs à la lumière des
évolutions technologiques, telles que les améliorations algorithmiques ou l’efficacité accrue du matériel informatique, si
nécessaire, afin que ces seuils reflètent l’état de la technique.

**[Article 52]**
4.
La Commission peut désigner un modèle d’IA à usage général comme présentant un risque systémique, d’office ou à la
suite d’une alerte qualifiée du groupe scientifique conformément à l’article 90, paragraphe 1, point a), sur la base des critères
énoncés à l’annexe XIII.
La Commission est habilitée à adopter des actes délégués conformément à l’article 97 pour modifier l’annexe XIII en
précisant et mettant à jour les critères énoncés à ladite annexe.
5.
Sur demande motivée d’un fournisseur dont le modèle a été désigné comme modèle d’IA à usage général présentant
un risque systémique en vertu du paragraphe 4, la Commission tient compte de la demande et peut décider de réévaluer si le
modèle d’IA à usage général peut encore être considéré comme présentant un risque systémique sur la base des critères
énoncés à l’annexe XIII. Une telle demande contient les éléments objectifs, détaillés et nouveaux qui sont apparus depuis la
décision de désignation. Les fournisseurs peuvent demander une réévaluation au plus tôt six mois après la décision de
désignation. Lorsque la Commission, à la suite de sa réévaluation, décide de maintenir la désignation en tant que modèle
d’IA à usage général présentant un risque systémique, les fournisseurs peuvent demander une réévaluation au plus tôt six
mois après cette décision.
6.
La Commission veille à ce qu’une liste des modèles d’IA à usage général présentant un risque systémique soit publiée
et tient cette liste à jour, sans préjudice de la nécessité de respecter et de protéger les droits de propriété intellectuelle et les
informations confidentielles de nature commerciale ou les secrets d’affaires conformément au droit de l’Union et au droit
national.

**[Article 52]**
1.
Lorsqu’un modèle d’IA à usage général remplit la condition visée à l’article 51, paragraphe 1, point a), le fournisseur
concerné en informe la Commission sans tarder et, en tout état de cause, dans un délai de deux semaines après la date
à laquelle ce critère est rempli ou après qu’il a été établi qu’il le sera. Cette notification comprend les informations
nécessaires pour démontrer que le critère pertinent a été rempli. Si la Commission apprend l’existence d’un modèle d’IA
à usage général présentant un risque systémique dont elle n’a pas été informée, elle peut décider de le désigner comme
modèle présentant un risque systémique.
2.
Le fournisseur d’un modèle d’IA à usage général qui remplit la condition visée à l’article 51, paragraphe 1, point a),
peut présenter, avec sa notification, des arguments suffisamment étayés pour démontrer que, exceptionnellement, bien qu’il
remplisse ce critère, le modèle d’IA à usage général ne présente pas, en raison de ses caractéristiques spécifiques, de risque
systémique et ne devrait donc pas être classé comme modèle d’IA à usage général présentant un risque systémique.
3.
Lorsque la Commission conclut que les arguments présentés conformément au paragraphe 2 ne sont pas
suffisamment étayés et que le fournisseur concerné n’a pas été en mesure de démontrer que le modèle d’IA à usage général
ne présente pas, en raison de ses caractéristiques spécifiques, de risque systémique, elle rejette ces arguments, et le modèle
d’IA à usage général est considéré comme un modèle d’IA à usage général présentant un risque systémique.

</details>

- Juge 14B : OUI — 
- Avis proposé par Claude : OUI — Conforme aux articles 51, 52 et 3 point 65.

**Ton verdict :** OUI

---

## mistral/s10 — Qu'est-ce qu'un bac à sable réglementaire de l'IA ?

**Réponse du modèle :**

Un **bac à sable réglementaire de l’IA** est défini comme :

*« un cadre contrôlé mis en place par une autorité compétente qui offre aux fournisseurs ou fournisseurs potentiels de systèmes d’IA la possibilité de développer, d’entraîner, de valider et de tester, lorsqu’il y a lieu en conditions réelles, un système d’IA innovant, selon un **plan du bac à sable** pour une durée limitée sous surveillance réglementaire »* **[Définition 55, Article 3]**.

<details><summary>Extraits fournis au modèle</summary>

**[Article 57]**
1.
Les États membres veillent à ce que leurs autorités compétentes mettent en place au moins un bac à sable
réglementaire de l’IA au niveau national, qui est opérationnel au plus tard le 2 août 2026. Ce bac à sable peut également être
établi conjointement avec les autorités compétentes d’autres États membres. La Commission peut fournir un soutien
technique, des conseils et des outils pour la mise en place et l’exploitation de bacs à sable réglementaires de l’IA.
L’obligation visée au premier alinéa peut également être remplie en participant à un bac à sable existant, pour autant que
cette participation offre un niveau de couverture nationale équivalent pour les États membres participants.
2.
Des bacs à sable réglementaires de l’IA supplémentaires au niveau régional ou au niveau local, ou établis
conjointement avec les autorités compétentes d’autres États membres peuvent également être mis en place.
3.
Le Contrôleur européen de la protection des données peut également créer un bac à sable réglementaire de l’IA pour
les institutions, organes et organismes de l’Union, et peut exercer les rôles et les tâches des autorités nationales compétentes
conformément au présent chapitre.

**[Article 57]**
9.
La mise en place de bacs à sable réglementaires de l’IA vise à contribuer aux objectifs suivants:
a) améliorer la sécurité juridique afin d’assurer le respect réglementaire du présent règlement ou, le cas échéant, d’autres
dispositions applicables du droit de l’Union et du droit national;
b) soutenir le partage des bonnes pratiques par la coopération avec les autorités participant au bac à sable réglementaire de
l’IA;
c) favoriser l’innovation et la compétitivité et faciliter la mise en place d’un écosystème d’IA;
d) contribuer à l’apprentissage réglementaire fondé sur des données probantes;
e) faciliter et accélérer l’accès au marché de l’Union pour les systèmes d’IA, en particulier lorsqu’ils sont fournis par des
PME, y compris des jeunes pousses.
10.
Les autorités nationales compétentes veillent à ce que, dans la mesure où les systèmes d’IA innovants impliquent le
traitement de données à caractère personnel ou relèvent à d’autres titres de la surveillance d’autres autorités nationales ou
autorités compétentes assurant ou encadrant l’accès aux données, les autorités nationales chargées de la protection des
données et ces autres autorités nationales ou autorités compétentes soient associées à l’exploitation du bac à sable
réglementaire de l’IA et participent au contrôle des aspects qui relèvent de leurs tâches et pouvoirs respectifs.

**[Article 3]**
53) «plan d’essais en conditions réelles», un document décrivant les objectifs, la méthode, la population et le champ
d’application géographique et la portée dans le temps, le suivi, l’organisation et la conduite des essais en conditions
réelles;
54) «plan du bac à sable», un document adopté conjointement entre le fournisseur participant et l’autorité compétente, qui
décrit les objectifs, les conditions, les délais, la méthodologie et les exigences applicables aux activités réalisées au sein
du bac à sable;
55) «bac à sable réglementaire de l’IA», un cadre contrôlé mis en place par une autorité compétente qui offre aux
fournisseurs ou fournisseurs potentiels de systèmes d’IA la possibilité de développer, d’entraîner, de valider et de tester,
lorsqu’il y a lieu en conditions réelles, un système d’IA innovant, selon un plan du bac à sable pour une durée limitée
sous surveillance réglementaire;
56) «maîtrise de l’IA», les compétences, les connaissances et la compréhension qui permettent aux fournisseurs, aux
déployeurs et aux personnes concernées, compte tenu de leurs droits et obligations respectifs dans le contexte du
présent règlement, de procéder à un déploiement des systèmes d’IA en toute connaissance de cause, ainsi que de
prendre conscience des possibilités et des risques que comporte l’IA, ainsi que des préjudices potentiels qu’elle peut
causer;

**[Article 57]**
16.
Les autorités nationales compétentes présentent des rapports annuels au Bureau de l’IA et au Comité IA, dont le
premier est élaboré dans un délai d’un an à compter de la mise en place du bac à sable réglementaire de l’IA, puis tous les
ans jusqu’à son terme, et un rapport final. Ces rapports fournissent des informations sur les progrès et les résultats de la
mise en œuvre de ces bacs à sable, y compris les bonnes pratiques, les incidents, les enseignements et les recommandations
concernant leur mise en place et, le cas échéant, sur l’application et la révision éventuelle du présent règlement, y compris
ses actes délégués et actes d’exécution, et sur l’application d’autres dispositions législatives de l’Union contrôlés par les
autorités compétentes dans le cadre du bac à sable. Les autorités nationales compétentes publient ces rapports annuels ou
des résumés de ceux-ci en ligne. La Commission tient compte, s’il y a lieu, des rapports annuels dans l’exercice de ses tâches
au titre du présent règlement.
17.
La Commission développe une interface unique et spécifique contenant toutes les informations pertinentes relatives
aux bacs à sable réglementaires de l’IA pour permettre aux parties prenantes d’interagir avec les bacs à sable réglementaires
de l’IA et de s’informer auprès des autorités compétentes, ainsi que de demander des orientations non contraignantes sur la
conformité de produits, services et modèles commerciaux innovants intégrant les technologies de l’IA, conformément
à l’article 62, paragraphe 1, point c). La Commission assure une coordination proactive avec les autorités nationales
compétentes, le cas échéant.

**[Article 58]**
g) que les procédures, processus et exigences administratives applicables en matière de demande, de sélection, de
participation et de sortie dans le cadre du bac à sable réglementaires de l’IA sont simples, facilement compréhensibles et
clairement communiqués afin de faciliter la participation des PME, y compris des jeunes pousses, disposant de capacités
juridiques et administratives limitées, et sont rationalisés dans toute l’Union, afin d’éviter la fragmentation et de
permettre que la participation à un bac à sable réglementaire de l’IA mis en place par un État membre ou par le
Contrôleur européen de la protection des données soit mutuellement et uniformément reconnue et produise les mêmes
effets juridiques dans l’ensemble de l’Union;
h) que la participation au bac à sable réglementaire de l’IA est limitée à une période adaptée à la complexité et à l’envergure
du projet, qui peut être prolongée par l’autorité nationale compétente;
i) que les bacs à sable réglementaire de l’IA facilitent le développement d’outils et d’infrastructures pour la mise à l’essai,
l’étalonnage des performances, l’évaluation et l’explication des aspects des systèmes d’IA pertinents pour l’apprentissage
réglementaire, tels que la précision, la solidité et la cybersécurité, ainsi que les mesures d’atténuation des risques d’atteinte
aux droits fondamentaux et à la société au sens large.

</details>

- Juge 14B : OUI — 
- Avis proposé par Claude : OUI — Citation exacte de la définition (article 3, point 55).

**Ton verdict :** OUI

---

## mistral/s12 — Quelle obligation de maîtrise de l'IA s'impose aux fournisseurs et aux déployeurs ?

**Réponse du modèle :**

Les fournisseurs et les déployeurs de systèmes d’IA doivent prendre des **mesures pour garantir, dans toute la mesure du possible, un niveau suffisant de maîtrise de l’IA** pour leur personnel et les autres personnes s’occupant du fonctionnement et de l’utilisation des systèmes d’IA pour leur compte.

Ces mesures doivent tenir compte :
- des **connaissances techniques, expérience, éducation et formation** des personnes concernées,
- du **contexte d’utilisation** des systèmes d’IA,
- des **personnes ou groupes de personnes** à l’égard desquels les systèmes sont destinés à être utilisés.

[Article 4]

<details><summary>Extraits fournis au modèle</summary>

**[Article 4]**
Les fournisseurs et les déployeurs de systèmes d’IA prennent des mesures pour garantir, dans toute la mesure du possible, un
niveau suffisant de maîtrise de l’IA pour leur personnel et les autres personnes s’occupant du fonctionnement et de
l’utilisation des systèmes d’IA pour leur compte, en prenant en considération leurs connaissances techniques, leur
expérience, leur éducation et leur formation, ainsi que le contexte dans lequel les systèmes d’IA sont destinés à être utilisés,
et en tenant compte des personnes ou des groupes de personnes à l’égard desquels les systèmes d’IA sont destinés à être
utilisés.

**[Article 74]**
b) les procédures d’essai ou d’audit et les vérifications fondées sur les données et la documentation communiquées par le
fournisseur ont été entièrement accomplies ou se sont révélées insuffisantes.
14.
Toute information ou documentation obtenue par les autorités de surveillance du marché est traitée conformément
aux obligations de confidentialité énoncées à l’article 78.

**[Article 50]**
2.
Les fournisseurs de systèmes d’IA, y compris de systèmes d’IA à usage général, qui génèrent des contenus de synthèse
de type audio, image, vidéo ou texte, veillent à ce que les sorties des systèmes d’IA soient marquées dans un format lisible
par machine et identifiables comme ayant été générées ou manipulées par une IA. Les fournisseurs veillent à ce que leurs
solutions techniques soient aussi efficaces, interopérables, solides et fiables que la technologie le permet, compte tenu des
spécificités et des limites des différents types de contenus, des coûts de mise en œuvre et de l’état de la technique
généralement reconnu, comme cela peut ressortir des normes techniques pertinentes. Cette obligation ne s’applique pas
dans la mesure où les systèmes d’IA remplissent une fonction d’assistance pour la mise en forme standard ou ne modifient
pas de manière substantielle les données d’entrée fournies par le déployeur ou leur sémantique, ou lorsque leur utilisation
est autorisée par la loi à des fins de prévention ou de détection des infractions pénales, d’enquêtes ou de poursuites en la
matière.

**[Article 62]**
a) fournit des modèles normalisés pour les domaines qui relèvent du présent règlement, comme précisé par le Comité IA
dans sa demande;
b) met au point et tient à jour une plateforme d’information unique fournissant des informations faciles à utiliser en
rapport avec le présent règlement pour tous les opérateurs dans l’ensemble de l’Union;
c) organise des campagnes de communication appropriées pour sensibiliser aux obligations découlant du présent
règlement;
d) évalue et promeut la convergence des bonnes pratiques en matière de procédures de passation de marchés publics en ce
qui concerne les systèmes d’IA.

**[Article 91]**
1.
La Commission peut demander au fournisseur du modèle d’IA à usage général concerné de fournir la documentation
établie par le fournisseur conformément aux articles 53 et 55, ou toute information supplémentaire nécessaire pour évaluer
la conformité du fournisseur avec le présent règlement.
2.
Avant d’envoyer la demande d’informations, le Bureau de l’IA peut entamer un dialogue structuré avec le fournisseur
du modèle d’IA à usage général.
3.
Sur demande dûment motivée du groupe scientifique, la Commission peut adresser une demande d’informations au
fournisseur d’un modèle d’IA à usage général, lorsque l’accès à ces informations est nécessaire et proportionné pour
l’accomplissement des tâches du groupe scientifique au titre de l’article 68, paragraphe 2.
4.
La demande d’informations mentionne la base juridique et l’objet de la demande, précise quelles informations sont
requises, fixe un délai dans lequel les informations doivent être fournies, et indique les amendes prévues à l’article 101 en
cas de fourniture d’informations inexactes, incomplètes ou trompeuses.
5.
Le fournisseur du modèle d’IA à usage général concerné, ou son représentant, fournit les informations demandées.
Dans le cas de personnes morales, d’entreprises ou de sociétés, ou lorsque le fournisseur n’a pas de personnalité juridique,
les personnes autorisées à les représenter en vertu de la loi ou de leurs statuts fournissent les informations demandées pour
le compte du fournisseur du modèle d’IA à usage général concerné. Les avocats dûment habilités à agir peuvent fournir des
informations pour le compte de leurs clients. Les clients demeurent néanmoins pleinement responsables si les informations
fournies sont incomplètes, inexactes ou trompeuses.

</details>

- Juge 14B : OUI — 
- Avis proposé par Claude : OUI — Reprise fidèle de l'article 4.

**Ton verdict :** OUI

---

## mistral/s13 — Qui doit réaliser une analyse d'impact sur les droits fondamentaux ?

**Réponse du modèle :**

D'après les extraits fournis, les **déployeurs** doivent réaliser une analyse d'impact sur les droits fondamentaux dans les cas suivants :

1. **Avant le déploiement d’un système d’IA à haut risque** (sauf pour les systèmes visés à l’[Annexe III, point 2]), lorsque :
   - Ils sont des **organismes de droit public** ou des **entités privées fournissant des services publics** ;
   - Ou lorsqu’ils déploient des systèmes d’IA à haut risque visés à l’[Annexe III, points 5b) et 5c)].

   [Article 27, paragraphe 1]

2. **Les autorités répressives** doivent également réaliser une analyse d’impact sur les droits fondamentaux avant l’utilisation de **systèmes d’identification biométrique à distance en temps réel** dans des espaces accessibles au public à des fins répressives.
   [Article 5, paragraphe 2]

<details><summary>Extraits fournis au modèle</summary>

**[Article 27]**
2.
L’obligation établie au paragraphe 1 s’applique à la première utilisation du système d’IA à haut risque. Le déployeur
peut, dans des cas similaires, s’appuyer sur des analyses d’impact sur les droits fondamentaux effectuées précédemment ou
sur des analyses d’impact existantes réalisées par le fournisseur. Si, au cours de l’utilisation du système d’IA à haut risque, le
déployeur estime qu’un des éléments énumérés au paragraphe 1 a changé ou n’est plus à jour, il prend les mesures
nécessaires pour mettre à jour les informations.
3.
Une fois l’analyse visée au paragraphe 1 du présent article effectuée, le déployeur en notifie les résultats à l’autorité de
surveillance du marché, et soumet le modèle visé au paragraphe 5 du présent article, rempli, dans le cadre de la notification.
Dans le cas visé à l’article 46, paragraphe 1, les déployeurs peuvent être exemptés de cette obligation de notification.
4.
Si l’une des obligations prévues au présent article est déjà remplie au moyen de l’analyse d’impact relative à la
protection des données réalisée en application de l’article 35 du règlement (UE) 2016/679 ou de l’article 27 de la directive
(UE) 2016/680, l’analyse d’impact sur les droits fondamentaux visée au paragraphe 1 du présent article complète ladite
analyse d’impact relative à la protection des données.
5.
Le Bureau de l’IA élabore un modèle de questionnaire, y compris au moyen d’un outil automatisé, afin d’aider les
déployeurs à se conformer de manière simplifiée aux obligations qui leur incombent en vertu du présent article.

**[Article 5]**
b) les conséquences de l’utilisation du système sur les droits et libertés de toutes les personnes concernées, notamment la
gravité, la probabilité et l’ampleur de ces conséquences.
En outre, l’utilisation de systèmes d’identification biométriques à distance en temps réel dans des espaces accessibles au
public à des fins répressives en vue de la réalisation de l’un des objectifs énumérés au paragraphe 1, premier alinéa, point h),
du présent article respecte les garanties et conditions nécessaires et proportionnées en ce qui concerne cette utilisation,
conformément au droit national qui l’autorise, notamment eu égard aux limitations temporelles, géographiques et relatives
aux personnes. L’utilisation du système d’identification biométrique à distance en temps réel dans des espaces accessibles au
public n’est autorisée que si l’autorité répressive a réalisé une analyse d’impact sur les droits fondamentaux conformément
à l’article 27 et a enregistré le système dans la base de données de l’UE prévue par l’article 49. Toutefois, dans des cas
d’urgence dûment justifiés, il est possible de commencer à utiliser ces systèmes sans enregistrement dans la base de données
de l’UE, à condition que cet enregistrement soit effectué sans retard injustifié.
3.
Aux fins du paragraphe 1, premier alinéa, point h), et du paragraphe 2, chaque utilisation à des fins répressives d’un
système d’identification biométrique à distance en temps réel dans des espaces accessibles au public est subordonnée à une
autorisation préalable octroyée par une autorité judiciaire ou une autorité administrative indépendante dont la décision est
contraignante de l’État membre dans lequel cette utilisation doit avoir lieu, délivrée sur demande motivée et conformément

**[Article 27]**
1.
Avant le déploiement d’un système d’IA à haut risque visé à l’article 6, paragraphe 2, à l’exception des systèmes d’IA
à haut risque destinés à être utilisés dans le domaine visé à l’annexe III, point 2, les déployeurs qui sont des organismes de
droit public ou des entités privées fournissant des services publics et les déployeurs de systèmes d’IA à haut risque visés
à l’annexe III, points 5), b) et c), effectuent une analyse de l’impact sur les droits fondamentaux que l’utilisation de ce système
peut produire. À cette fin, les déployeurs effectuent une analyse comprenant:
a) une description des processus du déployeur dans lesquels le système d’IA à haut risque sera utilisé conformément à sa
destination;
b) une description de la période pendant laquelle et de la fréquence à laquelle chaque système d’IA à haut risque est destiné
à être utilisé;
c) les catégories de personnes physiques et les groupes susceptibles d’être concernés par son utilisation dans le contexte
spécifique;
d) les risques spécifiques de préjudice susceptibles d’avoir une incidence sur les catégories de personnes physiques ou
groupes de personnes identifiés en vertu du point c) du présent paragraphe, compte tenu des informations fournies par
le fournisseur conformément à l’article 13;
e) une description de la mise en œuvre des mesures de contrôle humain, conformément à la notice d’utilisation;
f) les mesures à prendre en cas de matérialisation de ces risques, y compris les dispositifs relatifs à la gouvernance interne et
aux mécanismes de plainte internes.

**[Article 77]**
1.
Les autorités ou organismes publics nationaux qui supervisent ou font respecter les obligations au titre du droit de
l’Union visant à protéger les droits fondamentaux, y compris le droit à la non-discrimination, en ce qui concerne l’utilisation
des systèmes d’IA à haut risque visés à l’annexe III sont habilités à demander toute documentation créée ou conservée en
vertu du présent règlement et à y avoir accès dans une langue et un format accessibles lorsque l’accès à cette documentation
est nécessaire à l’accomplissement effectif de leur mandat dans les limites de leurs compétences. L’autorité ou l’organisme
public concerné informe l’autorité de surveillance du marché de l’État membre concerné de toute demande de ce type.
2.
Au plus tard le 2 novembre 2024, chaque État membre identifie les autorités ou organismes publics visés au
paragraphe 1 et met la liste de ces autorités ou organismes à la disposition du public. Les États membres notifient la liste à la
Commission et aux autres États membres, et tiennent cette liste à jour.
3.
Lorsque la documentation visée au paragraphe 1 ne suffit pas pour déterminer s’il y a eu violation des obligations au
titre du droit de l’Union protégeant les droits fondamentaux, l’autorité ou l’organisme public visé au paragraphe 1 peut
présenter à l’autorité de surveillance du marché une demande motivée visant à organiser des tests du système d’IA à haut
risque par des moyens techniques. L’autorité de surveillance du marché organise les tests avec la participation étroite de
l’autorité ou organisme public ayant présenté la demande dans un délai raisonnable après celle-ci.

**[Article 86]**
1.
Toute personne concernée faisant l’objet d’une décision prise par un déployeur sur la base des sorties d’un système
d’IA à haut risque mentionné à l’annexe III, à l’exception des systèmes énumérés au point 2 de ladite annexe, et qui produit
des effets juridiques ou affecte significativement cette personne de façon similaire d’une manière qu’elle considère comme
ayant des conséquences négatives sur sa santé, sa sécurité ou ses droits fondamentaux a le droit d’obtenir du déployeur des
explications claires et pertinentes sur le rôle du système d’IA dans la procédure décisionnelle et sur les principaux éléments
de la décision prise.
2.
Le paragraphe 1 ne s’applique pas à l’utilisation de systèmes d’IA pour lesquels des exceptions ou des restrictions
à l’obligation prévue audit paragraphe découlent du droit de l’Union ou du droit national dans le respect du droit de l’Union.
3.
Le présent article ne s’applique que dans la mesure où le droit visé au paragraphe 1 n’est pas prévu par ailleurs dans le
droit de l’Union.

</details>

- Juge 14B : NON — L'affirmation selon laquelle 'les autorités répressives doivent également réaliser une analyse d’impact sur les droits fondamentaux avant l’utilisation de systèmes d’identification biométrique à dista
- Avis proposé par Claude : OUI — Article 27 §1 précis (points 5 b/c, exception point 2) et article 5 §2 exact.

**Ton verdict :** OUI

---

## mistral/c01 — Un système d'IA qui trie automatiquement des CV pour un recrutement est-il à haut risque ?

**Réponse du modèle :**

Oui, un système d'IA qui trie automatiquement des CV pour un recrutement est considéré comme un **système d'IA à haut risque** selon l'**Annexe III, point 4a** :
*"systèmes d'IA destinés à être utilisés pour le recrutement ou la sélection de personnes physiques, en particulier pour publier des offres d'emploi ciblées, analyser et filtrer les candidatures et évaluer les candidats."*

<details><summary>Extraits fournis au modèle</summary>

**[Annexe III]**
c) systèmes d'IA destinés à être utilisés pour évaluer le niveau d'enseignement approprié qu'une personne recevra ou
sera en mesure d'atteindre, dans le contexte ou au sein d'établissements d'enseignement et de formation
professionnelle à tous les niveaux;
d) systèmes d'IA destinés à être utilisés pour surveiller et détecter des comportements interdits chez les étudiants lors
d'examens dans le contexte d'établissements d'enseignement et de formation ou en leur sein à tous les niveaux;
4.
Emploi, gestion de la main-d'œuvre et accès à l'emploi indépendant:
a) systèmes d'IA destinés à être utilisés pour le recrutement ou la sélection de personnes physiques, en particulier
pour publier des offres d'emploi ciblées, analyser et filtrer les candidatures et évaluer les candidats;
b) systèmes d'IA destinés à être utilisés pour prendre des décisions influant sur les conditions des relations
professionnelles, la promotion ou le licenciement dans le cadre de relations professionnelles contractuelles, pour
attribuer des tâches sur la base du comportement individuel, de traits de personnalité ou de caractéristiques
personnelles ou pour suivre et évaluer les performances et le comportement de personnes dans le cadre de telles
relations.
5.
Accès et droit aux services privés essentiels et aux services publics et prestations sociales essentiels:
a) systèmes d'IA destinés à être utilisés par les autorités publiques ou en leur nom pour évaluer l'éligibilité des
personnes physiques aux prestations et services d'aide sociale essentiels, y compris les services de soins de santé,
ainsi que pour octroyer, réduire, révoquer ou récupérer ces prestations et services;

**[Annexe III]**
Les systèmes d'IA à haut risque au sens de l'article 6, paragraphe 2, sont les systèmes d'IA répertoriés dans l'un des
domaines suivants:
1.
Biométrie, dans la mesure où leur utilisation est autorisée par le droit de l'Union ou le droit national applicable:
a) systèmes d'identification biométrique à distance.
Cela n'inclut pas les systèmes d'IA destinés à être utilisés à des fins de vérification biométrique dont la seule
finalité est de confirmer qu'une personne physique spécifique est la personne qu'elle prétend être;
b) systèmes d'IA destinés à être utilisés à des fins de catégorisation biométrique, en fonction d'attributs ou de
caractéristiques sensibles ou protégés, sur la base de la déduction de ces attributs ou de ces caractéristiques;
c) systèmes d'IA destinés à être utilisés pour la reconnaissance des émotions.
2.
Infrastructures critiques: systèmes d'IA destinés à être utilisés en tant que composants de sécurité dans la gestion et
l'exploitation d'infrastructures numériques critiques, du trafic routier ou de la fourniture d'eau, de gaz, de chauffage
ou d'électricité.
3.
Éducation et formation professionnelle:
a) systèmes d'IA destinés à être utilisés pour déterminer l'accès, l'admission ou l'affectation de personnes physiques
à des établissements d'enseignement et de formation professionnelle, à tous les niveaux;
b) systèmes d'IA destinés à être utilisés pour évaluer les acquis d'apprentissage, y compris lorsque ceux-ci sont
utilisés pour orienter le processus d'apprentissage de personnes physiques dans les établissements d'enseignement
et de formation professionnelle, à tous les niveaux;

**[Annexe VIII]**
12.
une notice d'utilisation en format électronique; ces informations ne sont pas à fournir pour les systèmes d'IA à haut
risque dans les domaines des activités répressives ou de la migration, de l'asile et de la gestion des contrôles aux
frontières visés à l'annexe III, points 1, 6 et 7;
13.
une adresse URL vers des informations supplémentaires (facultatif).
Section B - Informations à fournir par les fournisseurs de systèmes d'IA à haut risque conformément à l'article 49,
paragraphe 2
Les informations ci-après sont fournies et mises à jour par la suite en ce qui concerne les systèmes d'IA à enregistrer
conformément à l'article 49, paragraphe 2:
1.
le nom, l'adresse et les coordonnées du fournisseur;
2.
lorsque la soumission d'informations est effectuée par une autre personne pour le compte du fournisseur, le nom,
l'adresse et les coordonnées de cette personne;
3.
le nom, l'adresse et les coordonnées du mandataire, le cas échéant;
4.
la dénomination commerciale du système d'IA et toute référence supplémentaire non équivoque permettant
l'identification et la traçabilité du système d'IA;
5.
une description de la destination du système d'IA;
6.
la ou les conditions visées à l'article 6, paragraphe 3, sur la base desquelles le système d'IA est considéré comme
n'étant pas à haut risque;
7.
un résumé succinct des motifs pour lesquels le système d'IA est considéré comme n'étant pas à haut risque en
application de la procédure prévue à l'article 6, paragraphe 3;
8.
le statut du système d'IA (sur le marché ou en service; plus sur le marché/en service, rappelé);

**[Annexe VIII]**
à l'article 49
Section A - Informations à fournir par les fournisseurs de systèmes d'IA à haut risque conformément à l'article 49,
paragraphe 1
Les informations ci-après sont fournies et mises à jour par la suite en ce qui concerne les systèmes d'IA à haut risque
à enregistrer conformément à l'article 49, paragraphe 1:
1.
le nom, l'adresse et les coordonnées du fournisseur;
2.
lorsque la soumission d'informations est effectuée par une autre personne pour le compte du fournisseur, le nom,
l'adresse et les coordonnées de cette personne;
3.
le nom, l'adresse et les coordonnées du mandataire, le cas échéant;
4.
la dénomination commerciale du système d'IA et toute référence supplémentaire non équivoque permettant
l'identification et la traçabilité du système d'IA;
5.
une description de la destination du système d'IA ainsi que des composants et fonctions gérées au moyen de ce
système d'IA;
6.
une description de base et concise des informations utilisées par le système (données, entrées) et de sa logique de
fonctionnement;
7.
le statut du système d'IA (sur le marché ou en service; plus mis sur le marché/en service, rappelé);
8.
le type, le numéro et la date d'expiration du certificat délivré par l'organisme notifié et le nom ou le numéro
d'identification de cet organisme notifié, le cas échéant;
9.
une copie numérisée du certificat visé au point 8, le cas échéant;
10.
tout État membre dans lequel le système d'IA a été mis sur le marché, mis en service ou mis à disposition dans
l'Union;
11.
une copie de la déclaration UE de conformité visée à l'article 47;

**[Annexe III]**
c) systèmes d'IA destinés à être utilisés par les autorités publiques compétentes ou par les institutions, organes ou
organismes de l'Union, ou en leur nom, pour aider les autorités publiques compétentes à procéder à l'examen des
demandes d'asile, de visas et de titres de séjour et des plaintes connexes au regard de l'objectif visant à établir
l'éligibilité des personnes physiques demandant un statut, y compris les évaluations connexes de la fiabilité des
éléments de preuve;
d) systèmes d'IA destinés à être utilisés par les autorités publiques compétentes ou par les institutions, organes ou
organismes de l'Union, ou en leur nom, dans le cadre de la migration, de l'asile et de la gestion des contrôles aux
frontières, aux fins de la détection, de la reconnaissance ou de l'identification des personnes physiques,
à l'exception de la vérification des documents de voyage.
8.
Administration de la justice et processus démocratiques:
a) systèmes d'IA destinés à être utilisés par les autorités judiciaires ou en leur nom, pour les aider à rechercher et
à interpréter les faits ou la loi, et à appliquer la loi à un ensemble concret de faits, ou à être utilisés de manière
similaire lors du règlement extrajudiciaire d'un litige;
b) systèmes d'IA destinés à être utilisés pour influencer le résultat d'une élection ou d'un référendum ou le
comportement électoral de personnes physiques dans l'exercice de leur vote lors d'élections ou de référendums.
Sont exclus les systèmes d'IA aux sorties desquels les personnes physiques ne sont pas directement exposées, tels
que les outils utilisés pour organiser, optimiser ou structurer les campagnes politiques sous l'angle administratif
ou logistique.

</details>

- Juge 14B : OUI — 
- Avis proposé par Claude : OUI — Citation exacte de l'annexe III, point 4 a).

**Ton verdict :** OUI

---

## mistral/c02 — Une banque peut-elle utiliser une IA pour évaluer la solvabilité de ses clients ? Quel niveau de risque ?

**Réponse du modèle :**

Oui, une banque peut utiliser un système d’IA pour évaluer la solvabilité de ses clients, mais cela relève d’un **système d’IA à haut risque** selon le règlement.

**Source** : [Annexe III, point b] :
*"systèmes d'IA destinés à être utilisés pour évaluer la solvabilité des personnes physiques ou pour établir leur note de crédit"* (sauf pour la détection de fraudes financières).

<details><summary>Extraits fournis au modèle</summary>

**[Article 57]**
7.
Les autorités compétentes donnent aux fournisseurs et aux fournisseurs potentiels participant au bac à sable
réglementaire de l’IA des orientations sur les attentes réglementaires et la manière de satisfaire aux exigences et obligations
énoncées dans le présent règlement.
À la demande du fournisseur ou du fournisseur potentiel du système d’IA, l’autorité compétente fournit une preuve écrite
des activités menées avec succès dans le bac à sable. L’autorité compétente fournit également un rapport de sortie détaillant
les activités menées dans le bac à sable ainsi que les résultats et acquis d’apprentissage correspondants. Les fournisseurs
peuvent utiliser ces documents pour démontrer leur conformité avec le présent règlement au moyen de la procédure
d’évaluation de la conformité ou d’activités pertinentes de surveillance du marché. À cet égard, les rapports de sortie et la
preuve écrite fournie par l’autorité nationale compétente sont évalués de manière positive par les autorités de surveillance
du marché et les organismes notifiés, en vue d’accélérer les procédures d’évaluation de la conformité dans une mesure
raisonnable.
8.
Sous réserve des dispositions relatives à la confidentialité énoncées à l’article 78 et avec l’accord du fournisseur ou du
fournisseur potentiel, la Commission et le Comité IA sont autorisés à accéder aux rapports de sortie et en tiennent compte,
le cas échéant, dans l’exercice des tâches qui leur incombent en vertu du présent règlement. Si le fournisseur ou le
fournisseur potentiel et l’autorité nationale compétente y consentent explicitement, le rapport de sortie peut être mis à la
disposition du public par l’intermédiaire de la plateforme d’information unique visée au présent article.

**[Article 60]**
b) l’autorité de surveillance du marché de l’État membre où les essais en conditions réelles doivent être réalisés a approuvé
les essais en conditions réelles et le plan d’essais en conditions réelles; lorsque l’autorité de surveillance du marché n’a pas
fourni de réponse dans un délai de 30 jours, les essais en conditions réelles et le plan d’essais en conditions réelles sont
réputés approuvés; lorsque le droit national ne prévoit pas d’approbation tacite, les essais en conditions réelles restent
soumis à autorisation;

**[Article 74]**
6.
Pour les systèmes d’IA à haut risque mis sur le marché, mis en service ou utilisés par des établissements financiers
régis par la législation de l’Union sur les services financiers, l’autorité de surveillance du marché aux fins du présent
règlement est l’autorité nationale responsable de la surveillance financière de ces établissements en vertu de cette législation
dans la mesure où la mise sur le marché, la mise en service ou l’utilisation du système d’IA est directement liée à la
fourniture de ces services financiers.
7.
Par dérogation au paragraphe 6, dans des circonstances appropriées, et pour autant que la coordination soit assurée,
l’État membre peut désigner une autre autorité compétente comme autorité de surveillance du marché aux fins du présent
règlement.
Les autorités nationales de surveillance du marché surveillant les établissements de crédit réglementés régis par la directive
2013/36/UE, qui participent au mécanisme de surveillance unique institué par le règlement (UE) no 1024/2013, devraient
communiquer sans tarder à la Banque centrale européenne toute information identifiée dans le cadre de leurs activités de
surveillance du marché qui pourrait présenter un intérêt potentiel pour les missions de surveillance prudentielle de la
Banque centrale européenne définies dans ledit règlement.

**[Article 80]**
5.
Le fournisseur s’assure que toutes les mesures correctives appropriées sont prises pour tous les systèmes d’IA
concernés qu’il a mis à disposition sur le marché de l’Union.
6.
Lorsque le fournisseur du système d’IA concerné ne prend pas de mesures correctives adéquates dans le délai visé au
paragraphe 2 du présent article, l’article 79, paragraphe 5 à 9, s’applique.
7.
Lorsque, au cours de l’évaluation prévue au paragraphe 1 du présent article, l’autorité de surveillance du marché
établit que le système d’IA a été classé à tort par le fournisseur comme n’étant pas à haut risque afin de contourner
l’application des exigences figurant au chapitre III, section 2, le fournisseur fait l’objet d’amendes conformément
à l’article 99.
8.
Dans l’exercice de leur pouvoir de contrôle de l’application du présent article, et conformément à l’article 11 du
règlement (UE) 2019/1020, les autorités de surveillance du marché peuvent effectuer des contrôles appropriés, en tenant
compte notamment des informations stockées dans la base de données de l’UE visée à l’article 71 du présent règlement.

**[Annexe III]**
b) systèmes d'IA destinés à être utilisés pour évaluer la solvabilité des personnes physiques ou pour établir leur note
de crédit, à l'exception des systèmes d'IA utilisés à des fins de détection de fraudes financières;
c) systèmes d'IA destinés à être utilisés pour l'évaluation des risques et la tarification en ce qui concerne les
personnes physiques en matière d'assurance-vie et d'assurance maladie;
d) systèmes d'IA destinés à évaluer et hiérarchiser les appels d'urgence émanant de personnes physiques ou à être
utilisés pour envoyer ou établir des priorités dans l'envoi des services d'intervention d'urgence, y compris par la
police, les pompiers et l'assistance médicale, ainsi que pour les systèmes de tri des patients admis dans les services
de santé d'urgence.
6.
Répression, dans la mesure où leur utilisation est autorisée par le droit de l'Union ou le droit national applicable:
a) systèmes d'IA destinés à être utilisés par les autorités répressives ou par les institutions, organes et organismes de
l'Union, ou en leur nom, en soutien aux autorités répressives ou en leur nom pour évaluer le risque qu'une
personne physique devienne la victime d'infractions pénales;
b) systèmes d'IA destinés à être utilisés par les autorités répressives ou par les institutions, organes et organismes de
l'Union, ou en leur nom, en soutien aux autorités répressives, en tant que polygraphes ou outils similaires;
c) systèmes d'IA destinés à être utilisés par les autorités répressives ou par les institutions, organes et organismes de
l'Union, ou en leur nom, en soutien aux autorités répressives pour évaluer la fiabilité des preuves au cours
d'enquêtes ou de poursuites pénales;

</details>

- Juge 14B : NON — L'affirmation selon laquelle l'utilisation d'une IA pour évaluer la solvabilité relève **uniquement** d’un système d’IA à haut risque est **incomplète et trompeuse** : l'extrait de l'Annexe III (point
- Avis proposé par Claude : OUI — Citation exacte de l'annexe III, point 5 b), exception fraude comprise. Le juge s'est trompé.

**Ton verdict :** OUI

---
