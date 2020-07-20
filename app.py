from flask import Flask , render_template
import requests
app=Flask(__name__)


@app.route("/")
def main_page():
    return render_template("home.html")

@app.route("/bitcoin",methods=["get"])
def price():
    info = requests.get('https://api.coindesk.com/v1/bpi/currentprice/CNY.json')
    json_coin=info.json()
    time=json_coin['time']['updated']
    USD_rate=json_coin['bpi']['USD']['rate']
    USD_description=json_coin['bpi']['USD']['description']
    CNY_rate=json_coin['bpi']['CNY']['rate']
    CNY_description=json_coin['bpi']['CNY']['description']
    return render_template('Price.html',time=time,U_rate=USD_rate,U_des=USD_description,C_rate=CNY_rate,C_des=CNY_description)

if __name__ == "__main__":
    app.run(debug=True)












