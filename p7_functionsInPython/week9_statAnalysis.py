import pandas as pd
import seaborn as sns

tips = sns.load_dataset('tips')
# print(tips)

sns.lmplot()
penguins = sns.load_dataset('penguins')
sns.pairplot(penguins)
