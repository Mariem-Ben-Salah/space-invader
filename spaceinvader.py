"""Header
Quoi : Space invader
Qui : Mariem Ben Salah
"""




""" --- Importation des modules --- """
from tkinter import *
from tkinter import messagebox
import time
import random

"""_______________________________________________________________________"""

""" --- Classe --- """
class action :
    
    def __init__(self,id,coords):
        self.id =id
        self.coords = coords
        
    # decale l'instance d'un dy ou d'un dx 
    def decaler(self,dx,dy,indice):
        if (indice == "Tir"):
            self.coords = (self.coords[0] + dx, self.coords[1] + dy) 
            canevas.coords(self.id, self.coords[0], self.coords[1])
            
        if ((indice == "vaisseau") | (indice == "alien")):
            self.coords = (self.coords[0] + dx, self.coords[1] + dy) 
            canevas.coords(self.id, self.coords[0], self.coords[1])
            
    #rafraichit les positions d'une instance
    def poser(self,x,y, indice):
        self.coords = (x,y)
        if (indice == "vaisseau"):
            canevas.coords(self.id,self.coords[0],self.coords[1])
        if (indice == "Tir"):
            canevas.coords(self.id,self.coords[0],self.coords[1])

    def supprimer(self):
        canevas.delete(self.id)
        
      # Créer les instances  
    def créer(self, indice):
        
        if (indice == "s_coope"):
            self.id = canevas.create_image(10, 10, anchor = NW, image = s_coope_img)
            canevas.coords(self.id, self.coords[0], self.coords[1])

            
        if (indice == "vaisseau"):
            self.id = canevas.create_image(10, 10, anchor = NW, image = vaisseau_img)
            canevas.coords(self.id, self.coords[0], self.coords[1])

        if (indice == "alien"):
            photo = eval('alien_img'+str(random.randint(1,4)))
            self.id = canevas.create_image(10, 10, anchor = NW, image = photo )
            canevas.coords(self.id, self.coords[0], self.coords[1])

        if (indice == "Tir"):
            self.id = canevas.create_image(10, 10, anchor = NW, image = tir_v_img)
            canevas.coords(self.id, self.coords[0], self.coords[1])

        if (indice == "Tir_a"):
            self.id = canevas.create_image(10, 10, anchor = NW, image = tir_a_img)
            canevas.coords(self.id, self.coords[0], self.coords[1])
            
        if (indice == "bloc"):
            self.id = canevas.create_image(10, 10, anchor = NW, image = bloc_img)
            canevas.coords(self.id, self.coords[0], self.coords[1])

def credits():
    messagebox.showinfo('Crédits','Mariem Ben Salah \n 3ETI \n CPE Lyon')
    
""" --- Les fonctions --- """ 
#Gestion evenements clavier
def Clavier(event):
    touche = event.keysym
    
    #Déplacement vers la droite
    if ((touche == 'Right') and (vaisseau.coords[0] <= 790)):
        vaisseau.decaler(40,0,"vaisseau")

    #Déplacement vers la gauche
    if ((touche == 'Left') and (vaisseau.coords[0] >= 40)):
        vaisseau.decaler(-40,0,"vaisseau")

    #Tir allié  
    if touche == 'space': 
        Tir.poser(vaisseau.coords[0]+15,vaisseau.coords[1]-20, "Tir")

  

    


        
def main():
    global dx, vies, choc, compteur, score, number
    
    #Gestion alien
    for i in range(0,15):
        alien = eval("alien"+str(i))

        # gestion des bords
        if (alien.coords[0] > 830 and  alien.coords[0] < 900):
            dx = -3
        if alien.coords[0] < 0:
            dx = 3
            choc = 1

        # si le tire touche un alien
        if (abs(Tir.coords[0]-alien.coords[0])<40 and abs(Tir.coords[1]-alien.coords[1])<40):
            Tir.poser(-30,-30,"Tir")
            alien.poser(2000,2000,"alien")
            compteur -= 1
            score += 50
            l2.configure(text= "Score: "+str(score))
        alien.decaler(dx,0,"alien")
        
    #Gestion Bloc
    for i in range (30):
        bloc = eval("bloc"+str(i))

        # si un tir du vaisseau touche un bloc 
        if (abs(Tir.coords[0]-bloc.coords[0])<40 and abs(Tir.coords[1]-bloc.coords[1])<40):
            bloc.poser(2000,2000,"Tir")
            Tir.poser(-30,-30,"Tir")

        # si un tir d'un alien touche le bloc
        if (abs(Tir_a.coords[0]-bloc.coords[0])<40 and abs(Tir_a.coords[1]-bloc.coords[1])<40):
            bloc.poser(2000,2000,"Tir")
            Tir_a.poser(-30,-30,"Tir")
            number = 1

    #Deplacement vertical        
    if choc == 1: 
         choc = 0

         # Pour chaque alien
         for i in range (15):
             alien = eval("alien"+str(i))
             alien.decaler(0,60,"alien")
             
             # Si l'alien touche le fond
             if(alien.coords[1] > 490 and alien.coords[1] < 700):
                vies -= 1
                alien.poser(1000,1000,"alien")
                l3.configure(text = "Vies: "+str(vies))

                # Si le vaisseau n'a pas de vie
                if (vies == 0):
                    results = canevas.create_text(340, 260, fill = "red", text = "Tu as perdu\n"+"Score: "+str(score), font = ('Arial', '35'))
                    return

    #Gestion victoire
    if compteur == 0:
        results = canevas.create_text(340, 260, fill = "green", text = "Tu as gagné\n"+"Score: "+str(score), font = ('Arial', '35'))
        return

    #Si le tir d'un alien touche le vaisseau
    if ((abs(Tir_a.coords[0]-vaisseau.coords[0]) < 20) and (abs(Tir_a.coords[1]-vaisseau.coords[1]) < 20)):
        vies -= 1
        l3.configure(text = "Vies: "+str(vies))

        #Si le vaisseau n'a plus de vie
        if (vies == 0):
            results = canevas.create_text(340, 260, fill = "red", text = "Tu as perdu\n"+"Score: "+str(score), font = ('Arial', '35'))
            return

    #Gestion création tir alien
        # si le tir touche le fond ou touche un bloc ou le vaisseau
    if ((Tir_a.coords[1] > 575) or ((abs(Tir_a.coords[0]-vaisseau.coords[0]) < 20) and (abs(Tir_a.coords[1]-vaisseau.coords[1]) < 20)) or number == 1):
        n = random.randint(0, 9)
        alien = eval("alien"+str(n))
        Tir_a.poser(alien.coords[0]+15,alien.coords[1]-20, "Tir")
        number = 0

    # Déplacements tirs
    Tir.decaler(0,dy,"Tir")
    Tir_a.decaler(0,-dy,"Tir")

    # Gestion de la s_coope
    s_coope.decaler(-2,0,"alien")
    if s_coope.coords[0] < -50 :
        s_coope.poser(2000,1,"alien")
    
    # Gestion collision s_coope et tir vaisseau
    if (abs(Tir.coords[0]-s_coope.coords[0]) < 35) and (abs(Tir.coords[1]-s_coope.coords[1]) < 20):
        score += 150
        s_coope.decaler(0,-150,"alien")
        Tir.decaler(-30,-30,"Tir")


    
    #Repete cette fonction
    Mf.after(20,main)


  




"""_______________________________________________________________________"""

dx = 3 # deplacement horizental
vies = 3 #nb de vies du joueur
dy = -7 # déplacement vertical
choc = 0
compteur = 15 # nombre alien qui existent 
score = 0
number = 0  # pour savoir si un tir alien touche un bloc

#Création d'une fenètre
Mf = Tk()
Mf.geometry('1000x800')
Mf.title('Space invader')
Mf['bg'] = 'DodgerBlue3'

#Création d'un menu
mainmenu = Menu(Mf)
menu1 = Menu(mainmenu,tearoff = 0)
menu1.add_command(label = "Jouer", command = main)
menu1.add_command(label = "Quitter", command = Mf.destroy)
mainmenu.add_cascade(label = "Commandes", menu = menu1)
menu2 = Menu(mainmenu, tearoff = 0)
menu2.add_command(label = "A propos", command = credits )
mainmenu.add_cascade(label = " Aide", menu = menu2)
Mf.config(menu = mainmenu)


#Création des Frames
f1 = Frame(Mf,bg='cornsilk2', relief='groove', borderwidth = 2)
f1.pack(side = 'right', padx = 150, pady = 20 )
f2 = Frame(Mf, bg='brown4', relief = 'groove', borderwidth = 2)
f2.pack(side = 'top', padx = 20, pady = 10)

#Création d'un widget canvaset des images
s_coope_img = PhotoImage(file = "s_coope.png")
alien_img1 = PhotoImage(file = "alien.png")
alien_img2 = PhotoImage(file = "alien2.png")
alien_img3 = PhotoImage(file = "alien3.png")
alien_img4 = PhotoImage(file = "alien4.png")
vaisseau_img = PhotoImage(file = "vaisseau.png")
tir_a_img =  PhotoImage(file = "tir_alien.png")
tir_v_img =  PhotoImage(file = "tir_vaisseau.png")
bloc_img =  PhotoImage(file = "bloc.png")
photo = PhotoImage(master = Mf, file = 'space.png')
canevas = Canvas(Mf,bg='maroon', width = 860, height = 575)
canevas.create_image(100,100, image = photo)
canevas.focus_set()
canevas.bind('<Key>',Clavier)
canevas.pack(padx=30,pady=30)

# Création des Label
l2 = Label(f2, text = 'Score: 0', fg='black')
l2.pack(side = 'right', padx=50, pady = 20)
l3 = Label(f2, text = 'Vies: '+str(vies), fg='black')
l3.pack(side = 'left',padx=50, pady = 20)

#Création des boutons
BoutonJouer = Button(f1, text = 'Jouer', relief = 'groove', command = main)
BoutonJouer.pack(side = 'top' , padx = 50, pady = 50)

BoutonQuitter = Button(f1, text='Quitter', relief = 'groove' , command = Mf.destroy)
BoutonQuitter.pack(side = 'bottom', padx = 30, pady = 50)

#Création d'un alien
for j in range(3):
    for i in range(5):
        vars()['alien'+str(i+j*5)] = action("alien"+str(i+j*5), (50+i*100,60+60*j))
        vars()['alien'+str(i+j*5)].créer("alien")

#Création blocs
for j in range(2):
    for i in range(5):
        for k in range(3):
            vars()['bloc'+str(k*10+i+j*5)] = action("bloc"+str(i+j*5), (50+ k*270 + i*40, 400 + 40*j))
            vars()['bloc'+str(k*10+i+j*5)].créer("bloc")
        

# Création d'un vaisseau
vaisseau = action("vaisseau", (400,520))
vaisseau.créer("vaisseau")

# Création d'un tir
Tir = action("Tir", (-30,-30))
Tir.créer("Tir")

# Création d'un tir alien
Tir_a = action("Tir_a", (-40,-40))
Tir_a.créer("Tir_a")

# Création de la s_coope
s_coope = action("s_coope",(2000,8))
s_coope.créer("s_coope")

Mf.mainloop()

