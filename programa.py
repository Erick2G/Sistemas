import random
import numpy as np
from neurona_sistemas import Agent


spanish_data = np.genfromtxt('spanich_procesado.data',dtype='int',delimiter=',');
english_data = np.genfromtxt('english_procesado.data',dtype='int',delimiter=',');
german_data = np.genfromtxt('german_procesado.data',dtype='int',delimiter=',');

spanish = spanish_data[:,:27]
english = english_data[:,:27]
german = german_data[:,:27]

#Entrenamiento
red = Agent(27,17,2,0.2,0.2)

entrenamientos = 1500
for i in range(entrenamientos):
	for data in spanish:
		salidaRed,activacionesOcultas = red.calcNetOutput(list(data[:]),True)
		red.trainingEpisode([0,0],salidaRed,activacionesOcultas,list(data[:]))
	for data in english:
		salidaRed,activacionesOcultas = red.calcNetOutput(list(data[:]),True)
		red.trainingEpisode([0,1],salidaRed,activacionesOcultas,list(data[:]))
	for data in german:
		salidaRed,activacionesOcultas = red.calcNetOutput(list(data[:]),True)
		red.trainingEpisode([1,0],salidaRed,activacionesOcultas,list(data[:]))

sumaEn = 0
sumaEs = 0
sumaGe = 0

for data in spanish:
	salida = red.calcNetOutput(list(data[:]),False)
	if(salida[0]<.5 and salida[1]<.5):
		sumaEs+=1
	#print(salida)
for data in english:
	salida = red.calcNetOutput(list(data[:]),False)
	if(salida[0]<.5 and salida[1]>.5):
		sumaEn+=1
for data in german:
	salida = red.calcNetOutput(list(data[:]),False)
	if(salida[0]>.5 and salida[1]<.5):
		sumaGe+=1


print('Español: ',(sumaEs*100)/len(spanish))
print('English: ',(sumaEn*100)/len(english))
print('German: ',(sumaGe*100)/len(german))