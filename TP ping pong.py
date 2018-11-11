from random import randint
import tkinter
fenetre = tkinter.Tk()
framerate = 1000//60

#description de la fenetre graphique
couleurFond = "black"
largeurFond = 700
hauteurFond = 400

#description de la balle
xballe=largeurFond/2
yballe=hauteurFond/2
couleurBalle = "red"
rayon = 20
dx=0
dy=0
while -5 < dx < 5 and dy == 0:
    dx = randint(-10,10)
    dy = randint(-2,2)
formeBalle = 1

#description de la raquette 1
largeur = 10
hauteur = 100
xRaquette = 20
yRaquette = 230
couleurRaquette = "blue"
formeRaquette = 0

#descrption de la raquette 2
xRaquette2 = largeurFond - 20
yRaquette2 = 230
formeRaquette2 = 2

#♦descrption de la partie
PartieFinie = False

#Les fonctions
def afficher(couleur,forme):
    if forme == formeBalle:
        dessin.create_oval(xballe-rayon,yballe-rayon,xballe+rayon,yballe+rayon, fill= couleur)
    elif forme == formeRaquette:
        dessin.create_rectangle( xRaquette, yRaquette, xRaquette+largeur, yRaquette+hauteur, fill = couleur)

def bougerBalle():
    global xballe,yballe,dx,dy,PartieFinie
    if PartieFinie == False :
        afficher(couleurFond,formeBalle) 
        xballe += dx
        yballe += dy
        if xballe > largeurFond - 20:
            dx = -dx
        elif yballe > hauteurFond - 20:
            dy = -dy
        elif yballe < 20:
            dy = -dy
        elif xballe < 20:
            PartieFinie = True
        elif 40 < xballe < 50 and yRaquette < yballe < yRaquette+hauteur/2 and dy > 0:
            dx = -dx
            dy = -dy
        elif 40 < xballe < 50 and yRaquette < yballe < yRaquette+hauteur/2 and dy < 0:
            dx = -dx
        elif 40 < xballe < 50 and yRaquette+hauteur/2 < yballe < yRaquette+hauteur and dy > 0:
            dx = -dx
        elif 40 < xballe < 50 and yRaquette+hauteur/2 < yballe < yRaquette+hauteur and dy < 0:
            dx = -dx
            dy = -dy
        afficher(couleurBalle,formeBalle) 
        dessin.after(framerate,bougerBalle)
    elif PartieFinie == True:
        dessin.create_text(largeurFond/2,hauteurFond/2,text="Perdu", fill = "white",justify = "center",font="Times 40")

def bougerRaquette(evennement):
    global xRaquette, yRaquette
    afficher(couleurFond,formeRaquette)
    yRaquette = evennement.y - hauteur/2
    afficher(couleurRaquette,formeRaquette)

dessin = tkinter.Canvas(fenetre, width = largeurFond, height = hauteurFond, bg = couleurFond)
dessin.bind("<Motion>",bougerRaquette)
dessin.pack()
bougerBalle()
fenetre.mainloop()
