import numpy as np
import matplotlib.pyplot as plt
import skfuzzy as fuzz
from matplotlib import cm
import Functions as P1

temperature = np.arange(0, 35.5, 0.5)
people = np.arange(0, 20, 1)
speed = np.arange(0, 100, 1)

#Membership functions INPUTS
#Actual temperature
at_low = P1.Trapezoidal(temperature, 0, 0, 0, 10)
at_med = P1.Trapezoidal(temperature, 7, 15, 20, 28)
at_high = P1.Trapezoidal(temperature, 25, 35, 35, 35)

#Requested temperature
rt_low = P1.Trapezoidal(temperature, 0, 0, 0, 10)
rt_med = P1.Trapezoidal(temperature, 7, 15, 20, 28)
rt_high = P1.Trapezoidal(temperature, 25, 35, 35, 35)

#Number of people
p_few = P1.Trapezoidal(people, 0, 0, 5, 8)
p_med = P1.Trapezoidal(people, 5, 8, 12, 15)
p_lot = P1.Trapezoidal(people, 12, 15, 20, 20)

#Membership functions OUTPUTS
#Speed
s_low= P1.Trapezoidal(speed, 0, 0, 10, 35)
s_reg = P1.Trapezoidal(speed, 15, 40, 60, 85)
s_fast = P1.Trapezoidal(speed, 65, 90, 100, 100)

##Plotting membership functions
plt.figure(1)
plt.subplot(3, 3, 1)
plt.plot(temperature, at_low, 'b', linewidth=1.5, label='Low')
plt.plot(temperature, at_med, 'g', linewidth=1.5, label='Medium')
plt.plot(temperature, at_high, 'r', linewidth=1.5, label='High')
plt.title('Actual Temperature')
plt.ylabel('Membership degree')
plt.legend()

plt.subplot(3, 3, 4)
plt.plot(temperature, rt_low, 'b', linewidth=1.5, label='Low')
plt.plot(temperature, rt_med, 'g', linewidth=1.5, label='Medium')
plt.plot(temperature, rt_high, 'r', linewidth=1.5, label='High')
plt.title('Requested Temperature')
plt.ylabel('Membership degree')
plt.legend()

plt.subplot(3, 3, 7)
plt.plot(people, p_few, 'b', linewidth=1.5, label='Few')
plt.plot(people, p_med, 'g', linewidth=1.5, label='Medium')
plt.plot(people, p_lot, 'r', linewidth=1.5, label='Lot')
plt.title('Number of people')
plt.ylabel('Membership degree')
plt.legend()

plt.subplot(3, 3, 6)
plt.plot(speed, s_low, 'b', linewidth=1.5, label='Low')
plt.plot(speed, s_reg, 'g', linewidth=1.5, label='Medium')
plt.plot(speed, s_fast, 'r', linewidth=1.5, label='High')
plt.title('Speed')
plt.ylabel('Membership degree')
plt.legend()


plt.show()