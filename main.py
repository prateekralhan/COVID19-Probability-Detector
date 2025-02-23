from flask import Flask,render_template, request
import pickle

app = Flask(__name__)

file=open('ml_model.pkl','rb')
logreg=pickle.load(file)
file.close()

@app.route('/',methods=["GET","POST"])
def hello_world():
    if request.method == 'POST':
        myDict = request.form
        fever=int(myDict['fever'])
        age=int(myDict['age'])
        pain=int(myDict['pain'])
        runnyNose=int(myDict['runnyNose'])
        diffBreath=int(myDict['diffBreath'])
        #Inference code
        input_features=[fever,pain,age,runnyNose,diffBreath]
        infProb = logreg.predict_proba([input_features])[0][1]
        print(infProb)
        return render_template('show.html',inf=round(infProb*100))
    return render_template('index.html')
    #return 'Hello, World!'+str(infProb)


if __name__ == "__main__":
    app.run(debug=True)
