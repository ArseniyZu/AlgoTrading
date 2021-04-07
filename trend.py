def trend(data, ran):
  trend = "non"
  trendx = []
  trendy = []
  transdata = data[::-1].reset_index(drop=True)
  transdata = transdata[:ran]
  m1 = max(transdata["High"][: ran // 3])
  m2 = max(transdata["High"][ran // 3: ran // 3 * 2])
  m3 = max(transdata["High"][ran // 3 * 2:])
  min1 = min(transdata["Low"][: ran // 3])
  min2 = min(transdata["Low"][ran // 3: ran // 3 * 2])
  min3 = min(transdata["Low"][ran // 3 * 2:])
  if m3 > m2 > m1 or min3 > min2 > min1:
    trend = "down"
  elif m3 < m2 < m1 or min3 < min2 < min1:
    trend = "up"
  if trend == "down":
    trendy = [m1, m3]
    trendx = [len(data) - ran, len(data)]
  elif trend == "up":
    trendy = [min1, min3]
    trendx = [len(data) - ran, len(data)]
  return trend, trendx, trendy
