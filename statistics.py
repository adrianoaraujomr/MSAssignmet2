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

	print("meida =",media)
	print("mediana =",mediana)
	print("moda =",moda)
	print("minimo =",minimo)
	print("macimo =",maximo)
	print("desvio padrao =",desvio)
	print("variancia =",variancia)
	print("coeficiente de variancia =",coef_var)
	print("coeficiente de assimetria =",coef_ass)

	return media, mediana, moda, minimo, maximo, desvio, variancia, coef_var, coef_ass
