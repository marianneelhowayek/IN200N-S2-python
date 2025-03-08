import tkinter as tk
import random as rd

def choisir_couleur():
    global couleur_choix
    couleur_choix = input("Choisit une couleur \n")

def dess_cercle():
    centre_x = rd.randint(50, canva_width - 50)
    centre_y = rd.randint(50, canva_height - 50)
    canvas.create_oval(centre_x - 50, centre_y - 50, centre_x + 50, centre_y + 50, fill= couleur_choix)

def dess_carre():
    centre_x = rd.randint(50, canva_width - 50)
    centre_y = rd.randint(50, canva_height - 50)
    canvas.create_rectangle(centre_x - 50, centre_y - 50, centre_x + 50, centre_y + 50, fill= couleur_choix)

def dess_croix():
    centre_x = rd.randint(50, canva_width - 50)
    centre_y = rd.randint(50, canva_height - 50)
    canvas.create_line(centre_x, centre_y - 50, centre_x, centre_y + 50, fill= couleur_choix)
    canvas.create_line(centre_x - 50, centre_y, centre_x + 50, centre_y, fill= couleur_choix)

couleur_choix = "blue"

racine = tk.Tk()
racine.title("Mon dessin")

canva_width = 600
canva_height = 400
canvas = tk.Canvas(racine, bg= "black", height=canva_height, width=canva_width)

couleur = tk.Button(racine, text= "Choisir une couleur", font= ("helvetica", "11", "bold"), command= choisir_couleur)
cercle = tk.Button(racine, text= "Cercle", font= ("helvetica", "11", "bold"), command= dess_cercle)
carre = tk.Button(racine, text= "Carre", font= ("helvetica", "11", "bold"), command= dess_carre)
croix = tk.Button(racine, text= "Croix", font= ("helvetica", "11", "bold"), command= dess_croix)

canvas.grid(row= 1, column= 1, rowspan= 3)
couleur.grid(row= 0, column= 1)
cercle.grid(row= 1, column= 0)
carre.grid(row= 2, column= 0)
croix.grid(row= 3, column= 0)

racine.mainloop()