import subprocess

def deploy_docker_swarm_service(service_name, image_name):
    try:
        # Vérifie si le service existe déjà
        existing_service = subprocess.run(["docker", "service", "inspect", service_name], capture_output=True, text=True)

        if existing_service.returncode == 0:
            # Mise à jour du service si il existe
            print(f"Mise à jour du service {service_name} avec l'image {image_name}")
            subprocess.run(["docker", "service", "update", "--image", image_name, service_name])
        else:
            # Création du service si il n'existe pas
            print(f"Création d'un nouveau service {service_name} avec l'image {image_name}")
            subprocess.run(["docker", "service", "create", "--name", service_name, image_name])
    except Exception as e:
        print(f"Erreur lors du déploiement : {e}")

# Exemple d'utilisation
deploy_docker_swarm_service("mon-service", "mon-image:latest")
