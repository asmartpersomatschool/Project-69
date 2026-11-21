#Students have to create relationship and correlation charts for checking the relationship between various features of the given dataset. 
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv("gapminder(2007).csv", index_col=0)

sns.set_theme(style="whitegrid")

plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x="gdp_cap", y="life_exp", hue="continent")
plt.title("Scatter Plot: GDP per Capita vs Life Expectancy")
plt.xlabel("GDP per Capita ($)")
plt.ylabel("Life Expectancy (Years)")
plt.show()

plt.figure(figsize=(7, 5))
correlation_matrix = df[["population", "life_exp", "gdp_cap"]].corr()
sns.heatmap(
    correlation_matrix,
    annot=True,
    cmap="coolwarm",
    vmin=-1,
    vmax=1,
)
plt.title("Heatmap: Feature Correlation Matrix")
plt.show()

pair_fig = sns.pairplot(
    df[["population", "life_exp", "gdp_cap", "continent"]],
    hue="continent",
    diag_kind="kde",
)
pair_fig.fig.suptitle(
    "Pair Plot: Relationships Across Features by Continent", y=1.02
)
plt.show()
