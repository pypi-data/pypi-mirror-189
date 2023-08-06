import pandas as pd
from regbot import signal
#from regpredict.regbot import signal
df = pd.read_csv('two_hour_btc_regbot.csv')
df = df.dropna()
df = df.tail(600)
from pandarallel import pandarallel

pandarallel.initialize()
y_pred = []
def getSignal(open,close):
    return signal(open,close)


df = df[df['regbot-min'] == 1]
print(df.head())

df['result'] = df.parallel_apply(lambda row: getSignal(row['open'], row['close']), axis=1)

print(df.head())

print(len(df[df['result'] != df['enter_long']]), len(df))
