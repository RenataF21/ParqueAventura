from app import Flask
from app.controllers import usuarios, visitas  # Importar el controlador

# Crear una instancia de la aplicación Flask
app = Flask(__name__)

# Registrar el controlador
app.register_blueprint(usuarios, visitas)

# Ejecutar la aplicación
if __name__ == '__main__':
    app.run(debug=True) 