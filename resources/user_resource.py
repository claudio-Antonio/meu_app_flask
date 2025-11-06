from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from services.user_service import UserService

user_bp = Blueprint("user_bp", __name__)

@user_bp.route("/")
def hello():
    return jsonify({"message": "Bem-vindo à API Flask!"})

@user_bp.route("/health")
def health():
    return jsonify({"status": "ok", "message": "Serviço está operando"}), 200

@user_bp.route("/usuarios", methods=["GET"])
def get_usuarios():
    usuarios = UserService.listar_usuarios()
    return jsonify(usuarios), 200

@user_bp.route("/usuarios", methods=["POST"])
def create_usuario():
    data = request.get_json()
    if not data or "nome" not in data or "username" not in data:
        return jsonify({"erro": "Dados incompletos"}), 400

    nome = data["nome"]
    username = data["username"]
    senha = data.get("senha", "123")
    return UserService.criar_usuario(nome, username, senha)

@user_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    senha = data.get("senha")
    user = UserService.autenticar_usuario(username, senha)
    if not user:
        return jsonify({"erro": "Usuário ou senha inválidos"}), 401
    token = create_access_token(identity=username)
    return jsonify(access_token=token), 200

@user_bp.route("/protegido", methods=["GET"])
@jwt_required()
def protegido():
    current_user = get_jwt_identity()
    return jsonify({"message": f"Olá, {current_user}!"}), 200
