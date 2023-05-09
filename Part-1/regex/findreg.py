import regex as re
from flask import Flask, request, render_template

#obj  creation
app=Flask(__name__)

#routes
@app.route("/")
def fuc():
        return render_template("home.html")


@app.route("/",methods=["POST","GET"])
def redir_count():
   regex=request.form['regex']
   str=request.form['pattern']

   count=re.findall(regex,str)

   if request.method=="GET":
        return render_template("home.html")

   else:
        return render_template("final.html",match=count)
#main 
if __name__=='__main__':
    app.run(debug=True)



