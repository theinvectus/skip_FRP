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
🚀 Guía Paso a Paso para el Uso
Sigue estos pasos detallados para ejecutar el script con éxito:

Paso 1: Conectar el teléfono
Enciende tu dispositivo Samsung y conéctalo al ordenador mediante un cable USB original o de alta calidad.

Asegúrate de que el Administrador de dispositivos de Windows reconozca el puerto serie del módem de Samsung (suele aparecer como Samsung Mobile USB Modem).

Paso 2: Ejecutar el script
Ejecuta el script principal desde tu terminal o consola:

Bash
python nombre_del_script.py
Paso 3: Seleccionar el puerto serie
El script escaneará automáticamente los puertos serie disponibles en tu equipo y te mostrará una lista.

Te sugerirá un puerto por defecto. Simplemente pulsa INTRO para aceptarlo o escribe el nombre del puerto correcto (por ejemplo, COM3) si es necesario.

Paso 4: Abrir el menú de diagnóstico del teléfono (¡Muy Importante!)
En la pantalla de tu teléfono Samsung, ve a la pantalla de llamada de emergencia (o pulsa Llamada de emergencia en la pantalla de bloqueo FRP).

Marca el código secreto:

Plaintext
*#0*#
Se abrirá un menú de diagnóstico secreto en blanco con cuadros de pruebas (Test Mode).

Vuelve al ordenador y pulsa INTRO en la consola para continuar.

Paso 5: Habilitación de ADB
El script enviará automáticamente una secuencia de comandos AT optimizados para forzar la apertura del puerto de depuración ADB en el dispositivo.

Atención en la pantalla del teléfono: Mira la pantalla de tu Samsung. Debería aparecer una ventana emergente pidiendo autorizar la Depuración USB (Allow USB debugging?).

Marca la casilla "Permitir siempre desde este ordenador" y pulsa Permitir.

Paso 6: Ejecución del Bypass FRP
Una vez que el dispositivo autoriza la conexión ADB:

El script se reiniciará/esperará a que el ADB esté listo.

Subirá automáticamente el archivo binario frp.bin a la ruta temporal del dispositivo (/data/local/tmp/temp).

Le asignará permisos de ejecución (chmod 777) y lo ejecutará para completar el proceso.

🛠️ Estructura del Código
El script está dividido en dos bloques principales:

Módulo AT Utils: Gestiona la detección automática de puertos COM, la apertura del puerto serie a 115200 baudios y el envío automatizado de tramas AT de diagnóstico (AT+SWATD=1, AT+DUMPCTRL, etc.).

Módulo ADB Utils: Controla la interfaz con la herramienta ADB (adb.exe), verifica la conexión del dispositivo (wait-for-device), empuja los archivos necesarios y ejecuta los comandos de shell.

❓ Solución de Problemas (Troubleshooting)
El script se queda colgado en "Esperando al dispositivo mediante ADB...":

Asegúrate de haber aceptado la ventana emergente de depuración USB en la pantalla del teléfono. Si no aparece, desconecta y vuelve a conectar el cable USB, o reinicia el servidor ADB ejecutando adb kill-server.

Error de puerto serie no encontrado:

Comprueba que los drivers USB de Samsung estén bien instalados y que el Administrador de dispositivos no muestre errores amarillos en los puertos COM.
