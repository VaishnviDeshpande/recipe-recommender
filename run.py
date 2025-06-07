import webbrowser
from flask import Flask, render_template, request
from app.data_loader import load_data
from app.recommender import recommend_recipes
import threading

app = Flask(__name__)
df = load_data()

@app.route('/', methods=['GET', 'POST'])
def index():
    recipes = []
    if request.method == 'POST':
        ingredients = request.form['ingredients'].lower().split(',')
        ingredients = [i.strip() for i in ingredients]
        recipes = recommend_recipes(df, ingredients)
    return render_template('index.html', recipes=recipes)

def open_browser():
    webbrowser.open("http://127.0.0.1:5000")

if __name__ == '__main__':
    threading.Timer(1.25, open_browser).start()
    app.run(debug=True)
