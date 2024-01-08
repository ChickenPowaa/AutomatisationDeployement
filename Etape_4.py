import subprocess

def create_docker_image(image_name):
    """
    Cree une image docker
    """    
    subprocess.run(["docker", "build", "-t", image_name, "."])