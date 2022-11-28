from src.fone import Fone


class Contato:

    def __init__(self, nome):
        pass
    def getName(self) -> str:
        return ""

    def getQuantidadeFones(self) -> int:
        return 0

    def getFones(self) -> list:
        return None

    def adicionarFone(self, fone: Fone) -> bool:
        return False

    def removerFone(self, index: int) -> bool:
        return True
