# CLEANING DATA

import pandas as pd
import warnings

warnings.filterwarnings('ignore')

df = pd.read_csv("C:/Users/ziadh/OneDrive/Desktop/AI/Datasets/TMDB_movie_dataset.csv", parse_dates=['release_date'])
# print(f"before anything : {df.shape}")

df = df[df['vote_average'] != 0]
# print(f"after dropping (vote average = 0) movies : {df.shape}")

df.drop(['backdrop_path',
         'homepage',
         'poster_path',
         'original_title',
         'id',
         'imdb_id',
         'vote_count',
         'original_language',
         'tagline',
         'spoken_languages',
         'production_countries',
         'status'], inplace=True, axis=1)

df.drop_duplicates(subset='title', inplace=True)
print(f"after dropping title duplicates : {df.shape}")

df.dropna(inplace=True)
print(f"after dropping null values: {df.shape}")


# # print(df['profit(M)'].head())
# # print(df['profit(M)'].tail())
#

# IMPLEMENTING DUMMY ENCODING MANUALLY



# COMPANIES
df['production_companies'] = df['production_companies'].apply(lambda x: [company.strip() for company in x.split(',')])
production_companies = df.explode('production_companies')
company_stats = production_companies.groupby('production_companies').agg({
    'revenue': 'sum',
    'popularity': 'sum',
    'vote_average' : 'sum'
})
company_stats['combined_score'] = company_stats['revenue'] + company_stats['popularity'] + company_stats['vote_average']
top_20_companies = company_stats.nlargest(20, 'combined_score')
top_20_company_names = top_20_companies.index.tolist()
for company in top_20_company_names:
    df[company] = df['production_companies'].apply(lambda x: 1 if company in x else 0)


# GENRES
df['genres'] = df['genres'].apply(lambda x: [genre.strip() for genre in x.split(',')])
genres = df.explode('genres')
uniqueGenres = genres['genres'].unique()
for genre in uniqueGenres:
    df[genre] = df['genres'].apply(lambda x: 1 if genre in x else 0)

#
#


# df.to_csv("C:/Users/ziadh/OneDrive/Desktop/AI/Datasets/CleanedData.csv")