from tkinter import *
from time import *
from random import  *
#
#
# La fonction qui incrémente les cookies lors du click sur le bouton click
def aclick():
    global cookie, cookieParClick, golden, click, goldenNow, cps 
    if goldenNow == True:
        cookie += cookieParClick*1000
        nbCookies.set("Vous avez "+str(cookie)+" not(cookies)\n"+str(cps)+" cookie/sec")
        goldenNow = False
    else:
        cookie += cookieParClick
        nbCookies.set("Vous avez "+str(cookie)+" not(cookies)\n"+str(cps)+" cookie/sec")
    
    if golden==True:
        random = randint(0,999)
        if random == 0:
            random = -1
            click.destroy()
            click = Button(canvas, text="click", width=25, height=5, bg="yellow", command=aclick)
            click.pack(padx=410, pady=100)
            goldenNow = True
        else:
            random = -1
            click.destroy()
            click = Button(canvas, text="click", width=25, height=5, bg="red", command=aclick)
            click.pack(padx=410, pady=100)
    
            
            
    
# Les fonctions qui gère l'achats des gains automatiques
def gm():
    global nbgm, prixgm, proggm, cookie, cps, apportgm
    if cookie >= prixgm :
        nbgm += 1
        cookie -= prixgm
        prixgm = int(prixgm*proggm)
        proggm += 0.01
        gmtext.set("Grand-mères \n"+str(nbgm)+"\n"+"Prix : "+str(prixgm)+"\n +"+str(apportgm)+" cookies/Grand-mère")
        cps += apportgm
        nbCookies.set("Vous avez "+str(cookie)+" not(cookies)\n"+str(cps)+" cookie/sec")
    
def farm():
    global nbfarm, prixfarm, progfarm, cookie, cps, apportfarm
    if cookie >= prixfarm :
        nbfarm += 1
        cookie -= prixfarm
        prixfarm = int(prixfarm*progfarm)
        progfarm += 0.01
        farmtext.set("Ferme à cookies \n"+str(nbfarm)+"\n"+"Prix : "+str(prixfarm)+"\n +"+str(apportfarm)+" cookies/farm")
        cps += apportfarm
        nbCookies.set("Vous avez "+str(cookie)+" not(cookies)\n"+str(cps)+" cookie/sec")
        
def mine():
    global nbmine, prixmine, progmine, cookie, cps, apportmine
    if cookie >= prixmine :
        nbmine += 1
        cookie -= prixmine
        prixmine = int(prixmine*progmine)
        progmine += 0.01
        minetext.set("Mine\n"+str(nbmine)+"\n"+"Prix : "+str(prixmine)+"\n +"+str(apportmine)+" cookies/mine")
        cps += apportmine
        nbCookies.set("Vous avez "+str(cookie)+" not(cookies)\n"+str(cps)+" cookie/sec")
        
def usine():
    global nbusine, prixusine, progusine, cookie, cps, apportusine
    if cookie >= prixusine:
        nbusine += 1
        cookie -= prixusine
        prixusine = int(prixusine*progusine)
        progusine += 0.01
        usinetext.set("Usine\n"+str(nbusine)+"\n"+"Prix : "+str(prixusine)+"\n +"+str(apportusine)+" cookies/usine")
        cps += apportusine
        nbCookies.set("Vous avez "+str(cookie)+" not(cookies)\n"+str(cps)+" cookie/sec")
        
def bank():
    global nbbank, prixbank, progbank, cookie, cps, apportbank
    if cookie >= prixbank:
        nbbank += 1
        cookie -= prixbank
        prixbank = int(prixbank*progbank)
        progbank += 0.01
        banktext.set("Bank\n"+str(nbbank)+"\n"+"Prix : "+str(prixbank)+"\n +"+str(apportbank)+" cookies/bank")
        cps += apportbank
        nbCookies.set("Vous avez "+str(cookie)+" not(cookies)\n"+str(cps)+" cookie/sec")
        
def temple():
    global nbtemple, prixtemple, progtemple, cookie, cps, apporttemple
    if cookie >= prixtemple:
        nbtemple += 1
        cookie -= prixtemple
        prixtemple = int(prixtemple*progtemple)
        progtemple += 0.01
        templetext.set("Temple\n"+str(nbtemple)+"\n"+"Prix : "+str(prixtemple)+"\n +"+str(apporttemple)+" cookies/temple")
        cps += apporttemple
        nbCookies.set("Vous avez "+str(cookie)+" not(cookies)\n"+str(cps)+" cookie/sec")
        
        
def amelioClickUn():
    global cookieParClick, cookie, cps, amelioClickDeux
    if cookie >= 500:
        cookieParClick *= 2
        cookie -= 500
        nbCookies.set("Vous avez "+str(cookie)+" not(cookies)\n"+str(cps)+" cookie/sec")
        amelioClickUn.destroy()
        #amelioClickDeux.pack(side=LEFT, padx=10, ipady=15)
        
def amelioGmUn():
    global cookie, apportgm, cps, nbgm
    if cookie >= 5000:
        apportgm *= 2
        cookie -= 5000
        cps += nbgm
        nbCookies.set("Vous avez "+str(cookie)+" not(cookies)\n"+str(cps)+" cookie/sec")
        gmtext.set("Grand-mères \n"+str(nbgm)+"\n"+"Prix : "+str(prixgm)+"\n +"+str(apportgm)+" cookies/Grand-mère")
        amelioGmUn.destroy()
        
def amelioClickOr():
    global cookie, golden, cps
    if cookie >= 15000:
        cookie -= 15000
        golden = True
        nbCookies.set("Vous avez "+str(cookie)+" not(cookies)\n"+str(cps)+" cookie/sec")
        amelioClickOr.destroy()
        
def amelioFarmUn():
    global cookie, apportfarm, cps, nbfarm
    if cookie >= 12000:
        apportfarm *= 2
        cookie -= 12000
        cps += nbfarm
        nbCookies.set("Vous avez "+str(cookie)+" not(cookies)\n"+str(cps)+" cookie/sec")
        farmtext.set("Ferme\n"+str(nbfarm)+"\n"+"Prix : "+str(prixfarm)+"\n +"+str(apportfarm)+" cookies/farm")
        amelioFarmUn.destroy()

def amelioClickDeux():
    global cookieParClick, cookie, cps, amelioClickDeux
    if cookie >= 2500:
        cookie -= 2500
        cookieParClick *= 2
        nbCookies.set("Vous avez "+str(cookie)+" not(cookies)\n"+str(cps)+" cookie/sec")
        amelioclickDeux.destroy()



        
        
        
        
# La fonction qui incrémente les cookies périodiquement suivant les améliorations automatiques (1s)
def cookieParSeconde() :
    global cookie, apportgm, nbgm, apportfarm, nbfarm, apportmine, nbmine, apportusine, nbusine, apportbank, nbbank, apporttemple, nbtemple, cps
    cps = (nbgm*apportgm)+(nbfarm*apportfarm)+(nbmine*apportmine)+(nbusine*apportusine)+(nbbank*apportbank)+(nbtemple*apporttemple)
    cookie += cps
    nbCookies.set("Vous avez "+str(cookie)+" not(cookies)\n"+str(cps)+" cookie/sec")
    clicker.after(1000,cookieParSeconde)
    

#cookies
cookie = 100000
#cookies/click
cookieParClick = 1
#golden button activé?
golden = False
#golden maintenant?
goldenNow = False
#grand-mères
nbgm = 0
#prix des grand-mères
prixgm = 10
#variable qui fait augmenter exponentiellement le prix des Grand-mères
proggm = 1.1
#le nombre de cookies par seconde apporté par grand-mère
apportgm = 1
#pareil que au dessus mais pour les fermes
nbfarm = 0
prixfarm = 1000
progfarm = 1.1
apportfarm = 15
#mine
nbmine = 0
prixmine = 55000
progmine = 1.1
apportmine = 230
#usine
nbusine = 0
prixusine = 300000
progusine = 1.1
apportusine = 970
#bank
nbbank = 0
prixbank = 1250000
progbank = 1.1
apportbank = 5600
#temple
nbtemple = 0
prixtemple = 20000000
progtemple = 1.1
apporttemple = 25000
#cookie/sec
cps = 0
 
#Création page tkinter
clicker = Tk()
clicker.title("not(cookie) clicker")
clicker.geometry("1000x800")

#fond de page
canvas = Canvas(clicker, width=1000, height=800,)
canvas.place(x=0,y=0)

amelio = LabelFrame(canvas, text="Amélioration permanante de production")
amelio.pack(fill="both", padx=50, pady=40, side=TOP, ipady=25)

#texte nombre de cookies
nbCookies = StringVar()
nbCookies.set("Vous avez "+str(cookie)+" not(cookies)")

#affichage texte nb cookies
cookies = Label(clicker, textvariable=nbCookies)
cookies.pack(pady=300)

#Bouton click + lance aclick()
click = Button(canvas, text="click", width=25, height=5, bg="red", command=aclick)
click.pack(padx=410,pady=100)

#Frame des amélioration auto
autoAmelio = LabelFrame(clicker, text="Amélioration des not(cookies) automatiques")
autoAmelio.pack(fill="both", expand="yes", padx=50, pady=40, side=BOTTOM)

#texte du bouton d'achat de Grand-mères
gmtext = StringVar()
gmtext.set("Grand-mères \n"+str(nbgm)+"\n"+"Prix : "+str(prixgm)+"\n +"+str(apportgm)+" cookies/Grand-mère")

#Bouton grand-mère
gm = Button(autoAmelio, textvariable=gmtext, command=gm)
gm.pack(side=LEFT, padx= 10)

#texte du bouton d'achat de ferme
farmtext = StringVar()
farmtext.set("Ferme\n"+str(nbfarm)+"\n"+"Prix : "+str(prixfarm)+"\n +"+str(apportfarm)+" cookies/farm")

#bouton ferme
farm = Button(autoAmelio, textvariable=farmtext ,command=farm )
farm.pack(side=LEFT, padx=10)

minetext = StringVar()
minetext.set("Mine\n"+str(nbmine)+"\n"+"Prix : "+str(prixmine)+"\n +"+str(apportmine)+" cookies/mine")

mine = Button(autoAmelio, textvariable=minetext, command=mine)
mine.pack(side=LEFT, padx=10)

usinetext = StringVar()
usinetext.set("Usine\n"+str(nbusine)+"\n"+"Prix : "+str(prixusine)+"\n +"+str(apportusine)+" cookies/usine")


usine = Button(autoAmelio, textvariable=usinetext, command=usine)
usine.pack(side=LEFT, padx=10)

banktext = StringVar()
banktext.set("Bank\n"+str(nbbank)+"\n"+"Prix : "+str(prixbank)+"\n +"+str(apportbank)+" cookies/bank")

bank = Button(autoAmelio, textvariable=banktext, command=bank)
bank.pack(side=LEFT, padx=10)

templetext = StringVar()
templetext.set("Temple\n"+str(nbtemple)+"\n"+"Prix : "+str(prixtemple)+"\n +"+str(apporttemple)+" cookies/temple")

temple = Button(autoAmelio, textvariable=templetext, command=temple)
temple.pack(side=LEFT, padx=10)

amelioClickUntext = StringVar()
amelioClickUntext.set("Amélioration de clic \nLe gain de cookie par click \nest doublé\nPrix : 500 cookies")

amelioClickUn = Button(amelio, textvariable=amelioClickUntext, command=amelioClickUn)
amelioClickUn.pack(side=LEFT, padx=10, ipady=15)

amelioGmUntext = StringVar()
amelioGmUntext.set("Amélioration de la production\nde cookie des Grand-mères\nLa production est doublée\n Prix : 5000")

amelioGmUn = Button(amelio, textvariable=amelioGmUntext, command=amelioGmUn)
amelioGmUn.pack(side=LEFT, padx=10, ipady=15)

amelioFarmUntext = StringVar()
amelioFarmUntext.set("Amélioration de la production\nde cookie des Fermes\n La production est doublée\n 12000")

amelioFarmUn = Button(amelio, textvariable=amelioFarmUntext, command=amelioFarmUn)
amelioFarmUn.pack(side=LEFT, padx=10, ipady=15)

amelioClickOrtext = StringVar()
amelioClickOrtext.set("Donne une chance sur 1000 d'avoir \nle bouton 'Click' dorée qui donne \n1000 fois plus de cookie\n Prix : 15000")

amelioClickOr = Button(amelio, textvariable=amelioClickOrtext, command=amelioClickOr)
amelioClickOr.pack(side=LEFT, padx=10, ipady=15)

amelioClickDeuxtext = StringVar()

amelioClickDeuxtext.set("Amélioration de clic \nLe gain de cookie par click \nest doublé\nPrix : 2500 cookies WIP")
amelioClickDeux = Button(amelio, textvariable=amelioClickDeuxtext, command=amelioClickDeux)



#Lance cookieParSeconde()
cookieParSeconde()

mainloop()



