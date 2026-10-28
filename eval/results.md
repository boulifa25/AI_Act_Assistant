# Résultats de l'évaluation

20 questions (`eval/questions.jsonl`) : questions simples, cas d'usage à classer et questions pièges dont la réponse est absente du texte. Juge de fidélité : `ministral-14b-latest`.

La fidélité humaine provient de `eval/manual_review.md` : avis pré-remplis par Claude (chaque affirmation confrontée aux extraits fournis au modèle), relus et validés par l'auteur. L'accord juge / humain mesure la fiabilité du LLM juge lui-même.

| Métrique | `ollama/mistral` | `mistral/ministral-14b-latest` |
|---|---|---|
| Retrieval@5 | 88 % (15/17) | 88 % (15/17) |
| Citation de l'article attendu | 71 % (12/17) | 71 % (12/17) |
| Fidélité (vérification humaine) | 73 % (11/15) | 92 % (12/13) |
| Fidélité (LLM juge) | 29 % (4/14) | 46 % (6/13) |
| Accord juge / humain | 53 % (8/15) | 54 % (7/13) |
| Refus correct (pièges) | 100 % (3/3) | 100 % (3/3) |
| Faux refus (réponse existante) | 12 % (2/17) | 24 % (4/17) |
| Latence moyenne | 30.4 s | 4.6 s |
| Tokens moyens (entrée + sortie) | 2393 + 203 | 1857 + 169 |
| Coût pour 1 000 questions | 0.00 $ | 0.41 $ |

## Détail par question

| Question | Type | Attendu | `ollama/mistral` | `mistral/ministral-14b-latest` |
|---|---|---|---|---|
| Quelles sont les pratiques d'IA interdites par le règlement ? | simple | Article 5 | cite ❌ · fidèle ❌ · 121 s | cite ✅ · fidèle ❌ · 23 s |
| Comment le règlement définit-il un système d'IA ? | simple | Article 3 | cite ✅ · fidèle ✅ · 21 s | cite ✅ · fidèle ✅ · 3 s |
| Un chatbot doit-il informer l'utilisateur qu'il interagit avec une IA ? | simple | Article 50 | cite ❌ · fidèle ❌ · 22 s | refus ❌ · 1 s |
| Quel est le montant maximal de l'amende en cas de non-respect des pratiques interdites ? | simple | Article 99 | cite ✅ · fidèle ❌ · 19 s | cite ✅ · fidèle ❌ · 3 s |
| À partir de quelle date le règlement est-il applicable ? | simple | Article 113 | cite ✅ · fidèle ❌ · 25 s | cite ✅ · fidèle ❌ · 1 s |
| Quelles sont les exigences de contrôle humain pour les systèmes d'IA à haut risque ? | simple | Article 14 | cite ✅ · fidèle ? · 55 s | cite ✅ · fidèle ❌ · 10 s |
| Que doit contenir le système de gestion des risques d'un système d'IA à haut risque ? | simple | Article 9 | cite ✅ · fidèle ✅ · 43 s | cite ✅ · fidèle ❌ · 7 s |
| Quelles sont les obligations des fournisseurs de modèles d'IA à usage général ? | simple | Article 53 | cite ✅ · fidèle ❌ · 116 s | cite ✅ · fidèle ✅ · 19 s |
| Quand un modèle d'IA à usage général est-il considéré comme présentant un risque systémique ? | simple | Article 51 | cite ✅ · fidèle ❌ · 45 s | cite ✅ · fidèle ✅ · 5 s |
| Qu'est-ce qu'un bac à sable réglementaire de l'IA ? | simple | Article 57 | cite ✅ · fidèle ✅ · 23 s | cite ❌ · fidèle ✅ · 2 s |
| Les contenus générés par hypertrucage (deepfakes) doivent-ils être signalés ? | simple | Article 50 | cite ✅ · fidèle ❌ · 14 s | refus ❌ · 1 s |
| Quelle obligation de maîtrise de l'IA s'impose aux fournisseurs et aux déployeurs ? | simple | Article 4 | cite ✅ · fidèle ✅ · 21 s | cite ✅ · fidèle ✅ · 3 s |
| Qui doit réaliser une analyse d'impact sur les droits fondamentaux ? | simple | Article 27 | cite ✅ · fidèle ❌ · 14 s | cite ✅ · fidèle ❌ · 5 s |
| Le règlement s'applique-t-il aux systèmes d'IA utilisés à des fins militaires ? | simple | Article 2 | refus ❌ · 10 s | refus ❌ · 1 s |
| Un système d'IA qui trie automatiquement des CV pour un recrutement est-il à haut risque ? | cas | Annexe III, Article 6 | refus ❌ · 8 s | cite ✅ · fidèle ✅ · 2 s |
| Une banque peut-elle utiliser une IA pour évaluer la solvabilité de ses clients ? Quel niveau de risque ? | cas | Annexe III, Article 6 | cite ✅ · fidèle ❌ · 12 s | cite ✅ · fidèle ❌ · 2 s |
| Un employeur peut-il utiliser une IA de reconnaissance des émotions pour surveiller ses salariés ? | cas | Article 5 | cite ❌ · fidèle ❌ · 18 s | refus ❌ · 1 s |
| Quel est le salaire moyen d'un data scientist en France ? | piege | — | ✅ refus | ✅ refus |
| Combien coûte une évaluation de conformité auprès d'un organisme notifié ? | piege | — | ✅ refus | ✅ refus |
| Quel commissaire européen est chargé de l'application de l'AI Act ? | piege | — | ✅ refus | ✅ refus |
