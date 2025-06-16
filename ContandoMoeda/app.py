from flask import Flask, render_template

# Cria a aplicação Flask
app = Flask(__name__)

# Cria a rota que renderiza o arquivo HTML
@app.route('/')
def home():
    return render_template('index.html')

# Permite rodar o app diretamente com "python app.py"
if __name__ == '__main__':
    app.run(debug=True)