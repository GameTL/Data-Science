# %%
import pandas as pd
import plotly.graph_objects as go
n = 5  # n in head(n) determine the numbers of rows to read
dataframes1 = pd.read_csv('Small_Reviews.csv') # plain untouch csv as dataframes1


# plotly.graph_objects as go
list_of_scores = dataframes1.groupby(['Score'])['Score'].count() # extracting the data and count the nunbers of the rating
#print(list_of_scores)
print(dataframes1['Score'] != 3) # check if score is more than 3
graph1 = go.Figure(data=go.Bar(x=[1,2,3,4,5], y=list_of_scores))
graph1.update_traces(marker_color="turquoise",marker_line_color='rgb(8,48,107)', marker_line_width=1.5)
graph1.update_layout(title_text='Product Score')
graph1.show()

# %%
