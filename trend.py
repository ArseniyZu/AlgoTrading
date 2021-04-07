def trend_3max(data, ran):
  trend = "non"
  start = len(data) - ran
  m1 = max(data["High"][start: start + ran // 3])
  m2 = max(data["High"][start + ran // 3: start + ran // 3 * 2])
  m3 = max(data["High"][start + ran // 3 * 2:])
  if m3 > m2 > m1:
    trend = "up"
  elif m3 < m2 < m1:
    trend = "down"
  return trend


def trend_3min(data, ran):
  trend = "non"
  start = len(data) - ran
  m1 = min(data["Low"][start: start + ran // 3])
  m2 = min(data["Low"][start + ran // 3: start + ran // 3 * 2])
  m3 = min(data["Low"][start + ran // 3 * 2:])
  if m3 > m2 > m1:
    trend = "up"
  elif m3 < m2 < m1:
    trend = "down"
  return trend
  
