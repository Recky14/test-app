# importing the libraries
from flask import Flask,render_template,request
import pickle

#Global variables
app=Flask(__name__)
loaded_model=pickle.load(open('Milk.pkl','rb'))

#user defined routes
@app.route("/")
def home():
    return render_template('index.html')

@app.route("/prediction",methods=['POST'])
def predict():
    Temperature=request.form['Temprature']
    Taste=request.form['Taste']
    Fat=request.form['Fat']
    
    prediction=loaded_model.predict([[Temperature,Taste,Fat]])[0]
    
    if prediction==0:
        prediction="Bad Quality"
    elif prediction==1:
        prediction="Normal Quality"
    else :
        prediction="Good Quality"
        
    return render_template("index.html",output_prediction=prediction)


if __name__ =='__main__':
    app.run(debug=True)       


