import time
import mraa

#Les niveaux logiques des GPIO ne sont pas tous les memes (1.8 ou 3.3) 

#Schema  :  Out --- \---|--- masse
#			|		
#			In

#RANGEE= [33, 47, 48, 36]   # GP : 48, 49, 15, 14  
#COLONNE = [31, 45, 32, 46] # GP : 44, 45, 46, 47

mraa.Gpio(14).dir(mraa.DIR_OUT)
mraa.Gpio(20).dir(mraa.DIR_IN)

while True:
	mraa.Gpio(14).write(1)       #Sortie d une colonne
	if mraa.Gpio(20).read()== 1: #Lecture dune entree dune ligne
		print 'OK'
		time.sleep(1)

