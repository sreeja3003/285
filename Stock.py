import time
from datetime import date

import yfinance as yf
from flask import Flask, request
from pandas_datareader import data as pdr

now = time.strftime("%c")

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST']) #allow both GET and POST requests
def index():
    if request.method == 'POST':  #this block is only entered when the form is submitted
        stock = request.form['symbol']
        company_yfinance_object = yf.Ticker(stock)
        name = company_yfinance_object.info['longName'] + " (" + str(stock) +  ")\n\n"
        today = date.today()
        d1 = today.strftime("%Y-%m-%d")
        data = pdr.get_data_yahoo(stock, start=d1, end=d1)
        curr_time = now
        price = str(round(data.Close[0],2)) + " " + str(round(data.Close[0]-data.Open[0],2)) + " (" + str(round((data.Close[0]-data.Open[0])/data.Open[0],2)) + "%)"

        return '''<title>Python Finance Info</title>
            <form method="POST">
                <h3>Python Finance Info</h3><br/>
                <i>Input:</i><br/><br/>     
                Enter a symbol <input type="text" name="symbol">
                <input type="submit" value="Submit"><br/><br/>
            </form>
            <i>Output: </i><br/><br/> {} PDT   <br/><br/><br/> {}    <br/><br/><br/> {}    </h5>'''.format(curr_time, name, price)

    return '''<title>Python Finance Info</title>
        <form method="POST">
            <h3>Python Finance Info</h3><br/>
            <i> Input: </i><br/><br/>
            Enter a symbol: <input type="text" name="symbol"><br/>
            <input type="submit" value="Submit"><br/>
        </form>'''

@app.errorhandler(404)
def page_not_found(e):
    return '''{}'''. format(e)

@app.errorhandler(500)
def internal_server_error(e):
    return '''{}'''. format(e)

if __name__ == '__main__':
    app.run(debug=True)
