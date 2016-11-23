#
####################### 1.0 ##########################################
#pedir una secuencia y eliminar los "huecos" ( suelen ser un guion -)
#imprimir esa secuencia
#Comparar dos secuencias dadas(solo dar % de coincidencia)
#
######################## 2.0 ##########################################
#
#leer desde el archivo
#Imprimir y dar la opcion de guardar el resultado
#Imprimir una representacion grafica de las coincidencias ( como un blast)
import sys

class secuencia(object):
	"""docstring for secuencia"""
	def __init__(self,seq):
		
		self.seq = seq

	def ImprimirSecuencia(self):

		print(self.seq)

	# def EliminarHuecos(self):

	# 	nuevaseq = 1
	# 	return nuevaseq


	# def CompararSecuencia(self):

	# 	return porcoincid


	def LongitudSecuencia(self):

		return len(secuencia.seq)


	def SecuenciaComplement(self):
		x=(len(secuencia.seq))
		ComplSeq = list(range(x))
		indice=0
		#print(str(ComplSeq))
		while indice< (len(secuencia.seq)):
			base= secuencia.seq[indice]

			if base == "a":
				ComplSeq[indice]="t"
			elif base== "t":
				ComplSeq[indice]="a"

			elif base== "g":
				ComplSeq[indice]="c"
			elif base== "c":
				ComplSeq[indice]="g"

			indice += 1

		return ComplSeq

	def SecuenciaReversoComp(self,Seq):
		x=(len(Seq))
		RevSeq = list(range(x))

		for i in range(len(Seq)):
			RevSeq[i]=Seq[-(1+i)]
			#print(RevSeq[i])
		return RevSeq

	def ImprimirSecuencia(self,Seq):

		# for i in range(len(Seq)):
		# 	base=Seq[i]
		# 	print(base)
		for i in range(len(Seq)):

			base=Seq[i]
			sys.stdout.write(base)
			sys.stdout.flush()
				


seq1= input("introduce la secuencia: ")
#seq2= input("introduce la secuencia: ")

secuencia = secuencia(seq1)

longitud=secuencia.LongitudSecuencia()
print("la secuencia tiene " + str(longitud)+ " nucleotidos \n")
nueva=secuencia.SecuenciaComplement()
print("La secuencia complementaria es: ")
secuencia.ImprimirSecuencia(nueva) 
print("\n")
print("La secuencia reversocomplementaria es: ")
reverso=secuencia.SecuenciaReversoComp(nueva)
secuencia.ImprimirSecuencia(reverso)
input()
