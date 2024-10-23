from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
	return "Hello World!"


from flask import request

@app.route('/ricevi_parametri')
def ricevi_parametri():
    param1 = request.args.get('param1')
    param2 = request.args.get('param2')
    return f'Hai inviato i parametri: {param1} e {param2}'

from flask import jsonify
@app.route('/json')
def restituisci_json():
    data = {
        'nome': 'Alice',
        'eta': 30,
        'citta': 'Milano'
    }
    return jsonify(data)

'''
Assicurati di avere una directory chiamata templates nella stessa cartella del 
tuo script Python, e metti il file pagina.html al suo interno. Flask cercherà 
automaticamente i file HTML in quella directory quando usi render_template.

'''
from flask import render_template

@app.route('/page')
def leggi_html():
    return render_template('pagina.html')

#template dinamico
@app.route('/page2')
def pagina_dinamica():
    titolo = 'Benvenuto nella mia pagina dinamica!'
    messaggio = 'Questo è un messaggio dinamico passato dal backend al template.'
    return render_template('page2.html', titolo=titolo, messaggio=messaggio)


if __name__ == '__main__':
    app.run(debug=True)