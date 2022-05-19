#!/bin/bash

#script que baixa e extrai arquivos com blacklists do site com categorias desejadas




[ -z "$1" ] && echo "Uso: $0 nome da categoria" && exit 1

echo " http://dsi.ut-capitole.fr/blacklists/download/$1.tar.gz"

wget -c "http://dsi.ut-capitole.fr/blacklists/download/$1.tar.gz"
cat *.tar.gz | tar -xzvf - -i
rm -rf *.tar.gz
