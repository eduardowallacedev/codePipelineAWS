from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "<h1>Hola FIAP!</h1>\nMBA! o/ Versão 2 com deploy pela AWS, usando codepipeline e beanstalk"

if __name__ == '__main__':
    application.run()
