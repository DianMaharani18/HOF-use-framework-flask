
from flask import Flask, render_template 
import requests 
import json

# definisi flask
aplikasi = Flask(__name__, template_folder='template')

# ambil data dari api menggunakan json
data = json.load(open("dataset/movies.json"))

# membuat list utama
datamovies = []

# membuat list filter dan map
hurufkapital = []
listfilter = []
ratingatas = []
ratingbawah = []

for i in range(24):
    movies =  dict()
    movies['id'] = data[i]["id"]
    movies['Title'] = data[i]["title"]
    movies['Year'] = data[i]["year"]
    movies['Genre'] = data[i]["genres"]
    movies['Rating'] = data[i]['imdbRating']
    movies['Poster'] = data[i]['posterurl']

    # menambahkan list kolom title
    hurufkapital.append(movies['Title'])


    typeCapitalize = list(map(lambda x: x.capitalize(), hurufkapital))
    HurufBesar = [f'{i}' for i in typeCapitalize]
    movies['Title'] = HurufBesar[i]

    # menambahkan kolom Rating ke listfilter
    listfilter.append(movies['Rating'])
    datamovies.append(movies)

# memfilter film yang memiliki rating > 6
filterin = list(filter(lambda x: x > 6, listfilter))
for i in filterin:
    indeks = listfilter.index(i)
    movies = dict()
    movies['id'] = datamovies[indeks]["id"]
    movies['Title'] = datamovies[indeks]["Title"]
    movies['Year'] = datamovies[indeks]["Year"]
    movies['Genre'] = datamovies[indeks]["Genre"]
    movies['Rating'] = datamovies[indeks]['Rating']
    movies['Poster'] = datamovies[indeks]['Poster']
    ratingatas.append(movies)

# memfilter film yang memiliki rating < 6
filterin = list(filter(lambda x: x < 6, listfilter))
for i in filterin:
    indeks = listfilter.index(i)
    movies = dict()
    movies['id'] = datamovies[indeks]["id"]
    movies['Title'] = datamovies[indeks]["Title"]
    movies['Year'] = datamovies[indeks]["Year"]
    movies['Genre'] = datamovies[indeks]["Genre"]
    movies['Rating'] = datamovies[indeks]['Rating']
    movies['Poster'] = datamovies[indeks]['Poster']
    ratingbawah.append(movies)


# menjalankan flask yang dihubungkan ke html
@aplikasi.route('/')
def home():
    return render_template('index.html',movies=datamovies)

@aplikasi.route('/urutkan')
def urut():
    urutkandata = sorted(datamovies, key=lambda x : x['Rating'])
    return render_template ('sorted.html', movies=urutkandata)

@aplikasi.route('/filterlebih')
def filterLebih():
    datalebih = sorted(ratingatas, key=lambda x: x['Rating'], reverse=True)
    return render_template ('filter.html', movies=datalebih)

@aplikasi.route('/filterkurang')
def filterKurang():
    datakurang = sorted(ratingbawah, key=lambda x: x['Rating'], reverse=True)
    return render_template ('filter1.html', movies=datakurang)

@aplikasi.route('/author')
def author():
    return render_template('author.html')

if __name__ == "__main__":
    aplikasi.run()