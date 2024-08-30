from tkinter import Tk, Label, Button, Frame, TOP, LEFT, HORIZONTAL, Scale, Checkbutton, BooleanVar

class Surlignage(Button):
    def __init__(self, master, **kw):
        super().__init__(master, **kw)  # Initialisation de la classe parente

        self.bind("<Enter>", lambda event: self.curseur_entree())
        self.bind("<Leave>", lambda event: self.curseur_sortie())


    def curseur_entree(self):
        self.configure(bg="white", fg="black")

    def curseur_sortie(self):
        self.configure(bg="black", fg="white")

class MainMenu:
    def __init__(self):
        self.fen = Tk()
        self.var_IA_difficulty = 0
        self.var_Fullscreen = BooleanVar()
        self.fen["bg"] = "black"
        self.fen.title("Pong - Menu")
        self.main_frame = Frame(self.fen, bg="black")
        self.main_frame.pack(padx=20, pady=20)
        self.label_titre = Label(self.main_frame, text="Pong : ", bg="black", fg="white")
        self.label_titre.pack(side=TOP, pady=10)
        self.frame_difficulte = Frame(self.main_frame, bg="black")
        self.frame_difficulte.pack(pady=5)
        self.label_difficulte = Label(self.frame_difficulte, text="Difficulté IA : ", bg="black", fg="white")
        self.label_difficulte.pack(side=LEFT)

        def get_slider_value(val):
            self.var_IA_difficulty = val

        self.slider_difficulte = Scale(self.frame_difficulte, orient=HORIZONTAL, bg="black", fg="white", from_=0, to=5,
                                       command=get_slider_value)
        self.slider_difficulte.set(value=3)
        self.slider_difficulte.pack(side=LEFT)

        self.frame_check = Frame(self.main_frame, bg="black")
        self.frame_check.pack(pady=10)
        self.label_fullscreen = Label(self.frame_check, text="Fullscreen : ", bg="black", fg="white")
        self.label_fullscreen.pack(side=LEFT)
        self.check_fullscreen = Checkbutton(self.frame_check, bg="black", activebackground="black", variable=self.var_Fullscreen)
        self.check_fullscreen.pack(side=LEFT)


        self.frame_button = Frame(self.main_frame, bg="white")
        self.frame_button.pack(pady=10)
        self.button_jeu = Surlignage(self.frame_button, text="Jeu", padx=20, pady=5, bg="black", fg="white", command=self.fen.destroy)
        self.button_jeu.pack(padx=1, pady=1)


        """
        self.frame_outside_pong = Frame(self.main_frame, bg="white")
        self.frame_outside_pong.pack(pady=10)
        self.frame_inside_pong = Frame(self.frame_outside_pong, bg="black")
        self.frame_inside_pong.pack(padx=1, pady=1)
        self.frame_jeu = Frame(self.frame_inside_pong, bg="black")
        self.frame_jeu.pack(padx=5, pady=10)
        self.paddle_left = Label(self.frame_jeu, bg="white", padx=5)
        self.paddle_left.pack(side=LEFT)
        self.button_jeu = Button(self.frame_jeu, text="Jeu", padx=20, pady=5, bg="black", fg="white", command=self.fen.destroy)
        self.button_jeu.pack(padx=5, side=LEFT)
        self.paddle_right = Label(self.frame_jeu, bg="white", padx=5)
        self.paddle_right.pack(padx=1, pady=1, side=LEFT)
        """


        self.fen.mainloop()



    def get_ai_difficulty(self):
        return int(self.var_IA_difficulty)

    def get_fullscreen(self):
        return self.var_Fullscreen.get()