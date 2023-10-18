import sqlite3
from flask import Flask, render_template, jsonify
from datetime import datetime
from bokeh.plotting import figure, output_file
from bokeh.embed import components

# create a flask instance
app = Flask(__name__)

# create a route 
@app.route('/')
def index():
    # establish a connection to the database
    conn = sqlite3.connect('values.db')
    # create a cursor to execute SQL commands
    c = conn.cursor()
    # execute SQL command to select the latest values for tag12
    c.execute("SELECT date, value FROM robot WHERE name = 'tag12' ORDER BY date DESC LIMIT 10")
    # fetch the results and format them as (datetime, float) tuples
    results = c.fetchall()
    data = [(datetime.strptime(row[0], "%H:%M:%S"), row[1]) for row in results]
    # close the connection
    conn.close()

    # create a Bokeh figure with datetime x-axis and float y-axis
    p = figure(title='Tag 12 Values', x_axis_type='datetime')
    p.line([x[0] for x in data], [x[1] for x in data])

    # generate the HTML components of the plot
    script, div = components(p)

    # pass the script and div to the template
    return render_template("index.html", script=script, div=div)

if __name__ == '__main__':
    app.run(debug=True)
