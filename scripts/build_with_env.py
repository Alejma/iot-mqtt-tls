#!/usr/bin/env python3
"""
Script para compilar con variables de entorno en PlatformIO
"""
import os
import sys
import subprocess

def get_env_vars():
    """Obtiene las variables de entorno necesarias"""
    env_vars = {}
    
    # Variables requeridas
    required_vars = [
        'COUNTRY', 'STATE', 'CITY',
        'MQTT_SERVER', 'MQTT_PORT', 'MQTT_USER', 'MQTT_PASSWORD',
        'WIFI_SSID', 'WIFI_PASSWORD', 'ROOT_CA'
    ]
    
    for var in required_vars:
        value = os.getenv(var)
        if value:
            env_vars[var] = value
        else:
            print(f"Warning: Variable de entorno {var} no definida")
    
    return env_vars

def build_with_env():
    """Compila el proyecto con variables de entorno"""
    env_vars = get_env_vars()
    
    if not env_vars:
        print("No hay variables de entorno definidas. Usando valores por defecto del código.")
        print("Para usar variables de entorno, crea un archivo .env o configura las variables del sistema.")
        print("Ejemplo: export COUNTRY=colombia && export STATE=valle && export CITY=tulua")
        return subprocess.run(['pio', 'run', '-e', 'esp32dev'])
    
    # Construir comando con variables de entorno
    cmd = ['pio', 'run', '-e', 'esp32dev']
    
    # Agregar build flags para cada variable de entorno
    for var, value in env_vars.items():
        cmd.extend(['-D', f'{var}={value}'])
    
    print(f"Compilando con variables de entorno: {list(env_vars.keys())}")
    return subprocess.run(cmd)

if __name__ == '__main__':
    sys.exit(build_with_env().returncode)