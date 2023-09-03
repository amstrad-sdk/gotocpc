

# Nombre del programa
PROGRAM = home/destroyer/Documentos/Github/AMSTRAD/gotocpc/tools/bin/go2cpc.sh

# Parámetro a pasar al programa
PARAMETER = --build

# Ruta al entorno virtual (ajusta esta ruta según tu configuración)
VENV = /home/destroyer/Documentos/Github/AMSTRAD/gotocpc/.env

# Regla principal
all: activate_venv check_config
	./$(PROGRAM) $(PARAMETER)

# Regla para activar el entorno virtual
activate_venv:
	@if [ -d $(VENV) ]; then \
		. $(VENV)/bin/activate; \
	else \
		echo "El entorno virtual no existe en la ubicación especificada: $(VENV)"; \
		exit 1; \
	fi

# Regla para verificar la existencia de CPC.YAML
check_config:
	@if [ ! -f "cfg/CPC.YAML" ]; then \
		echo "El archivo "cfg/CPC.YAML" no existe en este directorio."; \
		exit 1; \
	fi

# Limpia los archivos generados
clean:
	rm -f $(PROGRAM)

.PHONY: all activate_venv check_config clean
