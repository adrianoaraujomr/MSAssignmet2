#/usr/bin/python3

from numpy import *
from scipy import stats as stt

alfa = .05

def relatorio(servico,wait,tr,idle):
	wt  = wait_time(wait,servico)
	qp  = queue_prob(wait,servico)
	ip  = idle_prob(idle,tr)
	st  = service_time(servico)
	syt = system_time(wait,servico)

	return [wt,qp,ip,st,syt]

def simul_stats(matrix):
	global alfa

	wt  = []
	qp  = []
	ip  = []
	st  = []
	syt = []
	for i in matrix:
		wt.append(i[0])
		qp.append(i[1])
		ip.append(i[2])
		st.append(i[3])
		syt.append(i[4])

	print("alfa :", alfa,"\n")

	media     = mean(wt)
	desvio    = std(wt)
	variancia = desvio*desvio
	t         = stt.t.ppf(1 - alfa,len(wt))
	h         = t*desvio/sqrt(len(wt))

	print("[",media - h,";",media + h,"]")
	print("wt media     :",media)
	print("wt desvio    :",desvio)
	print("wt variancia :",variancia)

	media     = mean(qp)
	desvio    = std(qp)
	variancia = desvio*desvio
	t         = stt.t.ppf(1 - alfa,len(qp))
	h         = t*desvio/sqrt(len(qp))

	print("[",media - h,";",media + h,"]")
	print("qp t         :",t)
	print("qp media     :",media)
	print("qp desvio    :",desvio)
	print("qp variancia :",variancia)

	media     = mean(ip)
	desvio    = std(ip)
	variancia = desvio*desvio
	t         = stt.t.ppf(1 - alfa,len(ip))
	h         = t*desvio/sqrt(len(ip))

	print("[",media - h,";",media + h,"]")
	print("ip t         :",t)
	print("ip media     :",media)
	print("ip desvio    :",desvio)
	print("ip variancia :",variancia)

	media     = mean(st)
	desvio    = std(st)
	variancia = desvio*desvio
	t         = stt.t.ppf(1 - alfa,len(st))
	h         = t*desvio/sqrt(len(st))

	print("[",media - h,";",media + h,"]")
	print("st media     :",media)
	print("st desvio    :",desvio)
	print("st variancia :",variancia)

	media     = mean(syt)
	desvio    = std(syt)
	variancia = desvio*desvio
	t         = stt.t.ppf(1 - alfa,len(syt))
	h         = t*desvio/sqrt(len(syt))

	print("[",media - h,";",media + h,"]")
	print("syt media     :",media)
	print("syt desvio    :",desvio)
	print("syt variancia :",variancia)

def stats(in_data): 
	media     = mean(in_data)
	mediana   = median(in_data)
#	moda      = stats.mode(in_data).mode[0] #max(in_data, key=list.count)
	minimo    = min(in_data)
	maximo    = max(in_data)
	desvio    = std(in_data)
	variancia = desvio*desvio
	coef_var  = 100*desvio/media
	coef_ass  = (media - moda)/mediana

	print("media =",media)
	print("mediana =",mediana)
	print("moda =",moda)
	print("minimo =",minimo)
	print("macimo =",maximo)
	print("desvio padrao =",desvio)
	print("variancia =",variancia)
	print("coeficiente de variancia =",coef_var)
	print("coeficiente de assimetria =",coef_ass)

	return media, mediana, moda, minimo, maximo, desvio, variancia, coef_var, coef_ass

#Tempo medio de espera na fila
#tempos de espera na fila/numero total de clientes
def wait_time(wait,servico):
	return sum(wait)/len(servico)

#Probabilidade de um cliente esperar na fila
#numero de clientes que esperaram/numero total de clientes
def queue_prob(wait,servico):
	return len(wait)/len(servico)

#Probabilidade do operador livre
#tempo livre do operador/tempo da simulação
def idle_prob(idle,tr):
	return idle/tr

#Tempo médio de serviço
def service_time(servico):
	return sum(servico)/len(servico)

#Tempo médio despendido no sistema
#tempos no sistema/numero de clientes
def system_time(wait,servico):
	return (sum(wait) + sum(servico))/len(servico)
