import tkinter as tk

class Application(object):
    def __init__(self):
        self.couleurs = ['white','black','red','orange','yellow','blue','cyan','green','pink','magenta']
        self.fenetre = tk.Tk()
        self.couleur_actuelle = "black"
        self.fenetre.geometry("1920x1080")
        self.fenetre.resizable(0, 0)
        self.fenetre.config(bg="#A1A1A1")
        self.fenetre.title("PaintPY_Sean")
        self.fenetre.state('zoomed')
        self.frame_principal = tk.Frame(self.fenetre)
        self.frame_principal.pack(side=tk.LEFT, padx=5,pady=5)
        
        self.generer_grid()
        
        self.frame_secondaire = tk.Frame(self.fenetre,bg="#A1A1A1")
        self.frame_secondaire.pack(side=tk.LEFT,padx=5,pady=5)

        self.label_couleur_actuelle = tk.Label(self.frame_secondaire, text=f"Couleur actuelle : {self.couleur_actuelle}")
        self.label_couleur_actuelle.grid(row=0,column=1,pady=5,padx=5)

        self.bouton_clear_grid = tk.Button(self.frame_secondaire, text=f"Clear la page", command=self.generer_grid)
        self.bouton_clear_grid.grid(row=0,column=2,pady=5,padx=5)

        for ligne, item in enumerate(self.couleurs):
            tk.Button(self.frame_secondaire, bg=item, text=f'    ', command=lambda couleur=item: self.methode_couleur_actuelle(couleur)).grid(row=ligne,column=0,pady=5)  

    def changer_couleur(self, row, column):
        tk.Button(self.frame_principal, text=f"     ", borderwidth=1, relief=tk.SOLID, bg=self.couleur_actuelle, command=lambda row=row, column=column: self.changer_couleur(row, column)).grid(column=column, row=row)
    
    def methode_couleur_actuelle(self, couleur):
        self.couleur_actuelle = couleur
        self.label_couleur_actuelle.config(text=f"Couleur actuelle : {self.couleur_actuelle}")

    def generer_grid(self):
        for colonne in range(40):
            for ligne in range(40):
                tk.Button(self.frame_principal, text=f"     ", borderwidth=1, relief=tk.SOLID, bg='white', command=lambda row=ligne, column=colonne: self.changer_couleur(row, column)).grid(column=colonne, row=ligne)

if __name__ == "__main__":
    app = Application()
    app.fenetre.mainloop()