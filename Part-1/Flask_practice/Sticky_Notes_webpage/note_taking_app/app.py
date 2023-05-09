from flask import Flask, render_template, request

app = Flask(__name__)

notes = []

@app.route('/', methods=["POST","GET"])
def index():
    note = request.form("note")
    if request.method=="post":
        return render_template("home.html", notes=notes)

    else:
        notes.append(note)



if __name__ == '__main__':
    app.run(debug=True)
    