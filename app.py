import subprocess
import sys


pip_freeze = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze'])
installed_packs = ([r.decode().split('==')[0] for r in pip_freeze.split()])
with open('requirements.txt', 'r') as req:
    packs = req.readlines()
    for pack in packs:
        if pack not in installed_packs:
            subprocess.check_call(
                [sys.executable, '-m', 'pip', 'install', pack])

from cryptography.fernet import Fernet