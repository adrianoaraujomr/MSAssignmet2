#!/usr/bin/python3

import math
import mms
import random_nro as rnd
import statistics as st

msconsole = True
repet = 15
servi = 1	

params = {
"alfa"  : 0.05,

"c_tipo" : "exp",
"s_tipo" : "unf",
"lf" : math.inf,
"nro_eventos" : 20,

"a" : 17,
"b" : 43,
"m" : 256,
"seed" : 13,

"c_lambd" : 1,
"c_media" : 10,
"c_devioP" : 2,
"c_inf" : 0,
"c_sup" : 6,
"c_det" : 2,

"s_lambd" : 1,
"s_media" : 10,
"s_devioP" : 2,
"s_inf" : 0,
"s_sup" : 6,
"s_det" : 2,
}

while msconsole:

	res = input("msconsole :$ ")
	vec = res.split(' ')
	if res == "quit":
		msconsole = False
		break
	elif res == "run":
		res = []
		for i in range(repet):
			print("Simulação :",i,":")
			print("")
			mms.set_params_global([ params["c_tipo"],
						params["s_tipo"],
						params["lf"],
						params["nro_eventos"]])

			mms.set_params_chegada([params["c_lambd"],
						params["c_media"],
						params["c_devioP"],
						params["c_inf"],
						params["c_sup"],
						params["c_det"]])

			mms.set_params_servico([params["s_lambd"],
						params["s_media"],
						params["s_devioP"],
						params["s_inf"],
						params["s_sup"],
						params["s_det"]])

			rnd.set_params([params["a"],
					params["b"],
					params["m"],
					params["seed"]])
			res.append(mms.run(servi))
#			print(res)
		st.simul_stats(res,params["alfa"])
	elif res == "help":
		fd = open("commands.in","r")
		for i in fd.readlines():
			print("	",i.replace('\n',""))
	elif vec[0] == "set":
		params[vec[1]] = int(vec[2])
	elif vec[0] == "set_dist":
		if vec[1] == "tec":
			params["c_tipo"] = vec[2]
		elif vec[1] == "ts":
			params["s_tipo"] = vec[2]
	elif vec[0] == "set_model":
		if   vec[1] == "mm1":
			servi = 1
		elif vec[1] == "mm2":
			servi = 2
		else:
			servi = int(vec[1])
	else :
		print('	',"Error, unkown command !!!")
