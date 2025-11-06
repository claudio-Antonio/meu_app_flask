from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from config import Config
from models.user import db
from resources.user_resource import user_bp

app = Flask(__name__)
app.config.from_object(Config)

CORS(app)
jwt = JWTManager(app)
db.init_app(app)

# Registrar blueprints (rotas)
app.register_blueprint(user_bp)

# Criar banco de dados automaticamente se não existir
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
