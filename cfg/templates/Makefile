# Nombre del programa
PROGRAM = go2cpc

# Parámetro a pasar al programa
PARAMETER = --build

# Regla principal
all: check_config
	./$(PROGRAM) $(PARAMETER)

# Regla para verificar la existencia de CPC.YAML
check_config:
	@if [ ! -f "cfg/CPC.YAML" ]; then \
		echo "El archivo "cfg/CPC.YAML" no existe en este directorio."; \
		exit 1; \
	fi

# Limpia los archivos generados
clean:
	rm -rf out

.PHONY: all check_config clean
