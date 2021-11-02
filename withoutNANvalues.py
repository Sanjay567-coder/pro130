import pandas as pd

df = pd.read_csv('final2.csv')
print(f'Old Shape of DataFrame: {df.shape}')
print(f'Old Coloumn Names: {list(df)}')

df = df.rename(columns={'Star_name': 'Star Name'})
df = df[df['Star Name'].notna()]
df = df[df['Distance'].notna()]
df = df[df['Mass'].notna()]
df = df[df['Radius'].notna()]

del df['Unnamed: 0']
del df['Luminosity']
print(f'New Shape of DataFrame: {df.shape}')
print(f'New Coloumn Names: {list(df)}')

df.to_csv('without nan values.csv')