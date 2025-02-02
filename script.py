#!/usr/bin/env python3
import os
import sys
import re


def normalize(filename):
    """
    Extrait le nom du mod sans la version.
    Exemple:
      "AwesomeMod-1.2.3.jar" → "awesomemod"
      "Cool_Mod_2.0.jar"  → "cool_mod"
    """
    name, _ = os.path.splitext(filename)
    # Cherche un pattern de version à la fin, précédé éventuellement d'un '-' ou '_'
    m = re.match(r"^(.*?)[-_]?(\d+(?:\.\d+)*)?$", name)
    if m:
        return m.group(1).lower()
    return name.lower()


def list_normalized_files(folder):
    """
    Retourne un dictionnaire:
      clé   : nom normalisé
      valeur: liste des fichiers originaux correspondants
    """
    files_dict = {}
    try:
        for f in os.listdir(folder):
            full_path = os.path.join(folder, f)
            if os.path.isfile(full_path):
                norm = normalize(f)
                files_dict.setdefault(norm, []).append(f)
    except FileNotFoundError:
        print(f"Le dossier '{folder}' n'existe pas.")
        sys.exit(1)
    return files_dict


def main():
    if len(sys.argv) != 3:
        print("Usage: python script.py <folder1> <folder2>")
        sys.exit(1)

    folder1, folder2 = sys.argv[1], sys.argv[2]

    files1 = list_normalized_files(folder1)
    files2 = list_normalized_files(folder2)

    set1 = set(files1.keys())
    set2 = set(files2.keys())

    only_in_1 = set1 - set2
    only_in_2 = set2 - set1

    if only_in_1:
        print("Fichiers présents uniquement dans le dossier 1:")
        for key in sorted(only_in_1):
            originals = ", ".join(files1[key])
            print(f"  {originals}")
    else:
        print("Aucun fichier unique trouvé dans le dossier 1.")

    if only_in_2:
        print("\nFichiers présents uniquement dans le dossier 2:")
        for key in sorted(only_in_2):
            originals = ", ".join(files2[key])
            print(f"  {originals}")
    else:
        print("\nAucun fichier unique trouvé dans le dossier 2.")


if __name__ == "__main__":
    main()
