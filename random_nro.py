#!/usr/bin/python3 

import math
import numpy as np
from datetime import datetime

a = 17
b = 43
m = 100
seed = 13
lambd = 1
media = 10
devioP = 2
inf = 0
sup = 99

#generates values between 0,99

def generateTime(tipo):
	if tipo == "det" :
		return mcl()
	else :
		return geraDistribuicao(tipo)

def show_params():
	print(a,b,m,seed,lambd,media,devioP,inf,sup)

def set_params(params):
	a,b,m,seed,lambd,media,devioP,inf,sup = params

def mcl():
	global seed
	global a
	global b
	global m

	seed = ((a * seed + b) % m)
	
	return seed    

def geraAleatorio():
	global seed
	global a
	global b
	global m

	seed = int(datetime.now().microsecond + seed)
	seed = ((a * seed + b) % m)
	
	return seed/m

    
def geraDistribuicao(tipo):
	global lambd
	global media
	global devioP
	global inf
	global sup

	aleat  = geraAleatorio()
	aleat2 = geraAleatorio()

#generates values between inf,sup
	if tipo == "unf":
		return int(inf + (sup - inf)* aleat)
	elif tipo == "exp":
		if aleat > 0:
			return math.ceil((-1/lambd)*np.log(1-aleat))
		else:
			return aleat
	elif tipo == "nrm":
		if aleat > 0: 
			z=math.sqrt((-2*np.log(aleat)))*math.cos(aleat2)
			return int(media + devioP*z)
	else:
		return aleat
