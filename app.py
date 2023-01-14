from flask import Flask, render_template
import scrapper
import pandas as pd

df = pd.read_csv('dane_spotify.csv')
#artists = df['artist']
artists = ['Eminem',"Selena Gomez","P!nk"]
images = []
i=0
for artist in artists:
   url = f"https:/{scrapper.GetImageSrc(artist)}"
   images.append(url)
   print(i)
   i=i+1
print(images)
test = zip(artists, images)
    

app = Flask(__name__)
@app.route('/')
def hello_world():
    return render_template('index.html', test = test)

    

if __name__ == '__main__':
    app.run()