import serial
import time
import collections
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.lines import Line2D
import numpy as np




def getSerialData(self,Samples,numData,serialConnection, lines):
    for i in range(numData):
        value  = float(serialConnection.readline().strip())  #Leer sensor / Read sensor
        data[i].append(value) #Guarda lectura en la última posición / #Save reading in the end position
        lines[i].set_data(range(Samples),data[i]) # Dibujar nueva linea / Drawn new line
        

##NO JALO COMO QUERIA
## CHECAR COMO MANDAR LOS DATOS DEL SERIAL A LA FUNCION PRINCIPAL
def readSerialData(self,serialConnection):
    Temp = int(serialConnection.readline().strip())  #Leer sensor / Read sensor
    Temp_req = int(serialConnection.readline().strip())  #Leer sensor / Read sensor
    People = int(serialConnection.readline().strip())  #Leer sensor / Read sensor
    print("Temperatura: ",Temp)    
    print("Temperatura Requerida: ",Temp_req)
    print("Personas: ",People)
    
    return Temp, Temp_req, People       


serialPort = 'COM4' # Puerto serial arduino / Arduino serial port
baudRate = 9600  # Baudios

try:
    serialConnection = serial.Serial(serialPort, baudRate) # Instanciar objeto Serial / Instance Serial Object
except:
    print('Cannot conect to the port')

Samples = 50  #Muestras / Samples
sampleTime = 150  #Tiempo de muestreo / Sample Time
numData = 3


# Limites de los ejes / Axis limit
xmin = 0
xmax = Samples

lines = []
data = []

for i in range(numData):
    data.append(collections.deque([0] * Samples, maxlen=Samples))
    lines.append(Line2D([], [], color='blue'))
    

fig = plt.figure()# Crea una nueva figura #Create a new figure.
ax1 = fig.add_subplot(3, 1, 1,xlim=(xmin, xmax), ylim=(-10, 40 ))
ax1.set_xlabel("Samples")
ax1.set_ylabel("Temperatura")
ax1.add_line(lines[0])

ax2 = fig.add_subplot(3, 1, 2,xlim=(xmin, xmax), ylim=(-10 , 40))
ax2.set_xlabel("Samples")
ax2.set_ylabel("Temp Requerida")
ax2.add_line(lines[1])

ax3 = fig.add_subplot(3, 1, 3,xlim=(xmin, xmax), ylim=(-5 , 25 ))
#ax3.title.set_text('Third Plot')
ax3.set_xlabel("Samples")
ax3.set_ylabel("Personas")
ax3.add_line(lines[2])


anim = animation.FuncAnimation(fig,getSerialData, fargs=(Samples,numData,serialConnection,lines), interval=sampleTime)
plt.show()




serialConnection.close() # cerrar puerto serial/ close serial port