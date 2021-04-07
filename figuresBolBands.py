from BollingerBands import punch_bolBands
import pandas as pd

def W_figure_criterion(right_max, left_max, middle_max, right_min, left_min):
  check = False
  if right_max > right_min and right_max > left_min:
    if left_max > right_min and left_max > left_min:
      if middle_max > left_min and middle_max > right_min:
        if middle_max < right_max / 2 and middle_max < left_max / 2:
          check = True
  return check

def find_W_figure(data, interval):
  W = "non"
  transdata = data[::-1].reset_index(drop=True)
  transdata = transdata[: interval]
  right_max = transdata.Low[0]
  left_max = transdata.Low[interval - 1]
  right_min_idx = transdata.Low[: interval // 2].idxmin()
  left_min_idx  = transdata.Low[interval // 2 + 1: interval].idxmin()
  right_min = min(transdata.Low[: interval // 2])
  left_min = min(transdata.Low[interval // 2 + 1: interval])
  middle_max = max(transdata.Low[right_min_idx + 1: left_min_idx])
  if W_figure_criterion(right_max, left_max, middle_max, right_min, left_min):
    W = "yes"
  return W

