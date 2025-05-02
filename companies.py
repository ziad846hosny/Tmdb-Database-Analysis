import pandas as pd
import warnings

warnings.filterwarnings('ignore')

# WE WILL BE CONCENTRATING ON THE TOP 20 MOVIE PRODUCTION COMPANIES
# top5movies                            :)
# average vote rate                     :)
# average runtime                       :)
# revenue achieved in the past 5 years  :)
# most movies adult wala la             :)
# most used genres                      :)

df = pd.read_csv("C:/Users/ziadh/OneDrive/Desktop/AI/Datasets/CleanedData.csv", parse_dates=['release_date'])
df.drop(['Unnamed: 0'], inplace=True, axis=1)

start = df.columns.get_loc('Warner Bros. Pictures')
end = df.columns.get_loc('Lionsgate') + 1

companyNames = df.iloc[:, start:end].columns.tolist()

top5Movies = []
for companyName in companyNames:
    movies = df[['title', 'revenue']][df[companyName] == 1].nlargest(5, 'revenue')
    top5Movies.append(movies['title'].tolist())

voteRate = []
for companyName in companyNames:
    voteRate.append(df['vote_average'][df[companyName] == 1].mean().round(2))

avgRuntime = []
for companyName in companyNames:
    avgRuntime.append(df['runtime'][df[companyName] == 1].mean().round(2))

adultPercentage = []
for companyName in companyNames:
    counts = df['adult'][df[companyName] == 1].value_counts()
    percentage = counts.iloc[0] / counts.values.sum() * 100
    adultPercentage.append(percentage)

start = df.columns.get_loc('Action')
end = df.columns.get_loc('Documentary') + 1
genres = df.iloc[:, start:end].columns.tolist()



genresPercentages = []
for companyName in companyNames:
    tempDf = df[df[companyName] == 1]
    onesOfAllGenres = 0
    for x in genres:
        if len(tempDf[x].value_counts().tolist()) == 1:
            continue
        onesOfAllGenres += tempDf[x].value_counts().tolist()[1]
    for genre in genres:
        if len(tempDf[genre].value_counts().tolist()) == 1:
            onesPercentage = 0
            genresPercentages.append(onesPercentage)
            continue
        onesCount = tempDf[genre].value_counts().tolist()[1]
        onesPercentage = (onesCount / onesOfAllGenres) * 100
        genresPercentages.append(onesPercentage)







#names
# top5movies                            :)
# average vote rate                     :)
# average runtime                       :)
# revenue achieved in the past 5 years  :)
# most movies adult wala la             :)
# most used genres                      :)

data = {
    'names': companyNames * 19,
    'top 5 movies': top5Movies * 19,
    'average vote rate': voteRate * 19,
    'average run time': avgRuntime * 19,
    'adult movies percentage': adultPercentage * 19,
    'genres names': genres * 20,
    'used genres percentages': genresPercentages
}

df = pd.DataFrame(data)
df.sort_values('names', inplace=True)

df.to_csv("C:/Users/ziadh/OneDrive/Desktop/AI/Datasets/CompaniesDataset.csv")
