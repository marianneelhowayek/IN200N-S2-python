import tkinter as tk

<<<<<<< HEAD
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


canvas.create_oval(x - 50, y0 + 50, x + 50, y0 - 50)
canvas.create_rectangle()

racine.mainloop()
=======
racine = tk.Tk() # Création de la fenêtre racine

label = tk.Label(racine, bg="red", fg="black",
                 text="couleur texte: " + "orange" + "\ncouleur fond: " + "white",
                 padx=100, pady=100, borderwidth=20,
                 font = ("helvetica", "30") 
                )

label1 = tk.Label(racine, text="Choisir une Couleur", font = ("helvetica", "11")) # création d'un widget
label2 = tk.Label(racine, text="cercle", font = ("helvetica", "11")) # création d'un widget
label3 = tk.Label(racine, text="carré", font = ("helvetica", "11")) # création d'un widget
label4 = tk.Label(racine, text="croix", font = ("helvetica", "11")) # création d'un widget

label1.grid(column=5, row=0) # positionnement du premier widget
label2.grid(column=0, row=3) # positionnement du deuxième widget
label3.grid(column=0, row=6) # positionnement du troisième widget
label4.grid(column=0, row=9) # positionnement du quatrième widget

racine.mainloop() # Lancement de la boucle principale
>>>>>>> c1077fdb19f04accaf6efba3ce259f324bdfe6c6
