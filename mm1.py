#!/usr/bin/python3

import math
import random
import statistics as st

def roletaServico(probS):
	S = 0
	r = 0
	for i in range(len(probS)):
		S += probS[i]
		r = random.uniform(0,S)
		if r > 0 and r <= 0.25:
			return 3
		elif r > 0.25 and r <= 0.35:
			return 1
		else:
			return 2

def roletaChegada(probC):
	S = 0
	r = 0
	for i in range(len(probC)):
		S += probC[i]
		r = random.uniform(0,S)
		if r > 0 and r <= 0.15:
			return 4
		elif r > 0.15 and r <= 0.20:
			return 1
		elif r > 0.20 and r <= 0.30:
			return 2
		else:
			return 3

def eventoChegada(tr,es,tf,hc,hs,probC,probS):
	tec = 0
	tr = hc
	ts = 0
	if es == 0:
		es = 1
		ts = roletaServico(probS)
		hs = tr + ts
	else:
		tf += 1
    
	tec = roletaChegada(probC)
	hc = tr + tec
    
	return tr,es,tf,hc,hs
    
def eventoSaida(tr,es,tf,hc,hs,probC,probS):
	tr = hs
	ts = 0
	if tf > 0:
		tf -= 1
		ts = roletaServico(probS)
		hs = tr + ts
	else:
		es = 0
		hs = math.inf
    
	return tr,es,tf,hc,hs


def main():
	str = ""
	probS = [0.35,0.40,0.25]
	probC = [0.20,0.30,0.35,0.15]
	tr = 0
	es = 0
	tf = 0
	hc = 0
	hs = math.inf
    
	nro_eventos = 20
	i = 0
	hc_ant = hc
	aux = []

	while i < nro_eventos:
		if hc < hs:
			tr,es,tf,hc,hs = eventoChegada(tr,es,tf,hc,hs,probC,probS)
			str = "Chegada"
		else:
			tr,es,tf,hc,hs = eventoSaida(tr,es,tf,hc,hs,probC,probS)
			str = "Saida"

		print(str)
		print("TR: ES: TF: HC: HS: ")
		print(tr," ",es," ",tf," ",hc," ",hs)
		i += 1
		if hc != hc_ant:
			aux.append(hc - hc_ant)
		hc_ant = hc

	print("fim")
	print(aux)
	st.stats(aux)

main()
