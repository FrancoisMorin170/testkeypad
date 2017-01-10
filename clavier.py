import time
import mraa

CLAVIER = [['1', '2', '3', 'A'], ['4', '5', '6', 'B'], ['7', '8', '9', 'C'], ['*', '0', '#', 'D']]

RANGEE= [33, 47, 48, 36]
COLONNE = [31, 45, 32, 46]
Z=0

while True:
        for j in range (4):
                mraa.Gpio(COLONNE[j]).dir(mraa.DIR_OUT)
                mraa.Gpio(COLONNE[j]).write(1)
	
        for i in range (4):
		mraa.Gpio(RANGEE[i]).dir(mraa.DIR_IN)
		
	try :
		for j in range(4):
			mraa.Gpio(COLONNE[j]).write(0)
			
			for i in range(4):
				Z=(mraa.Gpio(RANGEE[i]).read())
				if (Z == 0):
					print CLAVIER[i][j]
					time.sleep(0.5)
					while (Z == 0):
						pass
			mraa.Gpio(COLONNE[j]).write(1)
	except KeyboardInterrupt:
		Gpio.cleanup()
		

