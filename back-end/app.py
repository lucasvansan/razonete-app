from accounting_classes import Razonete
from flask import Flask, render_template

app = Flask(__name__) 

@app.route('/')
def printa():
    argumento = 'argumento teste'
    # return 'aaa'
    return render_template('templates/first_template.html', argumento=argumento)
# a = Razonete('Passivo',lanc_credito={'1a':2000})
# a.saldo()