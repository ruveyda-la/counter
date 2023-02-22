from flask import Flask, render_template,session ,redirect,request
# import the class from user.py

app = Flask(__name__)
app.secret_key = "secret app"
@app.route("/")
def index():
    if 'view' in session:
        session['view'] += 1
    else :
        session['view'] = 0
    if 'count' not in session:
        session['count'] = 0
    
    return render_template("index.html")

@app.route("/reset")
def reset():
    session.clear()
    return redirect('/')

@app.route("/click")
def clicking():
    session['count'] += 2
    return redirect('/')
    
@app.route("/increment", methods=['POST'])
def increment():
    session['count'] += int(((request.form['increment'])))
    return redirect('/')

            
if __name__ == "__main__":
    app.run(debug=True)
