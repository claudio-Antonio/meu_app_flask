from repositories.user_repository import UserRepository
from models.user import User

class UserService:
    @staticmethod
    def listar_usuarios():
        usuarios = UserRepository.find_all()
        return [u.to_dict() for u in usuarios]

    @staticmethod
    def criar_usuario(nome, username, senha="123"):
        if UserRepository.find_by_username(username):
            return {"erro": "Usuário já existe"}, 409
        
        novo_user = User(username=username, nome=nome)
        novo_user.set_password(senha)
        UserRepository.save(novo_user)
        return novo_user.to_dict(), 201

    @staticmethod
    def autenticar_usuario(username, senha):
        usuario = UserRepository.find_by_username(username)
        if usuario and usuario.check_password(senha):
            return usuario
        return None

    @staticmethod
    def deletar_usuario(user_id):
        sucesso = UserRepository.delete_by_id(user_id)
        if sucesso:
            return {"mensagem": "Usuário deletado com sucesso"}, 200
        return {"erro": "Usuário não encontrado"}, 404

