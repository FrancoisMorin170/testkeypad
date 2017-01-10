import time
import mraa

#Les niveaux logiques des GPIO ne sont pas tous les memes (1.8 ou 3.3) 


#CLAVIER = [['1', '2', '3', 'A'], ['4', '5', '6', 'B'], ['7', '8', '9','C'], ['*', '0', '#', 'D']]
#LIGNE   = [35, 26, 25, 13]   # GP : 131, 130, 129, 128  
#COLONNE = [21, 0, 20, 14]    # GP : 183, 182, 12, 13

#for j in range (4) : 
#	mraa.Gpio(COLONNE[j]).dir(mraa.DIR_OUT)
#	mraa.Gpio(LIGNE[j]).dir(mraa.DIR_IN)

mraa.Gpio(35).dir(mraa.DIR_OUT)
mraa.Gpio(26).dir(mraa.DIR_OUT)
mraa.Gpio(25).dir(mraa.DIR_OUT)
mraa.Gpio(13).dir(mraa.DIR_OUT)
mraa.Gpio(21).dir(mraa.DIR_IN)
mraa.Gpio(0).dir(mraa.DIR_IN)
mraa.Gpio(20).dir(mraa.DIR_IN)
mraa.Gpio(14).dir(mraa.DIR_IN)

mraa.Gpio(35).write(0)
mraa.Gpio(26).write(0)
mraa.Gpio(25).write(1)
mraa.Gpio(13).write(0)       #Sortie d une colonne

while True:
	L1=mraa.Gpio(21).read()		
        L2=mraa.Gpio(0).read()
        L3=mraa.Gpio(20).read()
        L4=mraa.Gpio(14).read()
	
	if mraa.Gpio(21).read() == 1: 
		print 'L1'
		time.sleep(0.2)
	if mraa.Gpio(0).read() == 1: 
                print 'L2'
                time.sleep(0.2)
	if mraa.Gpio(20).read() == 1: 
                print 'L3'
                time.sleep(0.2)
	if mraa.Gpio(14).read() == 1: 
                print 'L4'
                time.sleep(0.2)
