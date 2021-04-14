import numpy as np
import pandas as pd

def MACD(data, len1, len2, siglen):
  data['MACD'] = data.Close
  transdata = data[::-1].reset_index(drop=True)
  for i in range(len(transdata.Close) - len2):
    transdata["MACD"][i] = np.mean(trasndata.Close[i:i + len1]) - np.mean(transdata.Close[i: i + len2])
  for i in range(len(transdata["MACD"]) - siglen):
    transdata["Signal"][i] = np.mean(transdata["MACD"][i:i + siglen])
  data = transdata[::-1].reset_index(drop=True)
  return "MACD complete"
