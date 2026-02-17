import subprocess
import sys

def instalar_pygame():
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pygame"])

try:
    import pygame
    print("Pygame OK")
except ImportError:
    print("Pygame não encontrado. Instalando...")
    instalar_pygame()
