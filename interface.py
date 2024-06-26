from flask import Flask,request,jsonify,render_template
import config
from project_ecom.utils import ArticleReturns
import numpy as np

app = Flask(__name__)
@app.route("/")
def get_home():
    return "Probability of returns"

@app.route("/html_page")

def html():
    return render_template("ecom_returns.html")
    articleID      = articleID
    colorCode      = colorCode
    sizeCode       = sizeCode
    productGroup   = productGroup
    quantity       = quantity
    price          = price
    rrp            = rrp
    deviceID       = deviceID
    paymentMethod  = paymentMethod
    predicted_returns = returns[0]

@app.route("/predict_returns",methods= ["POST","GET"])
def get_article():
    if request.method == "POST":
        data = request.form
        print("user input data is >>>",data)
        age = eval(data["articleID"])
        gender = data["colorCode"]
        bmi = eval(data["sizeCode"])
        children = data["productGroup"]
        smoker  = data["quantity"]
        region = data["price"]
        rrp = data["rrp"]
        deviceID = data["deviceID"]
        paymentMethod = data["paymentMethod"]
        
        return_obj = Return_Articles(articleID, colorCode,sizeCode, productGroup, quantity, price, rrp, deviceID,paymentMethod)
        returns = return_obj.get_predict_returns()
        # return jsonify({"Result":f"Returned quantity is {returns[0]}"})
    


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=False)