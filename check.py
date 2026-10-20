import pandas as pd

df = pd.read_csv("spacex_launch_dash.csv")

# Q1 and Q2: successes, total launches, and success rate per site
print(df.groupby('Launch Site')['class'].agg(['sum', 'count', 'mean']))

# Q3 and Q4: success rate per payload band
bins = [0, 2000, 4000, 6000, 8000, 10000]
df['Payload Range'] = pd.cut(df['Payload Mass (kg)'], bins=bins, include_lowest=True)
print(df.groupby('Payload Range', observed=True)['class'].agg(['sum', 'count', 'mean']))

# Q5: success rate per booster version
print(df.groupby('Booster Version Category')['class'].agg(['sum', 'count', 'mean']))