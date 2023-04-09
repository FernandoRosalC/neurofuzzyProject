import numpy as np
import matplotlib.pyplot as plt
import skfuzzy as fuzz
from matplotlib import cm
import Functions as P1


def defuzzify(A,R,P):
    #print("actual temp: ", A)
    rule1 = np.fmin(at_low[A], np.fmin(rt_low[R], p_few[P]))
    rule2 = np.fmin(at_low[A], np.fmin(rt_low[R], p_med[P]))
    rule3 = np.fmin(at_low[A], np.fmin(rt_low[R], p_fast[P]))    
    rule4 = np.fmin(at_low[A], np.fmin(rt_med[R], p_few[P]))
    rule5 = np.fmin(at_low[A], np.fmin(rt_med[R], p_med[P]))
    rule6 = np.fmin(at_low[A], np.fmin(rt_med[R], p_fast[P]))
    rule7 = np.fmin(at_low[A], np.fmin(rt_high[R], p_few[P]))
    rule8 = np.fmin(at_low[A], np.fmin(rt_high[R], p_med[P]))
    rule9 = np.fmin(at_low[A], np.fmin(rt_high[R], p_fast[P]))
    rule10 = np.fmin(at_med[A], np.fmin(rt_low[R], p_few[P]))
    rule11 = np.fmin(at_med[A], np.fmin(rt_low[R], p_med[P]))
    rule12 = np.fmin(at_med[A], np.fmin(rt_low[R], p_fast[P]))
    rule13 = np.fmin(at_med[A], np.fmin(rt_med[R], p_few[P]))
    rule14 = np.fmin(at_med[A], np.fmin(rt_med[R], p_med[P]))
    rule15 = np.fmin(at_med[A], np.fmin(rt_med[R], p_fast[P]))
    rule16 = np.fmin(at_med[A], np.fmin(rt_high[R], p_few[P]))
    rule17 = np.fmin(at_med[A], np.fmin(rt_high[R], p_med[P]))
    rule18 = np.fmin(at_med[A], np.fmin(rt_high[R], p_fast[P]))
    rule19 = np.fmin(at_high[A], np.fmin(rt_low[R], p_few[P]))
    rule20 = np.fmin(at_high[A], np.fmin(rt_low[R], p_med[P]))
    rule21 = np.fmin(at_high[A], np.fmin(rt_low[R], p_fast[P]))
    rule22 = np.fmin(at_high[A], np.fmin(rt_med[R], p_few[P]))
    rule23 = np.fmin(at_high[A], np.fmin(rt_med[R], p_med[P]))
    rule24 = np.fmin(at_high[A], np.fmin(rt_med[R], p_fast[P]))
    rule25 = np.fmin(at_high[A], np.fmin(rt_high[R], p_few[P]))
    rule26 = np.fmin(at_high[A], np.fmin(rt_high[R], p_med[P]))
    rule27 = np.fmin(at_high[A], np.fmin(rt_high[R], p_fast[P]))
    
    global cut_low, cut_reg, cut_fast
    
    S_low_max = np.fmax(rule1, np.fmax(rule7, np.fmax(rule8, np.fmax(rule9, np.fmax(rule13, np.fmax(rule16, np.fmax(rule17, np.fmax(rule18, np.fmax(rule25, np.fmax(rule26, rule27))))))))))
    S_reg_max = np.fmax(rule2, np.fmax(rule4, np.fmax(rule5, np.fmax(rule10, np.fmax(rule14, np.fmax(rule19, rule22))))))
    S_fast_max = np.fmax(rule3, np.fmax(rule6, np.fmax(rule11, np.fmax(rule12, np.fmax(rule15, np.fmax(rule20, np.fmax(rule21, np.fmax(rule23, rule24))))))))
    
    cut_low = np.fmin(s_slow, np.full(len(s_slow), S_low_max))
    cut_reg = np.fmin(s_reg, np.full(len(s_reg), S_reg_max))
    cut_fast = np.fmin(s_fast, np.full(len(s_fast), S_fast_max))
    
    finalCut_Speed = np.fmax(cut_low, np.fmax(cut_reg, cut_fast))    
    
    return finalCut_Speed


temperature = np.arange(0, 36, 1)
people = np.arange(0, 36, 1)
speed = np.arange(0, 101, 1)

#Membership functions INPUTS
#Actual temperature
at_low = P1.Trapezoidal(temperature, 0, 0, 0, 10)
at_med = P1.Trapezoidal(temperature, 7, 15, 20, 28)
at_high = P1.Trapezoidal(temperature, 25, 36, 36, 36)

#Requested temperature
rt_low = P1.Trapezoidal(temperature, 0, 0, 0, 10)
rt_med = P1.Trapezoidal(temperature, 7, 15, 20, 28)
rt_high = P1.Trapezoidal(temperature, 25, 36, 36, 36)

#Number of people
p_few = P1.Trapezoidal(temperature, 0, 0, 0, 10)
p_med = P1.Trapezoidal(temperature, 7, 15, 20, 28)
p_fast = P1.Trapezoidal(temperature, 25, 36, 36, 36)

"""
#Number of people
p_few = P1.Trapezoidal(people, 0, 0, 5, 8)
p_med = P1.Trapezoidal(people, 5, 8, 12, 15)
p_fast = P1.Trapezoidal(people, 12, 15, 20, 20)
"""
#Membership functions OUTPUTS
#Speed
s_slow= P1.Trapezoidal(speed, 0, 0, 10, 35)
s_reg = P1.Trapezoidal(speed, 15, 40, 60, 85)
s_fast = P1.Trapezoidal(speed, 65, 90, 100, 100)

#A = round(int(input("Ingresa el valor de la temperatura actual: ")), 0)
#R = round(int(input("Ingresa el valor de la temperatura requerida: ")), 0)
#P = round(int(input("Ingresa el valor de la cantidad de personas: ")), 0)

A= 34
R = 11
P = 15

finalCut_Speed = defuzzify(A, R, P)

##Plotting membership functions
plt.figure(1)
plt.subplot(2, 2, 1)
plt.plot(temperature, at_low, 'b', linewidth=1.5, label='Low')
plt.plot(temperature, at_med, 'g', linewidth=1.5, label='Medium')
plt.plot(temperature, at_high, 'r', linewidth=1.5, label='High')
plt.title('Actual Temperature')
plt.ylabel('Membership degree')
plt.legend()

plt.subplot(2, 2, 2)
plt.plot(temperature, rt_low, 'b', linewidth=1.5, label='Low')
plt.plot(temperature, rt_med, 'g', linewidth=1.5, label='Medium')
plt.plot(temperature, rt_high, 'r', linewidth=1.5, label='High')
plt.title('Requested Temperature')
plt.ylabel('Membership degree')
plt.legend()

plt.subplot(2, 2, 3)
plt.plot(people, p_few, 'b', linewidth=1.5, label='Few')
plt.plot(people, p_med, 'g', linewidth=1.5, label='Medium')
plt.plot(people, p_fast, 'r', linewidth=1.5, label='Lot')
plt.title('Number of people')
plt.ylabel('Membership degree')
plt.legend()

plt.subplot(2, 2, 4)
plt.plot(speed, s_slow, 'b', linewidth=1.5, label='Low')
plt.plot(speed, s_reg, 'g', linewidth=1.5, label='Medium')
plt.plot(speed, s_fast, 'r', linewidth=1.5, label='High')
plt.title('Speed')
plt.ylabel('Membership degree')
plt.legend()



######################Plotting the final result######################
plt.figure(2)
#plt.plot(speed, s_slow, 'b', linewidth=1.5, label='Low')
#plt.plot(speed, s_reg, 'g', linewidth=1.5, label='Medium')
#plt.plot(speed, s_fast, 'r', linewidth=1.5, label='High')
plt.axis([0, 100, 0, 1.1])
plt.plot(speed, cut_low, 'b', linewidth=0.5, linestyle='--', )
plt.plot(speed, cut_reg, 'g', linewidth=0.5, linestyle='--')
plt.plot(speed, cut_fast, 'r', linewidth=0.5, linestyle='--')
plt.axvline(fuzz.defuzz(speed, finalCut_Speed, 'centroid'), color='k', linestyle='--', linewidth=1.5)

plt.fill_between(speed, finalCut_Speed, facecolor='Orange', alpha=0.7)
print("The speed is: ", fuzz.defuzz(speed, finalCut_Speed, 'centroid'))
plt.title('Speed')
#plt.legend()

######################Plotting surface######################
x = np.zeros((len(temperature), len(people)))

for i in temperature:
    for j in people:
        print(i, j)
        x[i][j] = fuzz.defuzz(speed, defuzzify(A, i, j), 'centroid')
        

temperature, people = np.meshgrid(temperature, people)
plt.figure(3)
ax1 = plt.axes(projection='3d')
ax1.plot_surface(temperature, people, x, rstride=1, cstride=1, cmap=cm.rainbow)
ax1.set_title('Seed plot')
ax1.set_xlabel('Temperature')
ax1.set_ylabel('People')
ax1.set_zlabel('Speed')


plt.show()