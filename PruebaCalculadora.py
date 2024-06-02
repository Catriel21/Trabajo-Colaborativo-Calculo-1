import sympy as sp
import customtkinter as ctk
from tkinter import messagebox

def calcular_derivada():
    try:
        funcion = entrada_funcion.get().strip()
        variable = entrada_variable.get().strip()
        orden = entrada_orden.get().strip()

        if not funcion or not variable:
            raise ValueError("Por favor, ingrese la función y la variable.")

        funcion_simb = sp.sympify(funcion)
        variable_simb = sp.symbols(variable)
        orden_derivada = int(orden) if orden else 1

        derivada = sp.diff(funcion_simb, variable_simb, orden_derivada)

        salida_derivada.configure(state="normal")
        salida_derivada.delete("1.0", ctk.END)
        salida_derivada.insert(ctk.END, f"Función original: {funcion}\n")
        salida_derivada.insert(ctk.END, f"Variable: {variable}\n")
        salida_derivada.insert(ctk.END, f"Orden de la derivada: {orden_derivada}\n")
        salida_derivada.insert(ctk.END, f"Derivada:\n{derivada}\n")
        salida_derivada.configure(state="disabled")
    except Exception as e:
        messagebox.showerror("Error", f"Ha ocurrido un error: {e}")

def limpiar_campos():
    entrada_funcion.delete(0, ctk.END)
    entrada_variable.delete(0, ctk.END)
    entrada_orden.delete(0, ctk.END)
    salida_derivada.configure(state="normal")
    salida_derivada.delete("1.0", ctk.END)
    salida_derivada.configure(state="disabled")

def salir():
    ventana.quit()

# Crear la ventana principal
ventana = ctk.CTk()
ventana.title("Calculadora de Derivadas")
ventana.geometry("600x400")
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Etiquetas y entradas para la función y la variable
etiqueta_funcion = ctk.CTkLabel(ventana, text="Función:")
etiqueta_funcion.grid(row=0, column=0, padx=10, pady=10, sticky="e")
entrada_funcion = ctk.CTkEntry(ventana, width=300)
entrada_funcion.grid(row=0, column=1, padx=10, pady=10, sticky="we")

etiqueta_variable = ctk.CTkLabel(ventana, text="Variable:")
etiqueta_variable.grid(row=1, column=0, padx=10, pady=10, sticky="e")
entrada_variable = ctk.CTkEntry(ventana, width=300)
entrada_variable.grid(row=1, column=1, padx=10, pady=10, sticky="we")

etiqueta_orden = ctk.CTkLabel(ventana, text="Orden de la derivada:")
etiqueta_orden.grid(row=2, column=0, padx=10, pady=10, sticky="e")
entrada_orden = ctk.CTkEntry(ventana, width=300)
entrada_orden.grid(row=2, column=1, padx=10, pady=10, sticky="we")

# Botones para calcular y limpiar
frame_botones = ctk.CTkFrame(ventana)
frame_botones.grid(row=3, column=0, columnspan=2, pady=10, sticky="we")

boton_calcular = ctk.CTkButton(frame_botones, text="Calcular Derivada", command=calcular_derivada)
boton_calcular.pack(side="left", padx=10)

boton_limpiar = ctk.CTkButton(frame_botones, text="Limpiar", command=limpiar_campos)
boton_limpiar.pack(side="left", padx=10)

# Campo de salida para mostrar la derivada
salida_derivada = ctk.CTkTextbox(ventana, height=10, width=50, state="disabled")
salida_derivada.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

# Configurar el grid layout
ventana.columnconfigure(1, weight=1)
ventana.rowconfigure(4, weight=1)

# Iniciar el bucle principal de la interfaz gráfica
ventana.mainloop()
