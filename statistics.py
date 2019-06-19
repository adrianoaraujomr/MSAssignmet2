#/usr/bin/python3

from numpy import *
from scipy.stats import mode

def stats(in_data): 
	media     = mean(in_data)
	mediana   = median(in_data)
	moda      = mode(in_data).mode[0] #max(in_data, key=list.count)
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
def idle_prob(idle,tr)
	return idle/tr

#Tempo médio de serviço
def service_time(servico):
	return sum(servico)/len(servico)

#Tempo médio despendido no sistema
#tempos no sistema/numero de clientes
def system_time(wait,servico):
	return (sum(wait) + sum(servico))/len(servico)
