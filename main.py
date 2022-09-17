from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def homepage_styles():
    return render_template('homepage_withCSS.html')


@app.route('/patient') #/patients has the picture was having trouble implementing a picture in the homepage
def homepage_styles_layout():
    return render_template('homepage_CSS_LO.html')

if __name__ == '__main__': 
    app.run(debug=True, host='0.0.0.0', port=80)
# make sure to run the file thru the commmand 
### python main.py