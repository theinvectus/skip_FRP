import os
import subprocess
import time
from typing import List
import serial
import serial.tools.list_ports as prtlst
from serial.tools import list_ports_common

# --- Configuración y Constantes ---
SERIAL_BAUDRATE = 115200
SERIAL_TIMEOUT = 12


# --- 1. Módulo AT Utils (Gestión de Puertos Serie) ---
def list_serial_ports() -> list_ports_common.ListPortInfo:
    ports = prtlst.comports()
    if len(ports) == 0:
        print("No hay puertos serie disponibles. Conecta el teléfono.")
        exit(1)
    print("####### Puertos serie disponibles #######")
    for port in ports:
        print(port)
    print("####### Fin de puertos serie #######")
    return ports[0]


def get_AT_serial(port: str) -> serial.Serial:
    return serial.Serial(
        port, baudrate=SERIAL_BAUDRATE, timeout=SERIAL_TIMEOUT
    )


def ATSend(io: serial.Serial, cmd: str) -> bool:
    if not io.isOpen():
        return False
    print(f"Enviando: {cmd.strip()}")
    io.write(cmd.encode())
    time.sleep(0.5)
    ret = io.read_all()
    print(f"Recibido: {ret}")

    if b"OK\r\n" in ret:
        return True
    if b"ERROR\r\n" in ret:
        return False
    if ret == b"\r\n":
        return False
    if ret == cmd.encode():
        return True
    if ret == b"":
        return False
    return True


def tryATCmds(io: serial.Serial, cmds: List[str]):
    for i, cmd in enumerate(cmds):
        print(f"Probando comando {i+1}")
        try:
            res = ATSend(io, cmd)
            if not res:
                print("OK")
        except:
            print(f"Error al enviar el comando {cmd}")
    try:
        io.close()
    except:
        print("No se pudo cerrar correctamente la conexión serie")


def enableADB():
    default_port = list_serial_ports()
    port = (
        input(f"Elige el puerto serie (por defecto={default_port.device}): ")
        or str(default_port.device)
    )
    io = get_AT_serial(port)
    print("Inicializando...")
    try:
        ATSend(io, "AT+KSTRINGB=0,3\r\n")
    except:
        pass

    print(
        "\n[!] ACCIÓN REQUERIDA: Ve al marcador de emergencia de tu Samsung e introduce *#0*#, luego pulsa INTRO aquí."
    )
    input()

    print("Habilitando la Depuración USB...")
    cmds = [
        "AT+DUMPCTRL=1,0\r\n",
        "AT+DEBUGLVC=0,5\r\n",
        "AT+SWATD=0\r\n",
        "AT+ACTIVATE=0,0,0\r\n",
        "AT+SWATD=1\r\n",
        "AT+DEBUGLVC=0,5\r\n",
    ]
    tryATCmds(io, cmds)
    print("La depuración USB debería estar habilitada.")
    print(
        "Si no aparece la ventana emergente en el teléfono, desconecta y vuelve a conectar el cable USB."
    )


# --- 2. Módulo ADB Utils corregido para Windows ---
def get_adb_executable():
    # Usa adb.exe directamente si está en la misma carpeta
    local_adb = "adb.exe" if os.name == "nt" else "./adb"
    if os.path.exists(local_adb):
        return local_adb
    return "adb"


def adb(cmd: str):
    adb_bin = get_adb_executable()
    return subprocess.call(f"{adb_bin} {cmd}", shell=True)


def waitForDevice():
    print("Esperando al dispositivo mediante ADB...")
    adb("kill-server")
    adb("wait-for-device")


def uploadAndRunFRPBypass():
    print("Enviando el binario de bypass FRP...")
    adb("push frp.bin /data/local/tmp/temp")
    print("Dando permisos 777...")
    adb("shell chmod 777 /data/local/tmp/temp")
    print("Ejecutando el binario...")
    adb("shell /data/local/tmp/temp")


# --- Flujo Principal ---
def main():
    print("--- 1. Habilitando ADB mediante comandos AT ---")
    enableADB()

    print("\n--- 2. Esperando conexión ADB y ejecutando Bypass FRP ---")
    waitForDevice()
    uploadAndRunFRPBypass()


if __name__ == "__main__":
    main()
