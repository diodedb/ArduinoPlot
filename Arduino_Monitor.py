"""
Listen to serial, return most recent numeric values
Lots of help from here:
http://stackoverflow.com/questions/1093598/pyserial-how-to-read-last-line-sent-from-serial-device
"""
from threading import Thread
import time
import serial
file_name=str(time.time())+'.log'
f = open(str(file_name), "w")

class SerialData(object):
    def __init__(self, init=50):
        try:
            self.ser = ser = serial.Serial(
                port='/dev/ttyACM0',
                baudrate=9600,
                bytesize=serial.EIGHTBITS,
                parity=serial.PARITY_NONE,
                stopbits=serial.STOPBITS_ONE,
                timeout=0.1,
                xonxoff=0,
                rtscts=0,
                interCharTimeout=None
            )
            
        except serial.serialutil.SerialException:
            #no serial connection
            self.ser = None
    
    def next(self):
        if not self.ser:
            return 100 #return anything so we can test when Arduino isn't connected
        while True:                                        # 
            if (self.ser.inWaiting()>0):
                myData = self.ser.readline().strip()
	        timestamp = datetime.datetime.now()
	        if(mydata<'1.5')                # Filtering unwanted values
	            print >>f, timestamp,"\t",int(time.time()),"\t",myData
            	    return myData
            	    
    def __del__(self):
        if self.ser:
            self.ser.close()
            f.close()

if __name__=='__main__':
    s = SerialData()
    for i in range(500):
        time.sleep(.015)
        print s.next()
