import pandas as pd
import matplotlib.pyplot as plt
path = 'C:\\Users\\wojda\\OneDrive\\Dokumenty\\GitHub\\skryptowe_jezyki_LAB\\skryptowe_jezyki_programowania\\LAB6\\movies.csv'
file = pd.DataFrame(pd.read_csv(path))

# podpunkt a)
print('Rekord o indeksie 2\n')
print(file.loc[2])
print('\nPodsumowanie danych z pliku\n')
print(pd.DataFrame.describe(file))

# podpunkt b)
file.drop('description', axis=1, inplace=True)
print('\nTen sam rekord po usunięciu kolumny\n')
print(file.loc[2])

# podpunkt c)
file.dropna(subset=['duration'], inplace=True)
# print(file.loc[19]) próba printowania tego rekordu skutkuje errorem bo został dropnięty

# podpunkt d)
file['duration'] = file['duration'].str.replace(
    ' min', '')  # usunięcie ' min' z kolumny
file['duration'].astype(int)  # zmiana typu kolumny na int
print('\n rekord o indeksie 12 po usunięciu\n\n', file.loc[12])

# podpunkt e)
print('\n*** opis kolumn duration oraz rating ***\n\n',
      file[['duration', 'rating']].describe())

# podpunkt f)
print(file[['title', 'rating', 'votes']].sort_values(by=['rating'], ascending=False))

# podpunkt g)
file['stars'] = round(file['rating'])
print(file.loc[12])

# podpunkt h)
diagram = file.groupby(['stars'])['stars'].count() # pogrupowanie i zliczenie rekordów
diagram.plot()
plt.show()

# podpunkt i)
file['duration'].astype(int).hist().set(xlabel = 'duration', ylabel = 'amount')
plt.show()