import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = sns.load_dataset("iris")

sns.pairplot(df, hue="species")
plt.show()

sns.heatmap(df.corr(), annot=True)
plt.show()
