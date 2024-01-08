import subprocess

def run_image(image_name):
    '''
    Image Deployment
    '''
    subprocess.run(["docker", "run", "-d", image_name])