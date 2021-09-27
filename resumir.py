from flask import Flask, request, render_template
from flask_restful import Resource, Api
from summa.summarizer import summarize
app = Flask(__name__)#creamos un objeto aplicación
api = Api(app)#creamos un objeto api
@app.route('/')#asignamos rutas dentro de la aplicación, en este caso el raíz
def my_form():
    return render_template('summarizer.html')#render_template muestra nuestro formulario web

@app.route('/', methods=['POST'])#asignamos rutas dentro de la aplicación

def my_form_post():#esta función recibe el texto del formulario html y devuelve un resumen
    text = request.form['text']#request.form recupera el texto del formulario, identificado por el atributo name del elemento text area del html
    text = summarize(text, language='spanish', ratio=0.2)
    return (text)
class Return_summary(Resource):#esta clase procesa un texto y devuelve un resumen
    def get(self, content):
        resumen=summarize(content, language='spanish', ratio=0.2)
        return resumen
api.add_resource(Return_summary, '/return_summary/<string:content>')#añadimos la clase anterior a la api
if __name__ == "__main__":
    app.run(debug=True)#la api se ejecuta, con debug habilitado para mostrar errores.
