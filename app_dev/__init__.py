from flask import Flask, render_template
import app_dev.modules.epp.importar_detecoes as importar_detecoes

app = Flask(__name__)

@app.route('/')
def index():
    importar_detecoes.detections_import()
    return render_template("inheritance.html")

if __name__ == '__main__':
    app.run(debug=True)