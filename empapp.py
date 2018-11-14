from flask import Flask,render_template,request
from empdata import Employees 
app=Flask(__name__)
getEmployees=Employees()

@app.route('/')
def index():
    return render_template('home.html')
@app.route('/employees')    
def employees():
    return render_template('employeedata.html',myEmp=getEmployees)
if(__name__=='__main__'):
    app.run(debug=True)