from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')
  
@app.route('/gallery')
def gallery():
    photos = os.listdir("static/photos")
    return render_template('gallery.html', photos=photos)
  
if __name__ == '__main__':
    app.run(debug=True)