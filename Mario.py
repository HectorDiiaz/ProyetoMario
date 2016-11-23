# -*- coding: utf-8 -*-
#utf para no tener problemas con las tildes

from tkinter import *
from random import randint
import pickle #para cargar/guardar la partida

#CLASE ENEMIGO TORTUGA SIMPLE
class Enemigo:

	def __init__(self, canvas, v2):
		self.enemigo1 = 0
		self.type = "tortuga" #id enemigo
		self.eliminado = False #para borrar la imagen
		self.velocidadx = 3 #velocidad horizontal
		self.gravedadafter = 0 #control de gravedad
		self.v2 = v2 #tk()
		self.canvas = canvas
		self.ene = PhotoImage(file="img/tortuga1.png").zoom(2)
		self.ene2 = PhotoImage(file="img/tortuga2.png").zoom(2)
		inicio=[[45, 105],[561, 105]] #posicion inicial
		n=randint(0,1) #random sale izquierda o derecha

		self.spriteinscreen = canvas.create_image(inicio[n][0],inicio[n][1], image=self.ene, anchor = CENTER)
		#random camina hacia la izquierda o derecha
		if (randint(0, 1) == 0):
			self.movimiento = "derecha"
			self.lastmovimiento = "derecha"

			self.canvas.itemconfig(self.spriteinscreen, image = self.ene2 )
		else:
			self.movimiento = "izquierda"
			self.lastmovimiento = "izquierda" #cuando se detiene esto almacena hacia donde estaba caminando

		self.estado = "gravedadactiva"

		self.gravedad() #activa la gravedad

	#Funcion que se encarga de todo el movimiento del enemigo
	def gravedad(self):
		if not self.eliminado:
			x=0
			if(self.movimiento == "izquierda"):
				x=-self.velocidadx
			elif self.movimiento == "derecha":
				x=self.velocidadx
			try:
				posx = self.canvas.coords(self.spriteinscreen)[0]
			except:
				posx = [0,0]

			#si se sale por la derecha de la pantalla aparece en la izquierda, y lo contrario
			if posx > 600:
				self.canvas.move(self.spriteinscreen, -600, 0)
			elif posx < 0:
				self.canvas.move(self.spriteinscreen, 600, 0)

			self.canvas.move(self.spriteinscreen, x, 0)

			#si la gravedad esta activa baja al enemigo
			if(self.estado=="gravedadactiva"):
				self.canvas.move(self.spriteinscreen, 0, 10)

			self.gravedadafter = self.canvas.after(50, self.gravedad)

	#elimina el enemigo
	def eliminar(self):
		self.eliminado=True
		self.ene = 0
		self.ene2= 0

#CLASE ENEMIGO TORTUGA ROJA, NECESITA 2 GOLPES PARA MORIR, mismos comentarios que los de enemigo 1
class Enemigo2:

	def __init__(self, canvas, v2):
		self.enemigo1 = 0
		self.v2 = v2
		self.velocidadx = 3
		self.type = "tortugaroja"
		self.canvas = canvas
		self.eliminado = False
		self.ene = PhotoImage(file="img/tortugaop1.png").zoom(2)
		self.ene2 = PhotoImage(file="img/tortugaop2.png").zoom(2)
		self.golpes = 0
		inicio=[[45, 105],[561, 105]]
		n=randint(0,1)
		self.spriteinscreen = canvas.create_image(inicio[n][0],inicio[n][1], image=self.ene, anchor = CENTER)
		if (randint(0, 1) == 0):
			self.lastmovimiento = "derecha"
			self.movimiento = "derecha"
			self.canvas.itemconfig(self.spriteinscreen, image = self.ene2 )
		else:
			self.lastmovimiento = "izquierda"
			self.movimiento = "izquierda"

		self.estado = "gravedadactiva"

		self.gravedad()


	def gravedad(self):
		if not self.eliminado:
			x=0
			if(self.movimiento == "izquierda"):
				x=-self.velocidadx
			elif self.movimiento == "derecha":
				x=self.velocidadx

			#python estaba dando problemas entonces use try para que no salieran
			try:
				posx = self.canvas.coords(self.spriteinscreen)[0]
			except:
				posx = [0, 0]

			if(posx > 600):
				self.canvas.move(self.spriteinscreen, -600, 0)
			elif(posx < 0):
				self.canvas.move(self.spriteinscreen, 600, 0)

			self.canvas.move(self.spriteinscreen, x, 0)

			if(self.estado=="gravedadactiva"):
				self.canvas.move(self.spriteinscreen, 0, 10)

			self.gravedadafter=self.canvas.after(50, self.gravedad)

	def eliminar(self):
		self.ene = 0
		self.ene2= 0
		self.eliminado=True


#CLASE PARA LA MOSCA QUE SALTA
class Enemigo3:

	def __init__(self, canvas, v2):

		self.enemigo1 = 0
		self.velocidadx = 3
		self.type = "mosca"
		self.y=10
		self.eliminado = False
		self.v2 = v2
		self.saltando=False
		self.impulsoy = 0
		self.veces = 0
		self.estadoy="arriba" #controla el movimiento vertical
		self.subiendo=True
		self.canvas = canvas
		self.ene = PhotoImage(file="img/mosca.png").zoom(2)
		inicio=[[45, 105],[561, 105]]
		n=randint(0,1)
		self.spriteinscreen = canvas.create_image(inicio[n][0],inicio[n][1], image=self.ene, anchor = CENTER)
		if (randint(0, 1) == 0):
			self.movimiento = "derecha"
			self.lastmovimiento = "derecha"
		else:
			self.movimiento = "izquierda"
			self.lastmovimiento = "izquierda"

		self.estado = "gravedadactiva"
		self.gravedad()
		self.canvas.after(2000, self.animarsaltar) #comienza la secuencia de salto
		self.moverdi()


	def animarsaltar(self):
		self.impulsoy = 70 #impulso de salto
		self.saltar()
		self.canvas.after(3000, self.animarsaltar)

	#funcion que controla el movimiento del enemigo
	def saltar(self):

		if(self.impulsoy>0):
			self.estado = "gravedadinactiva"
			self.saltando = True
			self.canvas.move(self.spriteinscreen, 0, -10)
			self.impulsoy-=10
			self.canvas.after(50, self.saltar)


		else:
			self.saltando=False
			self.estado = "gravedadactiva"

	#movimiento horizontal del enemigo
	def moverdi(self):
		x = 0
		if (self.movimiento == "izquierda"):
			x = -self.velocidadx
		elif self.movimiento == "derecha":
			x = self.velocidadx
		try:
			posx = self.canvas.coords(self.spriteinscreen)[0]
		except:
			posx = [0,0]
		if (posx > 600):
			self.canvas.move(self.spriteinscreen, -600, 0)
		elif (posx < 0):
			self.canvas.move(self.spriteinscreen, 600, 0)

		self.canvas.move(self.spriteinscreen, x, 0)
		self.canvas.after(50, self.moverdi)

	#Mantiene al enemigo pegado al suelo
	def gravedad(self):
		if not self.eliminado:
			if (self.estado == "gravedadactiva"):
				self.canvas.move(self.spriteinscreen, 0, 8)
			self.gravedadafter = self.canvas.after(100, self.gravedad)
	#para borrar al enemigo
	def eliminar(self):
		self.ene = 0
		self.eliminado = True



#CLASE PARA EL CANGREJO QUE CONGELA EL PISO
class Enemigo4:

	def __init__(self, canvas, tk):
		self.enemigo1 = 0
		self.velocidadx = 3
		self.eliminado=False
		self.type = "cangrejo"
		self.canvas = canvas
		self.yausocongelar = False
		self.ene = PhotoImage(file="img/cagrejo1.png").zoom(2)

		inicio=[[45, 105],[561, 105]]
		n=randint(0,1)
		self.spriteinscreen = canvas.create_image(inicio[n][0],inicio[n][1], image=self.ene, anchor = CENTER)
		if (randint(0, 1) == 0):
				self.movimiento = "derecha"
				self.lastmovimiento = "derecha"
		else:
			self.lastmovimiento ="izquierda"
			self.movimiento = "izquierda"

		self.estado = "gravedadactiva"

		self.gravedad() #activa la gravedad

	#control de movimiento
	def gravedad(self):
		x = 0
		if not self.eliminado: #reviso si aun sigue en pantalla
			if (self.movimiento == "izquierda"):
				x = -self.velocidadx
			elif self.movimiento == "derecha":
				x = self.velocidadx
			try: #daba error si no habia nada entonces uso try
				posx = self.canvas.coords(self.spriteinscreen)[0]
			except:
				posx = [0, 0]

			if (posx > 600):
				self.canvas.move(self.spriteinscreen, -600, 0)
			elif (posx < 0):
				self.canvas.move(self.spriteinscreen, 600, 0)

			self.canvas.move(self.spriteinscreen, x, 0)

			if (self.estado == "gravedadactiva"):
				self.canvas.move(self.spriteinscreen, 0, 10)

			self.canvas.after(50, self.gravedad)

	def eliminar(self):
		self.eliminado = True
		self.ene = 0


#				   CLASS JUGADOR
class Player:

	#Inicio todas las variables que necesitare para controlar a Player
	def __init__(self, nombre, canvas):
		self.estado = "gravedadactiva" #gravedad
		self.estado2 = "derecha" #Movimiento horizontal
		self.name = nombre
		self.saltando = False
		self.vidas = 3
		self.puntos = 0
		self.velocidad = 10 #velocidad de movimiento horizontal
		#Impulso de salto
		self.impulsoy = 0 #impulso de salto inicial, por defecto 0
		self.dirimages = "img/"+nombre+"/"
		#Nombres de las imagenes para usar
		self.sprites = [self.name+"1",self.name+"1i"]
		#Arreglo donde guardo imagenes una vez cargadas
		self.spritesloaded = []
		for sprite in self.sprites:
			self.spritesloaded.append( PhotoImage(file=self.dirimages+sprite+".png").zoom(2))

		#Guardo del canvas para usarlo en otras funciones
		self.canvas = canvas
		#constante de gravedad
		self.gravedadacc = 10
		#Referencia de la imagen en pantalla
		self.spriteinscreen = self.canvas.create_image(300, 460, image=self.spritesloaded[0], anchor = CENTER)

		#Activo la gravedad
		self.gravedad()


	def moverDerecha(self, e):
		self.canvas.itemconfig(self.spriteinscreen, image= self.spritesloaded[0])
		#mover derecha
		self.canvas.move(self.spriteinscreen, self.velocidad, 0)
		#Si se sale de la pantalla por la derecha, sale por la izquierda
		posx = self.canvas.coords(self.spriteinscreen)[0]
		if (posx > 600):
			self.canvas.move(self.spriteinscreen, -600, 0)


	def moverIzquierda(self,e):
		self.canvas.itemconfig(self.spriteinscreen, image= self.spritesloaded[1])

		#mover izquierda
		self.canvas.move(self.spriteinscreen, -self.velocidad, 0)
		#si se sale por la izquierda sale por la derecha
		posx = self.canvas.coords(self.spriteinscreen)[0]
		if (posx < 0):
			self.canvas.move(self.spriteinscreen, 600, 0)


	def gravedad(self):
		if(self.estado=="gravedadactiva"):
			#mover hacia abajo
			self.canvas.move(self.spriteinscreen, 0, self.gravedadacc)


	def animarsaltar(self, e):
		#impulso con el que salta
		if not self.saltando:
			self.impulsoy = 160
			#lo hago saltar
			self.saltar()


	def saltar(self):
		#Si tiene impulso salta
		if(self.impulsoy>0):
			self.estado = "gravedadinactiva"
			self.saltando = True
			self.canvas.move(self.spriteinscreen, 0, -self.gravedadacc)
			self.impulsoy-=10
			self.canvas.after(50, self.saltar)
		#Sino activo la gravedad
		else:
			self.saltando=False
			self.estado = "gravedadactiva"
			self.gravedad()


#				CLASS GAME
class Game:

	def __init__(self):
		self.enemigos = []
		self.jugadores = []
		self.nivel = 1
		self.powerup =0
		self.bow = 1 #pow
		self.tareasprogramadas = []
		self.nivelclear=False #para saber si no hay mas enemigos en cada nivel
		self.v3=False
		self.dificultad = 1 #dificultad, por defecto 1=facil


	def menu(self):
		self.v1 = Tk()

		canvas = Canvas(self.v1, width=600, height=454)  # tamaño self.v1
		canvas.pack()  # necesario para que el canvas funcione

		self.v1.title("Mario Bros")  # titulo
		canvas.config(bg="black")  # color de fondo
		Fondo = PhotoImage(file="Menu.png")
		lblImagen = Label(self.v1, image=Fondo).place(x=0, y=0)
		# Crear botones
		btnJugar = Button(self.v1, text="JUGAR", command=self.comenzarJuego, font=("Agency FB", 14), width=15, height=1).place(
			x=230, y=210)

		btnJugar = Button(self.v1, text="Dificultad", command=self.dificultadv, font=("Agency FB", 14), width=15,
						  height=1).place(
			x=230, y=260)

		btnControles = Button(self.v1, text="CONTROLES", command=self.controles, font=("Agency FB", 14), width=15,
							  height=1).place(x=230, y=310)
		btnSalir = Button(self.v1, text="SALIR", command=self.salir, font=("Agency FB", 14), width=15, height=1).place(x=230, y=360
																												  )
		self.v1.mainloop()
	#Aqui establezco la dificultad, que seria el movimiento horizontal de los enemigos (px/50ms)
	def dificultadelegir1(self):
		self.dificultad = 1
		self.newWindow2.destroy()


	def dificultadelegir2(self):
		self.dificultad = 2
		self.newWindow2.destroy()

	def dificultadelegir3(self):
		self.dificultad = 4
		self.newWindow2.destroy()


	def dificultadv(self):
		self.newWindow2 = Toplevel(self.v1)

		self.canvas = Canvas(self.newWindow2, width=600, height=450)  # tamaño ventana
		self.canvas.pack()  # necesario para que el canvas funcione

		self.newWindow2.title("Dificultad")  # titulo
		self.canvas.config(bg="black")  # color de fondo

		btnBack = Button(self.newWindow2, text="Facil", command=self.dificultadelegir1, font=("Agency FB", 14), width=10,
						 height=1).place(x=200, y=100)
		btnBack = Button(self.newWindow2, text="Normal", command=self.dificultadelegir2, font=("Agency FB", 14),
						 width=10,
						 height=1).place(x=200, y=200)
		btnBack = Button(self.newWindow2, text="Dificil", command=self.dificultadelegir3, font=("Agency FB", 14),
						 width=10,
						 height=1).place(x=200, y=300)

	def salir(self):
		self.ventana.destroy()


	def quitarco(self):
		self.newWindow.destroy()

	def controles(self):
		self.newWindow = Toplevel(self.v1)

		self.canvas = Canvas(self.newWindow, width=600, height=450)  # tamaño ventana
		self.canvas.pack()  # necesario para que el canvas funcione

		self.newWindow.title("Controles")  # titulo
		self.canvas.config(bg="black")  # color de fondo

		self.imgControles = PhotoImage(file="Menucontroles.png")
		EtiquetaImagen = Label(self.newWindow, image=self.imgControles).place(x=0, y=0)
		btnBack = Button(self.newWindow, text="Atras", command=self.quitarco, font=("Agency FB", 14), width=10, height=1).place(x=450, y=380)


	#Detecta si el objeto esta tocando alguna paltaforma
	def detecthitenemy(self, objeto, meta = False):

		#Posiciones de las plataformas
		det1 = self.canvas.find_overlapping(389, 376, 599, 391)
		det2 = self.canvas.find_overlapping(189, 394, 0, 380)
		det3 = self.canvas.find_overlapping(120, 256, 454, 273) #piso de la mitad
		det4 = self.canvas.find_overlapping(3, 126, 235, 142) #piso arriba izquierda
		det5 = self.canvas.find_overlapping(389, 126, 599, 142)#piso arriba derecha
		det6 = self.canvas.find_overlapping(0, 500, 596, 514)#piso de ladrillos
		det9 = self.canvas.find_overlapping(281, 388,313,421)#piso de ladrillos



		#Que plataforma esta tocando
		cond1= objeto in det1
		cond2 = objeto in det2
		cond3 = objeto in det3
		cond4 = objeto in det4
		cond5 = objeto in det5
		cond6 = objeto in det6
		cond7 = False
		cond8 = False
		cond9 = objeto in det9

		#Para saber si los enemigos llegaron a las tuberias de abajo y terminaron su recorrido
		if meta:
			det7 = self.canvas.find_overlapping(2, 496, 64, 469)  # piso de ladrillos
			det8 = self.canvas.find_overlapping(540, 464, 596, 500)#piso de ladrillos
			cond8=objeto in det7
			cond8=objeto in det8

		#Detecto si el objeto esta tocando alguna de las 6 plataformas
		if ( cond1 or cond2 or cond3 or cond4 or cond5 or cond6 or cond7 or cond8 or cond9):
			#retorno true or false de si esta tocando, para cada plataforma
			return [True, cond4, cond5, cond3,cond1, cond2, cond6, cond7, cond8, cond9]
		return [False,  cond4, cond5, cond3,cond1, cond2, cond6, cond7, cond8, cond9]

	#funcion que detecta las colisiones de todo lo que pasa en el juego
	def detecthit(self):

		for player in self.jugadores:
			actualplayer = player.spriteinscreen
		#detecta a los enemigos y las plataformas
			for enemy in self.enemigos:
				ancho = player.spritesloaded[0].width()
				posplayer = player.canvas.coords(player.spriteinscreen)
				posenemy = self.canvas.coords(enemy.spriteinscreen)

				if(posplayer[0]+ancho>posenemy[0] and posplayer[0]-ancho < posenemy[0] and posplayer[1]+30>posenemy[1] and posplayer[1]-30 < posenemy[1]):
					#Si el enemigo ya fue golpeado una vez se puede matar si no pierdo vida
					if enemy.movimiento == "quieto":
						self.canvas.delete(enemy.spriteinscreen)
						self.enemigos.remove(enemy)
						self.detectarnivel()

						player.puntos += 10

						#Si reuno 40 puntos, agrego una vida
						if(player.puntos%40 == 0):
							player.vidas +=1
							if player.name == "mario":
								self.canvas.itemconfig(self.mario2, text=str(self.jugadores[0].vidas) + " vidas")
							else:
								self.canvas.itemconfig(self.luigi2, text=str(self.jugadores[1].vidas) + " vidas")

						if player.name == "mario":
							self.canvas.itemconfig(self.mario3, text=str(self.jugadores[0].puntos) + " puntos")
						else:
							self.canvas.itemconfig(self.luigi3, text=str(self.jugadores[1].puntos) + " puntos")


					else:
						#sino entonces pierdo una vida
						player.vidas -=1


						#aqui quito vidas si tocan un enemigo que sigue vivo
						if player.name == "mario":
							self.canvas.itemconfig(self.mario2, text=str(self.jugadores[0].vidas) + " vidas")
						else:
							self.canvas.itemconfig(self.luigi2, text=str(self.jugadores[1].vidas) + " vidas")

						self.canvas.coords(player.spriteinscreen, 300, 470)

				condi = self.detecthitenemy(enemy.spriteinscreen, True)

				#Si estoy tocando el piso, ya no bajo mas
				if (condi[0]):
					enemy.estado = "gravedadinactiva"

				else:
					enemy.estado = "gravedadactiva"

				#Si es un cangrejo congela el piso
				if enemy.type=="cangrejo":
					if not enemy.yausocongelar:


						if(posenemy[0]<305 and posenemy[1]<132):
							if(not pisocongelado[0]):
								pisocongelado[0]=True
								enemy.yausocongelar = True

							self.dibujarHorizontal("pisoazul", "img/pisoflotante.png", 0, 133, 6)
						elif(posenemy[0]>305 and posenemy[1]<132):
							if (not pisocongelado[1]):
								pisocongelado[1] = True
								enemy.yausocongelar = True

							self.dibujarHorizontal("pisoazul2", "img/pisoflotante.png", 410, 133, 5)

						if posenemy[1]+20>264 and posenemy[1]-20<264:
							if (not pisocongelado[2]):
								pisocongelado[2] = True
								enemy.yausocongelar = True
							self.dibujarHorizontal("pisoazul3", "img/pisoflotante.png", 140, 264, 8)
				try:
					if condi[7] or condi[8]: #Si se sale de la pantalla los saca del nivel, por que ya llegaron a las tuberias de abajo
						self.canvas.delete(enemy.spriteinscreen)
						self.enemigos.remove(enemy)
						self.detectarnivel()
						#le quito una vida y puntos a los jugadores por dejar ganar al enemigo
						self.jugadores[0].vidas-=1
						self.jugadores[1].vidas -= 1
						self.jugadores[0].puntos -=20
						self.jugadores[1].puntos -= 20

						#actualizo los textos
						self.canvas.itemconfig(self.mario2, text=str(self.jugadores[0].vidas) + " vidas")
						self.canvas.itemconfig(self.mario3, text=str(self.jugadores[0].puntos) + " puntos")
						self.canvas.itemconfig(self.luigi2, text=str(self.jugadores[1].vidas) + " vidas")
						self.canvas.itemconfig(self.luigi3, text=str(self.jugadores[1].puntoss) + " puntos")



				except:
					pass


			#Detecta las coliciones de player con las plataformas
			condi = self.detecthitenemy(actualplayer)


			if condi[0]:
				c=0
				player.velocidad = 10 #velocidad horizontal

				#si toco la caja pow, entonces lo hago si me quedan usos
				if condi[9]:
					if self.bow>0:
						self.bow -= 1
						for enemy in self.enemigos:
							enemy.movimiento = "quieto"
							self.canvas.after(3000, self.recuperarmovimiento)
				condi= condi[1:]

				#si estoy en una plataforma congelada entonces mi movimiento es ahora de 2, en lugar de 10
				for elem in condi:
					try:
						if elem == True and pisocongelado[c]==True:
							player.velocidad=2
							break
						else:
							player.velocidad=10

					except:
						pass

					c += 1
				#desactivo la gravedad sino sigo derecho
				if player.estado == "gravedadactiva":
					player.estado="gravedadinactiva"

				elif player.saltando:

					ancho=player.spritesloaded[0].width()
					posplayer = player.canvas.coords(player.spriteinscreen)
					#reviso a cada enemigo para saber si lo golpeo
					for enemy in self.enemigos:
						posenemy= self.canvas.coords(enemy.spriteinscreen)

						#Las tortugas rojas necesitan 2 golpes, aqui hago los condicionales y detecto si golpeo al enemigo desde abajo
						if((posenemy[0]<posplayer[0]+ancho and posenemy[0]>posplayer[0]-ancho) and posenemy[1]<posplayer[1]+70 and posenemy[1]>posplayer[1]-50 ):
							if enemy.type != "tortugaroja":
								enemy.movimiento = "quieto"
							elif enemy.type == "tortugaroja":
								if enemy.golpes == 0:
									enemy.golpes+=1
								else:
									enemy.movimiento = "quieto"


					player.saltando=False
					player.impulsoy=0

					self.canvas.move(player.spriteinscreen, 0, 30)

					player.estado = "gravedadactiva"

			elif not player.saltando:
				player.estado = "gravedadactiva"
				player.gravedad()

		self.canvas.after(50, self.detecthit)

	#detecta si alguno murio, si es asi lo elimina y comienzo desde el nivel1
	def detectarmuerte(self):
		for player in self.jugadores:
			if player.vidas <= 0:
				for enemy in self.enemigos:
					enemy.eliminar()
				self.enemigos = []
				for player in self.jugadores:
					player.vidas = 3
					player.puntos = 0
					player.velocidad=10
				self.nivel = 1
				self.canvas.itemconfig(self.niveltexto, text="Nivel " + str(self.nivel))
				self.canvas.itemconfig(self.mario2, text=str(self.jugadores[0].vidas) + " vidas")
				self.canvas.itemconfig(self.mario3, text=str(self.jugadores[0].puntos) + " puntos")
				self.canvas.itemconfig(self.luigi2, text=str(self.jugadores[1].vidas) + " vidas")
				self.canvas.itemconfig(self.luigi3, text=str(self.jugadores[1].puntos) + " puntos")
				pisocongelado = [False, False, False, False, False, False]
				self.dibujarHorizontal("piso","img/piso.png", 0, 520, 20)
				self.dibujarHorizontal("pisoazul","img/pisoflotante2.png", 0, 133, 6)
				self.dibujarHorizontal("pisoazul2","img/pisoflotante2.png", 410, 133, 5)
				self.dibujarHorizontal("pisoazul3","img/pisoflotante2.png",140, 264, 8)
				self.dibujarHorizontal("pisoazul4","img/pisoflotante2.png", 0, 385, 5)
				self.dibujarHorizontal("pisoazul5","img/pisoflotante2.png", 410, 385, 5)
				
				self.nivel1()
		self.canvas.after(500, self.detectarmuerte)

	#sigue la direccion en la que estaban antes de detenerse
	def recuperarmovimiento(self):
		for enemy in self.enemigos:
			enemy.movimiento = enemy.lastmovimiento

	def comenzarJuego(self):
		self.v1.destroy()
		self.v2 = Tk()

		self.frame = Frame(bg="black")
		self.frame.pack()

		width1 = 600 #ancho
		height1 = 525 #altura

		self.canvas = Canvas(self.frame, width=width1, height=height1)  # tamaño ventana
		self.canvas.pack()  # necesario para que el canvas funcione

		#Dibujo las plataformas
		self.dibujarHorizontal("piso","img/piso.png", 0, 520, 20)
		self.dibujarHorizontal("pisoazul","img/pisoflotante2.png", 0, 133, 6)
		self.dibujarHorizontal("pisoazul2","img/pisoflotante2.png", 410, 133, 5)
		self.dibujarHorizontal("pisoazul3","img/pisoflotante2.png",140, 264, 8)
		self.dibujarHorizontal("pisoazul4","img/pisoflotante2.png", 0, 385, 5)
		self.dibujarHorizontal("pisoazul5","img/pisoflotante2.png", 410, 385, 5)

		#Los tubos de arriba
		tub1=PhotoImage(file="img/tuboentrada1.png").zoom(2)
		self.canvas.create_image(563, 76, image=tub1)

		tub2 = PhotoImage(file="img/tuboentrada2.png").zoom(2)
		self.canvas.create_image(40, 76, image=tub2)

		pow = PhotoImage(file="img/pow.png").zoom(2)
		self.canvas.create_image(297, 403, image=pow)

		#Los tubos de abajo
		tub3 = PhotoImage(file="img/tubosalida.png").zoom(2)
		self.canvas.create_image(34, 482, image=tub3)

		tub4 = PhotoImage(file="img/tubosalida2.png").zoom(2)
		self.canvas.create_image(573, 482, image=tub4)

		#texto nivel
		self.niveltexto = self.canvas.create_text(277, 289,  anchor="nw", fill="red")
		if self.nivel <=5:
			self.canvas.itemconfig(self.niveltexto, text="Nivel "+str(self.nivel))
		else:
			self.canvas.itemconfig(self.niveltexto, text="Ganaste!")


		#Creo al jugador
		self.jugadores.append(Player("mario", self.canvas))
		self.jugadores.append(Player("luigi", self.canvas))

		# Se agregan los textos
		self.mario = self.canvas.create_text(140, 10, anchor="nw", fill="red")
		self.canvas.itemconfig(self.mario, text="Mario")
		self.luigi = self.canvas.create_text(250, 10, anchor="nw", fill="red")
		self.canvas.itemconfig(self.luigi, text="Luigi")

		self.mario2 = self.canvas.create_text(140, 30, anchor="nw", fill="red")
		self.canvas.itemconfig(self.mario2, text=str(self.jugadores[0].vidas) + " vidas")
		self.luigi2 = self.canvas.create_text(250, 30, anchor="nw", fill="red")
		self.canvas.itemconfig(self.luigi2, text=str(self.jugadores[0].vidas) + " vidas")

		self.mario3 = self.canvas.create_text(140, 40, anchor="nw", fill="red")
		self.canvas.itemconfig(self.mario3, text=str(self.jugadores[0].puntos) + " puntos")
		self.luigi3 = self.canvas.create_text(250, 40, anchor="nw", fill="red")
		self.canvas.itemconfig(self.luigi3, text=str(self.jugadores[0].puntos) + " puntos")

		#Configuro la ventana y el canvas
		self.v2.title("Mario Bros")  # titulo
		self.canvas.config(bg="black")  # color de fondo

		#Asigno las teclas con los movimientos
		self.v2.bind("d", self.jugadores[0].moverDerecha)
		self.v2.bind("a", self.jugadores[0].moverIzquierda)
		self.v2.bind("w", self.jugadores[0].animarsaltar)
		self.v2.bind("<Button-1>", self.callback)

		self.v2.bind("<Right>", self.jugadores[1].moverDerecha)
		self.v2.bind("<Left>", self.jugadores[1].moverIzquierda)
		self.v2.bind("<Up>", self.jugadores[1].animarsaltar)

		Button(self.v2, text="guardar", command=self.guardarjuego, font=("Agency FB", 12), width=4, height=1).place(
			x=344, y=9)
		Button(self.v2, text="cargar", command=self.cargarjuego, font=("Agency FB", 12), width=4, height=1).place(
			x=394, y=9)
		self.detectarmuerte()

		#Funcion  que detecta todas las colisiones del juego
		self.detecthit()
		self.nivel1()
		#loop de la ventana
		self.v2.mainloop()

	def callback(self, event):
		print("clicked at", event.x, event.y)

	#FUNCION PARA GUARDAR JUEGO
	def guardarjuego(self):
		datos = [self.nivel,
				 self.jugadores[0].vidas,
				 self.jugadores[0].puntos,
				 self.jugadores[1].vidas,
				 self.jugadores[1].puntos,
				 ]
		#guardo en archivo
		with open('partidaguardada.txt', 'wb') as f:
			pickle.dump(datos, f)

	#Funcion para el boton CARGAR JUEGO
	def cargarjuego(self):

		with open('partidaguardada.txt', 'rb') as f:
			datos = pickle.load(f)
			for enemy in self.enemigos:
				enemy.eliminar()

			self.enemigos = []
			self.nivel=datos[0]
			self.jugadores[0].vidas = datos[1]
			self.jugadores[0].puntos = datos[2]
			self.jugadores[1].vidas = datos[3]
			self.jugadores[1].puntos = datos[4]
			self.canvas.itemconfig(self.niveltexto, text="Nivel "+ str(self.nivel))
			#actualizo todos los textos
			self.canvas.itemconfig(self.mario2, text=str(self.jugadores[0].vidas) + " vidas")
			self.canvas.itemconfig(self.mario3, text=str(self.jugadores[0].puntos) + " puntos")
			self.canvas.itemconfig(self.luigi2, text=str(self.jugadores[1].vidas) + " vidas")
			self.canvas.itemconfig(self.luigi3, text=str(self.jugadores[1].puntos) + " puntos")

			if self.nivel == 1:
				self.nivel1()
			elif self.nivel==2:
				self.nivel2()
			elif self.nivel==3:
				self.nivel3()
			elif self.nivel==4:
				self.nivel4()
			elif self.nivel==5:
				self.nivel5()

	#Funcion para dibujar una imagen repetidamente (la uso para dibujar las plataformas)
	def dibujarHorizontal(self,name, imagen, x , y, nveces):

		imagenes[name] = PhotoImage(file=imagen).zoom(2)
		#ancho de la imagen
		width = imagenes[name].width()
		#dibujo la imgen n veces, una al lado de la otra
		for n in range(0, nveces):
			self.canvas.create_image(x+(n*width), y, image=imagenes[name])


	#Las siguientes 4 funciones son usadas para agregar enemigos a los niveles
	def agregartortuga(self):
		x=Enemigo(self.canvas, self.v2)
		x.velocidadx=self.dificultad+2
		self.enemigos.append(x)


	def agregartortuga2(self):
		x = Enemigo2(self.canvas, self.v2)
		x.velocidadx = self.dificultad +2
		self.enemigos.append(x)


	def agregarmosca(self):
		x = Enemigo3(self.canvas, self.v2)
		x.velocidadx = self.dificultad +2
		self.enemigos.append(x)


	def agregarcangrejo(self):
		x = Enemigo4(self.canvas, self.v2)
		x.velocidadx = self.dificultad +2
		self.enemigos.append(x)

	#para terminar tareas proramadas
	def eliminartareas(self):
		self.v2.update_idletasks()

	#Detecta si ya termine el nivel y me manda al siguiente
	def detectarnivel(self):

		if self.enemigos == []:
			if self.nivel == 1:
				self.nivel += 1
				self.eliminartareas()
				self.nivel2()


			elif self.nivel == 2:
				self.nivel += 1
				self.eliminartareas()
				self.nivel3()

			elif self.nivel == 3:
				self.nivel += 1
				self.eliminartareas()
				self.nivel4()
			elif self.nivel == 4:
				self.eliminartareas()
				self.nivel = 5
				self.nivel5()
			elif self.nivel == 5:
				self.canvas.itemconfig(self.niveltexto, text="GANASTE")

	def nivel1(self):
		self.bow = 1
		self.canvas.itemconfig(self.niveltexto, text="Nivel 1")
		pisocongelado = [False, False, False, False, False, False]
		#proramo el orden en que salen los enemigos
		self.tareasprogramadas.append(self.canvas.after(2000, self.agregartortuga))
		self.tareasprogramadas.append(self.canvas.after(4000, self.agregartortuga))
		self.tareasprogramadas.append(self.canvas.after(6000, self.agregartortuga))
		self.tareasprogramadas.append(self.canvas.after(7000, self.agregartortuga))

	def nivel2(self):
		self.bow = 1
		pisocongelado = [False, False, False, False, False, False]
		self.tareasprogramadas.append(self.canvas.itemconfig(self.niveltexto, text="Nivel 2"))
		self.tareasprogramadas.append(self.canvas.after(2000, self.agregartortuga))#añado los enemigos
		self.tareasprogramadas.append(self.canvas.after(3000, self.agregartortuga2))
		self.tareasprogramadas.append(self.canvas.after(5000, self.agregartortuga2))
		self.tareasprogramadas.append(self.canvas.after(7000, self.agregartortuga))
		self.tareasprogramadas.append(self.canvas.after(9000, self.agregartortuga))
		#programo el powerup
		self.powerupimg = PhotoImage(file="img/powerup.png").zoom(2)

		self.canvas.after(4000, self.aparecerpowerup)
		self.canvas.after(8000, self.eliminarpowerup)

	#Para saber si algun player a tomado el powerup
	def detectarhitpower(self):
		det=self.canvas.find_overlapping(self.xpower, 353, self.xpower - 36, 389) #si esta tocando la caja
		for player in self.jugadores:
			if player.spriteinscreen in det:
				self.canvas.itemconfig(self.powerup, image='') #lo elimino
				self.bow = 3 #lo dejo usar la caja pow 3 veces


		self.powerupafter = self.canvas.after(50, self.detectarhitpower)
	#funcion para agregar en pantalla el powerup
	def aparecerpowerup(self):
		x = randint(50,400)
		self.xpower = x

		self.detectarhitpower()
		self.powerup = self.canvas.create_image(x, 353, image=self.powerupimg)

	#lo elimina de la pantalla
	def eliminarpowerup(self):
		self.canvas.after_cancel(self.powerupafter)
		self.canvas.itemconfig(self.powerup, image='')
	#Añado los enemigos del nivel 3
	def nivel3(self):
		self.bow = 1
		pisocongelado = [False, False, False, False, False, False]
		self.canvas.itemconfig(self.niveltexto, text="Nivel 3")
		self.canvas.after(2000, self.agregartortuga2)#añado enemigos
		self.canvas.after(4000, self.agregartortuga)
		self.canvas.after(6000, self.agregartortuga)
		self.canvas.after(10000, self.agregartortuga2)
		self.canvas.after(14000, self.agregartortuga)
		self.canvas.after(16000, self.agregartortuga)

		self.powerupimg = PhotoImage(file="img/powerup.png").zoom(2)

		self.canvas.after(8000, self.aparecerpowerup)
		self.canvas.after(10000, self.eliminarpowerup)
	#añado enemigos del nivel 4
	def nivel4(self):
		self.bow = 1
		pisocongelado = [False, False, False, False, False, False]
		self.canvas.itemconfig(self.niveltexto, text="Nivel 4")
		self.canvas.after(2000, self.agregartortuga)#añado los enemigos
		self.canvas.after(4000, self.agregartortuga)
		self.canvas.after(6000, self.agregartortuga2)
		self.canvas.after(8000, self.agregarmosca)
		self.canvas.after(10000, self.agregartortuga)
		self.canvas.after(12000, self.agregarmosca)

		self.powerupimg = PhotoImage(file="img/powerup.png").zoom(2)
		#añado el powerup
		self.canvas.after(1000, self.aparecerpowerup)
		self.canvas.after(3000, self.eliminarpowerup)


	#enemigos nivel 5
	def nivel5(self):
		self.bow = 1
		pisocongelado = [False, False, False, False, False, False]
		self.canvas.itemconfig(self.niveltexto, text="Nivel 5")

		pow = PhotoImage(file="img/pow.png").zoom(2)
		self.canvas.create_image(297, 403, image=pow)
		#añado los enemigos
		self.canvas.after(11000, self.agregartortuga)
		self.canvas.after(2000, self.agregarcangrejo)
		self.canvas.after(5000, self.agregartortuga)
		self.canvas.after(9000, self.agregartortuga)
		self.canvas.after(14000, self.agregartortuga)




#Inicia el juego
global imagenes, pisocongelado, juego
#Aqui se guardan las imagenes de los enemigos, sino se borran
imagenes = {}
#los pisos que congela los cangrejos
pisocongelado = [False, False, False, False, False, False]

#inicio Game
juego = Game()
#arranco por el menu
juego.menu()
