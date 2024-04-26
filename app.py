from flask import Flask, send_file, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')  

@app.route('/authorise')
def authorisation():
    return render_template('authorisation-page.html')

if __name__ == '__main__':
    app.run(debug=True)