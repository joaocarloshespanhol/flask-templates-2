from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    produtosacima =[
        ['Suco	24.90',
        'Salgado	5.50',
        'Lanche	18.50']
    ]
    produtosabaixo =[
        ['Refrigerante	4.50',
        'Pizza	2.50']
    ]
    return render_template ('index.html')

if __name__ == '__main__':
    app.run()
