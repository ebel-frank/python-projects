import pandas as pd
import matplotlib.pyplot as plt

fb = pd.read_csv('data/facebook.csv', index_col=0)

fb['MA15'] = fb['Close'].rolling(15).mean()
fb['MA50'] = fb['Close'].rolling(50).mean()

fb['Shares'] = [1 if fb.loc[ei, 'MA15'] > fb.loc[ei, 'MA50'] else 0 for ei in fb.index]

fb['Close1'] = fb['Close'].shift(-1)
fb['Profit'] = [fb.loc[ei, 'Close1'] - fb.loc[ei, 'Close'] if fb.loc[ei, 'Shares']==1 else 0 for ei in fb.index]
fb['Profit'].plot()
plt.axhline(y=0, color='red')

fb['wealth'] = fb['Profit'].cumsum()
print(fb.tail())

# plot the wealth to show the growth of profit over the period

fb['wealth'].plot()
print('Total money you win is {}'.format(fb.loc[fb.index[-2], 'wealth']))
print('Total money you spent is {}'.format(fb.loc[fb.index[0], 'Close']))

plt.legend()
plt.show()
