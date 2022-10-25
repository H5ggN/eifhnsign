import pandas as pd
df = pd.read_csv('IMDB-Movie-Data.csv')
df.info()

# Гипотеза 1: Жанр комедия популярнее, чем хоррор или триллер 
temp = df['Genre'].value_counts()
horror_genre_result = temp['Horror,Thriller']
comedy_genre_result = temp['Comedy']
print('Фильмы с жанром комедия', comedy_genre_result)
print('Фильмы с жанром ужас', horror_genre_result)

# Гипотеза 2. Часто встречающийся актер: Will Smith and Johnny Depp
def list_actors(actors):
    actors = actors.split(', ')
    return actors 

df['Actors'] = df['Actors'].apply(list_actors)
print(df['Actors'])

depp = 0
smith = 0
def count_actors(actors):
    global depp, smith
    if 'Johnny Depp' in actors:
        depp+=1
    if 'Will Smith' in actors:
        smith+=1
    return actors
df['Actors'].apply(count_actors)
print(depp)
print(smith)
df['Rating'].value_counts().plot(kind = 'Raiting', figsize = (8, 5))