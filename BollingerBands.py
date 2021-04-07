import numpy as np
from trend import trend

def punch_bolBands(data, interval):
  punch = "non"
  transdata = data[len(data) - interval:]
  MSE = np.mean(transdata)
  up = MSE + 2 * np.std(transdata)
  down = MSE - 2 * np.std(transdata)
  if transdata.High[-1] > up:
    punch = "up"
  elif transdata.Low[-1] < down:
    punch = "down"
  return punch

def walking_bolBands(data, interval):
  count_of_up_punches = 0
  count_of_down_punches = 0
  transdata = data[::-1]
  MSE_STD = [[np.mean(transdata[i: interval + i]), np.std(transdata[i: interval + i])] for i in range(interval)]
  up = []
  down = []
  for i in MSE_STD:
    up.append(i[0] + 2 * i[1])
    down.append(i[0] - 2 * i[1])
  for i in range(interval):
    if transdata.High[i] > up[i]:
      count_of_up_punches += 1
    if transdata.Low[i] > down[i]:
      count_of_down_punches += 1
  return count_of_up_punches, count_of_down_punches
