from flask import Flask, request
from flask import render_template
import random
import pycountry
app = Flask(__name__)

def generate_random_info(num):
    countries = []
    for country in pycountry.countries:
        countries.append(country.name)
    ships=[]
    for _ in range(num):
        name = random.choice(["fury3", "comet1", "valiant12", "rapid44", "immortal123", "meteor565"])
        year = random.randint(1980, 2020)
        country = random.choice(countries)
        tuple1 = (name, year, country)
        ships.append(tuple1)
    return ships


@app.route('/add')
def add_ship():
    return render_template('add_ship.html')


@app.route('/', methods=['POST', 'GET'])
def result():
    list1 = generate_random_info(20)
    if request.method == 'POST':
        result1 = request.form
        return render_template("ships_table_form.html", result=result1, ship_list=list1)
    else:
        return render_template("ships_table_form.html",result=None, ship_list=list1)

app.run()