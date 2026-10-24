import tkinter as tk
import time

tk.CENTER
window = tk.Tk()
n = int(1) 

window.geometry("500x300")
window.title("Reloj")
window.resizable(False, False)
window.config(bg = "black")

hora = tk.Label (window)
hora.config (bg = "white", font = ("Arial", 30), text= n)
hora.place (relx = 0.5, rely = 0.5, anchor = "center")

def actu():
    global n

while n != 20:
    hora.config(text= f"Hora : {n}")
    n+= 1
    print(n)
    time.sleep(1)
    window.after (1000, actu)

window.mainloop()