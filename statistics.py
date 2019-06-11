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

	return media, mediana, moda, minimo, maximo, desvio, variancia, coef_var, coef_ass
