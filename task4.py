import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import folium
from folium.plugins import HeatMap

df = pd.read_csv('dummy_us_accidents.csv')
df['Start_Time'] = pd.to_datetime(df['Start_Time'])

df['Hour'] = df['Start_Time'].dt.hour
plt.figure(figsize=(10, 5))
sns.countplot(x='Hour', data=df, color='skyblue')
plt.title('Accident Frequency by Hour of Day')
plt.show()

plt.figure(figsize=(10, 5))
sns.barplot(x='Weather_Condition', y='Severity', data=df, estimator=lambda x: len(x), errorbar=None)
plt.title('Accident Count by Weather Condition')
plt.show()

m = folium.Map(location=[39.8283, -98.5795], zoom_start=4)
heat_data = [[row['Start_Lat'], row['Start_Lng']] for index, row in df.iterrows()]
HeatMap(heat_data).add_to(m)
m.save('accident_hotspots.html')