import tkinter as tk 
import customtkinter
from tkinter import font
import yt
import threading

titulo = ""
url = ""

app = tk.Tk()
app.geometry("720x240")
app.resizable(width=False, height=False)
app.configure(bg="gray")

def verificar_hilo():
    if tarea.is_alive():
        app.after(100, verificar_hilo)
    else:
        btn_buscar.configure(state=tk.NORMAL)
        btn_musica.configure(state=tk.NORMAL)
        btn_video.configure(state=tk.NORMAL) 
        busqueda.configure(state=tk.NORMAL)
        progressbar.stop()


def buscar():
    global url
    global titulo
    url = busqueda.get()
    titulo = yt.nombre(url)
    label_inf.configure(text=titulo)
    print(url)

def hilos(selection,formato=None):
    global tarea
    global url
    progressbar.start()
    btn_buscar.configure(state=tk.DISABLED)
    btn_musica.configure(state=tk.DISABLED)
    btn_video.configure(state=tk.DISABLED)
    if selection == 0:
        busqueda.configure(state=tk.DISABLED)
        tarea = threading.Thread(target=buscar)
        tarea.start()
    elif selection == 1:
        tarea = threading.Thread(target=yt.musica, args=(url,))
        tarea.start()
    elif selection == 2:
        tarea = threading.Thread(target=yt.video, args=(url,formato))
        tarea.start()
    verificar_hilo()
        
def abrir_ventana_secundaria():
    # Crear una ventana secundaria.
    ventana_secundaria = tk.Toplevel()
    ventana_secundaria.title("Ventana secundaria")
    ventana_secundaria.configure(bg="gray")
    ventana_secundaria.geometry("950x100")
    ventana_secundaria.resizable(width=False, height=False)

    btn_cerrar = customtkinter.CTkButton(ventana_secundaria, text="Cerrar ventana", command=ventana_secundaria.destroy)
    btn_cerrar.pack(side="bottom", padx=10, pady=10, anchor="s")
    
    # Botones para diferentes calidades de video
    for calidad in ["1080", "720", "480", "360", "240", "144"]:
        btn_video = customtkinter.CTkButton(ventana_secundaria, text=f"{calidad}p",command=lambda: hilos(2,calidad))
        btn_video.pack(side="right", padx=10, pady=10, anchor="n")

# Entry para la búsqueda
busqueda = customtkinter.CTkEntry(app, corner_radius=9, width=77, font=customtkinter.CTkFont(family="Arial", size=14))
busqueda.pack(side="top", padx=10, pady=10, anchor="center", ipadx=2, ipady=2, fill="x")

label_inf = customtkinter.CTkLabel(app, text="Título",bg_color="transparent",text_color="black", fg_color="lightgray",corner_radius=9)
label_inf.pack(side="top", padx=30, pady=10,fill="both",anchor="w")

# frame

frame_botones = tk.Frame(app, bg="gray")
frame_botones.pack(side=tk.TOP, padx=10, pady=15, fill=tk.X)

frame_botones_top = tk.Frame(frame_botones,bg="gray")
frame_botones_top.pack(side=tk.TOP, padx=10, fill=tk.X)

frame_botones_bottom = tk.Frame(frame_botones,bg="gray")
frame_botones_bottom.pack(side=tk.BOTTOM, padx=10, fill=tk.X)

# botones

btn_buscar = customtkinter.CTkButton(frame_botones_top, text="Buscar", command=lambda: hilos(0,None))
btn_buscar.pack(side=tk.LEFT, padx=20, pady=10,expand=True, fill=tk.BOTH)

btn_musica = customtkinter.CTkButton(frame_botones_top, text="mp3", command=lambda: hilos(1,None))
btn_musica.pack(side=tk.LEFT, padx=20, pady=10,expand=True, fill=tk.BOTH)

btn_video = customtkinter.CTkButton(frame_botones_top, text="mp4", command=abrir_ventana_secundaria)
btn_video.pack(side=tk.LEFT, padx=10, pady=10,expand=True, fill=tk.BOTH)

progressbar = customtkinter.CTkProgressBar(frame_botones_bottom, orientation="horizontal",width=9,mode="indeterminate")
progressbar.pack(side="bottom", padx=10, pady=10,expand=True, fill=tk.BOTH)

app.mainloop()