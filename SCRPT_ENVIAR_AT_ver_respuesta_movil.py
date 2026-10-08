import time
import serial
import serial.tools.list_ports as prtlst

# --- Configuración del Puerto ---
PUERTO_OBJETIVO = "COM11"
BAUD_RATE = 115200
TIMEOUT = 2


def probar_comandos_at(puerto):
    """Abre el puerto serie y envía comandos AT de diagnóstico"""
    try:
        print(f"[*] Abriendo canal AT en {puerto} a {BAUD_RATE} baudios...")
        with serial.Serial(puerto, baudrate=BAUD_RATE, timeout=TIMEOUT) as ser:
            
            # Lista de comandos AT para probar respuesta
            comandos = [
                "AT\r\n",                # Sondeo básico
                "AT+CGMM\r\n",          # Consultar modelo
                "AT+KSTRINGB=0,3\r\n",  # Comando específico de diagnóstico Samsung
                "AT+SWATD=0\r\n"        # Control de depuración/AT de Samsung
            ]

            for cmd in comandos:
                print(f"\n[-->] Enviando: {cmd.strip()}")
                ser.write(cmd.encode())
                time.sleep(0.5)
                
                respuesta = ser.read_all()
                if respuesta:
                    print(f"[<--] Respuesta recibida: {respuesta}")
                else:
                    print("[-] Sin respuesta (Timeout del puerto).")

    except Exception as e:
        print(f"[-] Error al acceder al puerto {puerto}: {e}")


def main():
    print("--- PRUEBA DE COMANDOS AT EN PUERTO DE SERVICIO ---")
    
    # Verificar si el puerto especificado existe realmente
    ports = [p.device for p in prtlst.comports()]
    if PUERTO_OBJETIVO in ports:
        print(f"[+] ¡Puerto {PUERTO_OBJETIVO} encontrado en el sistema!")
        probar_comandos_at(PUERTO_OBJETIVO)
    else:
        print(f"[-] El puerto {PUERTO_OBJETIVO} no está activo actualmente. Comprueba la conexión USB.")


if __name__ == "__main__":
    main()