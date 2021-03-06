import tkinter as tk
import pygame
from tkinter.font import Font


class Countdown(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.wm_attributes('-fullscreen', 1)
        self.start = False
        self.text_size = 11
        pygame.init()
        raven = '''
                                                         Once upon
                                                     a midnight dreary,
                                                   while I pondered, weak
                                             and weary, Over many a quaint an
                                       d curious volume of forgotten lore, Whil
                                    e I nodded, nearly napping, suddenly there
                                    came a tapping, As of some one gently rapping,
                                                 rapping at my chamber door. .`Tis
                                                     some visitor,. I muttered, .tappi
                                                     ng at my chamber door- Only this, and nothi
                                                     ng mare." Ah, distinctly I remember it was in the
                                                       bleak December, And each separate dying ember wrough
                                                     t its ghost upon the floor. Eagerly I wished the morrow;-
                                                       vainly I had sought to borrow From my books surcease of sor
                                                         row-sorrow for the lost Lenore- For the rare and radiant maid
                                                         en whom the angels name Lenore- Nameless here for evermore. An
                                                         d the silken sad uncertain rustling of each purple curtain Thrilled
                                                         me-filled we with fantastic terrors never felt before; As that now, to
                                                          still the beating of my heart, I stood repeating, .'Tis some visitor en
                                                         treating entrance at my chamber door- Some late visitor entreating entrance
                                                          at my chamber door;- This it is and nothing more." Presently my soul grew s
                                                            tronger; hesitating then no longer, .Sir,. said I, .or Madam, truly your forgiv
                                                            eness I implore; But the fact is I was napping, and so gently you came rapping,
                                                            And so faintly you came tapping, tapping at my chamber door, That I scarce was su
                                                              re I heard you.-here I opened wide the door;- Darkness there, and nothing more.
                                                              Deep into that darkness peering, long I stood there wondering, fearing, Doubting
                                                                 , dreaming dreams no mortals ever dared to dream before; But the silence was u
                                                                   nbroken, and the stillness gave no token, And the only word there spoken was th
                                                                     e whispered word, "Lenore!" This I whispered, and an echo murmured back the word,
                                                                        .Lenore!.- Merely this, and nothing more. Back into the chamber turning, all my so
                                                                           ul within me burning, Soon again I heard a tapping somewhat louder than before. "Sure
                                                                               ly,. said I, "surely that issomething at my window lattice: Let me see, then, what th
                                                                                  erect is, and this mystery explore- Let my heart be still a moment and this mystery expl
                                                                                     ore;- 'Tis the wind and nothing more.. Open here I flung the shutter, when, with many
                                                                                     a flirt and flutter, In there stepped a stately raven of the coin tly days
                                                                                  of yo       re; Not t               he least obeisance made he; not      a min
                                                                               ute stopped      or staye                     d he; But, with mien of lord
                                                                             or lady, perched above my c                         hamber door- Perched upon
                                                                       a bust of Pallas just above my ch                                amber door- Perched, a
                                                                     n d sat, and nothing more. Then th                                    is ebony bird beguili
                                                                   ng my sad fancy into smiling, By the grave and ste                         rn decorum of the co
                                                                untenance it wore. "Though thy crest be shorn and shaven                         , thou,. I said, .a
                                                              rt sure no craven, Ghastly grim and ancient raven wandering                            from the Nightly s
                                                            hore- Tell me what thy lordly name is on the Night's Plutonian                             shore!. Quoth the
                                                         Raven, "Nevermore." Much I marvelled this ungainly fowl to hear discourse                         so plainly, Tho
                                                         ugh its answer little meaning-little relevancy bore; For we cannot help agr                                 eeing t
                                                       hat no living human being Ever yet was blest with seeing bird above his chamb
                                                     er door- Bird or beast upon the sculptured bust above his chamber door, With s
                                                     uch name as "Nevermore." But the raven, sitting lonely on the placid bust, spoke o
                                                     nly That one word, as if his soul in that one word he did outpour. Nothing further t
                                                     hen he uttered-not a feather then he fluttered- Till I scarcely more than mutter ed,
                                                       "other friends have flown before- On the morrow he will leave me, as my hopes have f lo
                                                         wn before." Then the bird said, "Nevermore."

        '''

        self.timeRemLabel = tk.Label(self, text="Time Remaning:", height=1, width=50,background="black",foreground="green",font=("Courier", 20))
        self.timeRemLabel.pack()
        self.label = tk.Label(self, text="", height=1, width=50)
        self.label.pack()
        self.configure(background="black")

        self.remaining = 35
        self.bind('<Escape>', self.escape_key)
        self.bind('<Control-Option-b>', self.bl_key)
        self.bind('<Control-Option-s>', self.br_key)
        self.bind('<Control-Option-m>', self.notification_key)
        self.bind('<Control-Option-p>',self.siren_key)
        self.bind('<Control-Option-h>',self.heartbeat_key)

        # Colors
        self.foreground_color = "green"

        # Sounds
        pygame.mixer.init()
        self.bg_music = pygame.mixer.Sound("bg_music.wav")
        self.heartbeat = pygame.mixer.Sound("heartbeat.wav")
        self.police = pygame.mixer.Sound("police-siren.wav")

        self.text = tk.Text(self, foreground=self.foreground_color,
                            background="black", insertbackground="green",
                            font=("Courier",self.text_size))
        self.text.insert("end", raven)
        self.text.focus()
        self.text.pack(fill="both", expand=True)
        self.display_time()

    def countdown(self):
        sound = None
        if self.remaining == 35:
            self.bg_music.set_volume(0.3)
            self.bg_music.play()
        elif self.remaining == 30:
            self.heartbeat.set_volume(0.3)
            self.heartbeat.play(loops=-1)
        elif self.remaining == 20:
            self.heartbeat.set_volume(0.6)
        elif self.remaining == 10:
            self.heartbeat.set_volume(1.0)
        elif self.remaining <= 0:
            self.label.configure(text="time's up!", font=("Courier", 44),
                                 foreground="red")
            self.text = ""
            self.bg_music.stop()
            self.heartbeat.stop()
            self.police.set_volume(1.0)
            self.police.play()
            self.start = False
        if self.start:
            self.display_time()
            self.remaining -= 1
            self.after(1000, self.countdown)

    def display_time(self):
        x = self.remaining
        seconds = x % 60
        x //= 60
        minutes = x % 60
        x //= 60
        hours = x % 24
        self.label.configure(text= "%02d:%02d:%02d" % (hours,minutes,seconds),
                             background="black", foreground=self.foreground_color,
                             font=("Courier", 44))
        if self.start:
            if self.text_size != 44:
                self.text_size = 44
                self.text.delete(1.0,"end")
                self.text.configure(font=("Courier", self.text_size))

    def escape_key(self,event):
        print("Quitting...")
        self.destroy()
    def bl_key(self,event):
        print("True...")
        if not self.start:
            self.start = True
            self.countdown()
        #self.remaining -=1
    def br_key(self,event):
        print("False...")
        if self.start:
            self.start = False
    def notification_key(self,event):
        sound = pygame.mixer.Sound("notification.wav")
        sound.set_volume(1.0)
        sound.play()
    def siren_key(self,event):
        if self.remaining == 0:
            self.siren.play()
    def heartbeat_key(self,event):
        sound = pygame.mixer.Sound("heartbeat.wav")
        sound.play()
    def heartbeat(self):
        sound = pygame.mixer.Sound("heartbeat.wav")
        sound.play()



if __name__ == "__main__":

    app = Countdown()

    app.mainloop()
