#!/usr/bin/python3 

import math
import numpy as np
from datetime import datetime

boo  = True
seed = 13
a = 17
b = 43
m = 256

def show_params():
	print("seed =",seed)
	print("a =",a)
	print("b =",b)
	print("m =",m)
	print("")

def set_params(params):
	global seed,a,b,m
	seed,a,b,m = params


def generateTime(params,tipo):
	if tipo == "det" :
		return params[5]
	else :
		return geraDistribuicao(params,tipo)


def geraAleatorio():
	global boo
	global seed
	global a
	global b
	global m

	if boo :
		seed += datetime.now().microsecond
		boo = False

	seed = ((a * seed + b) % (m - 1))
	
	return (seed + 1)/m

    
def geraDistribuicao(pr,tipo):
	aleat  = geraAleatorio()
	aleat2 = geraAleatorio()

	if tipo == "unf":
		return int(pr[3] + (pr[4] - pr[3])* aleat)
	elif tipo == "nrm":
		#Não estara definida se aleat for igual a 0
		z = math.sqrt((-2*np.log(aleat)))*math.cos(aleat2)
		return int(pr[1] + pr[2]*z)
	elif tipo == "exp":
		#Não estara definida se aleat for igual a 1
		return int(math.ceil((-1/pr[0])*np.log(1-aleat)))
