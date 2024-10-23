from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello Flask"

from flask import request
@app.route('/localizza')
def rxdati():
    p1 = request.args.get('lat')
    p2 = request.args.get('long')
    return f"coordinate: {p1} / {p2}"

from flask import jsonify
@app.route('/json')
def dati_in_json():
    data = {'nome':'Mario', 'eta':45, 'citta':'Roma'}
    return jsonify(data)

from flask import render_template
@app.route('/page1')
def getPage1():
    return render_template('page1.html')

@app.route('/page2')
def getPage2():
    v1 = "Divina Commedia"
    v2 = "Dante"
    return render_template('page2.html', titolo=v1, autore=v2)

if __name__ == '__main__':
    app.run(debug=True, port=8081)