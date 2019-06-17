#!/usr/bin/python3

import math
import random
import random_nro as rnd
import statistics as st

c_tipo = "det"
s_tipo = "det"
c_param = [1,10,2,0,6,2]
s_param = [1,10,2,0,6,2]
#	[0] lambd = 1
#	[1] media = 10
#	[2] devioP = 2
#	[3] inf = 0
#	[4] sup = 99
#	[5] t_det = 2
lf   = math.inf
nro_eventos = 20



def set_params_global(params):
	global c_tipo, s_tipo, lf, nro_eventos
	c_tipo, s_tipo, lf, nro_eventos = params

def set_params_chegada(params):
	c_param[0],c_param[1],c_param[2],c_param[3],c_param[4],c_param[5] = params

def set_params_servico(params):
	s_param[0],s_param[1],s_param[2],s_param[3],s_param[4],s_param[5] = params

def show_params():
	print("c_tipo =",c_tipo)
	print("s_tipo =",s_tipo)
	print("c_param =",c_param)
	print("s_param =",s_param)
	print("lf =",lf)
	print("nro_eventos =",nro_eventos)
	print("")

def eventoChegada(tr,es,tf,hc,hs):
	global s_param
	global s_tipo
	global c_param
	global c_tipo
	tec = 0
	tr = hc
	ts = 0

	if es == 0:
		es = 1
		ts = rnd.generateTime(s_param,s_tipo)
		print("ts =",ts)
		hs = tr + ts
	else:
		tf += 1
    
	tec = rnd.generateTime(c_param,c_tipo)
	print("tec =",tec)
	hc = tr + tec
    
	return tr,es,tf,hc,hs
    
def eventoSaida(tr,es,tf,hc,hs):
	global s_param
	global s_tipo
	tr = hs
	ts = 0

	if tf > 0:
		tf -= 1
		ts = rnd.generateTime(s_param,s_tipo)
		print("ts =",ts)
		hs = tr + ts
	else:
		es = 0
		hs = math.inf
    
	return tr,es,tf,hc,hs

def run():
	show_params()
	rnd.show_params()

	global nro_eventos 

	tr = 0
	es = 0
	tf = 0
	hc = 0
	hs = math.inf

	i = 0
	hc_ant = hc
	aux = []
	xua = []

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
		if hs != math.inf:
			xua.append(hs - tr)
		hc_ant = hc

	print("fim","\n")
	print(aux)
	print(xua,"\n")
	st.stats(aux)
