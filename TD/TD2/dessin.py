import tkinter as tk

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