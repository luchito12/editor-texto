
## **EdithorText**

**EdithorText** es un editor de texto simple y funcional diseñado para ofrecer una experiencia de edición de texto básica pero efectiva. Permite abrir, editar, y guardar archivos de texto en diferentes codificaciones, con soporte para personalización de la interfaz, como cambios en el color de fondo, el color del texto, el tamaño de la fuente y la fuente utilizada.

### **Características del Programa:**

1. **Interfaz gráfica con Tkinter**:
   - Usando Tkinter, una biblioteca gráfica estándar en Python, este editor proporciona una interfaz sencilla y fácil de usar.
   
2. **Codificación de Archivos**:
   - Detecta y muestra la codificación de los archivos que se abren. Utiliza la biblioteca `chardet` para detectar automáticamente la codificación, lo que permite abrir archivos en diferentes formatos de texto sin preocuparse por problemas de codificación.

3. **Personalización de la interfaz**:
   - Permite personalizar el color de fondo, el color del texto, la fuente y el tamaño de la fuente.
   - Estas configuraciones se guardan automáticamente en un archivo JSON y se cargan cada vez que se abre el programa.

4. **Resaltado de Sintaxis**:
   - Aunque actualmente está configurado para palabras clave de Python, el sistema puede ampliarse para agregar más lenguajes de programación en el futuro.

5. **Barra de Estado**:
   - Muestra información útil como el número de palabras, la posición actual del cursor en líneas y columnas, y la hora actual.
   - Al hacer clic sobre la hora, se inserta la hora actual en el texto.

6. **Funcionalidades de Archivo**:
   - **Abrir**: Permite abrir archivos de texto en diferentes codificaciones.
   - **Guardar**: Guarda el archivo actual.
   - **Guardar como**: Si el archivo no tiene nombre, permite guardar el archivo con un nombre específico.

7. **Configuración de la fuente**:
   - Cambia el tipo y tamaño de la fuente del texto.

8. **Menú de edición**:
   - Opciones para borrar el texto, seleccionar todo el contenido, y otras funciones básicas de edición.

9. **Compatibilidad multiplataforma**:
   - Funciona tanto en **Windows** como en **Linux**, utilizando bibliotecas estándar de Python, lo que hace fácil ejecutar el editor en diferentes sistemas operativos.

---

## **Instrucciones de Uso**:

### **1. Abrir un archivo:**
   - Haz clic en "Archivo" -> "Abrir" y selecciona el archivo de texto que deseas abrir. El editor detectará la codificación y mostrará el contenido correctamente.

### **2. Guardar un archivo:**
   - Para guardar el archivo, selecciona "Archivo" -> "Guardar" si ya tiene un nombre, o "Guardar como" para elegir una ubicación y nombre de archivo.

### **3. Modificar configuraciones:**
   - Para cambiar la configuración de la fuente o los colores de fondo y texto, ve al menú "Configuración" y selecciona las opciones correspondientes.

### **4. Barra de Estado:**
   - La barra de estado muestra información útil, como la cantidad de palabras, la posición del cursor y la hora actual. Puedes hacer clic sobre la hora para insertar la hora en el texto.

### **5. Resaltado de Sintaxis:**
   - A medida que escribas en el área de texto, las palabras clave de Python se resaltarán automáticamente en color azul.

---

## **Instrucciones para Ejecutar el Programa:**

### **En Windows:**

1. **Requisitos previos**:
   - Asegúrate de tener Python 3.x instalado en tu sistema.
   - Si no tienes Python, puedes descargarlo desde [python.org](https://www.python.org/downloads/).
   - Instala las bibliotecas necesarias ejecutando el siguiente comando en la terminal de Windows:
     ```bash
     pip install chardet pillow
     ```

2. **Ejecutar el Programa**:
   - Descarga o clona el repositorio del proyecto a tu computadora.
   - Abre una terminal de Windows (CMD o PowerShell) y navega a la carpeta donde tienes el archivo `EdithorText.py`.
   - Ejecuta el programa con:
     ```bash
     python EdithorText.py
     ```

### **En Linux:**

1. **Requisitos previos**:
   - Asegúrate de tener Python 3.x instalado en tu sistema.
   - Si no tienes Python, puedes instalarlo utilizando tu gestor de paquetes (por ejemplo, `apt` en Ubuntu).
   - Instala las bibliotecas necesarias ejecutando el siguiente comando:
     ```bash
     pip install chardet pillow
     ```

2. **Ejecutar el Programa**:
   - Descarga o clona el repositorio del proyecto a tu computadora.
   - Abre una terminal y navega a la carpeta donde tienes el archivo `EdithorText.py`.
   - Ejecuta el programa con:
     ```bash
     python EdithorText.py
     ```

---

## **Posibles Errores y Soluciones**:

- **Error: `ModuleNotFoundError: No module named 'chardet'`**:
  - Solución: Ejecuta `pip install chardet` para instalar la biblioteca `chardet`.



