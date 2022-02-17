from unicodedata import name
from pip import main
from waitress import serve
    
from Dairy.wsgi import application
    
if __name__ == '__main__':
    serve(application)