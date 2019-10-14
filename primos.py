import os
from flask import Flask, jsonify, request


app = Flask(__name__)

@app.route('/')
def eh_primo(n):
    if n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        for k in range(3, n//2+1):
            if n % k == 0:
                return False
        return True


def lista_primos():
    lista = []
    for i in range(2, 524):
        if eh_primo(i):
            lista.append(i)
    return lista

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)