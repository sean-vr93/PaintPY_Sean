import tkinter as tk
from tkinter import filedialog as tfd
from tkinter import messagebox as tmb
from PIL import Image, ImageTk
import os, PIL

class Application():
    def __init__(self):
        self.fenetre = tk.Tk()
        self.fenetre.config(bg="#A1A1A1")
        self.fenetre.title("PaintPy_Sean")
        self.couleurs = ['white','black','red','orange','yellow','blue','cyan','green','pink','magenta']
        self.filetypes = [("Tous les fichiers","*.*"),(".png","*.png"),(".jpeg","*.jpeg"),(".gif","*.gif"),(".jpg","*.jpg"),(".bmp","*.bmp"),(".ico","*.ico"),(".webp","*.webp"),(".jfif","*.jfif")]
        self.x_precedent, self.y_precedent = None, None
        self.click_pressed_down = False
        self.taille_pixel_actuel = 1
        self.couleur_actuelle = self.couleurs[1]
        ######################################################################
        self.barremenu = tk.Menu(self.fenetre)
        self.fenetre.config(menu = self.barremenu)
        self.fichier_menu = tk.Menu(self.barremenu, tearoff = 0)
        
        self.barremenu.add_cascade(label = "Programme", menu = self.fichier_menu)
        self.fichier_menu.add_command(label = "Nouvelle page", command=self.nouvelle_page)
        self.fichier_menu.add_command(label = "Charger une Image", command=self.charger_image)
        self.fichier_menu.add_command(label = "Sauvegarder une Image", command=self.sauvegarder_image)
        self.fichier_menu.add_separator()
        self.fichier_menu.add_command(label = "Quitter", command=self.quitter)
        
        self.menus_menu = tk.Menu(self.barremenu, tearoff = 0)
        self.barremenu.add_cascade(label = "Menus", menu = self.menus_menu)
        self.menus_menu.add_command(label = "Outils", command=self.lancer_toplevel)
        
        self.apropos_menu = tk.Menu(self.barremenu, tearoff = 0)
        self.barremenu.add_cascade(label = "À propos", menu = self.apropos_menu)
        self.apropos_menu.add_command(label = "Informations", command=self.informations)
        ######################################################################
        self.canvas = tk.Canvas(self.fenetre, width=800, height=800, bd=0, highlightthickness=0, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=1)
        self.canvas.bind("<Configure>", self.configure)
        self.fenetre.bind('<Motion>', self.motion)
        self.fenetre.bind('<Button-1>', self.dessiner)
        self.fenetre.bind('<ButtonRelease-1>', self.dessiner_nope)
        self.fenetre.bind('<Button-3>', self.effacer)
        self.fenetre.bind('<ButtonRelease-3>', self.effacer_nope)
        ######################################################################
        self.lancer_toplevel()
        #####################################################################

    def lancer_app(self):
        self.fenetre.mainloop()
    
    def lancer_toplevel(self):
        self.couleurs_toplevel = tk.Toplevel(self.fenetre)
        self.frame_couleurs = tk.Frame(self.couleurs_toplevel,bg="#A1A1A1")
        self.frame_couleurs.pack(side=tk.TOP,padx=5,pady=5)
        for ligne, item in enumerate(self.couleurs):
            tk.Button(self.frame_couleurs, bg=item, text=f'    ', command=lambda couleur=item: self.methode_couleur_actuelle(couleur)).grid(row=0,column=ligne,pady=5,padx=5)  
        self.label_couleur_actuelle = tk.Label(self.frame_couleurs, text=f"Couleur actuelle : {self.couleur_actuelle}")
        self.label_couleur_actuelle.grid(row=0,column=len(self.couleurs),pady=5,padx=5)
        self.frame_taille_pixels = tk.Frame(self.couleurs_toplevel,bg="#A1A1A1")
        self.frame_taille_pixels.pack(side=tk.TOP,padx=5,pady=5)
        self.bouton_moinsmoinsmoins = tk.Button(self.frame_taille_pixels, text='---', command=lambda plusoumoins="---": self.changer_taille_pixel(plusoumoins)).grid(row=0, column=0, pady=5, padx=5)
        self.bouton_moins = tk.Button(self.frame_taille_pixels, text='-', command=lambda plusoumoins="-": self.changer_taille_pixel(plusoumoins)).grid(row=0, column=1, pady=5, padx=5)
        self.label_taille_pixel_actuel = tk.Label(self.frame_taille_pixels, text=f"Taille actuelle : {self.taille_pixel_actuel}")
        self.label_taille_pixel_actuel.grid(row=0, column=2, pady=5, padx=5)
        self.bouton_plus = tk.Button(self.frame_taille_pixels, text='+', command=lambda plusoumoins="+": self.changer_taille_pixel(plusoumoins)).grid(row=0, column=3, pady=5, padx=5)
        self.bouton_plusplusplus = tk.Button(self.frame_taille_pixels, text='+++', command=lambda plusoumoins="+++": self.changer_taille_pixel(plusoumoins)).grid(row=0, column=4, pady=5, padx=5)

    def configure(self, event):
        w, h = event.width, event.height

    def nouvelle_page(self):
        self.canvas.delete("all")

    def dessiner(self, event):
        self.click_pressed_down = True
        x, y = event.x, event.y
        self.canvas.create_oval(x - self.taille_pixel_actuel, y + self.taille_pixel_actuel, x + self.taille_pixel_actuel, y - self.taille_pixel_actuel, fill=self.couleur_actuelle, outline=self.couleur_actuelle)
    
    def dessiner_nope(self, event):
        self.click_pressed_down = False
        x, y = event.x, event.y
        self.canvas.create_oval(x - self.taille_pixel_actuel, y + self.taille_pixel_actuel, x + self.taille_pixel_actuel, y - self.taille_pixel_actuel, fill=self.couleur_actuelle, outline=self.couleur_actuelle)
    
    def effacer(self, event):
        self.click_pressed_down = True
        x, y = event.x, event.y
        self.canvas.create_oval(x - self.taille_pixel_actuel, y + self.taille_pixel_actuel, x + self.taille_pixel_actuel, y - self.taille_pixel_actuel, fill="white", outline="white")
    
    def effacer_nope(self, event):
        self.click_pressed_down = False
        x, y = event.x, event.y
        self.canvas.create_oval(x - self.taille_pixel_actuel, y + self.taille_pixel_actuel, x + self.taille_pixel_actuel, y - self.taille_pixel_actuel, fill="white", outline="white")
    
    def motion(self, event):
        if self.click_pressed_down == True:
            x, y = event.x, event.y
            self.canvas.create_oval(x - self.taille_pixel_actuel, y + self.taille_pixel_actuel, x + self.taille_pixel_actuel, y - self.taille_pixel_actuel, fill=self.couleur_actuelle, outline=self.couleur_actuelle)
    
    def methode_couleur_actuelle(self, couleur):
        self.couleur_actuelle = couleur
        self.label_couleur_actuelle.config(text=f"Couleur actuelle : {self.couleur_actuelle}")

    def changer_taille_pixel(self, plusoumoins):
        if plusoumoins == "+":
            self.taille_pixel_actuel += 1
        elif plusoumoins == "+++":
            self.taille_pixel_actuel += 5
        elif plusoumoins == "-" and self.taille_pixel_actuel > 0:
            self.taille_pixel_actuel -= 1
        elif plusoumoins == "---":
            if self.taille_pixel_actuel <= 5: 
                self.taille_pixel_actuel = 0
            elif self.taille_pixel_actuel > 5:
                self.taille_pixel_actuel -= 5
        self.label_taille_pixel_actuel.config(text=f"Taille actuelle : {self.taille_pixel_actuel}")
    
    def charger_image(self):
        try:
            self.img = tfd.askopenfilename(title = "Sélectionner une image", filetypes = self.filetypes)
            self.image = PIL.Image.open(self.img)
            self.s = self.image.size
            if self.s[0] > 800 or self.s[1] > 800:
                self.redimmensionner_image()
            self.image = ImageTk.PhotoImage(self.image)
            self.canvas.create_image(0,0,anchor=tk.NW,image=self.image)
        except PIL.UnidentifiedImageError:
            tmb.showerror(title = "Erreur", message = "Le fichier selectionné n'est pas une image.")
        except PermissionError:
            tmb.showerror(title = "Erreur", message = "Vous n'avez pas la permission d'accéder à ce dossier.")

    def sauvegarder_image(self):
        self.canvas.postscript(file = 'img' + '.eps')
        img = Image.open('img' + '.eps')
        img.save('img' + '.png', 'png') 
    
    def redimmensionner_image(self):
        largeur_ratio, hauteur_ratio = 800 / self.s[0], 800 / self.s[1]
        meilleur_ratio = min(largeur_ratio, hauteur_ratio)
        self.w, self.h =  int(round(self.s[0] * meilleur_ratio)), int(round(self.s[1] * meilleur_ratio))
        self.image = self.image.resize((self.w,self.h))
    
    def quitter(self):
        self.fenetre.quit()
        self.fenetre.destroy()
    
    def informations(self):
        tmb.showinfo(title="PaintPy_Sean", message="Script réalisé par Sean vergauwen")

if __name__ == "__main__":
    app = Application()
    app.lancer_app()