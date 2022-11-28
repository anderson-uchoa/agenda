import unittest

from src.fone import Fone
from src.identificador import Identificador


class TestFone(unittest.TestCase):

    def testInicializacao(self):
        fone = Fone(Identificador.CASA, "(88)22161-5300")
        fone1 = Fone(Identificador.TRABALHO, "(88)93162-5665")
        fone2 = Fone(Identificador.CELULAR, "(35)90429-3605")
        fone3 = Fone(Identificador.CASA, "(76)95862-9705")
        fone4 = Fone(Identificador.TRABALHO, "(45)94200-0844")
        fone5 = Fone(Identificador.CASA, "(59)94762-3373")
        self.assertEqual(Identificador.CASA, fone.getIdentificador(),
                         "Ao inicializar um fone, o seu identificador deve ser igual ao informado no construtor.")
        self.assertEqual(Identificador.TRABALHO, fone1.getIdentificador(),
                         "Ao inicializar um fone, o seu identificador deve ser igual ao informado no construtor.")
        self.assertEqual(Identificador.CELULAR, fone2.getIdentificador(),
                         "Ao inicializar um fone, o seu identificador deve ser igual ao informado no construtor.")
        self.assertEqual(Identificador.CASA, fone3.getIdentificador(),
                         "Ao inicializar um fone, o seu identificador deve ser igual ao informado no construtor.")
        self.assertEqual(Identificador.TRABALHO, fone4.getIdentificador(),
                         "Ao inicializar um fone, o seu identificador deve ser igual ao informado no construtor.")
        self.assertEqual(Identificador.CASA, fone5.getIdentificador(),
                         "Ao inicializar um fone, o seu identificador deve ser igual ao informado no construtor.")
        self.assertEqual("(88)22161-5300", fone.getNumero(),
                         "Ao inicializar um fone, o seu numero deve ser igual ao informado no construtor.")

    def testValidarFoneCorretamente1(self):
        fone = Fone(Identificador.CASA, "(88)22161-5300")
        self.assertTrue(Fone.validarNumero(fone.getNumero()),
                        "Deve ser possível um numero de telefone que contenha apenas os caracteres - , () , . e digitos de 0-9.")

    def testValidarFoneCorretamente2(self):
        fone = Fone(Identificador.CASA, "88221615300")
        self.assertTrue(Fone.validarNumero(fone.getNumero()),
                        "Deve ser possível um numero de telefone que contenha apenas os caracteres - , () , . e digitos de 0-9.")

    def testValidarFoneCorretamente3(self):
        fone = Fone(Identificador.CASA, "15642-15(77)")
        self.assertTrue(Fone.validarNumero(fone.getNumero()),
                        "Deve ser possível um numero de telefone que contenha apenas os caracteres - , () , . e digitos de 0-9.")

    def testInvalidarFoneIncorreto1(self):
        fone = Fone(Identificador.CASA, "(99)1564-124a")
        self.assertFalse(fone.validarNumero(fone.getNumero()),
                         "Não deve ser possível um numero de telefone que não contenha apenas os caracteres de - , () , . e digitos de 0-9.")

    def testInvalidarFoneIncorreto2(self):
        fone = Fone(Identificador.CASA, "991564.124a[]")
        self.assertFalse(fone.validarNumero(fone.getNumero()),
                         "Não deve ser possível um numero de telefone que não contenha apenas os caracteres de - , () , . e digitos de 0-9.")

    def testInvalidarFoneIncorreto3(self):
        fone = Fone(Identificador.CASA, "numero123")
        self.assertFalse(fone.validarNumero(fone.getNumero()),
                         "Não deve ser possível um numero de telefone que não contenha apenas os caracteres de - , () , . e digitos de 0-9.")


if __name__ == '__main__':
    unittest.main()
