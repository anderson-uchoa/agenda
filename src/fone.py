from src.identificador import Identificador


class Fone:

    def __init__(self, identificador: Identificador, numero: str):
        pass

    @staticmethod
    def validarNumero(numero) -> bool:
        return True

    def getIdentificador(self) -> Identificador:
        return Identificador.CASA

    def getNumero(self) -> str:
        return ""
