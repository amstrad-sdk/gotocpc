#!/bin/sh


PROJECT="gotocpc"
FECHA=$(date '+%Y-%m-%d %H:%M:%S')
rojo='\033[0;31m'
reset_color='\033[0m'

generateChanges() {
    carpeta="VERSIONS"
    archivo_concatenado="CHANGES"
    if [ -e "CHANGES" ]; then
        rm CHANGES
    fi
    if [[ "$OSTYPE" == "linux-gnu" ]]; then
        archivos=$(find "$carpeta" -type f -exec ls -t -p "{}" + | awk '{print $NF}')
    elif [[ "$OSTYPE" == "darwin"* ]]; then
        archivos=$(find "$carpeta" -type f -exec ls -t -p "{}" + | awk '{print $NF}')
    else
        echo "Sistema operativo no compatible"
        exit 1
    fi
    for archivo in $archivos; do
        cat "$archivo" >> "$archivo_concatenado"
    done
    echo "Archivos concatenados en $archivo_concatenado\n"
}

echo ""
echo "================================================================================================"
echo "[*] BORRADO DE TEMPORALES"
echo "================================================================================================"
echo ""

    directorio_a_eliminar="dist"
    if [ -d "$directorio_a_eliminar" ]; then
        rm -r "$directorio_a_eliminar"
        echo "Directorio eliminado: $directorio_a_eliminar"
    else
        echo "El directorio no existe: $directorio_a_eliminar"
    fi
    directorio_a_eliminar="$PROJECT.egg-info"
    if [ -d "$directorio_a_eliminar" ]; then
        rm -r "$directorio_a_eliminar"
        echo "Directorio eliminado: $directorio_a_eliminar"
    else
        echo "El directorio no existe: $directorio_a_eliminar"
    fi
    directorio_a_eliminar="$PROJECT/__pycache__"
    if [ -d "$directorio_a_eliminar" ]; then
        echo "Directorio eliminado: $directorio_a_eliminar"
    else
        echo "El directorio no existe: $directorio_a_eliminar"
    fi

echo ""
echo "================================================================================================"
echo "[*] INSTALACION DE DEPENDENCIAS"
echo "================================================================================================"
echo ""
pip install build
pip install --upgrade twine
echo ""
echo "================================================================================================"
echo  "[*] HISTORIAL DE CAMBIOS"
echo "================================================================================================"
echo ""
if [ -z "$1" ]
then
    generateChanges
    CHANGES=`cat CHANGES`
    echo "$CHANGES"
    echo ""
    archivo="$PROJECT/__init__.py"
    version=$(grep -o "__version__ = '[0-9]\+\.[0-9]\+\.[0-9]\+'" "$archivo")
    version=$(echo "$version" | sed "s/__version__ = '//;s/'//")
    echo "================================================================================================"
    echo  "[*] NO PASAMOS VERSION. COMPILAMOS CON LA ACTUAL $version"
    echo "================================================================================================"
    echo ""
else
    version=$1
    version_a_verificar="VERSIONS/$version"
    if [ -e "$version_a_verificar" ]; then
        echo "El archivo $version_a_verificar existe."
        echo ""
    else
        echo "${rojo}ERROR: El archivo $version_a_verificar no existe.${reset_color}"
        exit
    fi
    echo "__version__ = '$version'" > "$PROJECT/__init__.py"
    echo "================================================================================================"
    echo "[*] COMPILAMOS SOFTWARE CON NUEVA VERSION $1"
    echo "================================================================================================"
    echo ""
   
fi

python3 -m build

echo ""
echo "================================================================================================"
echo "[*] CHEQUEAMOS FORMATE README.md"
echo "================================================================================================"
echo ""
twine check dist/*

if [ -z "$1" ]
then
    echo ""
else
    echo ""
    echo "================================================================================================"
    echo "[*] CREAMOS TAG $1 Y PUBLICAMOS EN GITHUB"
    echo "================================================================================================"
    echo ""
    git add .
    git commit -m "Generate Tag"
    git push
    git tag $version -m "$CHANGES"
    git push origin $version
fi


echo ""
echo "================================================================================================"
echo "[*] COMPILACION FINALIZADA $version"
echo "================================================================================================"
echo ""