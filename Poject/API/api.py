from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/")
def home():
    return 'Olá, esta é a minha API!'


@app.route("/A")
def dados():
    return jsonify({
        "nome": "Maria",
        "idade": 30,
        "cidade": "São Paulo"
    })

if __name__ == '__main__':
    app.run(debug=True)


