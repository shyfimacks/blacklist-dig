#!/usr/bin/env python3

"""
Script que faz dig nas linhas dos arquivos "domains" dentro dos diretorios
e escreve os IPs dos dominios
"""

import threading
import os
import subprocess

threads = []
resfile = None

dirs = os.listdir()

# Exemplo de como executar apenas algumas pastas:
#dirs = ["dating"]  

def parse_dig(domain):
    print('Parsing ' + domain)
    result = subprocess.getoutput("dig +short +answer " + domain)
    if result:
        resfile.write(result + "\n")

for d in dirs:

    if os.path.isfile(d):
        continue
    if d == ".git":
        continue

    file = open(d + "/domains")
    lines = file.readlines()
    resfile = open('result-'+d, 'w')
    
    for line in lines:
        thread = threading.Thread(target=parse_dig, args=[line])
        thread.start()
        thread.name = line
        threads.append(thread)

for thread in threads:
    thread.join()

resfile.close()
