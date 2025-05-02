import numpy as np
import pandas as pd
import warnings

warnings.filterwarnings('ignore')

df = pd.read_csv("C:/Users/ziadh/OneDrive/Desktop/AI/Datasets/CleanedData.csv", parse_dates=['release_date'])
df.drop(['Unnamed: 0'], inplace=True, axis=1)

start = df.columns.get_loc('Action')
end = df.columns.get_loc('Documentary') + 1

genres = df.iloc[:, start:end]
genreNames = genres.columns.tolist()
genreNames.sort()


df['release_date'] = pd.to_datetime(df['release_date'], format='%m/%d/%Y')
df['year'] = df['release_date'].dt.year

meanOfRevenue = np.mean(df['revenue'])

profitableGenres = []
meanRatios = []
for name in genreNames:
    genresMean = np.mean(df['revenue'][(df[name] == 1) & ((df['year'] >= 2018) & (df['year'] <= 2022))])
    print(f'mean ratio of {name} is {(genresMean / meanOfRevenue).round(3)}')
    if genresMean / meanOfRevenue > 1:
        profitableGenres.append(name)
    meanRatios.append((genresMean / meanOfRevenue).round(2))

print(f'The profitable genres are: {profitableGenres}')


top5Movies = []
for genreName in genreNames:
    movies = df[['title', 'revenue']][df[genreName] == 1].nlargest(5, 'revenue')
    for item in movies['title'].tolist():
        top5Movies.append(item)

pro = []
for x in genreNames:
    if x in profitableGenres:
        pro.append(True)
    else:
        pro.append(False)


rev = []
for name in genreNames:
    rev.append(df['revenue'][(df[name] == 1) & (df['year'] == 2018)].sum())

for name in genreNames:
    rev.append(df['revenue'][(df[name] == 1) & (df['year'] == 2019)].sum())

for name in genreNames:
    rev.append(df['revenue'][(df[name] == 1) & (df['year'] == 2020)].sum())

for name in genreNames:
    rev.append(df['revenue'][(df[name] == 1) & (df['year'] == 2021)].sum())

for name in genreNames:
    rev.append(df['revenue'][(df[name] == 1) & (df['year'] == 2022)].sum())

data = {
    'names': genreNames * 5,
    'meanRatios': meanRatios * 5,
    'profitable': pro * 5,
    'years' : [2018, 2019, 2020, 2021, 2022] * 19,
    'revenue' : rev
}

genresDataset = pd.DataFrame(data)

genresDataset.sort_values('names', inplace=True)
genresDataset['top 5 movies'] = top5Movies
# genresDataset.to_csv("C:/Users/ziadh/OneDrive/Desktop/AI/Datasets/GenresDataset.csv")