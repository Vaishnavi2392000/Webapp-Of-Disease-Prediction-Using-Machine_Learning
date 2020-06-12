from flask import Flask,request,render_template
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np

#pip freeze > requirements.txt
app=Flask(__name__)


@app.route("/",methods=["GET","POST"])
def home():
	if request.method=='GET':
		return render_template("form.html")
	else:
		ds=pd.read_csv('diabetes1.csv')
		X=ds.iloc[:,[0,1,2,5,6]]
		y=ds.iloc[::,-1]
		X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.75,random_state=0)
		model=LogisticRegression()
		model.fit(X_train,y_train)
		Pregnancies=int(request.form['Pregnancies'])
		Glucose=int(request.form['Glucose'])
		BloodPressure=int(request.form['BloodPressure'])
		BMI=float(request.form['BMI'])
		DiabetesPedigreeFunction=float(request.form['DiabetesPedigreeFunction'])
		new=np.array([[Pregnancies,Glucose,BloodPressure,BMI,DiabetesPedigreeFunction]])
		y_pred=model.predict(new)
		return render_template("result.html",y_pred=y_pred)



@app.route("/heart",methods=["GET","POST"])
def heart():
	if request.method=='GET':
		return render_template('form1.html')
	else:
		ds=pd.read_csv('heart.csv')
		X=ds.drop('target',axis=1)
		y=ds.iloc[:,-1]
		X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.25,random_state=0)
		reg=LogisticRegression()
		reg.fit(X_train,y_train)
		Age=int(request.form['Age'])
		gender=int(request.form['gender'])
		cp=int(request.form['cp'])
		trestbps=int(request.form['trestbps'])
		chol=int(request.form['chol'])
		fbs=int(request.form['fbs'])
		restecg=int(request.form['restecg'])
		thalach=int(request.form['thalach'])
		y_pred=reg.predict([[Age,gender,cp,trestbps,chol,fbs,restecg,thalach,ds['exang'].mean(),ds['oldpeak'].mean(),ds['slope'].mean(),ds['ca'].mean(),ds['thal'].mean()]])
		return render_template("result1.html",y_pred=y_pred)





if __name__ == '__main__':
	app.run(debug=True)
