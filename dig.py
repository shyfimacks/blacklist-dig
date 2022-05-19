#!/usr/bin/env python3

"""
Script que faz dig nas linhas dos arquivos "domains" dentro dos diretorios
e escreve os IPs dos dominios
"""

import os
import subprocess

dirs = os.listdir()

# Exemplo de como executar apenas algumas pastas:
#dirs = ["dating"]  


for d in dirs:

    if os.path.isfile(d):
        continue
    if d == ".git":
        continue

    resfile = open('result-'+d, 'w')
    resarr = []

    file = open(d + "/domains")
    lines = file.readlines()
    
    for line in lines:
        print(line)
        result = subprocess.getoutput("dig +short +answer " + line)
        if result:
            resarr.append(result + "\n")

    resfile.writelines(resarr)
    resfile.close()
