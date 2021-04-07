def trend(data, ran):
  trend = "non"
  trendx = []
  trendy = []
  start = len(data) - ran
  m1 = max(data["High"][start: start + ran // 3])
  m2 = max(data["High"][start + ran // 3: start + ran // 3 * 2])
  m3 = max(data["High"][start + ran // 3 * 2:])
  min1 = min(data["Low"][start: start + ran // 3])
  min2 = min(data["Low"][start + ran // 3: start + ran // 3 * 2])
  min3 = min(data["Low"][start + ran // 3 * 2:])
  if m3 > m2 > m1 or min3 > min2 > min1:
    trend = "up"
  elif m3 < m2 < m1 or min3 < min2 < min1:
    trend = "down"
  if trend == "down":
    trendy.append([m1, m3])
    trendx.append([start, len(data)])
  elif trend == "up":
    trendy.append([min1, min3])
    trendx.append([start, len(data)])
  return trendx, trendy
