import tkinter as tk
import time

tk.CENTER
window = tk.Tk()
n = int(0) 

window.geometry("500x300")
window.title("Reloj")
window.resizable(False, False)
window.config(bg = "black")


while n==0:
	hora = tk.Label (window)
	hora.config (bg = "white", font = ("Arial", 30), text= "Hla")
	hora.place (relx = 0.5, rely = 0.5, anchor = "center")
	n = n+1
	time.sleep(0.1)
	hora.destroy()




window.mainloop()