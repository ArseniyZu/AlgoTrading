from trend import trend
import pandas as pd

def punch_bolBands(data, interval, std):
  punch = "non"
  transdata = data[::-1].reset_index(drop=True)
  transdata = transdata[:interval]
  MSE = transdata.Close.mean()
  up = MSE + std * transdata.Close.std()
  down = MSE - std * transdata.Close.std()
  if transdata.High[0] > up:
    punch = "up"
  elif transdata.Low[0] < down:
    punch = "down"
  elif transdata.High[0] = up:
    punch = "up touch"
  elif transdata.Low[0] = down:
    punch = "down touch"
  return punch

def walking_bolBands(data, interval, ran, std):
  count_of_up_punches = 0
  count_of_down_punches = 0
  transdata = data[::-1].reset_index(drop=True)
  MSE_STD = [[transdata.Close[i: interval + i].mean(), transdata.Close[i: interval + i].std()] for i in range(ran)]
  up = []
  down = []
  for i in MSE_STD:
    up.append(i[0] + std * i[1])
    down.append(i[0] - std * i[1])
  for i in range(ran):
    if transdata.High[i] > up[i]:
      count_of_up_punches += 1
    if transdata.Low[i] < down[i]:
      count_of_down_punches += 1
  trend_bolB = trend(data, ran)[0]
  return trend_bolB, count_of_up_punches, count_of_down_punches
