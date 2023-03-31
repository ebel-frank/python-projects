import pandas as pd
import matplotlib.pyplot as plt

fb = pd.read_csv('data/facebook.csv', index_col=0)

print("This is the head\n", fb.head(1))
print("\nThis is the tail\n", fb.tail(1))
print(f"\nThe first index is: {fb.index[1]}")
print("\nThis is the columns\n", fb.columns)
print("\nThis dataframe has {} height and {} width".format(*fb.shape))  # number of rows and columns

# print(fb.describe())   # This returns the statistical summary of the data frame
# print(fb['Close'])      # selects the close column
# print(fb[['Open', 'Close']])      # selects the multiple column

# fb['AVERAGE'] = (fb['Close'] + fb['Close'].shift(1) + fb['Close'].shift(2)) / 3

fb['MA3'] = fb['Close'].rolling(15).mean()
print(fb[['Close', 'MA3']])
fb = fb.dropna()     # use dropna to remove any "Not a Number" data
# plot the moving average

plt.figure(figsize=(10, 8))
fb['MA3'].loc['2015-01-01':'2015-12-31'].plot(label='MA15')
fb['Close'].loc['2015-01-01':'2015-12-31'].plot(label='Close')
# plt.legend()
plt.show()
