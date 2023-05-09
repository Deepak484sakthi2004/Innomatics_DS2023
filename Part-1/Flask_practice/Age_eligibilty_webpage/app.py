from flask import Flask, request, render_template

app=Flask('__name__')

@app.route('/')
def home_fn():
    return render_template('home.html')

@app.route('/end', methods=['POST'])
def home_f():
    user=request.form.get('user')
    age=int(request.form.get('age')) 
   
    return render_template('final.html',user=user,age=age)
    
if __name__=='__main__':
    app.run(debug=True)

