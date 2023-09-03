#!/bin/bash

# Función para agregar la entrada al PATH
add_to_path() {
  local profile_file="$1"
  local entry="$2"
  
  # Verifica si la entrada ya existe en el archivo
  if ! grep -qF "$entry" "$profile_file"; then
    echo "Agregando la entrada al archivo $profile_file"
    echo "export PATH=\$PATH:$entry" >> "$profile_file"
  else
    echo "La entrada ya existe en el archivo $profile_file"
  fi
}

# Determinar el sistema operativo
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
  TOOLS_DIR="$SCRIPT_DIR/tools/bin/linux"
elif [[ "$OSTYPE" == "darwin"* ]]; then
  TOOLS_DIR="$SCRIPT_DIR/tools/bin/darwin"
else
  echo "Sistema operativo no compatible"
  exit 1
fi

# Directorio donde se encuentra este script
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Verifica si .bashrc existe
if [ -f "$HOME/.bashrc" ]; then
  add_to_path "$HOME/.bashrc" "$TOOLS_DIR"
fi

# Verifica si .zshrc existe
if [ -f "$HOME/.zshrc" ]; then
  add_to_path "$HOME/.zshrc" "$TOOLS_DIR"
fi


# INSTALAR REQUERIMENTS.TXT
# COMPILAR GOTOCPC
# INSTALAR GOTOCPC

echo "Script completado"
