import pandas as pd

url_htf = '/Users/duncan/Documents/programming/Python/myPyCharm/UCDPA_Project/fixturesTables.html'
html_tables = pd.read_html(url_htf, header=0)
df = html_tables[0].dropna()

del df['Unnamed: 5']

df.loc[:, 'DATE_D'] = df['DATE'].str.extract(r'(\d+)\.\d+')
df.loc[:, 'DATE_M'] = df['DATE'].str.extract(r'\d+\.(\d+)')
df.loc[:, 'S_HOME'] = df['SCORE'].str.extract(r'\((\d+)-\d+\)')
df.loc[:, 'S_AWAY'] = df['SCORE'].str.extract(r'\(\d+-(\d+)\)')

print(df.head())


# df['DATE_D'] = df['DATE'].str.extract(r'(\d+)\.\d+')
# df['DATE_M'] = df['DATE'].str.extract(r'\d+\.(\d+)')
# df['S_HOME'] = df['SCORE'].str.extract(r'\((\d+)-\d+\)')
# df['S_AWAY'] = df['SCORE'].str.extract(r'\(\d+-(\d+)\)')

# df['DATE_D'] = df['DATE'].str.extract('(\d+)\.\d+', expand=True)
# df['DATE_M'] = df['DATE'].str.extract('\d+\.(\d+)', expand=True)
# df['S_HOME'] = df['SCORE'].str.extract('\((\d+)-\d+\)', expand=True)
# df['S_AWAY'] = df['SCORE'].str.extract('\(\d+-(\d+)\)', expand=True)

# from pandasql import sqldf
# import pandas as pd
# from sklearn import datasets
#
# df_feature = datasets.load_iris(as_frame = True)['data']
# df_target = datasets.load_iris(as_frame = True)['target']
# print (type(df_feature))
# print (type(df_target))

print(2+5)
print(3**2)
