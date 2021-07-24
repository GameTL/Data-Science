#%%
import pandas as pd
import nltk
import plotly.graph_objects as go
from wordcloud import WordCloud, STOPWORDS 
import matplotlib.pyplot as plt
import seaborn as sns
color = sns.color_palette()
import plotly.offline as py
py.init_notebook_mode(connected=True)
import plotly.tools as tls 
import plotly.express as px
stopwords = set(STOPWORDS)

n = 5  # n in head(n) determine the numbers of rows to read
dataframes1 = pd.read_csv('Small_Reviews.csv') # plain untouch csv as dataframes1

#%%
# plotly.graph_objects as go
list_of_scores = dataframes1.groupby(['Score'])['Score'].count() # extracting the data and count the nunbers of the rating
#print(list_of_scores)
print(dataframes1['Score'] != 3) # check if score is more than 3
graph1 = go.Figure(data=go.Bar(x=[1,2,3,4,5], y=list_of_scores))
graph1.update_traces(marker_color="turquoise",marker_line_color='rgb(8,48,107)', marker_line_width=1.5)
graph1.update_layout(title_text='Product Score')
graph1.show()

#%%
dataframes1 = pd.read_csv('Small_Reviews.csv') # Small_Reviews.csv
comment_words = '' 
stopwords = set(STOPWORDS)
# Raw sheet = dataframe1 

# iterate through the csv file 
for val in dataframes1.Text:
           # typecaste each val to string val = str(val)
           # split the value 
           tokens = val.split() 
           # Converts each token into lowercase 
           for i in range(len(tokens)): 
                      tokens[i] = tokens[i].lower()
           comment_words += " ".join(tokens)+" "
# Spec of the printout
wordcloud = WordCloud(width = 1600, height = 1600, background_color ='black', stopwords = stopwords, min_font_size = 10).generate(comment_words) 
# plot the WordCloud image					 
plt.figure(figsize = (9, 9), facecolor = None) 
plt.imshow(wordcloud) 
plt.axis("off") 
plt.tight_layout(pad = 0) 
plt.show() 

dataframes1 = dataframes1[dataframes1['Score'] != 3]
#Split the csv into two positive and negetive csv
# Applying lambda function to find 
dataframes1['sentiment'] = dataframes1['Score'].apply(lambda rating : +1 if rating > 3 else -1)
positive_dataframes1 = dataframes1[dataframes1['sentiment'] == 1]
negetive_dataframes1 = dataframes1[dataframes1['sentiment'] == -1]


#%%

def general_word_cloud():
    stopwords.update(["br", "href","good","great"]) # For excluding words
    ## good and great removed because they were included in negative sentiment
    pos = " ".join(review for review in dataframes1.Summary) ##dataframes1.Summary conrespond to the column which contain text reviews in the pandas-ised dataframe##
    wordcloud2 = WordCloud(width = 1600, height = 1600, background_color ='black', stopwords = stopwords, 
                min_font_size = 10).generate(comment_words) 
    postive_plt.figure(figsize = (9, 9), facecolor = None) 
    postive_plt.imshow(wordcloud2)
    postive_plt.axis("off") # off the pixel axis
    postive_plt.show()



# %%
    
# Split the csv into two positive and negetive csv
# Applying lambda function to find 
dataframes1['sentiment'] = dataframes1['Score'].apply(lambda rating : +1 if rating > 3 else -1)
positive_dataframes1 = dataframes1[dataframes1['sentiment'] == 1]
negetive_dataframes1 = dataframes1[dataframes1['sentiment'] == -1]

# Postive Word Cloud
stopwords.update(["br", "href","good","great", "food"]) # For excluding words
positive_token_words = " ".join(review for review in positive_dataframes1.Summary)
positive_wordcloud = WordCloud(width = 1600, height = 1600, background_color ='white', stopwords = stopwords, 
           min_font_size = 10).generate(positive_token_words) 
plt.figure(figsize = (9, 9), facecolor = None) 
plt.imshow(positive_wordcloud)
plt.axis("off") # off the pixel axis
plt.show()

# Negetive Word Cloud
stopwords.update(["br", "href","good","great","food"]) # For excluding words
negetive_token_words = " ".join(review for review in negetive_dataframes1.Summary)
negetive_wordcloud = WordCloud(width = 1600, height = 1600, background_color ='black', stopwords = stopwords, min_font_size = 10).generate(negetive_token_words) 
plt.figure(figsize = (9, 9), facecolor = None) 
plt.imshow(negetive_wordcloud)
plt.axis("off") # off the pixel axis
plt.show()