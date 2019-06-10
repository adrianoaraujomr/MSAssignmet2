#/usr/bin/python3

tr = 0
es = 0
tf = 0
hc = 0
hs = 9999

def process_arrive_event():
	global tr
	global es
	global tf
	global hs 
	global hc

	if es == 0 :
		es = 1
		ts = generate_time()
		hs = tr + ts
	else :
		tf = tf + 1

	tec = generate_time()
	hc = tr + tec

def process_exit_event():
	global tr
	global es
	global tf
	global hs 

	if tf > 0 :
		tf = tf - 1
		ts = generate_time()
		hs = tr + ts
	else :
		es = 0
		hs = 9999

while True:
	if hc < hs :
		process_arrive_event()
	else :
		process_exit_event()

	aux = att_statistics()
	print(aux)


