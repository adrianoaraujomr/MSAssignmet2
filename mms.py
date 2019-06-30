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
nro_servidr = 1

chegadas = []
saidas   = []


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
	print("nro_servidr =",nro_servidr)
	print("")

def eventoChegada(tr,es,tf,hc,hs):
	global nro_servidr
	global s_param
	global s_tipo
	global c_param
	global c_tipo

	tec = 0
	tr = hc
	ts = 0

	if es < nro_servidr:
		es += 1
		ts = rnd.generateTime(s_param,s_tipo)
		hs = tr + ts
		saidas.append(ts)
	else:
		tf += 1
    
	tec = rnd.generateTime(c_param,c_tipo)
	hc = tr + tec
	chegadas.append(tec)

	return tr,es,tf,hc,hs
    
def eventoSaida(tr,es,tf,hc,hs):
	global s_param
	global s_tipo

	tr = hs
	ts = 0

	if tf > 0:
		tf -= 1
		ts = rnd.generateTime(s_param,s_tipo)
		hs = tr + ts
		saidas.append(ts)
	elif es > 1:
		es -= 1
		ts = rnd.generateTime(s_param,s_tipo)
		hs = tr + ts
		saidas.append(ts)
	else:
		es = 0
		hs = 999999
    
	return tr,es,tf,hc,hs

def run(nro_servidores):
	show_params()
	rnd.show_params()

	global nro_eventos, nro_servidr
	global chegadas, saidas

	nro_servidr = nro_servidores

	tr = 0
	es = 0
	tf = 0
	hc = 0
	hs = 999999

	rnd.boo  = True
	chegadas = []
	saidas   = []
	idle  = 0
	wait  = []
	index = 0
	nw    = 0

	i = 0

	while i < nro_eventos:
		if hc < hs and tf < lf:
			tr,es,tf,hc,hs = eventoChegada(tr,es,tf,hc,hs)
			if tf >= 1:
				wait.append(hc)
				nw += 1
		else:
			if nw > 0:
				wait[index] = hs - wait[index]
				index += 1
				nw    -= 1
			tr,es,tf,hc,hs = eventoSaida(tr,es,tf,hc,hs)

		if tf == 0:
			idle += hc - tr#		
#		print("chegadas",chegadas)
#		print("saidas  ",saidas)
#		print("esperas ",wait)
#		print("ociosos ",idle)
		print('TR:{:03d} ES:{:03d} TF:{:03d} HC:{:03d} HS:{:06d}'.format(tr,es,tf,hc,hs))
#		type(hc)
#		print('Relogio:{:d} Estado Servidor:{:d} Tamanho Fila:{:d} Proxima Chegada:{:d} Proxima Saida:{:d}'.format(tr,es,tf,hc,hs))
#		x = input()

		i += 1

	for i in range(index,len(wait)):
		wait[i] = tr - wait[i]
	wait = [x for x in wait if x > 0]
#	print("chegadas",chegadas)
#	print("saidas  ",saidas)
#	print("esperas ",wait)
#	print("ociosos ",idle)
	print("fim","\n")

	return st.relatorio(saidas,wait,tr,idle)
