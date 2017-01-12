import time
import mraa

# ESSAIS AVEC LA BREAKOUT BOARD en direct sur les pins avec 4 resistances de 220 à la masse sous les INputs
 
mraa.Gpio(35).dir(mraa.DIR_OUT) # J19-8
mraa.Gpio(26).dir(mraa.DIR_OUT)	# J18-13	
mraa.Gpio(25).dir(mraa.DIR_OUT)	# J18-12
mraa.Gpio(13).dir(mraa.DIR_OUT)	# J17-14
mraa.Gpio(21).dir(mraa.DIR_IN)	# J18-8
mraa.Gpio(0).dir(mraa.DIR_IN)	# J17-1
mraa.Gpio(20).dir(mraa.DIR_IN)	# J18-7
mraa.Gpio(14).dir(mraa.DIR_IN)	# J18-1
				# J18-3 : GND

mraa.Gpio(35).write(1)
mraa.Gpio(26).write(0)
mraa.Gpio(25).write(0)	#Colonne 3 active
mraa.Gpio(13).write(0)       

while True :	
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

