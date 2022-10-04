import os
from flask import Flask, render_template, json, request, jsonify

app = Flask(__name__)

@app.route('/teste')
def index():
    return render_template('testejson5.html')

@app.route('/api/exemplo', methods=['POST'])
def exemplo():

    json = request.get_json()
    nome = json['nome'].upper()
    time = json['time'].upper()
    posicao = json['posicao'].upper()
    return jsonify(nome=nome,time=time,posicao=posicao)
    
    
if __name__ == "__main__":
 port = int(os.environ.get("PORT", 5000))
 app.run(host='0.0.0.0', port=port)