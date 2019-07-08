from flask import Flask, render_template, request
#can send requests to urls with this library
import requests

#create app - dont need a db, so dont need to import a config
app = Flask(__name__)

#route for the landing page
@app.route('/')
def homepage():
    return render_template('/index.html')

#route for GETing the surf report
@app.route('/report', methods=['POST'])
def report():
    #get the value from the form
    '''
    county_name = request.form['countyName']
    r = requests.get('http://api.spitcast.com/api/county/water-temperature/'+county_name+'/')
    json_object = r.json()
    temp = json_object['fahrenheit']
    #return str(temp)
    '''
    banyans_report = request.form['banyans']
    r = requests.get('http://api.spitcast.com/api/county/water-temperature/orange-county')
    json_object = r.json()
    temp = json_object['fahrenheit']
    return render_template('report.html', temp=temp)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')