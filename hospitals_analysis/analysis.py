import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', 8)
general = pd.read_csv('test/general.csv')
prenatal = pd.read_csv('test/prenatal.csv')
sports = pd.read_csv('test/sports.csv')
pd.set_option('display.max_columns', None)
# print(general.head(20))
# print(prenatal.head(20))
# print(sports.head(20))

prenatal = prenatal.set_axis(list(general.columns), axis=1)
sports = sports.set_axis(list(general.columns), axis=1)

frames = [general, prenatal, sports]
df = pd.concat(frames, ignore_index=True)
df.drop('Unnamed: 0', axis=1, inplace=True)

df.dropna(how='all', inplace=True)


def replace_gender(x):
    if x == 'woman' or x == 'female':
        return 'f'
    elif x == 'man' or x == 'male':
        return 'm'


df['gender'] = df['gender'].apply(replace_gender)
df['gender'].fillna('f', inplace=True)
df.fillna(0, inplace=True)
# print(df.shape)
# print(df.sample(20, random_state=30))

# 1
print(df.groupby('hospital').count()['gender'])
# print('The answer to the 1st question is general')
# 2
print(pd.crosstab(df.hospital, df.diagnosis).loc['general']['stomach']/pd.crosstab(df.hospital, df.diagnosis).loc['general'].sum())
# print('The answer to the 2nd question is 0.325')
# 3

print(round(df.groupby(['hospital', 'diagnosis']).count().loc['sports']['mri']['dislocation'] /
            df.groupby(['hospital', 'diagnosis']).count().loc['sports']['mri'].sum(), 3))
# print('The answer to the 3rd question is 0.285')
# 4
print(abs(df.groupby('hospital').mean()['age']['general'] - df.groupby('hospital').mean()['age']['sports']))
print('The answer to the 4th question is 19.573256026111462')

# 5
# print(pd.crosstab(df.hospital, df.blood_test)['t'])
# print('The answer to the 5th question is prenatal, 325 blood tests')

# -----
# 1
print('The answer to the 1st question: 15-35')
df.plot(y='age', kind='hist', bins=15)
plt.show()

# 2
print('The answer to the 2nd question: pregnancy')
df.groupby('diagnosis').count()['mri'].plot(y='diagnosis', kind='pie')
plt.show()

# 3
print(df[['hospital', 'height']])
print(df[['hospital', 'height']].pivot(columns='hospital', values='height'))
general_df = df[['hospital', 'height']].pivot(columns='hospital', values='height')['general'].dropna()
prenatal_df = df[['hospital', 'height']].pivot(columns='hospital', values='height')['prenatal'].dropna()
sports_df = df[['hospital', 'height']].pivot(columns='hospital', values='height')['sports'].dropna()
plt.violinplot([general_df, prenatal_df, sports_df])
plt.show()


