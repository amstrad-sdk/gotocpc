#!/bin/sh

CHANGES=`cat CHANGES`
PROJECT="gotocpc"
FECHA=$(date '+%Y-%m-%d %H:%M:%S')

echo ""
echo "================================================================================================"
echo "[*] BORRADO DE TEMPORALES"
echo "================================================================================================"
echo ""

    directorio_a_eliminar="dist"
    if [ -d "$directorio_a_eliminar" ]; then
        # El directorio existe, así que lo eliminamos
        rm -r "$directorio_a_eliminar"
        echo "Directorio eliminado: $directorio_a_eliminar"
    else
        echo "El directorio no existe: $directorio_a_eliminar"
    fi
    directorio_a_eliminar="$PROJECT.egg-info"
    if [ -d "$directorio_a_eliminar" ]; then
        # El directorio existe, así que lo eliminamos
        rm -r "$directorio_a_eliminar"
        echo "Directorio eliminado: $directorio_a_eliminar"
    else
        echo "El directorio no existe: $directorio_a_eliminar"
    fi
    directorio_a_eliminar="$PROJECT/__pycache__"
    if [ -d "$directorio_a_eliminar" ]; then
        # El directorio existe, así que lo eliminamos
        echo "Directorio eliminado: $directorio_a_eliminar"
    else
        echo "El directorio no existe: $directorio_a_eliminar"
    fi

echo ""
echo "================================================================================================"
echo "[*] INSTALACION DE DEPENDENCIAS DE COMPILACION"
echo "================================================================================================"
echo ""
pip install build
echo ""
echo "================================================================================================"
echo  "[*] HISTORIAL DE CAMBIOS"
echo "================================================================================================"
echo ""
echo "$CHANGES"
echo ""
if [ -z "$1" ]
then
    archivo="$PROJECT/__init__.py"
    version=$(grep -o "__version__ = '[0-9]\+\.[0-9]\+\.[0-9]\+'" "$archivo")
    version=$(echo "$version" | sed "s/__version__ = '//;s/'//")
    echo "================================================================================================"
    echo  "[*] NO PASAMOS VERSION. COMPILAMOS CON LA ACTUAL $version"
    echo "================================================================================================"
    echo ""
else
    echo "__version__ = '$1'" > "$PROJECT/__init__.py"

    echo "================================================================================================"
    echo "[*] COMPILAMOS SOFTWARE CON NUEVA VERSION $1"
    echo "================================================================================================"
    echo ""
    version=$1
fi

python3 -m build

echo ""
echo "================================================================================================"
echo "[*] CREAMOS TAG $1 Y PUBLICAMOS EN GITHUB"
echo "================================================================================================"
echo ""
git tag $version -m "$CHANGES"
git push origin $version
echo ""
echo "================================================================================================"
echo "[*] COMPILACION FINALIZADA $version"
echo "================================================================================================"
echo ""