def trend(data, ran):
  trend = "non"
  trendx = []
  trendy = []
  transdata = data[::-1].reset_index(drop=True)
  transdata = transdata[:ran]
  m1 = max(transdata["High"][: ran // 3])
  m2 = max(transdata["High"][ran // 3: ran // 3 * 2])
  m3 = max(transdata["High"][ran // 3 * 2:])
  if m3 > m2 > m1:
    trend = "down"
  elif m3 < m2 < m1:
    trend = "up"
  if trend == "down":
    trendy = [m3, m1]
    trendx = [len(data) - ran, len(data)]
  elif trend == "up":
    trendy = [m3, m1]
    trendx = [len(data) - ran, len(data)]
  return trend, trendx, trendy
