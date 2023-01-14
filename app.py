from flask import Flask, render_template
import scrapper
import pandas as pd
import numpy
pd.options.display.max_colwidth = 9999999999999999999999999999999999



df = pd.read_csv('dane_spotify.csv')
df_two = df.drop_duplicates('artist')
df_three = df.groupby('artist').count().sort_values(by = 'artist')
df_four = df_two.sort_values(by= 'artist')
artists = df_four['artist']
howmuch = df_three['Unnamed: 0']
images = []
i=0

def GetArtistSongs(artist):
    songs = df[df['artist'] == artist]
    artist_songs = songs['title']
    artist_songs_year = songs['year']
    artist_songs_language = songs['language']
    artist_songs_genre = songs['top genre']

    return zip(list(artist_songs), list(artist_songs_year), list(artist_songs_language) ,list(artist_songs_genre))

def GetSongLyrics(title):
    song = df[df['title'] == title]
    lyrics = song['lyrics']
    return lyrics.item()


for artist in artists:
   url = f"https:/{scrapper.GetImageSrc(artist)}"

   images.append(url)
   print(f"{i/170 *100}%")
   i=i+1

test = zip(artists, images, howmuch)
    

app = Flask(__name__)
@app.route('/')
def hello_world():
    return render_template('index.html', test = test)

@app.route('/<artist>')
def profile(artist):
    photo = f"https:/{scrapper.GetImageSrc(artist)}"
    return render_template('artist.html',artist = artist, zipek = GetArtistSongs(artist), photo= photo)

@app.route('/<artist>/<title>')
def lyrics(artist,title):
    lyrics = GetSongLyrics(title)
    return render_template('lyrics.html',artist = artist, title = title, lyrics = lyrics)



if __name__ == '__main__':
    app.run()