import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = r"C:\Users\Aniket\Downloads\API_SP.POP.TOTL_DS2_en_csv_v2_451027\API_SP.POP.TOTL_DS2_en_csv_v2_451027.csv"

df = pd.read_csv(file_path, skiprows=4)

year = '2022'

df_clean = df.dropna(subset=[year]).copy()

df_sorted = df_clean.sort_values(by=year, ascending=False)

top_countries = df_sorted[df_sorted['Country Name'].isin([
    'India', 'China', 'United States', 'Indonesia', 'Pakistan',
    'Nigeria', 'Brazil', 'Bangladesh', 'Russia', 'Mexico'
])]

plt.figure(figsize=(12, 6))
sns.barplot(
    data=top_countries,
    x='Country Name',
    y=year,
    palette='viridis'
)

plt.title('Top 10 Most Populous Countries (2022)', fontsize=16)
plt.xlabel('Country', fontsize=12)
plt.ylabel('Total Population (in billions)', fontsize=12)

plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}B".format(x/1e9)))
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))

sns.histplot(
    data=df_clean,
    x=year,
    bins=30,
    log_scale=True,
    color='royalblue',
    kde=True
)

plt.title('Distribution of Country Populations (2022)', fontsize=16)
plt.xlabel('Total Population (Log Scale)', fontsize=12)
plt.ylabel('Number of Countries/Regions', fontsize=12)
plt.tight_layout()
plt.show()