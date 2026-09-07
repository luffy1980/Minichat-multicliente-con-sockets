import socket
import threading
import sys


HOST = "192.168.1.127"
PUERTO = 6066

def recibir_mensajes(cliente):
    """Escucha mensajes entrantes desde el servidor en segundo plano."""
    while True:
        try:
            mensaje = cliente.recv(1024).decode("utf-8")
            if not mensaje:
                break
            print(f"\n{mensaje}")
            print("Mensaje: ", end="", flush=True)
        except:
            break

def iniciar_cliente():
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        cliente.connect((HOST, PUERTO))
    except Exception as e:
        print(f"No se pudo conectar al servidor: {e}")
        sys.exit()

    print("===================================")
    print("          MINICHAT CLIENTE         ")
    print("===================================")
    
    nombre = input("Escribe tu nombre: ")
    cliente.sendall(nombre.encode("utf-8"))

    # Crear hilo para recibir mensajes concurrentemente
    hilo_receptor = threading.Thread(target=recibir_mensajes, args=(cliente,))
    hilo_receptor.daemon = True
    hilo_receptor.start()

    # Enviar mensajes en el hilo principal
    while True:
        mensaje = input("Mensaje: ")
        try:
            cliente.sendall(mensaje.encode("utf-8"))
            if mensaje.lower() == "/salir":
                break
        except:
            break

    cliente.close()

if __name__ == "__main__":
    iniciar_cliente()