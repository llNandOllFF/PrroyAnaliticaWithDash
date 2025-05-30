import subprocess
import sys

def instalar_dependencias():
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])
        print("dependencias ha sido instalado correctamente.")
    except subprocess.CalledProcessError as e:
        print(f"Error al instalar dependencias: {e}")
        sys.exit(1)

def main():
    instalar_dependencias() # comentar esta metodo si se va a usar debug en True
    from app import iniciar_app
    iniciar_app()
    
if __name__ == '__main__':
    main()