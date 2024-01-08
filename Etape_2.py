import subprocess

def compile_project():
    """
    Compile le Projet
    """
    subprocess.run(["npm", "install"])  # Installe les dépendances
    subprocess.run(["npm", "run", "build"])  # Compile le projet