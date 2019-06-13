#!/usr/bin/python3

import math
import random
import random_nro as rnd
import statistics as st

c_tipo = "det"
s_tipo = "det"
lf   = math.inf
nro_eventos = 20

def set_params(params):
	tipo, lf, nro_eventos = params

def show_params():
	print(tipo,lf,nro_eventos)

def eventoChegada(tr,es,tf,hc,hs):
	global tipo
	tec = 0
	tr = hc
	ts = 0
	if es == 0:
		es = 1
		ts = generateTime(c_tipo)
		hs = tr + ts
	else:
		tf += 1
    
	tec = roletaChegada(probC)
	hc = tr + tec
    
	return tr,es,tf,hc,hs
    
def eventoSaida(tr,es,tf,hc,hs):
	global tipo
	tr = hs
	ts = 0
	if tf > 0:
		tf -= 1
		ts = generateTime(s_tipo)
		hs = tr + ts
	else:
		es = 0
		hs = math.inf
    
	return tr,es,tf,hc,hs


	global nro_eventos 

	tr = 0
	es = 0
	tf = 0
	hc = 0
	hs = math.inf

	i = 0
	hc_ant = hc
	aux = []

	while i < nro_eventos:
		if hc < hs:
			tr,es,tf,hc,hs = eventoChegada(tr,es,tf,hc,hs)
		else:
			tr,es,tf,hc,hs = eventoSaida(tr,es,tf,hc,hs)

		print("TR: ES: TF: HC: HS: ")
		print(tr," ",es," ",tf," ",hc," ",hs)
		i += 1
		if hc != hc_ant:
			aux.append(hc - hc_ant)
		hc_ant = hc

	print("fim")
	print(aux)
	st.stats(aux)
