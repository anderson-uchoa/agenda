import unittest

from src.contato import Contato
from src.fone import Fone
from src.identificador import Identificador


class TestContato(unittest.TestCase):

    def testInicializacao(self):
        contato = Contato("Alex")
        self.assertEqual("Alex", contato.getName(),
                         "Ao inicializar um contato, o seu nome deve ser igual ao informado no construtor.")
        self.assertEqual(0, contato.getQuantidadeFones(),
                         "Ao inicializar um contato, não deve haver fones na lista de fones.")

    def testAdicinarFoneComNumeroCorreto(self):
        contato = Contato("Alex")
        self.assertTrue(contato.adicionarFone(Fone(Identificador.CASA, "(59)19536-2054")),
                        "Deve ser possível adicionar um fone a um conato se o número estiver correto.")
        self.assertTrue(contato.adicionarFone(Fone(Identificador.TRABALHO, "(16)69902-3026")),
                        "Deve ser possível adicionar um fone a um conato se o número estiver correto.")

    def testAdicionarFoneComNumeroIncorreto(self):
        contato = Contato("Alex")
        self.assertFalse(contato.adicionarFone(Fone(Identificador.CASA, "(59)195.36-20[5]4")),
                         "Não deve ser possível adicionar um fone a um contato se o número estiver incorreto.")
        self.assertFalse(contato.adicionarFone(Fone(Identificador.TRABALHO, "(59)num1597-753")),
                         "Não deve ser possível adicionar um fone a um contato se o número estiver incorreto.")

    def testRemoverFoneComIndexCorreto(self):
        contato = Contato("Alex")
        self.assertTrue(contato.adicionarFone(Fone(Identificador.CASA, "(59)19536-2054")),
                        "Deve ser possível adicionar um fone a um conato se o número estiver correto.")
        self.assertTrue(contato.adicionarFone(Fone(Identificador.TRABALHO, "(14)49574-2545")),
                        "Deve ser possível adicionar um fone a um conato se o número estiver correto.")
        self.assertTrue(contato.removerFone(0),
                        "Deve ser possível remover um contato se o index informado estiver presente na lista de fones.")
        self.assertTrue(contato.adicionarFone(Fone(Identificador.CELULAR, "(71)22666-0341")),
                        "Deve ser possível adicionar um fone a um conato se o número estiver correto.")
        self.assertTrue(contato.removerFone(1),
                        "Deve ser possível remover um contato se o index informado estiver presente na lista de fones.")

    def testRemoverFoneComIndexIncorreto(self):
        contato = Contato("Alex")
        self.assertTrue(contato.adicionarFone(Fone(Identificador.CASA, "(59)19536-2054")),
                        "Deve ser possível adicionar um fone a um conato se o número estiver correto.")
        self.assertFalse(contato.removerFone(2),
                         "Não deve ser possível remover um contato se o index informado não estiver presente na lista de fones.")
        self.assertFalse(contato.removerFone(-1),
                         "Não deve ser possível remover um contato se o index informado não estiver presente na lista de fones.")


if __name__ == '__main__':
    unittest.main()
