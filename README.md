# Python HTTP Honeypot

## Descripción
Honeypot en Python que simula un panel de login y registra intentos de acceso y actividad sospechosa.

## Funcionalidades
- Captura de requests HTTP
- Registro de credenciales
- Detección de rutas sospechosas
- Logs en JSON
- Script de análisis de eventos

## Tecnologías
- Python
- Flask

## Cómo ejecutarlo

1. Clonar el repositorio 
   ```bash
    git clone https://github.com/tu-usuario/python-honeypot-lab.git
    cd python-honeypot-lab
   
2. Crear entorno virtual
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate

3. Instalar dependencias necesarias:
   ```bash
   pip install -r requirements.txt

4. Ejecutar el honeypot
   ```bash
   python honeypot.py

5. Probar el honeypot
Desde navegador accede a /login e introducir credenciales.
Desde el terminal: 
   ```bash
   curl http://127.0.0.1:8080/admin
    curl -X POST http://127.0.0.1:8080/login \
    -d "username=admin&password=123456"
   
6. Ver logs generados 
   ```bash
   tail -f logs/events.jsonl

7. Ejecutar análisis de logs
   ```bash
   python analyze_logs.py

El script mostrará estadísticas sobre la actividad registrada. Obteniendo un resumen como el siguiente: 

=== Resumen de eventos ===
request: 10
suspicious_request: 5
credential_attempt: 3

=== Top 5 IPs ===
127.0.0.1: 18

=== Top 5 rutas ===
/login: 8
/admin: 4
/wp-login.php: 3

=== Top 5 user-agents ===
curl/8.5.0: 6
Mozilla/5.0: 12

=== Usernames más probados ===
admin: 2
root: 1

## Interpretación 

- Rutas sospechosas como /admin o /wp-login.php indican actividad automatizada o escaneo.
- Múltiples intentos de login pueden sugerir ataques de fuerza bruta.
- User-agents como curl suelen estar asociados a pruebas automatizadas o scripts.
- Repetición de IPs permite identificar posibles fuentes de ataque o testing.

## Utilidades

- Detectar patrones de comportamiento malicioso
- Identificar endpoints expuestos más atacados
- Analizar intentos de autenticación
- Simular un entorno básico de monitorización tipo SOC

