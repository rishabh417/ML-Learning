from flask import Flask,render_template

app = Flask(__name__)  # Create an instance of Flask, which will be your WSGI(Web Server Gateway Interface) or act as WSGI
                        # inside Flask we give entry point of this application

@app.route("/")
def welcome():
    return "Welcom to Basic Flask app skeleton modified again"

@app.route("/index")
def indexPage():
    return "Welcome to index page"

@app.route("/just")
def justPage():
    return render_template('just.html')

@app.route("/just_not_present")
def justPage2():
    return render_template('just_not_present.html') 
    '''
    render_template is going to check for templates folder for just_not_present.html or any file you wrote inside it.
    '''

if __name__ == '__main__':
    app.run(debug=True)   # debug = True helps to automatically restart the server when changes are saved.   

