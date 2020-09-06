import numpy as np
import pickle
import joblib
from pickle import load
from flask import Flask, request, jsonify, render_template
from joblib import load

app = Flask(__name__)
pipe=load('final.save')
#model = pickle.load(open('model.pkl', 'rb'))


# with open('model.pkl', 'rb') as f:
#     model1 = pickle.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/y_predict',methods=['POST'])
def y_predict():
    '''
    For rendering results on HTML GUI
    '''
    x_test = [x for x in request.form.values()]
    print(x_test)
    '''test=trans.transform(x_test)
    print(test)'''
    if x_test[1]=="France" or "france":
    	x_test[1]=0
    elif x_test[1]=="germany" or "Germany":
    	x_test[1]=1
    elif x_test[1]=="spain" or "Spain":
    	x_test[1]=2
    x=[x_test]
    prediction = pipe.predict(x)
    print(prediction)
    output=prediction[0]
    
    return render_template('index.html', prediction_text='Exited {}'.format(output))

'''@app.route('/predict_api',methods=['POST'])
def predict_api():
    
    #For direct API calls trought request
    
    data = request.get_json(force=True)
    prediction = model.y_predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)'''

if __name__ == "__main__":
    app.run(debug=True)
