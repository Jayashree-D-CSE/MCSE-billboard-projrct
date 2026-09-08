
# Billboard Hot 100 Analysis Script
import billboard
import pandas as pd
import matplotlib.pyplot as plt

# Fetch Hot 100
chart = billboard.ChartData('hot-100')
data = [{"Rank": s.rank, "Song": s.title, "Artist": s.artist, "Weeks_on_Chart": s.weeks} for s in chart]
df = pd.DataFrame(data)

# Clean
df["Weeks_on_Chart"] = pd.to_numeric(df["Weeks_on_Chart"], errors="coerce").fillna(0).astype(int)
df["Song"] = df["Song"].str.strip().str.title()
df["Artist"] = df["Artist"].str.strip().str.title()

# Save dataset
df.to_csv("billboard_hot100.csv", index=False)

print("✅ Data saved to billboard_hot100.csv")
print(df.head())
