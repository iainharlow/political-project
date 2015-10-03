from flask import Flask,render_template
app_polinet = Flask(__name__)

@app_polinet.route('/index')
def index_polinet():
    return render_template('poliselect.html')

if __name__ == "__main__":
    app_polinet.run(debug=True)
