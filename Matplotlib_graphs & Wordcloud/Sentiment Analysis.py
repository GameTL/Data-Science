import pandas as pd
import plotly.graph_objects as go

n = 5  # n in head(n) determine the numbers of rows to read
dataframes = pd.read_csv('Reviews.csv')

print(dataframes)

fig = go.Figure(data=go.Bar(y=[2, 3, 10]))
fig.show()