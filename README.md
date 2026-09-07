# Minichat Multicliente con Sockets

Aplicación de chat cliente-servidor implementada mediante sockets de red, permitiendo la comunicación simultánea entre múltiples usuarios conectados a un servidor central.

## Características

* **Arquitectura Cliente-Servidor:** El servidor gestiona las conexiones entrantes y retransmite los mensajes a los clientes activos.
* **Soporte Multicliente:** Manejo de múltiples sesiones concurrentes mediante hilos/procesos para evitar bloqueos.
* **Comunicación en Tiempo Real:** Envío y recepción de mensajes a través de sockets TCP/IP.

## Requisitos

* Compilador o entorno de ejecución correspondiente (por ejemplo: GCC, Python 3, o Java JDK según los archivos del proyecto).
* Conexión de red local o acceso por loopback (`127.0.0.1`).

## Instrucciones de Uso

### 1. Iniciar el Servidor
Ejecuta el archivo del servidor en una terminal:
```bash
# Ejemplo de ejecución del servidor:
# python servidor.py
# o ./servidor
