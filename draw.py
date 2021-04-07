import plotly.graph_objects as go
import matplotlib.pyplot as plt

def drawCandle(df, left, right):
    fig = go.Figure(data=[go.Candlestick(x=[i for i in range(left, right + 1)],
                open=df["Open"][left: right + 1],
                high=df["High"][left: right + 1],
                low=df['Low'][left: right + 1],
                close=df['Close'][left: right + 1])])
    fig.update_layout(title=f"df")
    fig.show()
    
def drawTrend(df, trendx, trendy):
  fig = go.Figure(data=[go.Candlestick(x=[i for i in range(len(df))],
                open=df["Open"],
                high=df["High"],
                low=df['Low'],
                close=df['Close'])])
  fig.add_trace(go.Scatter, x = trendx, y = trendy,
                mode = "lines")
  fig.show()
