import random
import playsound

lista = ['ex021a.mp3', 'ex021b.mp3', 'ex021c.mp3' ]
musica = random.choice(lista)
playsound.playsound(musica)