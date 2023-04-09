import numpy as np
import matplotlib.pyplot as plt
import skfuzzy as fuzz
from matplotlib import cm
import Functions as P1

def defuzzify(F,G):
    rule1 = np.fmin(F_NE[F], G_NE[G])
    rule2 = np.fmin(F_NE[F], G_N[G])
    rule3 = np.fmin(F_NE[F], G_W[G])
    rule4 = np.fmin(F_NE[F], G_S[G])
    rule5 = np.fmin(F_NE[F], G_SE[G])
    rule6 = np.fmin(F_N[F], G_NE[G])    
    rule7 = np.fmin(F_N[F], G_N[G])
    rule8 = np.fmin(F_N[F], G_W[G])
    rule9 = np.fmin(F_N[F], G_S[G])
    rule10 = np.fmin(F_N[F], G_SE[G])
    rule11 = np.fmin(F_W[F], G_NE[G])
    rule12 = np.fmin(F_W[F], G_N[G])
    rule13 = np.fmin(F_W[F], G_W[G])
    rule14 = np.fmin(F_W[F], G_S[G])
    rule15 = np.fmin(F_W[F], G_SE[G])
    rule16 = np.fmin(F_S[F], G_NE[G])
    rule17 = np.fmin(F_S[F], G_N[G])
    rule18 = np.fmin(F_S[F], G_W[G])
    rule19 = np.fmin(F_S[F], G_S[G])
    rule20 = np.fmin(F_S[F], G_SE[G])
    rule21 = np.fmin(F_SE[F], G_NE[G])
    rule22 = np.fmin(F_SE[F], G_N[G])
    rule23 = np.fmin(F_SE[F], G_W[G])
    rule24 = np.fmin(F_SE[F], G_S[G])
    rule25 = np.fmin(F_SE[F], G_SE[G])

    global cut_S_low, cut_S_med, cut_S_high, cut_D_CW, cut_D_DM, cut_D_ACW

    S_low_max = np.fmax(rule1, np.fmax(rule5, np.fmax(rule7, np.fmax(rule13, np.fmax(rule19, np.fmax(rule21, rule25))))))
    S_med_max = np.fmax(rule2, np.fmax(rule4, np.fmax(rule6, np.fmax(rule8, np.fmax(rule10, np.fmax(rule12, np.fmax(rule14, np.fmax(rule16, np.fmax(rule18, np.fmax(rule20, np.fmax(rule22, rule24)))))))))))
    S_high_max = np.fmax(rule3, np.fmax(rule9, np.fmax(rule11, np.fmax(rule15, np.fmax(rule17, rule23)))))
    
    D_CW_max = np.fmax(rule2, np.fmax(rule3, np.fmax(rule8, np.fmax(rule9, np.fmax(rule14, np.fmax(rule15, np.fmax(rule16, np.fmax(rule17, np.fmax(rule20, np.fmax(rule21, rule22))))))))))
    D_DM_max = np.fmax(rule1, np.fmax(rule7, np.fmax(rule13, np.fmax(rule19, rule25))))
    D_ACW_max = np.fmax(rule4, np.fmax(rule5, np.fmax(rule6, np.fmax(rule10, np.fmax(rule11, np.fmax(rule12, np.fmax(rule18, np.fmax(rule23, rule24))))))))

    cut_S_low = np.fmin(S_low, np.full(len(S_low),S_low_max))
    cut_S_med = np.fmin(S_med, np.full(len(S_med),S_med_max))
    cut_S_high = np.fmin(S_high, np.full(len(S_high),S_high_max))

    cut_D_CW = np.fmin(D_CW, np.full(len(D_CW),D_CW_max))
    cut_D_DM = np.fmin(D_DM, np.full(len(D_DM),D_DM_max))
    cut_D_ACW = np.fmin(D_ACW, np.full(len(D_ACW),D_ACW_max))

    finalcut_S = np.fmax(cut_S_low, np.fmax(cut_S_med, cut_S_high))
    finalcut_D = np.fmax(cut_D_CW, np.fmax(cut_D_DM, cut_D_ACW))

    return [finalcut_S,finalcut_D]

generator = np.arange(0, 360, 1)
flag = np.arange(0, 360, 1)
speed = np.arange(0, 101, 1)
direction = np.arange(0, 5.1, 0.1)

F_NE = P1.Trapezoidal(flag, 0, 0, 10, 80)
F_N = P1.Trapezoidal(flag, 10, 80, 100, 170)
F_W = P1.Trapezoidal(flag, 100, 170, 190, 260)
F_S = P1.Trapezoidal(flag, 190, 260, 280, 350)
F_SE = P1.Trapezoidal(flag, 280, 350, 359, 359) 

G_NE = P1.Trapezoidal(generator, 0, 0, 10, 80)
G_N = P1.Trapezoidal(generator, 10, 80, 100, 170)
G_W = P1.Trapezoidal(generator, 100, 170, 190, 260)
G_S = P1.Trapezoidal(generator, 190, 260, 280, 350)
G_SE = P1.Trapezoidal(generator, 280, 350, 359, 359)

S_low = P1.Trapezoidal(speed, 0, 0, 10, 35)
S_med = P1.Trapezoidal(speed, 15, 40, 60, 85)
S_high = P1.Trapezoidal(speed, 65, 90, 100, 100)

D_CW = P1.Triangular(direction, 0, 0, 2.4)
D_DM = P1.Triangular(direction, 2.3, 2.5, 2.7)
D_ACW = P1.Triangular(direction, 2.6, 5, 5)

F = round(int(input("Ingresa el valor en Flag: ")), 0)
G = round(int(input("Ingresa el valor en Generator: ")), 0)

finalcut = defuzzify(F, G)

###############################PLOTTING 1##################################
plt.figure(1)
plt.subplot(411)
plt.plot(flag, F_NE, 'b', linewidth=1.5, label='F_NE')
plt.plot(flag, F_N, 'g', linewidth=1.5, label='F_N')
plt.plot(flag, F_W, 'r', linewidth=1.5, label='F_W')
plt.plot(flag, F_S, 'c', linewidth=1.5, label='F_S')
plt.plot(flag, F_SE, 'm', linewidth=1.5, label='F_SE')
plt.title('FLAG')
plt.ylabel('Membership')
plt.legend()

plt.subplot(412)
plt.plot(generator, G_NE, 'b', linewidth=1.5, label='G_NE')
plt.plot(generator, G_N, 'g', linewidth=1.5, label='G_N')
plt.plot(generator, G_W, 'r', linewidth=1.5, label='G_W')
plt.plot(generator, G_S, 'c', linewidth=1.5, label='G_S')
plt.plot(generator, G_SE, 'm', linewidth=1.5, label='G_SE')
plt.title('GENERATOR')
plt.ylabel('Membership')
plt.legend()

plt.subplot(413)
plt.plot(speed, S_low, 'b', linewidth=1.5, label='S_low')
plt.plot(speed, S_med, 'g', linewidth=1.5, label='S_med')
plt.plot(speed, S_high, 'r', linewidth=1.5, label='S_high')
plt.title('SPEED')
plt.ylabel('Membership')
plt.legend()

plt.subplot(414)
plt.plot(direction, D_CW, 'b', linewidth=1.5, label='D_CW')
plt.plot(direction, D_DM, 'g', linewidth=1.5, label='D_DM')
plt.plot(direction, D_ACW, 'r', linewidth=1.5, label='D_ACW')
plt.title('DIRECTION')
plt.ylabel('Membership')
plt.legend()

###############################PLOTTING 2##################################
plt.figure(2)
plt.subplot(211)
plt.plot(speed, S_low, 'b', linewidth=1.5, label='S_low')
plt.plot(speed, S_med, 'g', linewidth=1.5, label='S_med')
plt.plot(speed, S_high, 'r', linewidth=1.5, label='S_high')
plt.plot(speed, cut_S_low, 'k--', linewidth=1.5, label='cut_S_low')
plt.plot(speed, cut_S_med, 'y--', linewidth=1.5, label='cut_S_med')
plt.plot(speed, cut_S_high, 'c--', linewidth=1.5, label='cut_S_high')
plt.plot(speed, finalcut[0], 'm--', linewidth=1.5, label='finalcut_S')
plt.axvline(fuzz.defuzz(speed,finalcut[0], 'centroid'), linewidth=1.5, color='r', label='Centroid')
print(fuzz.defuzz(speed,finalcut[0], 'centroid'))
plt.title('SPEED')
plt.ylabel('Membership')
plt.legend()

plt.subplot(212)
plt.plot(direction, D_CW, 'b', linewidth=1.5, label='D_CW')
plt.plot(direction, D_DM, 'g', linewidth=1.5, label='D_DM')
plt.plot(direction, D_ACW, 'r', linewidth=1.5, label='D_ACW')
plt.plot(direction, cut_D_CW, 'k--', linewidth=1.5, label='cut_D_CW')
plt.plot(direction, cut_D_DM, 'y--', linewidth=1.5, label='cut_D_DM')
plt.plot(direction, cut_D_ACW, 'c--', linewidth=1.5, label='cut_D_ACW')
plt.plot(direction, finalcut[1], 'm--', linewidth=1.5, label='finalcut_D')
plt.axvline(fuzz.defuzz(direction,finalcut[1], 'centroid'), linewidth=1.5, color='r', label='Centroid')
print(fuzz.defuzz(direction,finalcut[1], 'centroid'))
plt.title('DIRECTION')
plt.ylabel('Membership')
plt.legend()

###############################PLOTTING 3##################################

x = np.zeros((len(flag),len(generator)))
y = np.zeros((len(flag),len(generator)))

for i in flag:
    for j in generator:
        print(i,j)
        x[i][j] = fuzz.defuzz(speed,defuzzify(i,j)[0], 'centroid')
        y[i][j] = fuzz.defuzz(direction,defuzzify(i,j)[1], 'centroid')

flag, generator = np.meshgrid(flag, generator)

plt.figure(3)
#plot surface
ax1 = plt.axes(projection='3d')
ax1.plot_surface(flag, generator, x, rstride=1, cstride=1, cmap=cm.rainbow)
ax1.set_title('Speed surface')
ax1.set_xlabel('flag')
ax1.set_ylabel('generator')
ax1.set_zlabel('speed')

plt.figure(4)
ax2 = plt.axes(projection='3d')
ax2.plot_surface(flag, generator, y, rstride=1, cstride=1, cmap=cm.rainbow)
ax2.set_title('Direction surface')
ax2.set_xlabel('flag')
ax2.set_ylabel('generator')
ax2.set_zlabel('direction')

plt.show()
