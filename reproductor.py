import tkinter as tk
from tkinter import filedialog
import pygame

pygame.mixer.init()
def cargar_cancion():
    cancion = filedialog.askopenfilename(
        title="Elige una cancion",
        filetypes=(("Archivos MP3", "*.mp3"), ("Todos los Archivos", "*.*"))
    )
    if cancion:
        pygame.mixer.music.load(cancion)
        etiqueta_estado.config(text=f"Cargada: {cancion.split('/')[-1]}")
def reproducir():
    pygame.mixer.music.play()
    etiqueta_estado.config(text="Reproduciendo...")
def pausar():
    pygame.mixer.music.pause()
    etiqueta_estado.config(text="Pausada")
def reanudar():
    pygame.mixer.music.unpause()
    etiqueta_estado.config(text="Reanudando...")
def detener():
    pygame.mixer.music.stop()
    etiqueta_estado.config(text="Detenida")

ventana = tk.Tk()
ventana.title("Youtube Music En Python")
ventana.geometry("450x350")
ventana.config(bg="black")

etiqueta_titulo = tk.Label(ventana, text="Youtube Music En Python", font=("comic sans ms", 20), bg="black", fg="white")
etiqueta_titulo.pack(pady=15)

etiqueta_estado = tk.Label(ventana, text="No hay canción cargada", font=("comic sans ms", 12), bg="black", fg="white")
etiqueta_estado.pack(pady=5)

marco_botones = tk.Frame(ventana, bg="black")
marco_botones.pack(pady=20)

btn_cargar = tk.Button(ventana, text="Cargar Canción", command=cargar_cancion, width=15, bg="#3498db", fg="white")
btn_cargar.pack(pady=5)

btn_reproducir = tk.Button(marco_botones, text="▶ Play", command=reproducir, width=8)
btn_reproducir.grid(row=0, column=0, padx=5)

btn_pausar = tk.Button(marco_botones, text="⏸ Pausa", command=pausar, width=8)
btn_pausar.grid(row=0, column=1, padx=5)

btn_reanudar = tk.Button(marco_botones, text="⏯ Reanudar", command=reanudar, width=8)
btn_reanudar.grid(row=1, column=0, padx=5, pady=5)

btn_detener = tk.Button(marco_botones, text="⏹ Stop", command=detener, width=8)
btn_detener.grid(row=1, column=1, padx=5, pady=5)

ventana.mainloop()