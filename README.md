# 🎓 Sujets de Projets L3 – Génie Informatique & Transformation Numérique Universitaire

> Université de Mahajanga · Année 2025–2026 · Encadrant : M. BEZARA Roussel Florent

## 📖 Description

Ce dépôt contient **10 fiches de sujets de projets** prêtes à distribuer aux étudiants de Licence 3 Génie Informatique. Chaque sujet est purement technique (développement, IA, sécurité, analyse de données) tout en étant connecté à la problématique de la **gestion pédagogique et administrative face à la transformation numérique** dans les universités malgaches.

## 📂 Structure du dépôt

```
├── README.md                              ← Ce fichier
├── sujets-projets-L3-genie-informatique.md  ← Document principal (10 fiches + annexes)
└── anonymize.py                           ← Script Python d'anonymisation prêt à l'emploi
```

## 🗂️ Les 10 sujets

| # | Titre | Domaine |
|---|-------|---------|
| 1 | Certifier l'authenticité des diplômes via empreinte cryptographique | Sécurité / Crypto |
| 2 | Automatiser le pointage étudiant par QR code dynamique | Mobile / IoT |
| 3 | Construire un moteur de recommandation pédagogique par ML | IA / Machine Learning |
| 4 | Créer une plateforme de signalement anonyme des dysfonctionnements | Web / Gouvernance |
| 5 | Concevoir un système de suivi des heures d'enseignement | SI / Workflow |
| 6 | Analyser les processus administratifs par process mining | Data Science |
| 7 | Détecter les textes générés par IA dans les travaux académiques | NLP / Intégrité |
| 8 | Développer un chatbot d'assistance administrative | NLP / Chatbot |
| 9 | Mettre en place un vote électronique sécurisé | Sécurité / Crypto |
| 10 | Construire un tableau de bord décisionnel pédagogique | BI / Dashboard |

## 📎 Annexes incluses

- ✅ Modèle de consentement éclairé imprimable
- ✅ Clause de réutilisation des données
- ✅ Script Python d'anonymisation (SHA-256 salé)
- ✅ Schéma CSV standardisé pour la remise des données
- ✅ Checklist technique d'anonymisation
- ✅ Message de recrutement des participants

## 🔧 Utilisation du script d'anonymisation

```bash
# Installer Python 3.x (aucune dépendance externe)

# Avec sel aléatoire
python anonymize.py donnees_brutes.csv donnees_anonymisees.csv

# Avec sel fixe (reproductibilité)
export ANON_SALT="mon_sel_secret_2025"
python anonymize.py donnees_brutes.csv donnees_anonymisees.csv
```

## 📄 Licence

Ce document est diffusé sous licence [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).

---

*M. BEZARA Roussel Florent – Université de Mahajanga – 2026*
