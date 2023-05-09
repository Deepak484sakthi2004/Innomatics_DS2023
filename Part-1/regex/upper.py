#IMPORTING THE MODULE/FRAMEWORK FLASK 
from flask import Flask, request, render_template
#CREATING AN OBJECT FOR THE FLASK CLASS
app=Flask(__name__)

#THE ENDPOINT
@app.route('/')
def Homeage():
    return "Welcome the Home Page For Operations"

@app.route('/op')
def op_page():
    return render_template("op.html")

@app.route('/upper')
def upper():
    
    str=request.args.get('str')
    return str.upper()

@app.route('/lower')
def lower():
    str=request.args.get('str')
    return str.lower()

@app.route('/capital')
def capital():
    str=request.args.get('str')
    return str.capitalize()

if __name__=='__main__':
    app.run(debug=True)