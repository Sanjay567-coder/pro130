import pandas as pd

df = pd.read_csv('final2.csv')
print(f'Old Shape of DataFrame: {df.shape}')
print(f'Old Coloumn Names: {list(df)}')

df = df.rename(columns={'Star_name': 'Star Name'})

del df['Unnamed: 0']
del df['Luminosity']
print(f'New Shape of DataFrame: {df.shape}')
print(f'New Coloumn Names: {list(df)}')

df.to_csv('with nan values.csv')