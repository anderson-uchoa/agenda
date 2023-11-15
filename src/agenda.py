from src.contato import Contato
from src.identificador import Identificador


class Agenda:

    def __init__(self):
        pass

    def getContatos(self) -> list:
        return None

    def getQuantidadeDeContatos(self) ->  int:
        return 0

    def getContato(self, nome:str) -> Contato:
        return None

    def adicionarContato(self, contato: Contato) -> bool:
        return True

    def removerContato(self, nome: str) -> bool:
        return False

    def removerFone(self, nome:str, index: int) -> bool:
        return False

    def getQuantidadeDeFonesPorIdentificador(self, identificador: Identificador) -> int:
        return 0

    def getQuantidadeTotalDeFones(self) -> int:
        return 0

    def pesquisar(self, expressao:str) -> list:
        return None