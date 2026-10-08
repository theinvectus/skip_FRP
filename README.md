# Samsung FRP Bypass & ADB Enabler (Script Python)

Herramienta automatizada en **Python** para habilitar la depuración USB (ADB) en dispositivos Samsung a través del puerto serie (comandos AT en el menú secreto `*#0*#`) y posteriormente automatizar el proceso de bypass FRP (Factory Reset Protection).

> **Aviso legal:** Este script está diseñado exclusivamente con fines educativos, de investigación y para que los técnicos puedan recuperar el acceso a sus propios dispositivos legítimos bloqueados.

---

## 📋 Requisitos Previos

Antes de ejecutar el script, asegúrate de tener instalado lo siguiente en tu ordenador:

1. **Python 3.8 o superior** instalado en el sistema.
2. **Controladores (Drivers) USB de Samsung** instalados correctamente en tu PC (puedes usar *Samsung Smart Switch* o los drivers oficiales de Samsung) para que el puerto serie y ADB reconozcan el teléfono.
3. El archivo binario de bypass (`frp.bin`) en la misma carpeta que el script (si vas a usar la función de carga de FRP).
4. El ejecutable de ADB (`adb.exe` en Windows o `adb` en Linux/Mac) en la misma ruta o accesible desde las variables de entorno del sistema.

---

## ⚙️ Instalación

1. Clona este repositorio o descarga los archivos en tu ordenador:
   ```bash
   git clone [https://github.com/tu-usuario/tu-repositorio.git](https://github.com/tu-usuario/tu-repositorio.git)
   cd tu-repositorio
