#!/usr/bin/python3

import math
import mm1
import random_nro as rnd

msconsole = True

queue = 1

params = {
"c_tipo" : "det",
"s_tipo" : "det",
"lf" : math.inf,
"nro_eventos" : 20,
"a" : 17,
"b" : 43,
"m" : 100,
"seed" : 13,
"lambd" : 1,
"media" : 10,
"devioP" : 2,
"inf" : 0,
"sup" : 99,
}

while msconsole:
	res = input("msconsole :$ ")
	vec = res.split(' ')
	if res == "quit":
		msconsole = False
		break
	elif res == "run":
		if queue == 1 :
			mm1.set_params([params["c_tipo"],
					params["s_tipo"],
					params["lf"],
					params["nro_eventos"]])
			rnd.set_params([params["a"],
					params["b"],
					params["m"],
					params["seed"],
					params["lambd"],
					params["media"],
					params["devioP"],
					params["inf"],
					params["sup"],])
			mm1.run()
#		else :
#			mm2.run()
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
	else :
		print('	',"Error, unkown command !!!")
