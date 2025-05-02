import pandas as pd
import warnings

warnings.filterwarnings('ignore')

df = pd.read_csv("C:/Users/ziadh/OneDrive/Desktop/AI/DA Project/Datasets/CleanedData.csv")
df.drop(['Unnamed: 0'], inplace=True, axis=1)

df = df[['title', 'keywords']]
df['keywords'] = df['keywords'].str.replace(',', '')

df = df.iloc[0:30000]

from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

englishStopWords = stopwords.words('english')

vectorizer = TfidfVectorizer(stop_words=englishStopWords)
tfidf = vectorizer.fit_transform(df['keywords'])
cosineSim = cosine_similarity(tfidf)
cosineSim = pd.DataFrame(cosineSim)
indices = pd.Series(df.index, index=df['title'])


def movieRecommendationSystem(title, cosineSim=cosineSim, num=5):
    i = indices[title]
    indexes = cosineSim[i].nlargest(num+1).index.tolist()
    recommendedMovies = indices[indexes].index.tolist()
    return recommendedMovies[1:num+1]


recommendedMovies = movieRecommendationSystem('Avatar')
for movie in recommendedMovies:
    print(movie)