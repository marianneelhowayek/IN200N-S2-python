import tkinter as tk

racine = tk.Tk()
racine.title("Mon dessin")

canvas = tk.Canvas(racine, bg="black", height=500, width=500)

couleur = tk.Button(racine, text="Choisir une couleur", font=("helvetica", "11"))
cercle = tk.Button(racine, text="Cercle", font=("helvetica", "11"))
carre = tk.Button(racine, text="Carré", font=("helvetica", "11"))
croix = tk.Button(racine, text="Croix", font=("helvetica", "11"))

canvas.grid(row= 7, column= 3)
couleur.grid(row= 0, column= 3)
cercle.grid(row= 3, column= 0)
carre.grid(row= 5, column= 0)
croix.grid(row= 6, column= 0)


# canvas.create_oval(x - 50, y0 + 50, x + 50, y0 - 50)
# canvas.create_rectangle()

racine.mainloop()