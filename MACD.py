import numpy as np
import pandas as pd

def MACD(data, lendata, len1, len2, siglen):
  data['MACD'] = data.Close
  data["Signal"] = data.Close
  transdata = data[::-1].reset_index(drop=True)
  transdata = transdata[:lendata]
  for i in range(len(transdata.Close) - len2):
    transdata["MACD"][i] = np.mean(transdata.Close[i:i + len1]) - np.mean(transdata.Close[i: i + len2])
  for i in range(len(transdata["MACD"]) - siglen):
    transdata["Signal"][i] = np.mean(transdata["MACD"][i:i + siglen])
  data = transdata[::-1].reset_index(drop=True)
  data = data[len2 + siglen:]
  data["HIST_MACD"] = data.MACD - data.Signal
  return data

def find_cross(data):
  signal = 0
  if data.iloc[-2]["HIST_MACD"] > 0 and data.iloc[-1]["HIST_MACD"] < 0:
    signal = "Down"
  elif data.iloc[-2]["HIST_MACD"] < 0 and data.iloc[-1]["HIST_MACD"] > 0:
    signal = "Up"
  return signal
