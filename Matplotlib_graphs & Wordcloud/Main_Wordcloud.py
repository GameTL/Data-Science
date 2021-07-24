'''
Input : txt file of normal words
Output : worldcloud of the most occuring words
'''
# %%
# Setting
REALATIVE_FILE_PATH_NAME = "lizziecomment.txt" # name of the file consist of long string of words
IMAGE_WIDTH = 1600
IMAGE_HEIGHT = 1600
BACKGROUND_COLOUR = "white"
MINIMUM_FONT_SIZE = 10


# %%
# Setting
from wordcloud import WordCloud, STOPWORDS 
import matplotlib.pyplot as plt
stopwords = set(STOPWORDS)
n = 5  # n in head(n) determine the numbers of rows to read
with open(REALATIVE_FILE_PATH_NAME, "r") as file:
    df = file.read()
print(df)

# %%

wordcloud = WordCloud(width = IMAGE_WIDTH, height = IMAGE_HEIGHT, background_color = BACKGROUND_COLOUR, stopwords = stopwords, min_font_size = MINIMUM_FONT_SIZE).generate(df) 
plt.figure(figsize = (9, 9), facecolor = None) 
plt.imshow(wordcloud)
plt.axis("off") # off the pixel axis
plt.show()




