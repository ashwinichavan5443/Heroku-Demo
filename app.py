import numpy as np
import pickle
from flask import Flask, request,jsonify,render_template

# create flask app using Flask
app=Flask(__name__)

#load model
model=pickle.load(open('salary_model.pkl','rb'))

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():

	int_features=[int(x) for x in request.form.values()]
	final_features = [np.array(int_features)]
	prediction=model.predict(final_features)
	output=round(prediction[0],2)
	return render_template('index.html',prediction_text='Employee Salary should be $ {}'.format(output))

if __name__ == "__main__":
	app.run(debug=True)