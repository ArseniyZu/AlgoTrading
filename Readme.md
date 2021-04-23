```python
!git clone https://github.com/ArseniyZu/AlgoTrading.git
%cd AlgoTrading/
```

    Cloning into 'AlgoTrading'...
    remote: Enumerating objects: 183, done.[K
    remote: Counting objects: 100% (183/183), done.[K
    remote: Compressing objects: 100% (176/176), done.[K
    remote: Total 183 (delta 101), reused 16 (delta 3), pack-reused 0[K
    Receiving objects: 100% (183/183), 106.99 KiB | 855.00 KiB/s, done.
    Resolving deltas: 100% (101/101), done.
    /content/AlgoTrading
    


```python
!git pull
```

    remote: Enumerating objects: 5, done.[K
    remote: Counting objects: 100% (5/5), done.[K
    remote: Compressing objects: 100% (3/3), done.[K
    remote: Total 3 (delta 2), reused 0 (delta 0), pack-reused 0[K
    Unpacking objects: 100% (3/3), done.
    From https://github.com/ArseniyZu/AlgoTrading
       2dd8f64..6fe119e  main       -> origin/main
    Updating 2dd8f64..6fe119e
    Fast-forward
     MACD.py | 2 [32m+[m[31m-[m
     1 file changed, 1 insertion(+), 1 deletion(-)
    


```python
pip install ta
```

    Collecting ta
      Downloading https://files.pythonhosted.org/packages/a9/22/a355ecf2d67da8150332d22ef65c3a1f79109528279bf5d40735b6f2bd72/ta-0.7.0.tar.gz
    Requirement already satisfied: numpy in /usr/local/lib/python3.7/dist-packages (from ta) (1.19.5)
    Requirement already satisfied: pandas in /usr/local/lib/python3.7/dist-packages (from ta) (1.1.5)
    Requirement already satisfied: pytz>=2017.2 in /usr/local/lib/python3.7/dist-packages (from pandas->ta) (2018.9)
    Requirement already satisfied: python-dateutil>=2.7.3 in /usr/local/lib/python3.7/dist-packages (from pandas->ta) (2.8.1)
    Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.7/dist-packages (from python-dateutil>=2.7.3->pandas->ta) (1.15.0)
    Building wheels for collected packages: ta
      Building wheel for ta (setup.py) ... [?25l[?25hdone
      Created wheel for ta: filename=ta-0.7.0-cp37-none-any.whl size=28716 sha256=53c7b24ba212a0ee0d1b2793cd27484f53738d9a6cd3403ec19f9972bf589330
      Stored in directory: /root/.cache/pip/wheels/dd/88/30/de9553fb54a474eb7480b937cdbb140bdda613d29cf4da7994
    Successfully built ta
    Installing collected packages: ta
    Successfully installed ta-0.7.0
    


```python
import pandas as pd
import matplotlib.pyplot as plt
from draw import drawCandle, drawTrend, draw_Idic
from trend import trend
from operations import Operations
from BollingerBands import punch_bolBands, walking_bolBands
from figuresBolBands import find_W_figure
from MACD import MACD, find_cross
import ta
```


```python
df = pd.read_csv('МТС.txt', sep=";", usecols=["<OPEN>", "<DATE>", "<CLOSE>", "<LOW>", "<HIGH>"], decimal=",")
df.columns = ["Date", "Open", "High", "Low", "Close"]
df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Date</th>
      <th>Open</th>
      <th>High</th>
      <th>Low</th>
      <th>Close</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>20170103</td>
      <td>259.95</td>
      <td>268.40</td>
      <td>259.00</td>
      <td>262.65</td>
    </tr>
    <tr>
      <th>1</th>
      <td>20170104</td>
      <td>262.85</td>
      <td>263.10</td>
      <td>257.05</td>
      <td>259.30</td>
    </tr>
    <tr>
      <th>2</th>
      <td>20170105</td>
      <td>260.80</td>
      <td>264.75</td>
      <td>258.00</td>
      <td>260.50</td>
    </tr>
    <tr>
      <th>3</th>
      <td>20170106</td>
      <td>259.45</td>
      <td>262.70</td>
      <td>254.00</td>
      <td>257.00</td>
    </tr>
    <tr>
      <th>4</th>
      <td>20170109</td>
      <td>257.00</td>
      <td>259.55</td>
      <td>255.45</td>
      <td>258.40</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.shape
```




    (1008, 5)




```python
drawCandle(df, 0, len(df))
```

![png](images/output_1.png)




```python
df["aroon_up"] = ta.trend.aroon_up(df.Close, 14)
df["aroon_down"] = ta.trend.aroon_down(df.Close, 14)
df[15:20]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Date</th>
      <th>Open</th>
      <th>High</th>
      <th>Low</th>
      <th>Close</th>
      <th>aroon_up</th>
      <th>aroon_down</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>15</th>
      <td>20170124</td>
      <td>267.80</td>
      <td>269.85</td>
      <td>265.10</td>
      <td>265.70</td>
      <td>85.714286</td>
      <td>28.571429</td>
    </tr>
    <tr>
      <th>16</th>
      <td>20170125</td>
      <td>266.00</td>
      <td>269.70</td>
      <td>265.70</td>
      <td>268.00</td>
      <td>78.571429</td>
      <td>21.428571</td>
    </tr>
    <tr>
      <th>17</th>
      <td>20170126</td>
      <td>268.00</td>
      <td>279.00</td>
      <td>268.00</td>
      <td>277.50</td>
      <td>100.000000</td>
      <td>14.285714</td>
    </tr>
    <tr>
      <th>18</th>
      <td>20170127</td>
      <td>277.45</td>
      <td>279.55</td>
      <td>273.05</td>
      <td>277.05</td>
      <td>92.857143</td>
      <td>7.142857</td>
    </tr>
    <tr>
      <th>19</th>
      <td>20170130</td>
      <td>277.50</td>
      <td>278.95</td>
      <td>273.90</td>
      <td>276.35</td>
      <td>85.714286</td>
      <td>7.142857</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.Date.iloc[-1]
```




    20201230




```python
df.Date.iloc[0]
```




    20170103




```python
draw_Idic(df, df.aroon_up, df.aroon_down) # Up - orange, Down - Blue
```
![png](images/output_2.png)




```python
df["Stoch"] = ta.momentum.stoch(df.High, df.Low, df.Close, 14)
df["StockSig"] = ta.momentum.stoch_signal(df.High, df.Low, df.Close, 14)
```


```python
draw_Idic(df, df.Stoch, df.StockSig)
```
![png](images/output_3.png)


### Стратегия 1. Использование индикаторов Aroon и Stochastic.


```python
# start budget = 10000$
strategy1 = Operations(10000)
# Simulation of the bot on the test dataset (Strategy1)
for i in range(100, len(df)):
  data = df[:i]
  if trend(data, 14)[0] == "down":
    if data.Stoch.iloc[-2] > data.Stoch.iloc[-14]:
      strategy1.buy("MTC", 25, data.Open.iloc[-1])
    check = [data.aroon_down.iloc[-3] < data.aroon_up.iloc[-3], data.aroon_down.iloc[-2] > data.aroon_up.iloc[-2]]
    if bool(set(check)):
      strategy1.sell("MTC", 25, data.Open.iloc[-1])
    elif check.count(False) == 2:
      if data.Close.iloc[-3] < data.Open.iloc[-3] and data.Close.iloc[-2] > data.Open.iloc[-2]:
        strategy1.buy("MTC", 25, data.Open.iloc[-1])
  if trend(data, 14)[0] == "up":
    if data.Stoch.iloc[-2] > 80 or data.aroon_up.iloc[-2] > 80:
      strategy1.buy("MTC", 25, data.Open.iloc[-1])
```

    No asset of this ticker
    No asset of this ticker
    No asset in estate
    No asset in estate
    No asset in estate
    No asset in estate
    No asset in estate
    No asset in estate
    No asset in estate
    No asset in estate
    No asset in estate
    No asset in estate
    No asset in estate
    No asset in estate
    No money in budget
    No money in budget
    No money in budget
    No money in budget
    No money in budget
    No money in budget
    No money in budget
    No money in budget
    No money in budget
    No money in budget
    No money in budget
    No money in budget
    No money in budget
    No money in budget
    No money in budget
    No money in budget
    No money in budget
    No money in budget
    No money in budget
    No money in budget
    No money in budget
    No money in budget
    No money in budget
    No money in budget
    No money in budget
    No money in budget
    No money in budget
    No money in budget
    No money in budget
    No money in budget
    No money in budget
    No money in budget
    No asset in estate
    No asset in estate
    No asset in estate
    No asset in estate
    No money in budget
    No money in budget
    No money in budget
    No money in budget
    No asset in estate
    No asset in estate
    No asset in estate
    No asset in estate
    No asset in estate
    No asset in estate
    No asset in estate
    No asset in estate
    No asset in estate
    No asset in estate
    No money in budget
    No money in budget
    No money in budget
    No money in budget
    No money in budget
    No money in budget
    No money in budget
    No money in budget
    No money in budget
    No money in budget
    No money in budget
    No money in budget
    No money in budget
    No money in budget
    No asset in estate
    No money in budget
    No money in budget
    No money in budget
    No money in budget
    No asset in estate
    No asset in estate
    No asset in estate
    No asset in estate
    No asset in estate
    No asset in estate
    No asset in estate
    No asset in estate
    No asset in estate
    No asset in estate
    No money in budget
    No asset in estate
    No asset in estate
    No asset in estate
    No asset in estate
    No money in budget
    No money in budget
    No money in budget
    No asset in estate
    No asset in estate
    No asset in estate
    No asset in estate
    No money in budget
    No money in budget
    No asset in estate
    No asset in estate
    No asset in estate
    No asset in estate
    No asset in estate
    No asset in estate
    No asset in estate
    No asset in estate
    No asset in estate
    No asset in estate
    No asset in estate
    No asset in estate
    No asset in estate
    No asset in estate
    No asset in estate
    No money in budget
    No money in budget
    No money in budget
    No money in budget
    No money in budget
    No money in budget
    No money in budget
    No asset in estate
    No asset in estate
    No asset in estate
    No asset in estate
    No asset in estate
    No asset in estate
    No asset in estate
    No asset in estate
    No money in budget
    No asset in estate
    No asset in estate
    No asset in estate
    No asset in estate
    No asset in estate
    No asset in estate
    No asset in estate
    No asset in estate
    No asset in estate
    No asset in estate
    No asset in estate
    No asset in estate
    No asset in estate
    No asset in estate
    No money in budget
    No money in budget
    No money in budget
    No money in budget
    No money in budget
    No money in budget
    No money in budget
    No money in budget
    No money in budget
    No asset in estate
    No asset in estate
    No asset in estate
    No asset in estate
    No asset in estate
    No asset in estate
    No asset in estate
    No money in budget
    No money in budget
    No money in budget
    No money in budget
    No money in budget
    No money in budget
    No money in budget
    No money in budget
    No money in budget
    No money in budget
    No money in budget
    No asset in estate
    No asset in estate
    No asset in estate
    No asset in estate
    No asset in estate
    No asset in estate
    No asset in estate
    No asset in estate
    No asset in estate
    No money in budget
    No asset in estate
    No money in budget
    No money in budget
    No money in budget
    No money in budget
    No money in budget
    No money in budget
    No money in budget
    No money in budget
    No money in budget
    No money in budget
    No money in budget
    No money in budget
    No money in budget
    No asset in estate
    No asset in estate
    No asset in estate
    No asset in estate
    No asset in estate
    No asset in estate
    No asset in estate
    No asset in estate
    No asset in estate
    No asset in estate
    No asset in estate
    No asset in estate
    No asset in estate
    No asset in estate
    No asset in estate
    No asset in estate
    No money in budget
    No money in budget
    No money in budget
    No money in budget
    No money in budget
    No money in budget
    No money in budget
    No asset in estate
    No asset in estate
    No asset in estate
    No asset in estate
    No asset in estate
    No asset in estate
    No asset in estate
    No money in budget
    No money in budget
    No money in budget
    No money in budget
    No money in budget
    No money in budget
    No money in budget
    No money in budget
    No money in budget
    No money in budget
    No money in budget
    No money in budget
    No money in budget
    No money in budget
    No money in budget
    No money in budget
    No money in budget
    No asset in estate
    No asset in estate
    No asset in estate
    No asset in estate
    No money in budget
    No money in budget
    No money in budget
    No money in budget
    No money in budget
    No money in budget
    No money in budget
    No money in budget
    No money in budget
    No money in budget
    No money in budget
    No money in budget
    No money in budget
    No money in budget
    No money in budget
    No money in budget
    No money in budget
    No asset in estate
    No money in budget
    No money in budget
    No money in budget
    No money in budget
    No money in budget
    No asset in estate
    No asset in estate
    No asset in estate
    No asset in estate
    No asset in estate
    No asset in estate
    No asset in estate
    No asset in estate
    No asset in estate
    No asset in estate
    No asset in estate
    No money in budget
    No money in budget
    No money in budget
    No money in budget
    No money in budget
    No money in budget
    No money in budget
    No money in budget
    No money in budget
    No money in budget
    No money in budget
    No money in budget
    No money in budget
    No money in budget
    No money in budget
    No money in budget
    No money in budget
    No asset in estate
    No asset in estate
    No asset in estate
    No asset in estate
    No asset in estate
    No asset in estate
    No asset in estate
    No asset in estate
    No money in budget
    No money in budget
    No asset in estate
    No money in budget
    No money in budget
    No money in budget
    No money in budget
    No money in budget
    No money in budget
    No money in budget
    No money in budget
    No money in budget
    No money in budget
    No money in budget
    No money in budget
    No money in budget
    No money in budget
    No money in budget
    No money in budget
    No money in budget
    No money in budget
    No asset in estate
    No asset in estate
    No asset in estate
    No asset in estate
    No asset in estate
    No money in budget
    No money in budget
    No money in budget
    No money in budget
    No money in budget
    No asset in estate
    No asset in estate
    No asset in estate
    No asset in estate
    No asset in estate
    No asset in estate
    No asset in estate
    No asset in estate
    No asset in estate
    No asset in estate
    No asset in estate
    No asset in estate
    No money in budget
    No money in budget
    No asset in estate
    No asset in estate
    No asset in estate
    No asset in estate
    No asset in estate
    No money in budget
    No money in budget
    No money in budget
    No money in budget
    


```python
strategy1.budget + strategy1.assets["MTC"] * df.Open.iloc[-1]
```




    11756.25



### Доходность составила около 11.8% за 4 года. Что является 2.95% годовых.       
### В данной стратегии не учтена комиссия => результат     неудовлетворительный. Возможные причины:      
1. "Неудобная тестовая выборка" для используемых индикаторов.        
2. Индикаторы не всегда точно подтверждают реальный тренд.    
