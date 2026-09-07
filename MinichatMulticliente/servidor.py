import socket
import threading

# Configuración del servidor
HOST = "0.0.0.0"  # Escucha en todas las interfaces de red
PUERTO = 6066

clientes = []
nombres = []

def transmitir(mensaje, cliente_actual=None):
    """Envía un mensaje a todos los clientes excepto al emisor."""
    for cliente in clientes:
        if cliente != cliente_actual:
            try:
                cliente.sendall(mensaje.encode("utf-8"))
            except:
                eliminar_cliente(cliente)

def eliminar_cliente(cliente):
    """Elimina el socket y nombre del cliente desconectado."""
    if cliente in clientes:
        indice = clientes.index(cliente)
        clientes.remove(cliente)
        nombre = nombres[indice]
        nombres.remove(nombre)
        print(f"{nombre} se desconectó.")
        cliente.close()

def atender_cliente(cliente, direccion):
    """Maneja la comunicación individual con cada cliente conectado."""
    print(f"Cliente conectado: {direccion}")
    nombre = ""
    try:
        # Recibir nombre del usuario
        nombre = cliente.recv(1024).decode("utf-8")
        clientes.append(cliente)
        nombres.append(nombre)
        
        print(f"{nombre} se ha conectado.")
        mensaje = f"*** {nombre} se ha unido al chat ***"
        transmitir(mensaje, cliente)

        # Bucle de recepción de mensajes
        while True:
            datos = cliente.recv(1024)
            if not datos:
                break
            
            mensaje = datos.decode("utf-8")
            if mensaje.lower() == "/salir":
                break

            mensaje_completo = f"{nombre}: {mensaje}"
            print(mensaje_completo)
            transmitir(mensaje_completo, cliente)

    except Exception as e:
        print(f"Error con {direccion}: {e}")
    finally:
        if cliente in clientes:
            indice = clientes.index(cliente)
            nombre = nombres[indice]
            clientes.remove(cliente)
            nombres.remove(nombre)
            mensaje = f"*** {nombre} ha abandonado el chat ***"
            transmitir(mensaje)
            cliente.close()
            print(f"{nombre} se desconectó.")

def iniciar_servidor():
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind((HOST, PUERTO))
    servidor.listen()
    
    print("===================================")
    print("         SERVIDOR DE CHAT          ")
    print("===================================")
    print(f"Escuchando en el puerto {PUERTO}...")

    while True:
        cliente, direccion = servidor.accept()
        hilo = threading.Thread(
            target=atender_cliente,
            args=(cliente, direccion)
        )
        hilo.start()
        print(f"Hilos activos: {threading.active_count() - 1}")

if __name__ == "__main__":
    iniciar_servidor()