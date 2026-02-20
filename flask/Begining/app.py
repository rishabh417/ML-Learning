from flask import Flask,render_template,request

app = Flask(__name__)  # Create an instance of Flask, which will be your WSGI(Web Server Gateway Interface) or act as WSGI
                        # inside Flask we give entry point of this application

@app.route("/")
def welcome():
    return "Welcom to Basic Flask app skeleton modified again"

@app.route("/index")
def indexPage():
    return render_template("index.html")

@app.route("/about")
def justPage():
    return render_template('about.html')

@app.route("/just_not_present")
def justPage2():
    return render_template('just_not_present.html') 
    '''
    render_template is going to check for templates folder for just_not_present.html or any file you wrote inside it.
    '''

@app.route('/form',methods=['GET','POST'])
def form():
    if request.method == 'POST':
        name = request.form.get('name')
        return f'Hello {name} !'
    return render_template('form.html')

@app.route('/submit',methods=['GET','POST'])
def submit():
    if request.method == 'POST':
        name = request.form.get('name')
        return f"Hello {name} !"
    return render_template('form.html')

@app.route('/success/<int:score>')
def success(score):
    res=""
    if score >= 50:
        res = "PASSED"
    else:
        res = "FAILED"
    return render_template('result.html',results=res)



if __name__ == '__main__':
    app.run(debug=True)   # debug = True helps to automatically restart the server when changes are saved.   

