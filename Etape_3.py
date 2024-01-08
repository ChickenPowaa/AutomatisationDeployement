import subprocess

def run_sonarqube_analysis():
    """
    Run SonarQube ---> Besoin d'avoir configuré sonarqube
    """    
    subprocess.run(["sonar-scanner"])