# 📋 Sujets de Projets – Licence 3 Génie Informatique

> **Université de Mahajanga** – Faculté des Sciences – Département Génie Informatique  
> **Année universitaire 2025–2026**  
> **Encadrant** : M. BEZARA Roussel Florent – Enseignant non permanent & Doctorant D1 (EAD 3SH / EDGVM)

---

## Table des matières

- [Présentation générale](#présentation-générale)
- [Fiches de sujets](#fiches-de-sujets)
  - [Fiche 1 – Certifier l'authenticité des diplômes via une empreinte cryptographique](#fiche-1--certifier-lauthenticité-des-diplômes-via-une-empreinte-cryptographique)
  - [Fiche 2 – Automatiser le pointage étudiant par QR code dynamique et tableau de bord temps réel](#fiche-2--automatiser-le-pointage-étudiant-par-qr-code-dynamique-et-tableau-de-bord-temps-réel)
  - [Fiche 3 – Construire un moteur de recommandation pédagogique par apprentissage automatique](#fiche-3--construire-un-moteur-de-recommandation-pédagogique-par-apprentissage-automatique)
  - [Fiche 4 – Créer une plateforme de signalement anonyme des dysfonctionnements universitaires](#fiche-4--créer-une-plateforme-de-signalement-anonyme-des-dysfonctionnements-universitaires)
  - [Fiche 5 – Concevoir un système de suivi et de calcul automatisé des heures d'enseignement](#fiche-5--concevoir-un-système-de-suivi-et-de-calcul-automatisé-des-heures-denseignement)
  - [Fiche 6 – Analyser les processus administratifs universitaires par process mining](#fiche-6--analyser-les-processus-administratifs-universitaires-par-process-mining)
  - [Fiche 7 – Détecter les textes générés par IA dans les travaux académiques](#fiche-7--détecter-les-textes-générés-par-ia-dans-les-travaux-académiques)
  - [Fiche 8 – Développer un chatbot d'orientation et d'assistance administrative pour les étudiants](#fiche-8--développer-un-chatbot-dorientation-et-dassistance-administrative-pour-les-étudiants)
  - [Fiche 9 – Mettre en place un système de vote électronique sécurisé pour les élections universitaires](#fiche-9--mettre-en-place-un-système-de-vote-électronique-sécurisé-pour-les-élections-universitaires)
  - [Fiche 10 – Construire un tableau de bord décisionnel pour le pilotage pédagogique d'un département](#fiche-10--construire-un-tableau-de-bord-décisionnel-pour-le-pilotage-pédagogique-dun-département)
- [Versions condensées](#versions-condensées)
- [Annexes](#annexes)
  - [A. Modèle de consentement éclairé](#a-modèle-de-consentement-éclairé)
  - [B. Clause de réutilisation des données](#b-clause-de-réutilisation-des-données)
  - [C. Script Python d'anonymisation](#c-script-python-danonymisation)
  - [D. Schéma CSV standardisé](#d-schéma-csv-standardisé)
  - [E. Checklist technique d'anonymisation](#e-checklist-technique-danonymisation)
  - [F. Message de recrutement](#f-message-de-recrutement)

---

## Présentation générale

Ces sujets sont conçus pour des étudiants de **Licence 3 en Génie Informatique**. Chaque projet est **purement technique** (développement, IA, sécurité, réseaux, analyse de données) tout en étant connecté à la problématique de la **gestion pédagogique et administrative face à la transformation numérique** dans les universités malgaches.

**Durée** : 3 à 6 mois · **Livrables** : code source, prototype fonctionnel, jeu de données anonymisé, rapport (20–30 pages), présentation orale.

**Règles communes** :

- Chaque projet prévoit un **Plan B** en cas de refus d'accès aux données institutionnelles.
- Le consentement des participants est **obligatoire** (modèle fourni en annexe).
- Les données doivent être **anonymisées** selon la checklist et le script fournis.
- Le jeu de données remis doit respecter le **schéma CSV standardisé** (annexe D).

---

## Fiches de sujets

---

### Fiche 1 – Certifier l'authenticité des diplômes via une empreinte cryptographique

**Domaine** : Sécurité / Cryptographie / Développement web

#### Problématique

La falsification de diplômes fragilise la crédibilité des établissements supérieurs malgaches et pénalise les diplômés légitimes. Les solutions blockchain existent mais restent coûteuses et complexes à déployer localement. Comment proposer un mécanisme de certification numérique léger, vérifiable par un tiers, sans infrastructure lourde ?

#### Objectifs

1. Développer une API REST générant un hash SHA-256 salé unique pour chaque diplôme émis.
2. Implémenter un portail web public de vérification par saisie de code ou scan de QR code.
3. Stocker les empreintes dans une base relationnelle avec horodatage et traçabilité des vérifications.
4. Valider la résistance du système via au moins 50 scénarios de test (diplôme valide, altéré, inexistant).
5. Rédiger une analyse comparative avec une approche blockchain (coût, complexité, faisabilité locale).

#### Méthodologie détaillée

| Étape | Description | Outils / Technologies |
|-------|------------|----------------------|
| 1. État de l'art (2 sem.) | Revue des méthodes de certification numérique (hash, PKI, blockchain) | Google Scholar, Zotero |
| 2. Conception | Modélisation UML : cas d'utilisation, classes, séquences | StarUML, draw.io |
| 3. Backend | API REST avec génération de hash salé, stockage en base | Python/Flask ou Node.js/Express, `hashlib` ou `crypto`, PostgreSQL |
| 4. Frontend | Portail de vérification + génération QR | React ou Vue.js, `qrcode.js` ou `python-qrcode` |
| 5. Tests | 50 scénarios automatisés (valide, modifié, inexistant, rejeu) | pytest ou Jest |
| 6. Rédaction | Rapport technique + comparaison blockchain + préparation soutenance | LaTeX ou Word |

#### Schéma de jeu de données (CSV)

| Colonne | Type | Exemple |
|---------|------|---------|
| `hash_id` | TEXT | `a3f8c2e1b7d9f031` |
| `date_emission` | DATE (ISO) | `2025-06-15` |
| `type_diplome` | TEXT | `Licence` &#124; `Master` &#124; `Doctorat` |
| `etablissement_code` | TEXT | `UMG` |
| `salt` | TEXT | `x9k2m8p4...` |
| `verification_count` | INT | `12` |
| `derniere_verif` | DATETIME | `2025-09-01T14:30:00` |

#### Taille minimale d'échantillon

≥ 50 diplômes simulés (données fictives via Faker) pour couvrir l'ensemble des cas de test.

#### Livrables attendus

- Code source (dépôt Git) avec README et instructions de déploiement
- Prototype déployable (Docker Compose)
- Jeu de données de test (50+ enregistrements, CSV)
- Rapport technique (20–30 pages) avec comparaison blockchain
- Présentation (15 diapositives)

#### Calendrier indicatif

| Mois | Activités |
|------|-----------|
| M1 | État de l'art + conception UML |
| M2 | Développement backend (API + base) |
| M3 | Développement frontend + intégration QR |
| M4 | Tests (50 scénarios) + corrections |
| M5 | Rédaction rapport + soutenance |

#### Contraintes éthiques et IT

- Aucune donnée réelle de diplôme : le jeu est **entièrement synthétique**.
- Si des exemples réels sont fournis (Plan A) : anonymisation **avant** tout stockage.
- Autorisation du service informatique requise pour déploiement réseau.
- Risque : fuite d'empreintes → chiffrement TLS + accès restreint par rôle.

#### Plan B

Générer 100 % des données via la bibliothèque **Faker** (Python) en respectant le schéma CSV défini.

#### Questionnaire court (≤ 10 questions)

1. À quelle fréquence votre établissement reçoit-il des demandes de vérification de diplômes ? *(Jamais / Rarement / Mensuellement / Hebdomadairement)*
2. Avez-vous déjà rencontré un cas suspect de faux diplôme ? *(Oui / Non / Ne sait pas)*
3. Quel est le délai moyen pour vérifier un diplôme actuellement ? *(< 1 jour / 1–3 jours / > 3 jours)*
4. Seriez-vous favorable à un système de vérification en ligne ? *(Échelle 1–5)*
5. Quelles informations minimales devrait contenir un certificat numérique ? *(Choix multiples)*
6. Quel support privilégiez-vous pour la vérification ? *(Web / Mobile / QR code / Autre)*

#### Critères d'évaluation

| Critère | Poids | Indicateurs |
|---------|-------|-------------|
| Technique | 40 % | Qualité du code, couverture de tests, sécurité du hachage |
| Expérimental | 30 % | Nombre de scénarios testés, taux de détection correcte |
| Livrables | 30 % | Clarté du rapport, documentation, qualité de la présentation |

#### Extensions possibles (Master / Thèse)

- Intégration blockchain (Ethereum/Hyperledger Fabric)
- Architecture fédérée multi-établissements avec API partagée
- Application mobile de scan avec vérification hors-ligne
- Étude d'acceptabilité auprès des employeurs et recruteurs malgaches

---

### Fiche 2 – Automatiser le pointage étudiant par QR code dynamique et tableau de bord temps réel

**Domaine** : Développement mobile / IoT / Systèmes d'information

#### Problématique

Les feuilles d'émargement papier sont sujettes aux erreurs, à la fraude (signature pour un absent) et ne permettent aucune analyse en temps réel. La numérisation du suivi de présence ouvre la voie à des tableaux de bord pédagogiques et à la détection précoce du décrochage. Comment concevoir un système fiable, peu coûteux, adapté aux contraintes de connectivité locale ?

#### Objectifs

1. Développer une application mobile pour scanner des QR codes de séance générés dynamiquement.
2. Concevoir un backend REST avec stockage des données de présence et gestion des sessions.
3. Créer un tableau de bord web affichant en temps réel : taux de présence, absentéisme par matière, alertes.
4. Tester le système avec ≥ 30 étudiants sur 4 semaines consécutives.
5. Mesurer le gain de temps par rapport à l'appel manuel (t-test pré/post).

#### Méthodologie détaillée

| Étape | Description | Outils / Technologies |
|-------|------------|----------------------|
| 1. Analyse des besoins (2 sem.) | Entretiens avec 3–5 enseignants et le service scolarité | Guide d'entretien semi-directif |
| 2. Conception | Diagrammes UML + maquettes UI | Figma, draw.io |
| 3. Backend | API REST, gestion des séances, QR dynamique par séance (expiration 5 min) | Laravel 11 ou Express.js, MySQL/PostgreSQL |
| 4. Application mobile | Scan caméra QR + affichage statut | React Native (`react-native-camera`) ou Flutter |
| 5. Dashboard | Visualisations interactives (taux, courbes, alertes) | Vue.js ou React + Chart.js |
| 6. Test pilote (4 sem.) | Déploiement réel + collecte feedback | Questionnaire post-test |
| 7. Analyse + rédaction | Comparaison temps d'appel, analyse statistique | Python (pandas, scipy) |

#### Schéma de jeu de données (CSV)

| Colonne | Type | Exemple |
|---------|------|---------|
| `presence_id` | INT | `1` |
| `etudiant_hash` | TEXT (SHA-256) | `b7e2a...f31` |
| `seance_id` | INT | `42` |
| `matiere_code` | TEXT | `INF301` |
| `date_seance` | DATE (ISO) | `2025-10-07` |
| `heure_scan` | TIME | `08:15:32` |
| `methode_scan` | TEXT | `QR` &#124; `NFC` |
| `statut` | TEXT | `Present` &#124; `Retard` &#124; `Absent` |

#### Taille minimale d'échantillon

30 étudiants × 4 semaines × 3 séances/semaine = **360 enregistrements minimum**. Seuil de 30 pour t-test comparatif (temps d'appel).

#### Livrables attendus

- Code source mobile + backend (dépôt Git)
- Dashboard web fonctionnel
- Jeu de données anonymisé (CSV, 360+ lignes)
- Rapport technique (20–30 pages) avec analyse comparative
- Présentation (15 diapositives)

#### Calendrier indicatif

| Mois | Activités |
|------|-----------|
| M1 | Analyse besoins + conception + maquettes |
| M2 | Développement backend + base de données |
| M3 | Développement mobile + intégration |
| M4 | Dashboard + test pilote (4 semaines) |
| M5 | Analyse données + rédaction rapport |
| M6 | Finalisation + soutenance |

#### Contraintes éthiques et IT

- Consentement écrit obligatoire de chaque étudiant participant.
- Anonymisation par hachage SHA-256 salé dans le jeu de données publié.
- Aucune géolocalisation collectée.
- Conservation des données : 1 an après soutenance, puis destruction.
- Risque : perception de surveillance → communication transparente + droit de retrait effectif.

#### Plan B

Simuler 30 étudiants virtuels avec des scripts Python générant des patterns de présence réalistes (taux d'absentéisme 10–20 %, retards aléatoires).

#### Questionnaire court

1. Combien de temps dure habituellement l'appel en début de cours ? *(< 5 min / 5–10 min / > 10 min)*
2. La feuille d'émargement actuelle vous semble-t-elle fiable ? *(Échelle 1–5)*
3. Possédez-vous un smartphone avec caméra ? *(Oui / Non)*
4. Seriez-vous à l'aise avec un scan QR pour pointer votre présence ? *(Échelle 1–5)*
5. Quelles fonctionnalités attendez-vous d'un tableau de bord de présence ? *(Choix multiples)*
6. Avez-vous déjà utilisé une application de pointage numérique ? *(Oui / Non)*

#### Critères d'évaluation

| Critère | Poids | Indicateurs |
|---------|-------|-------------|
| Technique | 40 % | Architecture REST, code mobile, design UI/UX |
| Expérimental | 30 % | Données collectées, comparaison temps d'appel |
| Livrables | 30 % | Documentation, rapport, dashboard fonctionnel |

#### Extensions possibles

- Détection automatique via Bluetooth Low Energy (BLE beacons)
- Modèle prédictif de décrochage basé sur l'absentéisme (régression logistique)
- Intégration avec un LMS (Moodle)
- Extension multi-campus avec synchronisation cloud

---

### Fiche 3 – Construire un moteur de recommandation pédagogique par apprentissage automatique

**Domaine** : Intelligence artificielle / Machine Learning / LMS

#### Problématique

Les plateformes LMS universitaires proposent un accès uniforme aux ressources sans tenir compte du niveau, de l'historique ou des préférences de l'étudiant. L'apprentissage automatique permet de personnaliser dynamiquement l'expérience pédagogique. Comment développer un moteur de recommandation réaliste et intégrable dans un contexte universitaire malgache à ressources limitées ?

#### Objectifs

1. Collecter ou simuler un jeu de données d'interactions étudiant-ressource (≥ 5 000 interactions).
2. Implémenter un filtrage collaboratif (SVD ou KNN) avec la bibliothèque Surprise.
3. Implémenter un filtrage basé sur le contenu (TF-IDF sur les métadonnées des ressources).
4. Combiner les deux approches dans un module hybride avec pondération configurable.
5. Évaluer la qualité des recommandations via precision@10, recall@10 et NDCG.

#### Méthodologie détaillée

| Étape | Description | Outils / Technologies |
|-------|------------|----------------------|
| 1. État de l'art (2 sem.) | Systèmes de recommandation en éducation | Google Scholar, Zotero |
| 2. Données | Extraction logs Moodle (si accès) ou génération synthétique | pandas, Faker |
| 3. Prétraitement | Nettoyage, normalisation, matrice utilisateur-item | pandas, numpy |
| 4. Filtrage collaboratif | SVD, KNN sur matrice d'interactions | `scikit-surprise` |
| 5. Filtrage contenu | TF-IDF sur titres/descriptions des ressources | `scikit-learn` (TfidfVectorizer) |
| 6. Module hybride | Pondération linéaire des scores, grid search sur alpha | Python |
| 7. Évaluation | Split train/test 80/20, métriques precision@k, recall@k, NDCG | scikit-learn, Surprise |
| 8. Prototype | API Flask servant les recommandations + interface web | Flask, React/Vue.js |

#### Schéma de jeu de données (CSV)

| Colonne | Type | Exemple |
|---------|------|---------|
| `interaction_id` | INT | `1` |
| `user_hash` | TEXT | `c4d1e...a82` |
| `resource_id` | INT | `305` |
| `resource_type` | TEXT | `PDF` &#124; `Video` &#124; `Quiz` |
| `action` | TEXT | `view` &#124; `download` &#124; `complete` |
| `rating` | FLOAT (1-5) | `4.0` |
| `timestamp` | DATETIME | `2025-09-15T10:22:00` |
| `session_duration_sec` | INT | `1200` |

#### Taille minimale d'échantillon

100 utilisateurs × 50 ressources = **5 000 interactions** minimum (simulées si nécessaire). Seuil minimal pour un SVD exploitable.

#### Livrables attendus

- Code source Python (notebooks + scripts) sur dépôt Git
- API Flask de recommandation avec interface web minimale
- Jeu de données (CSV, 5 000+ interactions)
- Rapport (20–30 pages) avec analyse des métriques
- Présentation (15 diapositives)

#### Calendrier indicatif

| Mois | Activités |
|------|-----------|
| M1 | État de l'art + collecte/génération données |
| M2 | Prétraitement + filtrage collaboratif |
| M3 | Filtrage contenu + modèle hybride |
| M4 | API + interface web + évaluation complète |
| M5 | Rédaction + soutenance |

#### Contraintes éthiques et IT

- Logs Moodle : autorisation de l'administrateur LMS + anonymisation immédiate.
- Aucun identifiant direct dans le jeu publié (hachage + suppression IP).
- Risque : biais algorithmique → audit des recommandations sur des profils variés.

#### Plan B

Générer un jeu synthétique de 5 000 interactions avec des profils étudiants réalistes (3 niveaux × 5 domaines) via script Python + Faker.

#### Questionnaire court

1. Utilisez-vous régulièrement la plateforme LMS de votre université ? *(Jamais / Parfois / Souvent / Toujours)*
2. Trouvez-vous facilement les ressources pertinentes ? *(Échelle 1–5)*
3. Quels types de ressources consultez-vous le plus ? *(PDF / Vidéos / Quiz / Forums)*
4. Aimeriez-vous recevoir des recommandations personnalisées ? *(Oui / Non / Peut-être)*
5. Sur quels critères devrait se baser une recommandation ? *(Choix multiples)*
6. Combien de temps passez-vous par semaine sur le LMS ? *(< 1h / 1–3h / 3–5h / > 5h)*

#### Critères d'évaluation

| Critère | Poids | Indicateurs |
|---------|-------|-------------|
| Technique | 40 % | Code ML propre, choix algorithmiques justifiés, pipeline reproductible |
| Expérimental | 30 % | Métriques (precision@10, recall@10, NDCG), analyse |
| Livrables | 30 % | Documentation, API fonctionnelle, rapport |

#### Extensions possibles

- Deep learning (autoencodeurs variationnels, transformers)
- Recommandation en temps réel (streaming)
- Plugin Moodle intégré
- A/B test avec étudiants réels sur un semestre

---

### Fiche 4 – Créer une plateforme de signalement anonyme des dysfonctionnements universitaires

**Domaine** : Développement web / Sécurité / Gouvernance numérique

#### Problématique

Les dysfonctionnements administratifs (retards, procédures opaques, irrégularités) dans les universités malgaches sont rarement signalés par crainte de représailles. Une plateforme numérique garantissant l'anonymat technique (pas de logs IP, pas de compte obligatoire) pourrait améliorer la transparence institutionnelle. Comment assurer un anonymat vérifiable tout en maintenant la crédibilité des signalements ?

#### Objectifs

1. Développer une application web avec soumission anonyme (zéro donnée identifiante stockée côté serveur).
2. Implémenter une catégorisation des signalements (retard, irrégularité, corruption présumée, autre).
3. Concevoir un module de modération avec workflow (nouveau → en cours → traité / rejeté).
4. Produire un tableau de bord statistique (types, fréquences, délais de traitement).
5. Réaliser un test utilisateur SUS (System Usability Scale) avec ≥ 30 participants.

#### Méthodologie détaillée

| Étape | Description | Outils / Technologies |
|-------|------------|----------------------|
| 1. Étude comparative (2 sem.) | Analyse de 3–5 plateformes de signalement existantes | Web, documentation |
| 2. Conception | Wireframes + modèle de données + architecture MVC | Figma, draw.io |
| 3. Développement | Application web avec anonymat by design : pas de login, pas de log IP, token jetable | Laravel 11 + Livewire ou Django, MySQL |
| 4. Modération | Interface admin avec états, filtres, notifications | Livewire ou Django Admin |
| 5. Dashboard | Visualisations statistiques | Chart.js ou Recharts |
| 6. Test utilisateur | 30 participants, scénarios prédéfinis, questionnaire SUS | Formulaire post-test |
| 7. Analyse + rédaction | Score SUS, feedback qualitatif, rédaction rapport | Python (statistiques) |

#### Schéma de jeu de données (CSV)

| Colonne | Type | Exemple |
|---------|------|---------|
| `signalement_id` | INT | `1` |
| `token_suivi` | TEXT | `tkn_8f3a2b...` |
| `categorie` | TEXT | `retard` &#124; `irregularite` &#124; `corruption` &#124; `autre` |
| `service_concerne` | TEXT | `Scolarité` &#124; `Finances` &#124; `Examens` |
| `date_soumission` | DATETIME | `2025-10-12T09:45:00` |
| `statut` | TEXT | `nouveau` &#124; `en_cours` &#124; `traite` &#124; `rejete` |
| `score_urgence` | INT (1–5) | `3` |

#### Taille minimale d'échantillon

30 participants pour le test SUS + 50 signalements simulés pour peupler le dashboard.

#### Livrables attendus

- Code source (dépôt Git) avec documentation de déploiement
- Application déployable (Docker ou serveur partagé)
- Jeu de données simulé (50+ signalements, CSV)
- Rapport technique (20–30 pages) avec résultats SUS
- Présentation (15 diapositives)

#### Calendrier indicatif

| Mois | Activités |
|------|-----------|
| M1 | Étude comparative + conception |
| M2 | Développement backend + anonymat |
| M3 | Module modération + dashboard |
| M4 | Tests utilisateurs (30 participants) |
| M5 | Analyse résultats + rédaction |
| M6 | Finalisation + soutenance |

#### Contraintes éthiques et IT

- **Minimisation des données** : aucun identifiant personnel stocké, pas d'IP loggée.
- Token jetable non lié à l'identité du soumetteur.
- Consentement uniquement pour le test utilisateur (pas pour le signalement lui-même).
- Risque : signalements diffamatoires → modération + charte d'utilisation obligatoire.

#### Plan B

Réaliser le test utilisateur avec des étudiants volontaires hors cadre institutionnel, en utilisant des scénarios entièrement fictifs.

#### Questionnaire court

1. Avez-vous déjà rencontré un dysfonctionnement administratif à l'université ? *(Oui / Non)*
2. L'avez-vous signalé ? *(Oui / Non)* → Si non, pourquoi ? *(Peur / Inutile / Pas de canal)*
3. Utiliseriez-vous une plateforme de signalement anonyme ? *(Échelle 1–5)*
4. [Post-test] La soumission a-t-elle été facile ? *(Échelle 1–5)*
5. [Post-test] Faites-vous confiance à la garantie d'anonymat du système ? *(Échelle 1–5)*
6. [Post-test] Score SUS (10 questions standard).

#### Critères d'évaluation

| Critère | Poids | Indicateurs |
|---------|-------|-------------|
| Technique | 40 % | Architecture anonymat, qualité du code, sécurité |
| Expérimental | 30 % | Score SUS, résultats test utilisateur, feedback |
| Livrables | 30 % | Complétude de la plateforme, rapport, présentation |

#### Extensions possibles

- Classification automatique des signalements par NLP (BERT / CamemBERT)
- Analyse de sentiments sur les descriptions textuelles
- Chatbot WhatsApp pour signalement vocal (speech-to-text)
- Étude longitudinale d'impact sur la gouvernance universitaire

---

### Fiche 5 – Concevoir un système de suivi et de calcul automatisé des heures d'enseignement

**Domaine** : Systèmes d'information / Développement web / Workflow

#### Problématique

La gestion des heures d'enseignement (statutaires et supplémentaires) dans les universités malgaches s'appuie souvent sur des tableurs ou des fiches papier, ce qui entraîne des erreurs de calcul, des retards de paiement et des contestations. Un système numérique centralisé avec validation hiérarchique et alertes automatiques fiabiliserait ce processus critique. Comment modéliser les règles métier spécifiques à chaque établissement dans un outil paramétrable ?

#### Objectifs

1. Modéliser les règles de calcul (heures statutaires, supplémentaires, taux horaire par grade).
2. Développer une application web avec saisie, validation hiérarchique (enseignant → chef de département → DRH) et calcul automatique.
3. Implémenter des alertes par email/SMS (dépassement de quota, anomalies, échéances).
4. Produire des exports PDF et Excel conformes aux modèles administratifs existants.
5. Valider avec des données couvrant 50 enseignants sur 1 semestre.

#### Méthodologie détaillée

| Étape | Description | Outils / Technologies |
|-------|------------|----------------------|
| 1. Recueil besoins (2 sem.) | Entretiens DRH, service financier, 5 enseignants | Guide d'entretien |
| 2. Modélisation | Règles métier (grades, quotas, taux), diagrammes UML | draw.io |
| 3. Backend | API + workflow de validation multi-niveaux | Laravel 11 + Livewire, MySQL |
| 4. Frontend + alertes | Interface responsive + notifications email/SMS | TailwindCSS, Vonage ou MAPI |
| 5. Exports | PDF + Excel conformes aux modèles existants | DomPDF, Maatwebsite/Laravel-Excel |
| 6. Tests | 50 enseignants × 1 semestre, validation par recoupement manuel | Données réelles anonymisées ou simulées |

#### Schéma de jeu de données (CSV)

| Colonne | Type | Exemple |
|---------|------|---------|
| `enseignant_hash` | TEXT | `e8f1c...b47` |
| `grade` | TEXT | `Professeur` &#124; `MC` &#124; `Assistant` |
| `matiere_code` | TEXT | `INF201` |
| `type_heure` | TEXT | `CM` &#124; `TD` &#124; `TP` |
| `nb_heures` | FLOAT | `4.0` |
| `date_seance` | DATE (ISO) | `2025-09-22` |
| `semestre` | TEXT | `S1-2025` |
| `statut_validation` | TEXT | `soumis` &#124; `validé` &#124; `rejeté` |
| `montant_calc` | FLOAT (MGA) | `120000` |

#### Taille minimale d'échantillon

50 enseignants × 16 semaines = **800+ enregistrements**.

#### Livrables attendus

- Code source Laravel (dépôt Git)
- Application déployable avec documentation
- Exports PDF/Excel fonctionnels
- Jeu de données (CSV, 800+ lignes)
- Rapport technique (20–30 pages)
- Présentation (15 diapositives)

#### Calendrier indicatif

| Mois | Activités |
|------|-----------|
| M1 | Recueil besoins + modélisation règles métier |
| M2 | Développement backend + workflow validation |
| M3 | Frontend + alertes + exports |
| M4 | Tests avec données (50 enseignants) |
| M5 | Corrections + rédaction rapport |
| M6 | Finalisation + soutenance |

#### Contraintes éthiques et IT

- Données salariales sensibles : anonymisation obligatoire (hachage noms, suppression contacts).
- Accès restreint par rôle (RBAC). Autorisation DRH requise pour données réelles.
- Risque : résistance au changement → prévoir formation et communication.

#### Plan B

Générer 50 enseignants fictifs avec profils réalistes (grades, matières, volumes horaires typés) via Faker.

#### Questionnaire court

1. Comment gérez-vous actuellement vos heures supplémentaires ? *(Papier / Tableur / Logiciel / Autre)*
2. Rencontrez-vous des erreurs de calcul ? *(Jamais / Rarement / Souvent)*
3. Quel est le délai moyen entre saisie et paiement ? *(< 1 mois / 1–3 mois / > 3 mois)*
4. Quelles fonctionnalités jugez-vous prioritaires ? *(Choix multiples : calcul auto, alerte, export, historique)*
5. Seriez-vous prêt à utiliser un outil numérique ? *(Échelle 1–5)*
6. Préférez-vous les notifications par email ou SMS ? *(Email / SMS / Les deux / Aucun)*

#### Critères d'évaluation

| Critère | Poids | Indicateurs |
|---------|-------|-------------|
| Technique | 40 % | Modélisation des règles, workflow, qualité du code, exports |
| Expérimental | 30 % | Exactitude des calculs, comparaison avec calcul manuel |
| Livrables | 30 % | Documentation, application fonctionnelle, rapport |

#### Extensions possibles

- Intégration avec le système de paie existant
- Module prévisionnel budgétaire (projection des heures suppl. sur l'année)
- Application mobile pour la saisie par les enseignants
- Déploiement multi-établissement avec paramétrage des règles

---

### Fiche 6 – Analyser les processus administratifs universitaires par process mining

**Domaine** : Process mining / Data science / Analyse de données

#### Problématique

Les processus administratifs (inscriptions, délibérations, délivrance de documents) suivent théoriquement des procédures définies, mais les pratiques réelles s'en écartent souvent de manière invisible. Le process mining permet de reconstruire objectivement les parcours réels à partir de logs numériques et de détecter goulots d'étranglement, boucles et déviations. Comment adapter cette technique au contexte universitaire malgache pour améliorer la transparence et l'efficacité ?

#### Objectifs

1. Collecter ou simuler un event log d'au moins 500 cas (processus d'inscription ou de délibération).
2. Appliquer des algorithmes de découverte de processus (Alpha Miner, Heuristic Miner, Inductive Miner).
3. Identifier les goulots d'étranglement par analyse de performance temporelle.
4. Détecter les déviations par conformance checking (alignments).
5. Visualiser les résultats dans un rapport interactif (Jupyter Notebook ou dashboard web).

#### Méthodologie détaillée

| Étape | Description | Outils / Technologies |
|-------|------------|----------------------|
| 1. État de l'art (2 sem.) | Process mining en éducation, outils PM4Py / ProM | Littérature scientifique |
| 2. Modélisation BPMN | Processus idéal (inscription ou délibération) | Camunda Modeler, draw.io |
| 3. Collecte données | Extraction logs SI scolarité ou génération synthétique | SQL, pandas |
| 4. Prétraitement | Conversion au format XES/CSV event log | pandas, PM4Py |
| 5. Analyse | Découverte + conformance checking + analyse performance | PM4Py |
| 6. Visualisation | Petri nets, BPMN découverts, heatmaps temporelles | PM4Py, matplotlib, plotly |
| 7. Rédaction | Interprétation des résultats + recommandations | — |

#### Schéma de jeu de données (CSV)

| Colonne | Type | Exemple |
|---------|------|---------|
| `case_id` | TEXT | `INS-2025-0001` |
| `activity` | TEXT | `Depot_dossier` &#124; `Verification` &#124; `Paiement` &#124; `Validation` |
| `timestamp` | DATETIME | `2025-09-01T08:30:00` |
| `resource` | TEXT | `Agent_A` (anonymisé) |
| `cost` | FLOAT | `25000` |
| `departement` | TEXT | `Informatique` |
| `statut_final` | TEXT | `complet` &#124; `abandon` &#124; `rejet` |

#### Taille minimale d'échantillon

500 cas × 4–8 événements/cas = **2 000–4 000 lignes** d'event log.

#### Livrables attendus

- Scripts Python (Jupyter Notebooks) documentés
- Event log (CSV/XES, 500+ cas)
- Modèles de processus découverts (images Petri net / BPMN)
- Rapport (20–30 pages) avec analyse des déviations
- Présentation (15 diapositives)

#### Calendrier indicatif

| Mois | Activités |
|------|-----------|
| M1 | État de l'art + modélisation BPMN |
| M2 | Collecte/génération event log + prétraitement |
| M3 | Découverte + conformance checking |
| M4 | Analyse performance + visualisations |
| M5 | Rédaction + soutenance |

#### Contraintes éthiques et IT

- Logs institutionnels : autorisation direction + service informatique.
- Anonymisation des noms d'agents et étudiants dans les event logs.
- Risque : ré-identification indirecte par combinaison de champs → agrégation et généralisation.

#### Plan B

Générer un event log synthétique à partir du modèle BPMN, avec injection de 15–20 % de déviations (boucles, sauts d'étapes, délais anormaux).

#### Questionnaire court

1. Connaissez-vous les étapes officielles du processus d'inscription ? *(Oui / Partiellement / Non)*
2. Avez-vous constaté des étapes sautées ou inversées ? *(Oui / Non)*
3. Quel est le délai moyen pour une inscription complète ? *(< 1 sem. / 1–2 sem. / > 2 sem.)*
4. Quelles étapes vous semblent les plus lentes ? *(Choix multiples)*
5. Avez-vous déjà entendu parler du process mining ? *(Oui / Non)*
6. Seriez-vous favorable à un audit numérique des processus ? *(Échelle 1–5)*

#### Critères d'évaluation

| Critère | Poids | Indicateurs |
|---------|-------|-------------|
| Technique | 40 % | Maîtrise PM4Py, pipeline reproductible, qualité du code |
| Expérimental | 30 % | Qualité de l'event log, pertinence des déviations détectées |
| Livrables | 30 % | Visualisations, rapport, documentation |

#### Extensions possibles

- Process mining en temps réel (streaming events)
- Prédiction de délais par machine learning
- Extension à d'autres processus (examens, réclamations, stages)
- Étude comparative multi-universités malgaches

---

### Fiche 7 – Détecter les textes générés par IA dans les travaux académiques

**Domaine** : Intelligence artificielle / NLP / Intégrité académique

#### Problématique

L'essor des modèles de langage (ChatGPT, Claude, etc.) pose un défi majeur pour l'intégrité académique : les enseignants peinent à distinguer un texte rédigé par un étudiant d'un texte généré par IA. Les outils de détection existants sont majoritairement anglophones et peu adaptés au français académique. Comment développer un classificateur binaire (humain vs IA) performant sur des textes académiques francophones ?

#### Objectifs

1. Constituer un corpus bilingue (français principalement, malgache optionnel) de textes académiques humains et générés par IA (≥ 500 textes).
2. Extraire des features linguistiques discriminantes (perplexité, diversité lexicale, longueur de phrases, entropie).
3. Entraîner et comparer au moins 3 classificateurs (Logistic Regression, Random Forest, SVM).
4. Évaluer les performances (accuracy, precision, recall, F1-score) avec validation croisée 5-fold.
5. Développer une interface web simple permettant de soumettre un texte et d'obtenir un score de probabilité.

#### Méthodologie détaillée

| Étape | Description | Outils / Technologies |
|-------|------------|----------------------|
| 1. État de l'art (2 sem.) | Détection IA, features linguistiques, outils existants (GPTZero, ZeroGPT) | Littérature |
| 2. Collecte corpus | Textes humains : mémoires, rapports étudiants (anonymisés). Textes IA : génération via API Claude/GPT sur mêmes sujets | API Anthropic/OpenAI, collecte manuelle |
| 3. Feature engineering | Extraction : perplexité (GPT-2 via HuggingFace), diversité lexicale (TTR, hapax), entropie, distribution longueur de phrases | Python, HuggingFace `transformers`, nltk, spacy |
| 4. Modélisation | Entraînement LR, RF, SVM ; grid search hyperparamètres | scikit-learn |
| 5. Évaluation | Cross-validation 5-fold, matrice de confusion, courbe ROC | scikit-learn, matplotlib |
| 6. Interface web | Upload texte → score de probabilité IA/humain | Flask + HTML/CSS |
| 7. Rédaction | Rapport + analyse des erreurs (faux positifs/négatifs) | — |

#### Schéma de jeu de données (CSV)

| Colonne | Type | Exemple |
|---------|------|---------|
| `text_id` | INT | `1` |
| `text_content` | TEXT | `Le développement durable...` (extrait) |
| `label` | TEXT | `human` &#124; `ai_generated` |
| `source_model` | TEXT | `null` &#124; `claude-3` &#124; `gpt-4` |
| `language` | TEXT | `fr` &#124; `mg` |
| `word_count` | INT | `850` |
| `domain` | TEXT | `informatique` &#124; `gestion` &#124; `sciences` |
| `perplexity_score` | FLOAT | `42.7` |
| `lexical_diversity` | FLOAT | `0.72` |

#### Taille minimale d'échantillon

≥ 250 textes humains + 250 textes IA = **500 textes minimum**. Justification : seuil pour un entraînement supervisé fiable avec cross-validation.

#### Livrables attendus

- Code source Python (notebooks + scripts) sur dépôt Git
- Corpus annoté (CSV, 500+ textes avec features)
- Interface web de détection fonctionnelle
- Rapport (20–30 pages) avec analyse des performances et des erreurs
- Présentation (15 diapositives)

#### Calendrier indicatif

| Mois | Activités |
|------|-----------|
| M1 | État de l'art + constitution du corpus |
| M2 | Feature engineering + analyse exploratoire |
| M3 | Entraînement des classificateurs + tuning |
| M4 | Évaluation + interface web |
| M5 | Rédaction + soutenance |

#### Contraintes éthiques et IT

- Textes étudiants collectés avec consentement + anonymisation (suppression noms, promo, sujets identifiants).
- Les textes générés par IA sont clairement étiquetés et ne sont jamais présentés comme humains.
- Risque : faux positifs accusant un étudiant innocent → communiquer que l'outil est une aide, pas un verdict.

#### Plan B

Si l'accès à des mémoires réels est refusé, utiliser des textes académiques francophones en accès libre (HAL, theses.fr, articles Wikipedia) comme substitut pour la classe « humain ».

#### Questionnaire court

1. Avez-vous déjà utilisé un outil d'IA générative pour un travail académique ? *(Oui / Non / Partiellement)*
2. Pensez-vous qu'un enseignant peut distinguer un texte IA d'un texte humain ? *(Échelle 1–5)*
3. Êtes-vous favorable à un outil de détection IA dans votre université ? *(Échelle 1–5)*
4. Dans quel contexte l'usage de l'IA vous semble-t-il acceptable ? *(Choix multiples)*
5. [Post-test interface] L'outil était-il facile à utiliser ? *(Échelle 1–5)*
6. [Post-test interface] Faites-vous confiance au résultat affiché ? *(Échelle 1–5)*

#### Critères d'évaluation

| Critère | Poids | Indicateurs |
|---------|-------|-------------|
| Technique | 40 % | Qualité du feature engineering, code ML, pipeline |
| Expérimental | 30 % | Métriques (F1 ≥ 0.80 visé), analyse des erreurs |
| Livrables | 30 % | Corpus annoté, interface fonctionnelle, rapport |

#### Extensions possibles

- Fine-tuning d'un modèle BERT/CamemBERT pour la détection
- Extension au malgache académique
- Détection de textes partiellement générés (paragraphes mixtes)
- Plugin Moodle pour vérification automatique à la soumission

---

### Fiche 8 – Développer un chatbot d'orientation et d'assistance administrative pour les étudiants

**Domaine** : NLP / Développement web / Chatbot / IA conversationnelle

#### Problématique

Les étudiants malgaches perdent un temps considérable à chercher des informations administratives dispersées (procédures d'inscription, calendriers, contacts, règlements). Un chatbot intelligent capable de répondre en français (et optionnellement en malgache) réduirait la charge du personnel administratif et améliorerait l'expérience étudiante. Comment construire un assistant conversationnel fiable avec des ressources techniques limitées ?

#### Objectifs

1. Constituer une base de connaissances structurée (FAQ, procédures, contacts, calendriers) de ≥ 100 entrées.
2. Implémenter un moteur de recherche sémantique (TF-IDF ou embeddings) pour retrouver la réponse la plus pertinente.
3. Développer une interface de chat web responsive intégrée au site de l'université.
4. Optionnel : connecter le chatbot à WhatsApp via l'API Cloud WhatsApp Business.
5. Évaluer la qualité des réponses via un test utilisateur (≥ 30 participants, 10 questions types).

#### Méthodologie détaillée

| Étape | Description | Outils / Technologies |
|-------|------------|----------------------|
| 1. Collecte de la base de connaissances (3 sem.) | Recueil auprès des services (scolarité, examens, stages), structuration JSON/CSV | Entretiens, documents officiels |
| 2. Moteur de recherche | TF-IDF (léger, sans API) ou embeddings Sentence-BERT | scikit-learn ou `sentence-transformers` |
| 3. Backend chatbot | API REST servant les réponses, gestion du contexte conversationnel | Python/Flask ou Node.js/Express |
| 4. Interface web | Widget de chat responsive, intégrable en iframe | React ou Vue.js |
| 5. Intégration WhatsApp (optionnel) | Webhook + API Cloud WhatsApp Business | Node.js, Meta Cloud API |
| 6. Test utilisateur | 30 participants, 10 questions types, mesure de satisfaction | Questionnaire post-test |
| 7. Rédaction | Rapport + analyse des performances du chatbot | — |

#### Schéma de jeu de données (CSV)

| Colonne | Type | Exemple |
|---------|------|---------|
| `entry_id` | INT | `1` |
| `question` | TEXT | `Comment s'inscrire en L1 ?` |
| `answer` | TEXT | `Pour vous inscrire en L1, il faut...` |
| `category` | TEXT | `inscription` &#124; `examen` &#124; `stage` &#124; `calendrier` |
| `language` | TEXT | `fr` &#124; `mg` |
| `source_doc` | TEXT | `reglement_interieur_2025.pdf` |
| `last_updated` | DATE | `2025-09-01` |

#### Taille minimale d'échantillon

≥ 100 paires question-réponse dans la base de connaissances. ≥ 30 participants pour le test utilisateur.

#### Livrables attendus

- Code source (dépôt Git) avec documentation
- Base de connaissances structurée (JSON/CSV, 100+ entrées)
- Chatbot web fonctionnel et déployable
- Rapport (20–30 pages) avec évaluation
- Présentation (15 diapositives)

#### Calendrier indicatif

| Mois | Activités |
|------|-----------|
| M1 | Collecte base de connaissances + structuration |
| M2 | Moteur de recherche sémantique + backend |
| M3 | Interface web + intégration |
| M4 | Tests utilisateurs (30 participants) |
| M5 | Analyse + rédaction + soutenance |

#### Contraintes éthiques et IT

- Aucune donnée personnelle collectée via le chatbot (pas de login requis pour poser une question).
- Logs de conversation anonymisés (pas d'IP, pas d'identifiant).
- Consentement uniquement pour le test utilisateur.
- Risque : réponses incorrectes → disclaimer + renvoi vers le service compétent en cas de doute.

#### Plan B

Si l'accès aux documents officiels est limité, constituer la base à partir des informations publiques du site web de l'université + entretiens avec des étudiants expérimentés.

#### Questionnaire court

1. Où cherchez-vous habituellement les informations administratives ? *(Site web / Secrétariat / Camarades / Réseaux sociaux)*
2. Combien de temps passez-vous en moyenne pour obtenir une réponse administrative ? *(< 30 min / 30 min–2h / > 2h)*
3. [Post-test] Le chatbot a-t-il répondu correctement à vos questions ? *(Échelle 1–5)*
4. [Post-test] L'interface était-elle intuitive ? *(Échelle 1–5)*
5. [Post-test] Utiliseriez-vous ce chatbot au quotidien ? *(Oui / Non / Peut-être)*
6. Quelles catégories d'information vous manquent le plus ? *(Choix multiples)*

#### Critères d'évaluation

| Critère | Poids | Indicateurs |
|---------|-------|-------------|
| Technique | 40 % | Qualité du moteur NLP, architecture, code propre |
| Expérimental | 30 % | Taux de réponses correctes, satisfaction utilisateur |
| Livrables | 30 % | Base de connaissances, chatbot fonctionnel, rapport |

#### Extensions possibles

- Intégration d'un LLM local (Mistral, LLaMA) pour des réponses génératives
- Support multilingue complet (français + malgache)
- Apprentissage continu à partir des questions non résolues
- Intégration vocale (speech-to-text pour accessibilité)

---

### Fiche 9 – Mettre en place un système de vote électronique sécurisé pour les élections universitaires

**Domaine** : Sécurité / Cryptographie / Développement web

#### Problématique

Les élections universitaires (délégués, conseil d'administration, associations) reposent sur des bulletins papier : coûteux en logistique, lents à dépouiller et vulnérables aux contestations. Un système de vote électronique doit garantir simultanément l'authenticité du votant, le secret du vote et l'intégrité du décompte. Comment concilier ces exigences avec une solution techniquement réalisable par un étudiant L3 ?

#### Objectifs

1. Concevoir un protocole de vote garantissant : authentification, anonymat du bulletin, intégrité du résultat.
2. Développer une application web avec authentification sécurisée (token ou code unique).
3. Implémenter un mécanisme de vérifiabilité individuelle (le votant peut vérifier que son vote a été compté).
4. Réaliser un audit de sécurité basique (tests d'injection, rejeu, double vote).
5. Tester avec un scrutin simulé de ≥ 50 votants.

#### Méthodologie détaillée

| Étape | Description | Outils / Technologies |
|-------|------------|----------------------|
| 1. État de l'art (2 sem.) | Protocoles de vote électronique (Helios, ElectionGuard, mix-nets) | Littérature cryptographique |
| 2. Conception protocole | Schéma : génération de tokens uniques, chiffrement du bulletin, décompte vérifiable | Diagrammes de séquence |
| 3. Backend | API REST avec gestion des scrutins, authentification, stockage chiffré | Laravel ou Django, PostgreSQL |
| 4. Frontend | Interface de vote responsive + page de résultats temps réel | React ou Vue.js |
| 5. Sécurité | Tests d'injection SQL, XSS, CSRF, double vote, rejeu de token | OWASP ZAP, tests manuels |
| 6. Scrutin simulé | 50 votants, 3 candidats, 2 scrutins (uninominal + liste) | Recrutement volontaires |
| 7. Rédaction | Rapport + analyse de sécurité | — |

#### Schéma de jeu de données (CSV)

| Colonne | Type | Exemple |
|---------|------|---------|
| `vote_id` | INT | `1` |
| `scrutin_id` | INT | `1` |
| `token_hash` | TEXT (SHA-256) | `f7a2c...d89` |
| `candidat_id` | INT | `3` |
| `timestamp` | DATETIME | `2025-11-15T10:30:00` |
| `ip_anonymized` | TEXT | `[supprimé]` |
| `is_verified` | BOOLEAN | `true` |

#### Taille minimale d'échantillon

≥ 50 votants × 2 scrutins = **100 bulletins** minimum.

#### Livrables attendus

- Code source (dépôt Git) avec documentation de sécurité
- Application de vote déployable (Docker)
- Rapport d'audit de sécurité (tests effectués + résultats)
- Jeu de données du scrutin simulé (CSV, 100+ bulletins)
- Rapport technique (20–30 pages)
- Présentation (15 diapositives)

#### Calendrier indicatif

| Mois | Activités |
|------|-----------|
| M1 | État de l'art + conception du protocole |
| M2 | Développement backend + authentification |
| M3 | Frontend + mécanisme de vérifiabilité |
| M4 | Tests de sécurité + scrutin simulé (50 votants) |
| M5 | Analyse + rédaction rapport |
| M6 | Finalisation + soutenance |

#### Contraintes éthiques et IT

- **Secret du vote** : aucun lien stocké entre l'identité du votant et son bulletin.
- Tokens à usage unique, non réutilisables.
- Hébergement sur serveur sécurisé (HTTPS obligatoire).
- Risque : contestation des résultats → vérifiabilité individuelle + logs d'audit.

#### Plan B

Si le recrutement de 50 votants réels est impossible, simuler les votes avec des scripts automatisés tout en gardant 10–15 testeurs réels pour l'évaluation UX.

#### Questionnaire court

1. Avez-vous déjà voté lors d'une élection universitaire ? *(Oui / Non)*
2. Faites-vous confiance au processus de dépouillement actuel ? *(Échelle 1–5)*
3. Seriez-vous favorable au vote électronique pour les élections universitaires ? *(Échelle 1–5)*
4. [Post-test] Le processus de vote en ligne était-il clair ? *(Échelle 1–5)*
5. [Post-test] Avez-vous pu vérifier que votre vote a été compté ? *(Oui / Non)*
6. [Post-test] Recommanderiez-vous ce système ? *(Échelle 1–5)*

#### Critères d'évaluation

| Critère | Poids | Indicateurs |
|---------|-------|-------------|
| Technique | 40 % | Protocole cryptographique, qualité du code, tests de sécurité |
| Expérimental | 30 % | Scrutin simulé réussi, résultats d'audit, feedback votants |
| Livrables | 30 % | Documentation sécurité, rapport, application fonctionnelle |

#### Extensions possibles

- Chiffrement homomorphe pour décompte sans déchiffrement individuel
- Support mobile natif (React Native)
- Intégration avec l'annuaire LDAP de l'université
- Étude comparative avec les systèmes de vote utilisés dans d'autres universités

---

### Fiche 10 – Construire un tableau de bord décisionnel pour le pilotage pédagogique d'un département

**Domaine** : Business Intelligence / Data visualization / Systèmes d'information

#### Problématique

Les responsables de départements universitaires manquent d'indicateurs synthétiques pour piloter la performance pédagogique : taux de réussite, répartition des notes, charge enseignante, évolution des effectifs. Les données existent souvent dans des tableurs dispersés mais ne sont ni centralisées ni visualisées. Comment agréger ces sources hétérogènes dans un tableau de bord interactif et actualisable ?

#### Objectifs

1. Identifier et formaliser les indicateurs clés de performance pédagogique (KPI) d'un département.
2. Concevoir un pipeline ETL (Extract, Transform, Load) pour agréger les données depuis des sources hétérogènes (CSV, Excel, base de données).
3. Développer un tableau de bord web interactif avec filtres dynamiques (par année, matière, promotion).
4. Implémenter au moins 6 visualisations : taux de réussite, distribution des notes, évolution effectifs, charge enseignante, répartition CM/TD/TP, alertes.
5. Tester avec des données couvrant 3 années académiques (réelles anonymisées ou simulées).

#### Méthodologie détaillée

| Étape | Description | Outils / Technologies |
|-------|------------|----------------------|
| 1. Recueil des besoins (2 sem.) | Entretiens avec le chef de département, 3 enseignants, la scolarité | Guide d'entretien |
| 2. Identification des KPI | Formalisation des indicateurs : taux de réussite, moyenne, médiane, écart-type, charge, effectifs | Benchmark littérature |
| 3. Pipeline ETL | Extraction des données sources, nettoyage, transformation, chargement | Python (pandas), SQL |
| 4. Base de données analytique | Modèle en étoile (fait + dimensions) | PostgreSQL ou SQLite |
| 5. Dashboard | Interface web interactive avec filtres et drill-down | React + Recharts / D3.js, ou Metabase (open source) |
| 6. Tests | Validation des calculs avec données réelles sur 3 ans | Comparaison avec calculs manuels |
| 7. Rédaction | Rapport + guide utilisateur du dashboard | — |

#### Schéma de jeu de données (CSV)

| Colonne | Type | Exemple |
|---------|------|---------|
| `etudiant_hash` | TEXT | `d4a1f...c82` |
| `annee_academique` | TEXT | `2024-2025` |
| `niveau` | TEXT | `L1` &#124; `L2` &#124; `L3` |
| `matiere_code` | TEXT | `INF101` |
| `note_finale` | FLOAT | `13.5` |
| `statut` | TEXT | `admis` &#124; `ajourné` &#124; `abandon` |
| `enseignant_hash` | TEXT | `e7b3d...f91` |
| `type_heure` | TEXT | `CM` &#124; `TD` &#124; `TP` |
| `nb_heures` | FLOAT | `30` |

#### Taille minimale d'échantillon

3 années × 100 étudiants × 8 matières = **2 400 enregistrements** minimum (simulés si nécessaire).

#### Livrables attendus

- Code source (dépôt Git) : pipeline ETL + dashboard
- Base de données analytique peuplée
- Dashboard web fonctionnel avec 6+ visualisations
- Jeu de données (CSV, 2 400+ lignes)
- Rapport technique (20–30 pages) avec guide utilisateur
- Présentation (15 diapositives)

#### Calendrier indicatif

| Mois | Activités |
|------|-----------|
| M1 | Recueil besoins + identification KPI + modèle de données |
| M2 | Pipeline ETL + base analytique |
| M3 | Développement dashboard (6 visualisations) |
| M4 | Tests + validation calculs |
| M5 | Rédaction + guide utilisateur |
| M6 | Finalisation + soutenance |

#### Contraintes éthiques et IT

- Données de notes = données sensibles : anonymisation obligatoire (hachage identifiants).
- Accès restreint par rôle (seul le chef de département et les enseignants concernés).
- Autorisation du département requise pour données réelles.
- Risque : mauvaise interprétation des KPI → former les utilisateurs, documenter les limites.

#### Plan B

Générer 3 années de données académiques fictives avec des distributions réalistes (moyenne 10–12, écart-type 3–4, taux de réussite 50–70 %) via script Python + numpy.

#### Questionnaire court

1. Disposez-vous actuellement d'indicateurs de performance pédagogique ? *(Oui / Partiellement / Non)*
2. Sous quel format sont stockées vos données de notes ? *(Excel / Base de données / Papier / Mixte)*
3. Quels indicateurs jugez-vous les plus importants ? *(Choix multiples : taux réussite, moyenne, effectifs, charge, abandon)*
4. Consulteriez-vous un tableau de bord régulièrement ? *(Échelle 1–5)*
5. Quels filtres vous seraient utiles ? *(Par année / Par matière / Par niveau / Par enseignant)*
6. Souhaitez-vous des alertes automatiques (ex : taux de réussite < 30 %) ? *(Oui / Non)*

#### Critères d'évaluation

| Critère | Poids | Indicateurs |
|---------|-------|-------------|
| Technique | 40 % | Pipeline ETL, modèle de données, qualité du code, visualisations |
| Expérimental | 30 % | Exactitude des KPI, validation sur 3 ans, pertinence des indicateurs |
| Livrables | 30 % | Dashboard fonctionnel, guide utilisateur, rapport |

#### Extensions possibles

- Prédiction du taux de réussite par machine learning (régression)
- Intégration temps réel avec le SI de scolarité
- Extension multi-départements avec vue comparative
- Application mobile pour consultation rapide des KPI

---

## Versions condensées

> **Fiche 1** – Prototype web (Flask/Node) générant un hash SHA-256 unique par diplôme, stocké en base, avec vérification publique par QR code. Sécurisation documentaire dans la transformation numérique.

> **Fiche 2** – Application mobile enregistrant la présence étudiante via QR code dynamique, avec dashboard temps réel (taux d'absentéisme, alertes). Amélioration du suivi pédagogique par le numérique.

> **Fiche 3** – Module IA (filtrage collaboratif + contenu) recommandant cours, documents et exercices adaptés au profil étudiant. Personnalisation pédagogique via la transformation numérique.

> **Fiche 4** – Plateforme web (Laravel/Django) de signalement anonyme des dysfonctionnements universitaires, avec modération et tableau de bord statistique. Transparence et gouvernance administrative.

> **Fiche 5** – Application web centralisant le suivi des heures d'enseignement avec calcul automatique, validation hiérarchique, alertes et exports PDF/Excel. Optimisation RH enseignante.

> **Fiche 6** – Analyse de logs de processus administratifs via PM4Py pour découvrir les parcours réels, identifier les goulots d'étranglement et détecter les déviations. Optimisation par le numérique.

> **Fiche 7** – Classificateur binaire (humain vs IA) entraîné sur un corpus de textes académiques francophones, avec interface web de détection. Intégrité académique face aux LLM.

> **Fiche 8** – Chatbot conversationnel (TF-IDF/embeddings) répondant aux questions administratives courantes des étudiants, intégré au site web et optionnellement à WhatsApp.

> **Fiche 9** – Système de vote électronique web avec authentification par token, secret du bulletin, vérifiabilité individuelle et audit de sécurité. Modernisation de la gouvernance.

> **Fiche 10** – Tableau de bord décisionnel agrégeant les données pédagogiques (notes, effectifs, charge) via pipeline ETL, avec visualisations interactives et filtres dynamiques.

---

## Annexes

### A. Modèle de consentement éclairé

> **À imprimer et faire signer par chaque participant.**

---

**FORMULAIRE DE CONSENTEMENT ÉCLAIRÉ**

**Titre du projet** : *[Insérer le titre du sujet]*  
**Responsable** : *[Nom de l'étudiant]*, sous la supervision de M. BEZARA Roussel Florent, Université de Mahajanga.

Je soussigné(e) ________________________________, accepte de participer volontairement à cette étude dans le cadre d'un projet de fin d'études en Licence 3 Génie Informatique.

J'ai été informé(e) que :

- Mes données seront **anonymisées** (hachage cryptographique, suppression des identifiants directs) avant toute analyse ou publication.
- Les données collectées pourront être **réutilisées**, sous forme anonymisée, dans des travaux académiques ultérieurs (mémoires, thèses, publications) liés à la transformation numérique universitaire, pendant une durée maximale de **5 ans** après la collecte *(voir clause détaillée en annexe B)*.
- Les **données brutes** seront conservées pendant **1 an** après la soutenance, puis détruites.
- Je peux me **retirer à tout moment** sans justification ; mes données seront supprimées sous 7 jours.
- **Aucune donnée nominative** ne sera publiée ou transmise à des tiers.

| | |
|---|---|
| Date : ___/___/______ | Signature du participant : ____________________ |
| Date : ___/___/______ | Signature du responsable : ____________________ |

---

### B. Clause de réutilisation des données

> **Texte à insérer dans le formulaire de consentement ou à joindre en annexe.**

*« J'accepte que les données collectées dans le cadre de cette étude, une fois anonymisées de manière irréversible (hachage cryptographique des identifiants, suppression des informations directement identifiantes), puissent être réutilisées dans des travaux académiques ultérieurs (mémoires de Master, thèses de doctorat, publications scientifiques) portant sur la transformation numérique et la gestion pédagogique universitaire, pour une durée maximale de cinq (5) ans à compter de la date de collecte. Passé ce délai, les données anonymisées seront définitivement supprimées. »*

---

### C. Script Python d'anonymisation

> **Fichier : `anonymize.py`** – Prêt à utiliser. Hachage SHA-256 salé, suppression IP, agrégation dates.

```python
#!/usr/bin/env python3
"""Script d'anonymisation des données étudiantes / administratives.
Usage : python anonymize.py input.csv output.csv

Fonctionnalités :
- Hachage SHA-256 salé des colonnes identifiantes
- Suppression des colonnes sensibles (IP, MAC, adresse)
- Agrégation des dates de naissance (année uniquement)

Auteur : Projet L3 Génie Informatique – Université de Mahajanga
"""
import csv
import hashlib
import sys
import os
import secrets

# ──── Configuration ────
SALT = os.environ.get("ANON_SALT", secrets.token_hex(16))
COLS_TO_HASH = ["nom", "prenom", "email", "matricule", "telephone"]
COLS_TO_DROP = ["adresse_ip", "adresse_mac", "adresse_postale"]
COLS_DATE_AGGREGATE = ["date_naissance"]  # -> annee_naissance


def sha256_salted(value: str) -> str:
    """Retourne un hash SHA-256 salé tronqué à 16 caractères."""
    return hashlib.sha256(
        (SALT + str(value).strip().lower()).encode("utf-8")
    ).hexdigest()[:16]


def aggregate_date(date_str: str) -> str:
    """Réduit une date ISO à l'année uniquement."""
    try:
        return date_str.strip()[:4]
    except Exception:
        return "XXXX"


def anonymize_row(row: dict) -> dict:
    """Anonymise une ligne du CSV."""
    out = {}
    for col, val in row.items():
        col_lower = col.lower().strip()
        if col_lower in [c.lower() for c in COLS_TO_DROP]:
            continue
        elif col_lower in [c.lower() for c in COLS_TO_HASH]:
            out[col + "_hash"] = sha256_salted(val)
        elif col_lower in [c.lower() for c in COLS_DATE_AGGREGATE]:
            out["annee_" + col.replace("date_", "")] = aggregate_date(val)
        else:
            out[col] = val
    return out


def main():
    if len(sys.argv) < 3:
        print(f"Usage: python {sys.argv[0]} input.csv output.csv")
        print("  Variables d'environnement :")
        print("    ANON_SALT : sel personnalisé (défaut : généré aléatoirement)")
        sys.exit(1)

    infile, outfile = sys.argv[1], sys.argv[2]

    print(f"[*] Fichier source     : {infile}")
    print(f"[*] Fichier sortie     : {outfile}")
    print(f"[*] Salt utilisé       : {SALT}")
    print(f"[*] Colonnes hachées   : {COLS_TO_HASH}")
    print(f"[*] Colonnes supprimées: {COLS_TO_DROP}")
    print(f"[*] Dates agrégées     : {COLS_DATE_AGGREGATE}")
    print()

    with open(infile, "r", encoding="utf-8") as fin:
        reader = csv.DictReader(fin)
        rows = [anonymize_row(r) for r in reader]

    if not rows:
        print("[!] Aucune donnée trouvée.")
        return

    with open(outfile, "w", encoding="utf-8", newline="") as fout:
        writer = csv.DictWriter(fout, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)

    print(f"[+] {len(rows)} lignes anonymisées → {outfile}")
    print("[*] IMPORTANT : conservez le sel séparément :")
    print(f"    echo '{SALT}' > salt.key && chmod 600 salt.key")


if __name__ == "__main__":
    main()
```

**Utilisation** :

```bash
# Générer un sel fixe (recommandé pour reproductibilité au sein d'un projet)
export ANON_SALT="mon_sel_secret_2025"

# Anonymiser
python anonymize.py donnees_brutes.csv donnees_anonymisees.csv

# Conserver le sel en sécurité
echo "$ANON_SALT" > salt.key && chmod 600 salt.key
```

---

### D. Schéma CSV standardisé

> **Format obligatoire pour la remise des jeux de données.**

| Colonne | Type | Format / Exemple | Obligatoire |
|---------|------|-----------------|-------------|
| `record_id` | INT | Auto-incrémenté (1, 2, 3...) | Oui |
| `project_code` | TEXT | `FICHE1` &#124; `FICHE2` &#124; ... &#124; `FICHE10` | Oui |
| `user_hash` | TEXT (16 car.) | `a3f8c2e1b7d9f031` | Oui |
| `timestamp` | DATETIME ISO | `2025-09-15T10:22:00` | Oui |
| `category` | TEXT | Libre selon le projet | Oui |
| `value_numeric` | FLOAT | `4.5` | Si applicable |
| `value_text` | TEXT | Max 500 caractères | Si applicable |
| `source` | TEXT | `reel` &#124; `simule` &#124; `mixte` | Oui |
| `notes` | TEXT | Commentaire libre | Non |

**Règles** :
- Encodage : **UTF-8 sans BOM**
- Séparateur : **virgule** (`,`)
- Dates : **ISO 8601** (`YYYY-MM-DDTHH:MM:SS`)
- Décimales : **point** (`.`)
- Texte contenant des virgules : entre **guillemets doubles** (`"texte, avec virgule"`)

---

### E. Checklist technique d'anonymisation

| # | Étape | Description | Exemple |
|---|-------|-------------|---------|
| 1 | ☐ Hachage des identifiants | SHA-256 salé sur : nom, prénom, email, matricule, téléphone | `BEZARA Florent` → `a3f8c2e1b7d9f031` |
| 2 | ☐ Suppression des champs sensibles | Retirer : adresse IP, MAC, adresse postale | `192.168.1.45` → `[supprimé]` |
| 3 | ☐ Agrégation des dates | Dates de naissance → année uniquement | `1998-03-15` → `1998` |
| 4 | ☐ Généralisation géographique | Adresses précises → région/ville | `Lot 42 Mahabibo` → `Mahajanga` |
| 5 | ☐ Vérification croisée | Aucune combinaison de champs ne permet la ré-identification | Grade + matière + année → vérifier unicité |
| 6 | ☐ Test de réversibilité | Tenter de retrouver une identité depuis le fichier anonymisé | Doit échouer |
| 7 | ☐ Stockage du sel | Fichier séparé, protégé par mot de passe | `salt.key` (chmod 600) |
| 8 | ☐ Documentation | Procédure consignée dans la section « Anonymisation » du rapport | Section méthodologie |

---

### F. Message de recrutement

> **À diffuser par email, groupe WhatsApp ou affichage.**

---

Bonjour,

Dans le cadre d'un projet de recherche en **Licence 3 Génie Informatique** à l'Université de Mahajanga, nous recherchons des **volontaires** (étudiants ou personnels) pour participer à un test utilisateur ou répondre à un court questionnaire (**5–10 minutes**). Votre participation est **anonyme** et **volontaire**. Les résultats contribueront à améliorer les outils numériques de gestion pédagogique et administrative de notre université.

Pour participer ou en savoir plus, contactez : **[Nom]** à **[email / téléphone]**.

Merci !

---

## Licence

Ce document est diffusé sous licence [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). Vous êtes libre de le partager et de l'adapter à condition de créditer l'auteur et de partager sous les mêmes conditions.

---

*Document généré par M. BEZARA Roussel Florent – Mars 2026*
