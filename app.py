from flask import Flask, jsonify, request , render_template, url_for, redirect
#from graphviz import render
import pandas as pd
import pickle
import numpy as np

app = Flask(__name__, template_folder='template')

@app.route("/")
def home():
    return render_template("predict.html")

@app.route("/predict", methods=['POST'])
def do_prediction():
    
#    json = request.get_json()
    int_features = [float(x) for x in request.form.values()]
    print("int_fea", int_features)
    final_features = [np.array(int_features)]
    model = pickle.load(open('house-linear.pkl','rb'))
#    df = pd.DataFrame(json, index=[0])
    print("finalfeature" , final_features)
    y_predict = model.predict(final_features)

    result = {"Predicted House Price" : y_predict[0]}
    print(y_predict)
    return render_template("predict.html", prediction_text='Your predicted price is Rs {}'.format(y_predict))
    #return jsonify(result)

if __name__ == "__main__":
#    app.run(debug=True, port=80, host='0.0.0.0')
    app.run(host='0.0.0.0',port=80)