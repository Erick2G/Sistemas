import numpy as np
from procesar_entradas import estructuraSilaba


spanish_datos = np.genfromtxt('spanish.data',dtype='str',delimiter=',');
english_datos = np.genfromtxt('english.data',dtype='str',delimiter=',');
german_datos = np.genfromtxt('aleman.data',dtype='str',delimiter=',');

textoS = ''
for data in english_datos:
	temp =estructuraSilaba(data);
	for e in temp:
		textoS+=str(e)+',';
	textoS+='\n';
f= open("english_procesado.data","w+")
f.write(str(textoS))
f.close()
textoS = ''
for data in spanish_datos:
	temp =estructuraSilaba(data);
	for e in temp:
		textoS+=str(e)+',';
	textoS+='\n';
f= open("spanich_procesado.data","w+")
f.write(str(textoS))
f.close()
textoS = ''
for data in german_datos:
	temp =estructuraSilaba(data);
	for e in temp:
		textoS+=str(e)+',';
	textoS+='\n';
f= open("german_procesado.data","w+")
f.write(str(textoS))
f.close()