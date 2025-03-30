import tkinter as tk
import chardet  # Necesario para detectar la codificación de archivos
from tkinter import filedialog, messagebox, simpledialog
import json
import os
import time

class TextEditorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("EdithorText - Sin Documento")
        self.root.geometry("600x400")
        
        # Establecer el ícono de la ventana
        self.root.iconbitmap("icono.ico")  # Asegúrate de que el archivo icono.ico está en la misma carpeta

        # Inicializar tamaño de fuente y fuente predeterminada
        self.font_size = 12
        self.font_family = "Arial"
        self.encoding = "utf-8"  # Valor por defecto
        
        # Área de texto
        self.text_area = tk.Text(root, wrap=tk.WORD, font=(self.font_family, self.font_size))
        self.text_area.grid(row=0, column=0, sticky="nsew")  # Se ajusta al espacio disponible
        self.text_area.bind("<KeyRelease>", self.highlight_syntax)  # Para resaltar cuando se escriba
        self.text_area.bind("<ButtonRelease-1>", self.update_status_bar)  # Actualizar barra de estado al hacer clic
        self.text_area.bind("<KeyRelease>", self.update_status_bar)  # Actualizar barra de estado al escribir
        
        # Inicializar colores predeterminados
        self.bg_color = "#FFFFFF"  # Blanco por defecto
        self.text_color = "#000000"  # Negro por defecto

        # Cargar configuración de color al iniciar
        self.load_settings()  
        
        # Menú
        self.menu_bar = tk.Menu(root)
        self.root.config(menu=self.menu_bar)
        
        # Menú Archivo
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Archivo", menu=self.file_menu)
        self.file_menu.add_command(label="Abrir", command=self.open_file)
        self.file_menu.add_command(label="Guardar", command=self.save_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Salir", command=root.quit)

        # Menú Editar
        self.edit_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Editar", menu=self.edit_menu)
        self.edit_menu.add_command(label="Borrar texto", command=self.clear_text)
        self.edit_menu.add_command(label="Seleccionar todo", command=self.select_all)

        # Menú Configuración
        self.config_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Configuración", menu=self.config_menu)
        self.config_menu.add_command(label="Cambiar color de fondo", command=self.change_bg_color)
        self.config_menu.add_command(label="Cambiar color de texto", command=self.change_text_color)
        self.config_menu.add_command(label="Agrandar texto", command=self.increase_font)
        self.config_menu.add_command(label="Reducir texto", command=self.decrease_font)
        self.config_menu.add_command(label="Cambiar fuente", command=self.change_font)  # Opción para cambiar fuente
        self.config_menu.add_command(label="Ocultar/Mostrar Barra de Estado", command=self.toggle_status_bar)

        # Barra de estado
        self.status_bar = tk.Frame(root, height=25, bg="lightgray")
        self.status_bar.grid(row=1, column=0, sticky="ew")  # Ajustar al fondo de la ventana
        
        self.word_count_label = tk.Label(self.status_bar, text="Palabras: 0", bg="lightgray")
        self.word_count_label.pack(side=tk.LEFT, padx=5)

        self.position_label = tk.Label(self.status_bar, text="Línea: 1, Columna: 1", bg="lightgray")
        self.position_label.pack(side=tk.LEFT, padx=5)

        self.time_label = tk.Label(self.status_bar, text="", bg="lightgray")
        self.time_label.pack(side=tk.RIGHT, padx=5)

        # Añadir un evento de clic sobre la hora para insertarla en el texto
        self.time_label.bind("<Button-1>", self.insert_time_to_text)
        
        # Actualizar hora cada segundo
        self.update_time()
        
        # Configuración de expansión para las filas y columnas de la ventana
        root.grid_rowconfigure(0, weight=1)
        root.grid_columnconfigure(0, weight=1)
        
        self.filename = None  # Variable para almacenar el nombre del archivo actual

    def open_file(self):
        file_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        
        if file_path:  # Si el usuario seleccionó un archivo
            try:
                with open(file_path, "rb") as file:
                    raw_data = file.read()
                    result = chardet.detect(raw_data)  # Detectar encoding
                    self.encoding = result["encoding"] if result["encoding"] else "utf-8"

                with open(file_path, 'r', encoding=self.encoding) as file:
                    content = file.read()
                    self.text_area.delete(1.0, tk.END)  # Limpiar el área de texto
                    self.text_area.insert(tk.END, content)  # Cargar el contenido del archivo
                
                self.filename = file_path  # Guardar el nombre del archivo
                self.update_window_title()  # Actualizar el título con el nombre del archivo
                self.encoding_label.config(text=f"Encoding: {self.encoding}")  # Actualizar en barra de estado
            except Exception as e:
                messagebox.showerror("Error", f"Hubo un problema al abrir el archivo: {e}")

    def save_file(self):
        if self.filename:
            content = self.text_area.get(1.0, tk.END)
            try:
                with open(self.filename, 'w', encoding='utf-8') as file:
                    file.write(content)
            except Exception as e:
                messagebox.showerror("Error", f"Hubo un problema al guardar el archivo: {e}")
        else:
            self.save_as_file()  # Si no tiene nombre de archivo, usar 'Guardar como'

    def save_as_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        
        if file_path:
            content = self.text_area.get(1.0, tk.END)
            try:
                with open(file_path, 'w', encoding='utf-8') as file:
                    file.write(content)
                self.filename = file_path  # Guardar el nombre del archivo
                self.update_window_title()  # Actualizar el título con el nombre del archivo
            except Exception as e:
                messagebox.showerror("Error", f"Hubo un problema al guardar el archivo: {e}")

    def update_window_title(self):
        if self.filename:
            file_name = self.filename.split('/')[-1]  # Obtener solo el nombre del archivo
            self.root.title(f"EdithorText - {file_name}")
        else:
            self.root.title("EdithorText - Sin Documento")

    def clear_text(self):
        self.text_area.delete(1.0, tk.END)

    def change_bg_color(self):
        color = simpledialog.askstring("Color de fondo", "Introduce el color de fondo (código hex):")
        if color:
            self.bg_color = color
            self.text_area.config(bg=color)
            self.save_settings()  # Guardar configuración al cambiar el color

    def change_text_color(self):
        color = simpledialog.askstring("Color de texto", "Introduce el color del texto (código hex):")
        if color:
            self.text_color = color
            self.text_area.config(fg=color)
            self.save_settings()  # Guardar configuración al cambiar el color

    def increase_font(self):
        self.font_size += 2
        self.text_area.config(font=(self.font_family, self.font_size))

    def decrease_font(self):
        if self.font_size > 8:
            self.font_size -= 2
            self.text_area.config(font=(self.font_family, self.font_size))

    def change_font(self):
        # Crear un cuadro de diálogo para elegir la fuente
        font_choice = simpledialog.askstring("Seleccionar fuente", "Introduce el nombre de la fuente (e.g., Arial, Times New Roman, Courier),debe estar previamente instalada en el sistema:")
        if font_choice:
            self.font_family = font_choice
            self.text_area.config(font=(self.font_family, self.font_size))
            self.save_settings()  # Guardar configuración al cambiar la fuente

    def save_settings(self):
        settings = {
            "bg_color": self.bg_color,
            "text_color": self.text_color,
            "font_size": self.font_size,
            "font_family": self.font_family  # Guardar también la fuente seleccionada
        }
        with open("settings.json", "w") as file:
            json.dump(settings, file)

    def load_settings(self):
        if os.path.exists("settings.json"):
            with open("settings.json", "r") as file:
                settings = json.load(file)
                self.bg_color = settings.get("bg_color", "#FFFFFF")
                self.text_color = settings.get("text_color", "#000000")
                self.font_size = settings.get("font_size", 12)
                self.font_family = settings.get("font_family", "Arial")  # Cargar la fuente guardada
                # Cargar la configuración de color y fuente después de que text_area esté disponible
                self.text_area.config(bg=self.bg_color, fg=self.text_color, font=(self.font_family, self.font_size))

    def highlight_syntax(self, event=None):
        # Palabras clave de Python como ejemplo
        python_keywords = ["def", "class", "import", "for", "if", "else", "return", "True", "False"]
        
        # Recoger todo el texto en el área
        text = self.text_area.get(1.0, tk.END)
        
        # Eliminar los resaltados previos
        self.text_area.tag_delete("keyword")
        
        # Resaltar las palabras clave
        for keyword in python_keywords:
            start_index = "1.0"
            while True:
                start_index = self.text_area.search(r"\b" + keyword + r"\b", start_index, stopindex=tk.END)
                if not start_index:
                    break
                end_index = f"{start_index}+{len(keyword)}c"
                self.text_area.tag_add("keyword", start_index, end_index)
                self.text_area.tag_config("keyword", foreground="blue")  # Cambiar color a azul

    def select_all(self):
        self.text_area.tag_add("sel", "1.0", tk.END)

    def update_status_bar(self, event=None):
        # Contador de palabras
        text = self.text_area.get(1.0, tk.END).strip()
        word_count = len(text.split()) if text else 0
        self.word_count_label.config(text=f"Palabras: {word_count}")
        
        # Contador de líneas y columnas
        line, col = self.text_area.index(tk.INSERT).split(".")
        self.position_label.config(text=f"Línea: {line}, Columna: {col}")
        
    def update_time(self):
        # Mostrar hora actual en la barra de estado
        current_time = time.strftime("%H:%M:%S")
        self.time_label.config(text=f"Hora: {current_time}")
        self.root.after(1000, self.update_time)  # Actualizar cada segundo
    
    def toggle_status_bar(self):
        # Alternar visibilidad de la barra de estado
        if self.status_bar.winfo_ismapped():  # Si la barra está visible
            self.status_bar.grid_forget()  # Ocultarla
        else:
            self.status_bar.grid(row=1, column=0, sticky="ew")  # Mostrarla de nuevo

    def insert_time_to_text(self, event=None):
        # Insertar la hora actual en la posición del cursor
        current_time = time.strftime("%H:%M:%S")
        self.text_area.insert(tk.INSERT, current_time)

if __name__ == "__main__":
    root = tk.Tk()
    app = TextEditorApp(root)
    root.mainloop()
