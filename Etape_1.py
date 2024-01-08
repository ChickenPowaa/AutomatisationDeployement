import subprocess
import os

def retrieve_code(repo_url, dest_folder):
    """
    Clone ou met à jour le code du dépôt git.

    param repo_url: URL du dépôt git.
    param dest_folder: Dossier de destination pour le clone ou la mise à jour.
    """

    if os.path.isdir(dest_folder):
        # Le dossier existe, donc on met à jour le code
        print(f"Mise à jour du code dans {dest_folder}")
        try:
            subprocess.run(["git", "-C", dest_folder, "pull", "origin", "master"])
        except Exception as e:
            print(f"Erreur lors de la mise à jour du code : {e}")
    else:
        # Le dossier n'existe pas, donc on clone le dépôt
        print(f"Clonage du dépôt {repo_url} dans {dest_folder}")
        try:
            subprocess.run(["git", "clone", repo_url, dest_folder])
        except Exception as e:
            print(f"Erreur lors du clonage du dépôt : {e}")

# Exemple d'utilisation
retrieve_code("https://github.com/theoernould/projet-rentree-front-forked", dest_folder)
