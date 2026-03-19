# Python HTTP Honeypot

## Descripción

Honeypot HTTP desarrollado en Python que simula un panel de autenticación expuesto con el objetivo de registrar actividad sospechosa y capturar intentos de acceso.

El proyecto permite monitorizar peticiones HTTP, detectar rutas frecuentemente utilizadas en escaneos automatizados y almacenar eventos en logs estructurados para su posterior análisis.

Forma parte de un laboratorio defensivo orientado a Blue Team y monitorización básica de amenazas.

---

## Funcionalidades

- Captura de peticiones HTTP
- Simulación de panel de login
- Registro de credenciales introducidas
- Detección de rutas sospechosas
- Almacenamiento de eventos en formato JSON Lines
- Script de análisis de logs
- Integración con un dashboard de threat intelligence para enriquecer IPs detectadas

---

## Tecnologías

- Python
- Flask
- JSON Lines

---

## Estructura del proyecto
   
	python-honeypot-lab/
	├── honeypot.py
	├── analyze_logs.py
	├── requirements.txt
	├── templates/
	│   └── login.html
	├── logs/
	│   └── events.jsonl
	└── README.md

## Cómo ejecutarlo

1. Clonar el repositorio 
   ```bash
    git clone https://github.com//python-honeypot-lab.git]
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

## Integración con [Threat Intelligence Dashboard](https://github.com/ignaciowarleta/threat-intel-dashboard) 

Los logs generados por este honeypot pueden utilizarse en el proyecto complementario Threat Intelligence Dashboard, diseñado para enriquecer y priorizar IPs sospechosas mediante fuentes públicas de threat intelligence.

Flujo de uso:

1.	El honeypot registra eventos en logs/events.jsonl
2.	El dashboard extrae IPs únicas desde ese fichero
3.	Las IPs se enriquecen con reputación, geolocalización y scoring de riesgo
4.	Se priorizan las más sospechosas para su análisis

Esto permite construir un pequeño laboratorio defensivo compuesto por captura, análisis y priorización de amenazas.

