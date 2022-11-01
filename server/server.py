from flask import Flask, request, jsonify
import util

# Creates a Flask app
app = Flask(__name__)

# To expose HTTP endpoint is through:
@app.route('/get_workclass_names')
def get_workclass_names():
    response = jsonify({
        'workclass': util.get_workclass_names()
        })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


@app.route('/get_education_names')
def get_education_names():
    response = jsonify({
        'education': util.get_education_names()
        })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


@app.route('/get_marital_status')
def get_marital_status():
    response = jsonify({
        'marital_status': util.get_marital_status_names()
        })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.route('/predict_income', methods=['POST'])
def predict_income():
    age = int(request.form['age'])
    workclass = request.form['workclass'] 
    education = request.form['education'] 
    marital_status = request.form['marital_status'] 

    response = jsonify({
        'income': util.get_income(age, workclass, education, marital_status)
        })

    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


if __name__ == '__main__':
    print("Starting the python Flask Server")
    util.load_saved_artifacts()
    app.run()
