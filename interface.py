from flask import Flask, render_template, jsonify, request
import config
from utils import Real_estate
from werkzeug.datastructures import MultiDict
import traceback
app = Flask(__name__)

@app.route('/')
def home():
    return render_template ("text.html")
    # return "Hi, How are you?"


@app.route('/predict_rate', methods = ["GET","POST"])
def predict_rate():
    try:
        if request.method == "POST":
            data = request.form.get

            # print("User Data is :",data)
            # No	X1_transaction_date	X2_house_age	X3_distance_to_the_nearest_MRT_station	X4_number_of_convenience_stores	X5_latitude	X6_longitude
            No=int(data('No'))
            X1_transaction_date = eval(data('X1_transaction_date'))
            X2_house_age = eval(data('X2_house_age'))
            X3_distance_to_the_nearest_MRT_station = eval(data('X3_distance_to_the_nearest_MRT_station'))
            X4_number_of_convenience_stores=eval(data('X4_number_of_convenience_stores'))
            X5_latitude = eval(data('X5_latitude'))
            X6_longitude = eval(data('X6_longitude'))

            Real_estate_rate= Real_estate(No,X1_transaction_date,X2_house_age,X3_distance_to_the_nearest_MRT_station,X4_number_of_convenience_stores,X5_latitude,X6_longitude)
            
            rate = Real_estate_rate.get_predicted_rate()

            return  render_template("text.html",prediction= rate)
           
        else:
            data = request.args.get
            No=data('No')
            X1_transaction_date = eval(data('X1_transaction_date'))
            X2_house_age = eval(data("X2_house_age"))
            X3_distance_to_the_nearest_MRT_station = eval(data('X3_distance_to_the_nearest_MRT_station'))
            X4_number_of_convenience_stores=eval(data('X4_number_of_convenience_stores'))
            X5_latitude = eval(data('X5_latitude'))
            X6_longitude = eval(data("X6_longitude"))

            
            

            Real_estate_rate= Real_estate(No,X1_transaction_date,X2_house_age,X3_distance_to_the_nearest_MRT_station,X4_number_of_convenience_stores,X5_latitude,X6_longitude)

            rate = Real_estate_rate.get_predicted_rate()

            return  render_template("text.html",prediction= rate)

    except:
        print(traceback.print_exc())
        # return  jsonify({"Message" : "Unsuccessful"})           


if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5006,debug=False)