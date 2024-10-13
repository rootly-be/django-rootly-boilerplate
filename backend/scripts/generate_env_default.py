import os
from pathlib import Path

def generate_env_default():
    # Obtenir le chemin du répertoire parent (là où se trouve manage.py et .env)
    base_dir = Path(__file__).resolve().parent.parent

    # Chemin vers le fichier .env (un niveau au-dessus de scripts/)
    env_file = base_dir / '.env'

    # Chemin vers le fichier .env.default (un niveau au-dessus de scripts/)
    env_default_file = base_dir / '.env.default'

    # Lire le fichier .env et créer le .env.default sans les valeurs
    with open(env_file, 'r') as env, open(env_default_file, 'w') as env_default:
        for line in env:
            if '=' in line and not line.startswith('#'):
                key = line.split('=')[0].strip()
                env_default.write(f"{key}=\n")
            else:
                env_default.write(line)  # Garder les commentaires et les lignes vides

if __name__ == "__main__":
    generate_env_default()
