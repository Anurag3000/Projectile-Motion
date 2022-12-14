# -*- coding: utf-8 -*-
"""Organised_With_GNU.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Vm2Jm7EIccI-lWuK3YGk93FR-kYFXmM5
"""

import numpy as np
import math
import pandas as pd

# Y = [Y0, Y1, Y2, Y3]
'''
Since our project requires us to solve 2 second order simultaneous ODEs each of
which are broken down into 2 first order ODE (making it 4 simultaneous eqn) in 
total, we presume Y = [Y0, Y1, Y2, Y3].
Here:
Y0 = x
Y1 = dx/dt = (vx)
Y2 = y
Y3 = dy/dt = (vy)

Now, the initial conditions that we are going to pass into the function are:
Y0(t=0) = x(t=0) = 0
Y1(t=0) = dx/dt = (Vx) = 29cosθ [29 m/s is the usual initial velocity of modern day elite atheletes]
Y2(t=0) = y = 2m (since the athelete lauches the javelin from little above their shoulders)
Y3(t=0) = dy/dt = (Vy) = 29sinθ [29 m/s is the usual initial velocity of modern day elite atheletes]
'''
def f(t, Y0, Y1, Y2, Y3, case):
  if case == "drag":
    k = 0.5*1.255*2.5*0.003
  else: 
    k = 0
  fx_drag = -1*k*29*Y1
  fy_drag = -1*k*29*Y3
  m = 0.8
  fni_Y0 = Y1
  fni_Y1 = fx_drag/m
  fni_Y2 = Y3
  fni_Y3 = fy_drag/m - 9.8
  return fni_Y0, fni_Y1, fni_Y2, fni_Y3

def euler(Y0, Y1, Y2, Y3, a, b, case, l1, grph_key, file_name): 
  N = 999
  h = (b - a)/(N + 1)
  tn = []
  Y0n = []
  Y1n = []
  Y2n = []
  Y3n = []
  for i in range(0, N):
    t = a + i*h
    tn.append(t)
    Y0n.append(Y0)
    Y1n.append(Y1)
    Y2n.append(Y2)
    Y3n.append(Y3)
    fni_Y0, fni_Y1, fni_Y2, fni_Y3 = f(t, Y0, Y1, Y2, Y3, case)
    Y0 = Y0 + h*fni_Y0
    Y1 = Y1 + h*fni_Y1
    Y2 = Y2 + h*fni_Y2
    Y3 = Y3 + h*fni_Y3
    if Y2<=0:
      break   
  if grph_key == 0:
    if case == "no drag":
      print()
    else:
      data_euler_1 = {"x": Y0n, "y" : Y2n}
      my_data111 = pd.DataFrame(data_euler_1)
      my_data111.to_csv(file_name, index = False)
  else:
    return Y0n[-1]

def rk4(Y0, Y1, Y2, Y3, a, b, case, l1, grph_key, file_name): 
  N = 999
  h = (b - a)/(N + 1)
  tn = []
  Y0n = []
  Y1n = []
  Y2n = []
  Y3n = []
  for i in range(0, N):
    t = a + i*h
    tn.append(t)
    Y0n.append(Y0)
    Y1n.append(Y1)
    Y2n.append(Y2)
    Y3n.append(Y3)
    m1_0, m1_1, m1_2, m1_3 = f(t, Y0, Y1, Y2, Y3, case)
    m2_0, m2_1, m2_2, m2_3 = f(t + h/2, Y0 + m1_0*h/2, Y1 + m1_1*h/2, Y2 + m1_2*h/2, Y3 + m1_3*h/2, case)
    m3_0, m3_1, m3_2, m3_3 = f(t + h/2, Y0 + m2_0*h/2, Y1 + m2_1*h/2, Y2 + m2_2*h/2, Y3 + m2_3*h/2, case)
    m4_0, m4_1, m4_2, m4_3 = f(t + h, Y0 + m3_0*h, Y1 + m3_1*h, Y2 + m3_1*h, Y3 + m3_1*h, case)
    mrk4_0 = (m1_0 + 2*m2_0 + 2*m3_0 + m4_0)/6
    mrk4_1 = (m1_1 + 2*m2_1 + 2*m3_1 + m4_1)/6
    mrk4_2 = (m1_2 + 2*m2_2 + 2*m3_2 + m4_2)/6
    mrk4_3 = (m1_3 + 2*m2_3 + 2*m3_3 + m4_3)/6
    Y0 = Y0 + h*mrk4_0
    Y1 = Y1 + h*mrk4_1
    Y2 = Y2 + h*mrk4_2
    Y3 = Y3 + h*mrk4_3
    if Y2<=0:
      break   
  if grph_key == 0:
    if case == "no drag":
      print()
    else:
      data_rk4_1 = {"x": Y0n, "y" : Y2n}
      my_data112 = pd.DataFrame(data_rk4_1)
      my_data112.to_csv(file_name, index = False)
  else:
    return Y0n[-1]

def rk2(Y0, Y1, Y2, Y3, a, b, case, l1, grph_key, file_name): 
  N = 999
  h = (b - a)/(N + 1)
  tn = []
  Y0n = []
  Y1n = []
  Y2n = []
  Y3n = []
  for i in range(0, N):
    t = a + i*h
    tn.append(t)
    Y0n.append(Y0)
    Y1n.append(Y1)
    Y2n.append(Y2)
    Y3n.append(Y3)
    k1_0, k1_1, k1_2, k1_3 = f(t, Y0, Y1, Y2, Y3, case)
    k1_0, k1_1, k1_2, k1_3 = h*k1_0, h*k1_1, h*k1_2, h*k1_3
    k2_0, k2_1, k2_2, k2_3 = f(t+h, Y0 + k1_0, Y1 + k1_1, Y2 + k1_2, Y3 + k1_3, case)
    k2_0, k2_1, k2_2, k2_3 = h*k2_0, h*k2_1, h*k2_2, h*k2_3
    Y0 = Y0 + (k1_0 + k2_0)/2
    Y1 = Y1 + (k1_1 + k2_1)/2
    Y2 = Y2 + (k1_2 + k2_2)/2
    Y3 = Y3 + (k1_3 + k2_3)/2
    if Y2<=0:
      break   
  if grph_key == 0:
    if case == "no drag":
      print()
    else:
      data_rk2_1 = {"x": Y0n, "y" : Y2n}
      my_data113 = pd.DataFrame(data_rk2_1)
      my_data113.to_csv(file_name, index = False)
  else:
    return Y0n[-1]

#CALL:
angle_list = [25, 30, 45, 50, 38]
file_names_euler =['EulerTrajectory25.csv', 'EulerTrajectory30.csv', 'EulerTrajectory45.csv', 'EulerTrajectory50.csv', 'EulerTrajectory38.csv']
file_names_rk2 =['rk2Trajectory25.csv', 'rk2Trajectory30.csv', 'rk2Trajectory45.csv', 'rk2Trajectory50.csv', 'rk2Trajectory38.csv']
file_names_rk4 =['rk4Trajectory25.csv', 'rk4Trajectory30.csv', 'rk4Trajectory45.csv', 'rk4Trajectory50.csv', 'rk4Trajectory38.csv']
label_list = ["25$^{\circ}$", "30$^{\circ}$", "45$^{\circ}$", "50$^{\circ}$", "38$^{\circ}$"]

for i in range(0, 5):
  Y3 = 29*math.sin(0.0174533*angle_list[i])
  Y1 = 29*math.cos(0.0174533*angle_list[i])
  euler(0, Y1, 2, Y3, 0, 5, "drag", label_list[i], 0, file_names_euler[i])

for i in range(0, 5):
  Y3 = 29*math.sin(0.0174533*angle_list[i])
  Y1 = 29*math.cos(0.0174533*angle_list[i])
  rk2(0, Y1, 2, Y3, 0, 5, "drag", label_list[i], 0, file_names_rk2[i])

for i in range(0, 5):
  Y3 = 29*math.sin(0.0174533*angle_list[i])
  Y1 = 29*math.cos(0.0174533*angle_list[i])
  rk4(0, Y1, 2, Y3, 0, 5, "drag", label_list[i], 0, file_names_rk4[i])

angle = []
x_with_drag_euler = []
x_without_drag_euler = []
row_euler = []
record_euler = []
x_with_drag_rk2 = []
x_without_drag_rk2 = []
row_rk2 = []
record_rk2 = []
x_with_drag_rk4 = []
x_without_drag_rk4 = []
row_rk4 = []
record_rk4 = []

for i in range(0, 90):
  Y3 = 29*math.sin(0.0174533*i)
  Y1 = 29*math.cos(0.0174533*i)
  xn_with_drag_euler = euler(0, Y1, 2, Y3, 0, 5, "drag", label_list[0], 1, 'does not matter')
  xn_without_drag_euler = euler(0, Y1, 2, Y3, 0, 5, "no drag", label_list[0], 1, 'does not matter')
  x_with_drag_euler.append(xn_with_drag_euler)
  x_without_drag_euler.append(xn_without_drag_euler)
  angle.append(i)
  row_euler.append(i)
  row_euler.append(xn_with_drag_euler)
  record_euler.append(row_euler)
  row_euler = []
data_euler_2_wo = {"theta": angle, "range" : x_without_drag_euler}
my_data211 = pd.DataFrame(data_euler_2_wo)
my_data211.to_csv('EulerVariationWO.csv', index = False)
data_euler_2_w = {"theta": angle, "range" : x_with_drag_euler}
my_data212 = pd.DataFrame(data_euler_2_w)
my_data212.to_csv('EulerVariationW.csv', index = False)

for i in range(0, 90):
  Y3 = 29*math.sin(0.0174533*i)
  Y1 = 29*math.cos(0.0174533*i)
  xn_with_drag_rk2 = rk2(0, Y1, 2, Y3, 0, 5, "drag", label_list[0], 1, 'does not matter')
  xn_without_drag_rk2 = rk2(0, Y1, 2, Y3, 0, 5, "no drag", label_list[0], 1, 'does not matter')
  x_with_drag_rk2.append(xn_with_drag_rk2)
  x_without_drag_rk2.append(xn_without_drag_rk2)
  #angle.append(i)
  row_rk2.append(i)
  row_rk2.append(xn_with_drag_rk2)
  record_rk2.append(row_rk2)
  row_rk2 = []
data_rk2_2_wo = {"theta": angle, "range" : x_without_drag_rk2}
my_data221 = pd.DataFrame(data_rk2_2_wo)
my_data221.to_csv('rk2VariationWO.csv', index = False)
data_rk2_2_w = {"theta": angle, "range" : x_with_drag_rk2}
my_data222 = pd.DataFrame(data_rk2_2_w)
my_data222.to_csv('rk2VariationW.csv', index = False)

for i in range(0, 90):
  Y3 = 29*math.sin(0.0174533*i)
  Y1 = 29*math.cos(0.0174533*i)
  xn_with_drag_rk4 = rk4(0, Y1, 2, Y3, 0, 5, "drag", label_list[0], 1, 'does not matter')
  xn_without_drag_rk4 = rk4(0, Y1, 2, Y3, 0, 5, "no drag", label_list[0], 1, 'does not matter')
  x_with_drag_rk4.append(xn_with_drag_rk4)
  x_without_drag_rk4.append(xn_without_drag_rk4)
  #angle.append(i)
  row_rk4.append(i)
  row_rk4.append(xn_with_drag_rk4)
  record_rk4.append(row_rk4)
  row_rk4 = []

data_rk4_2_wo = {"theta": angle, "range" : x_without_drag_rk4}
my_data231 = pd.DataFrame(data_rk4_2_wo)
my_data231.to_csv('rk4VariationWO.csv', index = False)
data_rk4_2_w = {"theta": angle, "range" : x_with_drag_rk4}
my_data232 = pd.DataFrame(data_rk4_2_w)
my_data232.to_csv('rk4VariationW.csv', index = False)
