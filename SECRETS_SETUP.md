# Configuración de Secrets para IoT MQTT TLS

Este proyecto ahora utiliza variables de entorno para manejar todos los secretos de forma segura. Los secretos ya no están hardcodeados en el código fuente.

## Variables de Entorno Requeridas

### Configuración de Ubicación
- `COUNTRY`: País donde se encuentra el dispositivo (ej: "colombia")
- `STATE`: Estado donde se encuentra el dispositivo (ej: "valle") 
- `CITY`: Ciudad donde se encuentra el dispositivo (ej: "tulua")

### Configuración del Servidor MQTT
- `MQTT_SERVER`: Dirección del servidor MQTT (ej: "mqtt.alvarosalazar.freeddns.org")
- `MQTT_PORT`: Puerto del servidor MQTT (ej: 8883)
- `MQTT_USER`: Usuario MQTT (ej: "alvaro")
- `MQTT_PASSWORD`: Contraseña del usuario MQTT (ej: "supersecreto")

### Configuración de WiFi
- `WIFI_SSID`: Nombre de la red WiFi (ej: "univalle")
- `WIFI_PASSWORD`: Contraseña de la red WiFi (ej: "Univalle")

### Certificado de Seguridad
- `ROOT_CA`: Certificado raíz en formato PEM para conexiones TLS

## Configuración Local

### 1. Crear archivo .env
Copia el archivo `.env.template` como `.env` y configura tus valores:

```bash
cp .env.template .env
```

Luego edita `.env` con tus valores reales.

### 2. Compilar con PlatformIO

#### Opción A: Compilar con valores por defecto (recomendado para desarrollo)
```bash
platformio run -e esp32dev
```

#### Opción B: Compilar con variables de entorno específicas
```bash
platformio run -e esp32dev \
  -DCOUNTRY=colombia \
  -DSTATE=valle \
  -DCITY=tulua \
  -DMQTT_SERVER=mqtt.usuario.freeddns.org \
  -DMQTT_PORT=8883 \
  -DMQTT_USER=alvaro \
  -DMQTT_PASSWORD=supersecreto \
  -DWIFI_SSID=wifi \
  -DWIFI_PASSWORD=password \
  -DROOT_CA="-----BEGIN CERTIFICATE-----..."
```

#### Opción C: Usar el script de Python (recomendado para CI/CD)
```bash
python scripts/build_with_env.py
```

## Configuración en GitHub Secrets

Para usar GitHub Actions, configura los siguientes secrets en tu repositorio:

1. Ve a tu repositorio en GitHub
2. Click en "Settings" → "Secrets and variables" → "Actions"
3. Click en "New repository secret"
4. Agrega cada una de las variables de entorno como secrets:

### Secrets requeridos en GitHub:
- `COUNTRY`
- `STATE` 
- `CITY`
- `MQTT_SERVER` (servidor MQTT)
- `MQTT_PORT`
- `MQTT_USER`
- `MQTT_PASSWORD`
- `WIFI_SSID`
- `WIFI_PASSWORD`
- `ROOT_CA`

## Configuración de Variables de Entorno en Terminal

También puedes configurar las variables de entorno directamente en tu terminal:

```bash
export COUNTRY="colombia"
export STATE="valle"
export CITY="tulua"
export MQTT_SERVER="mqtt.alvarosalazar.freeddns.org"
export MQTT_PORT="8883"
export MQTT_USER="alvaro"
export MQTT_PASSWORD="supersecreto"
export WIFI_SSID="univalle"
export WIFI_PASSWORD="Univalle"
export ROOT_CA="-----BEGIN CERTIFICATE-----\n..."
```

## Compilación con Variables Específicas

Puedes sobrescribir variables específicas durante la compilación:

```bash
platformio run -e esp32dev --environment-variables "COUNTRY=mexico,STATE=cdmx,CITY=mexico"
```

## Seguridad

- **NUNCA** commitees el archivo `.env` al repositorio
- El archivo `.env` está incluido en `.gitignore`
- Usa GitHub Secrets para CI/CD
- Mantén tus secrets seguros y no los compartas

## Archivos Modificados

- `src/secrets.cpp`: Ahora lee variables de entorno con valores por defecto
- `platformio.ini`: Configurado para usar variables de entorno
- `.env.template`: Template con todas las variables necesarias
- `.github/workflows/build.yml`: Workflow que usa GitHub Secrets