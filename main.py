from flask import Flask
from flask import (
    request, flash, url_for, redirect, g, render_template)

import random
import pycountry
app = Flask(__name__)


def generate_random_info(num):
    countries = []
    for country in pycountry.countries:
        countries.append(country.name)
    ships = []
    for i in range(num):
        name = f"ship #{i}"
        year = random.randint(1980, 2020)
        country = random.choice(countries)
        size = 5*i+1
        description = f" this is ship {i}"
        tuple1 = (name, year, country, size, description)
        ships.append(tuple1)
    return ships, countries


db1, countries = generate_random_info(20) # пока очень грубо представляю базу данных


@app.route('/add')
def add_ship():
    return render_template('add_ship.html')


@app.route('/', methods=['POST', 'GET'])
def result():
    list1 = db1
    if request.method == 'POST':
        result1 = request.form
        return render_template("ships_table_form.html", result=result1, ship_list=list1)
    else:
        return render_template("ships_table_form.html", result=None, ship_list=list1)#


@app.route('/edit', methods=["GET", "POST"])
def edit():
    if request.method == 'POST':
        if (not request.form['name'] or
                not request.form['country'] or
                not request.form['ship_description']or
                not request.form['built_year'] or
                not request.form['size']):
            flash('Please enter all the fields', 'error')
        else:
            t1 = (request.form['name'], request.form['built_year'], request.form['country'],
                  request.form['size'], request.form['ship_description'])
            db1.append(t1)
        return redirect(url_for("result"))
    else:
        ship_name = request.args.get('name')
        for ship in db1:
            if ship_name == ship[0]:
                db1.remove(ship)
        return render_template('edit.html', countries=countries)


@app.route('/delete', methods=["GET", "POST"])
def delete():
    if request.method == "GET":
        ship_name = request.args.get('name')
        print(ship_name)
        for ship_row in db1:
            if ship_name == ship_row[0]:
                db1.remove(ship_row)
        return render_template("ships_table_form.html", result=None, ship_list=db1)


if __name__ == '__main__':
    app.run()