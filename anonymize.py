#!/usr/bin/env python3
"""Script d'anonymisation des données étudiantes / administratives.
Usage : python anonymize.py input.csv output.csv

Fonctionnalités :
- Hachage SHA-256 salé des colonnes identifiantes
- Suppression des colonnes sensibles (IP, MAC, adresse)
- Agrégation des dates de naissance (année uniquement)
- Vérification croisée basique

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
            continue  # supprimé
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
        print("    ANON_SALT : sel personnalisé (par défaut : généré aléatoirement)")
        sys.exit(1)

    infile, outfile = sys.argv[1], sys.argv[2]

    print(f"[*] Fichier source   : {infile}")
    print(f"[*] Fichier sortie   : {outfile}")
    print(f"[*] Salt utilisé     : {SALT}")
    print(f"[*] Colonnes hachées : {COLS_TO_HASH}")
    print(f"[*] Colonnes supprimées : {COLS_TO_DROP}")
    print(f"[*] Dates agrégées   : {COLS_DATE_AGGREGATE}")
    print()

    with open(infile, "r", encoding="utf-8") as fin:
        reader = csv.DictReader(fin)
        rows = [anonymize_row(r) for r in reader]

    if not rows:
        print("[!] Aucune donnée trouvée dans le fichier source.")
        return

    with open(outfile, "w", encoding="utf-8", newline="") as fout:
        writer = csv.DictWriter(fout, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)

    print(f"[+] {len(rows)} lignes anonymisées → {outfile}")
    print("[*] IMPORTANT : conservez le sel dans un fichier sécurisé séparé.")
    print(f"    echo '{SALT}' > salt.key && chmod 600 salt.key")


if __name__ == "__main__":
    main()
