# Image pdf downloader.
Herramienta para descargar imágenes secuenciales desde una fuente y convertirlas en un archivo pdf.
---
## Características:
- Descarga secuencias de imágenes.
- Convierte automáticamente a pdf.
- Limpieza automática (elimina las imágenes despues de crear el pdf).
- Configurable (no incluye fuentes predefinidas).
---
## Requisitos: 

### 1. Instalar python. 
Descárgalo desde: https://www.python.org/downloads/

Durante la instalación marca la casilla "add python to path".

### 2. Verifica la instalación.
Abre una terminal, cmd o powershell en windows y escribe: 
python --version

Debería mostrar en pantalla algo como "python 3.x.x"
---

### 3. Ir a la carpeta del proyecto.
Escribe en la terminal, cd "dirección", por ejemplo, cd C:\Users\TuUsuario\Downloads\image-pdf-downloader
---
### 4. Instalar dependencias.
Ejecuta pip install -r requirements.txt
---

### Como usar.
Escribe en la terminal python downloader.py. Debes de estar en la carpeta del proyecto antes para esto sigue el paso 3.
---
### Ingresar datos.

El programa pedirá:
- ID (identificador de contenido).
- Base URL (ejemplo: https://servidor.com/contents/)
- Referer (ejemplo: https://sitio.com/)
---
## Resultado.
El script generará un archivo PDF con el ID proporcionado dentro de la carpeta del proyecto.
---
## Notas.
- Esta herramienta es genérica y no incluye enlaces predefinidos.
- El usuario debe proporcionar sus propias URLs e identificadores.
- Uso recomendado para fines personales o educativos.

---

## Licencia

Uso libre bajo responsabilidad del usuario.

