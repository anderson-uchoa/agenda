import unittest

from src.agenda import Agenda
from src.contato import Contato
from src.fone import Fone
from src.identificador import Identificador


class TestAgenda(unittest.TestCase):

    def testInicializacao(self):
        agenda = Agenda()
        self.assertEqual(0, agenda.getQuantidadeDeContatos(),
                         "Ao inicializar uma agenda, não deve haver nenhum contato na lista de contatos.")

    def testAdicionarContatoComSucesso(self):
        agenda = Agenda()
        contato = Contato("Alex")
        self.assertTrue(contato.adicionarFone(Fone(Identificador.TRABALHO, "(59)19536-2054")),
                        "Deve ser possível adicionar um fone a um contato se o número estiver correto.")
        self.assertTrue(contato.adicionarFone(Fone(Identificador.CASA, "(63)54612-5374")),
                        "Deve ser possível adicionar um fone a um contato se o número estiver correto.")
        self.assertEqual(2, contato.getQuantidadeFones(),
                         "Ao adicionar telefones válidos, eles serão salvos na lista de telefones do contato.")
        self.assertTrue(agenda.adicionarContato(contato),
                        "Deve ser possível adcionar um contato na lista de contatos se o nome ainda não existir.")
        self.assertEqual(1, agenda.getQuantidadeDeContatos(),
                         "Ao adicionar um contato válido, ele será salvo na lista de contatos da agenda.")

    def testAdicionarContatoSemTelefone(self):
        agenda = Agenda()
        contato = Contato("Alex")
        self.assertFalse(agenda.adicionarContato(contato),
                         "Deve ser possível adcionar um contato na lista de contatos se o nome ainda não existir.")
        self.assertEqual(0, agenda.getQuantidadeDeContatos(),
                         "Ao adicionar um contato válido, ele será salvo na lista de contatos da agenda.")

    def testAdicionarContatoRepetido(self):
        agenda = Agenda()
        contato = Contato("Alex")
        contato1 = Contato("Alex")
        self.assertTrue(contato.adicionarFone(Fone(Identificador.TRABALHO, "(59)19536-2054")),
                        "Deve ser possível adicionar um fone a um conato se o número estiver correto.")
        self.assertTrue(contato1.adicionarFone(Fone(Identificador.CELULAR, "(16)69902-3026")),
                        "Deve ser possível adicionar um fone a um conato se o número estiver correto.")
        self.assertTrue(contato1.adicionarFone(Fone(Identificador.CASA, "(51)31658-4460")),
                        "Deve ser possível adicionar um fone a um conato se o número estiver correto.")
        self.assertTrue(agenda.adicionarContato(contato),
                        "Deve ser possível adcionar um contato na lista de contatos se o nome ainda não existir.")
        self.assertFalse(agenda.adicionarContato(contato1),
                         "Não deve ser possível adicionar um contato na lista de contatos se o nome já existir.")
        self.assertEqual(1, agenda.getQuantidadeDeContatos(),
                         "Ao adicionar um contato válido, ele será salvo na lista de contatos da agenda.")
        self.assertEqual(3, contato.getQuantidadeFones(),
                         "Se o contato já existir deve ser possível apenas adicionar os novos telefones no contato já existente.")

    def testRemoverContatoComSucesso(self):
        agenda = Agenda()
        contato = Contato("Alex")
        self.assertTrue(contato.adicionarFone(Fone(Identificador.TRABALHO, "(59)19536-2054")),
                        "Deve ser possível adicionar um fone a um conato se o número estiver correto.")
        contato.adicionarFone(Fone(Identificador.CASA, "(16)69902-3026"))
        self.assertTrue(agenda.adicionarContato(contato),
                        "Deve ser possível adcionar um contato na lista de contatos se o nome ainda não existir.")
        self.assertTrue(agenda.removerContato("Alex"),
                        "Deve ser possível remover um contato se o nome estiver cadastrado na lista de contatos da agenda.")
        self.assertEqual(0, agenda.getQuantidadeDeContatos(),
                         "Ao remover um contato ele automáticamente irá ser excluído da lista de contatos.")

    def testRemoverFoneDoContatoDaAgenda(self):
        agenda = Agenda()
        contato = Contato("Alex")
        fone = Fone(Identificador.TRABALHO, "(59)19536-2054")
        self.assertTrue(contato.adicionarFone(fone),
                        "Deve ser possível adicionar um fone a um conato se o número estiver correto.")
        contato.adicionarFone(Fone(Identificador.CELULAR, "(16)69902-3026"))
        self.assertTrue(agenda.adicionarContato(contato),
                        "Deve ser possível adcionar um contato na lista de contatos se o nome ainda não existir.")
        self.assertTrue(agenda.removerFone("Alex", 1),
                        "Deve ser possível remover um contato se o nome do contato estiver cadastrado na agenda e se indice do fone corresponder a um fone.")
        self.assertEqual(1, contato.getQuantidadeFones(),
                         "Ao remover um fone pelo indice o fone irá ser excluído permanentemente da lista de fones do contato.")
        fones = [fone]
        restantes = contato.getFones()
        self.assertEqual(fones, restantes,
                         "Ao remover um fone pelo indice o fone que será excluído tem que corresponder exatamente ao indíce que foi informado.")

    def testRemoverFoneDoContatoDaAgendaComNomeNaoCadastrado(self):
        agenda = Agenda()
        contato = Contato("Alex")
        self.assertTrue(contato.adicionarFone(Fone(Identificador.TRABALHO, "(59)19536-2054")),
                        "Deve ser possível adicionar um fone a um conato se o número estiver correto.")
        self.assertTrue(agenda.adicionarContato(contato),
                        "Deve ser possível adcionar um contato na lista de contatos se o nome ainda não existir.")
        self.assertFalse(agenda.removerFone("Alexx", 1),
                         "Não deve ser possível remover um fone de um contato se o nome do contato não estiver cadastrado na lista")

    def testRemoverFoneDoContatoDaAgendaComIndiceIncorreto(self):
        agenda = Agenda()
        contato = Contato("Alex")
        self.assertTrue(contato.adicionarFone(Fone(Identificador.TRABALHO, "(59)19536-2054")),
                        "Deve ser possível adicionar um fone a um conato se o número estiver correto.")
        self.assertTrue(agenda.adicionarContato(contato),
                        "Deve ser possível adcionar um contato na lista de contatos se o nome ainda não existir.")
        self.assertFalse(agenda.removerFone("Alex", 2),
                         "Não deve ser possível remover um fone de um contato se o indice do fone não conrresponder ao indice válido na lista de fones")

    def testRemoverContatoComNomeNaoCadastrado(self):
        agenda = Agenda()
        contato = Contato("Alex")
        self.assertTrue(contato.adicionarFone(Fone(Identificador.TRABALHO, "(59)19536-2054")),
                        "Deve ser possível adicionar um fone a um conato se o número estiver correto.")
        contato.adicionarFone(Fone(Identificador.CELULAR, "(16)69902-3026"))
        self.assertTrue(agenda.adicionarContato(contato),
                        "Deve ser possível adcionar um contato na lista de contatos se o nome ainda não existir.")
        self.assertFalse(agenda.removerContato("Ana"),
                         "Não deve ser possível remover um contato se o nome do contato não estiver cadastrado na lista de contatos da agenda.")

    def testRecuperarContato(self):
        agenda = Agenda()
        contato = Contato("Ana")
        self.assertTrue(contato.adicionarFone(Fone(Identificador.TRABALHO, "(59)19536-2054")),
                        "Deve ser possível adicionar um fone a um conato se o número estiver correto.")
        self.assertTrue(agenda.adicionarContato(contato),
                        "Deve ser possível adcionar um contato na lista de contatos se o nome ainda não existir.")
        recuperado = agenda.getContato("Ana")
        self.assertIsNotNone(recuperado, "Deve ser possivel recuperar um contato ja adicionado")
        self.assertEqual(1, recuperado.getQuantidadeFones(), "O contato recuperado tem 1 telefone")

    def testRecuperarContatoInexistente(self):
        agenda = Agenda()
        recuperado = agenda.getContato("Ana")
        self.assertIsNone(recuperado, "Deve ser possivel recuperar um contato ja adicionado")

    def testPesquisandoContatosPorNomes(self):
        agenda = Agenda()
        contato = Contato("Ana")
        contato1 = Contato("Adriele")
        contato2 = Contato("Ariele")
        self.assertTrue(contato.adicionarFone(Fone(Identificador.TRABALHO, "(59)19536-2054")),
                        "Deve ser possível adicionar um fone a um conato se o número estiver correto.")
        self.assertTrue(contato1.adicionarFone(Fone(Identificador.CELULAR, "(46)40354-9846")),
                        "Deve ser possível adicionar um fone a um conato se o número estiver correto.")
        self.assertTrue(contato2.adicionarFone(Fone(Identificador.TRABALHO, "(37)44338-4811")),
                        "Deve ser possível adicionar um fone a um conato se o número estiver correto.")
        self.assertTrue(agenda.adicionarContato(contato),
                        "Deve ser possível adcionar um contato na lista de contatos se o nome ainda não existir.")
        self.assertTrue(agenda.adicionarContato(contato1),
                        "Deve ser possível adcionar um contato na lista de contatos se o nome ainda não existir.")
        self.assertTrue(agenda.adicionarContato(contato2),
                        "Deve ser possível adcionar um contato na lista de contatos se o nome ainda não existir.")
        resultadoExato = [contato1, contato2]
        resultado = agenda.pesquisar("ri")
        self.assertEquals(resultadoExato, resultado,
                          "Deve ser possível encontrar contatos na lista de contatos se o padrão conrresponder a qualquer nome, identificado ou telefones")

    def testPesquisandoContatosPorNumeros(self):
        agenda = Agenda()
        contato = Contato("Geoana")
        contato1 = Contato("Adriele")
        contato2 = Contato("Ana")
        self.assertTrue(contato.adicionarFone(Fone(Identificador.TRABALHO, "(59)19536-9999")),
                        "Deve ser possível adicionar um fone a um conato se o número estiver correto.")
        self.assertTrue(contato1.adicionarFone(Fone(Identificador.CELULAR, "(46)40354-8453")),
                        "Deve ser possível adicionar um fone a um conato se o número estiver correto.")
        self.assertTrue(contato2.adicionarFone(Fone(Identificador.TRABALHO, "(37)44338-4999")),
                        "Deve ser possível adicionar um fone a um conato se o número estiver correto.")
        self.assertTrue(agenda.adicionarContato(contato),
                        "Deve ser possível adcionar um contato na lista de contatos se o nome ainda não existir.")
        self.assertTrue(agenda.adicionarContato(contato1),
                        "Deve ser possível adcionar um contato na lista de contatos se o nome ainda não existir.")
        self.assertTrue(agenda.adicionarContato(contato2),
                        "Deve ser possível adcionar um contato na lista de contatos se o nome ainda não existir.")
        resultadoExato = [contato2, contato]
        resultado = agenda.pesquisar("999")
        self.assertEqual(resultadoExato, resultado,
                         "Deve ser possível encontrar contatos na lista de contatos se o padrão conresponder a qualquer nome, identificado ou telefones")

    def testPesquisandoContatosSemNenhumResultado(self):
        agenda = Agenda()
        contato = Contato("Ana")
        contato1 = Contato("Adriele")
        contato2 = Contato("Ariele")
        self.assertTrue(contato.adicionarFone(Fone(Identificador.TRABALHO, "(59)19536-9999")),
                        "Deve ser possível adicionar um fone a um conato se o número estiver correto.")
        self.assertTrue(contato1.adicionarFone(Fone(Identificador.CELULAR, "(46)40354-9846")),
                        "Deve ser possível adicionar um fone a um conato se o número estiver correto.")
        self.assertTrue(contato2.adicionarFone(Fone(Identificador.TRABALHO, "(37)44338-4811")),
                        "Deve ser possível adicionar um fone a um conato se o número estiver correto.")
        self.assertTrue(agenda.adicionarContato(contato),
                        "Deve ser possível adcionar um contato na lista de contatos se o nome ainda não existir.")
        self.assertTrue(agenda.adicionarContato(contato1),
                        "Deve ser possível adcionar um contato na lista de contatos se o nome ainda não existir.")
        self.assertTrue(agenda.adicionarContato(contato2),
                        "Deve ser possível adcionar um contato na lista de contatos se o nome ainda não existir.")
        resultadoExato = []
        resultado = agenda.pesquisar("xyz")

        self.assertEqual(resultadoExato, resultado,
                         "Não deve ser possível retornar nenhum resultado de pesquisa se o padrão não conresponder a nenhum nome, identificador ou telefone.")

    def testAgendaEmOrdemAlfabetica(self):
        agenda = Agenda()
        contato = Contato("Carlos")
        contato1 = Contato("Adriele")
        contato2 = Contato("Biatriz")
        self.assertTrue(contato.adicionarFone(Fone(Identificador.TRABALHO, "(59)19536-9999")),
                        "Deve ser possível adicionar um fone a um conato se o número estiver correto.")
        self.assertTrue(contato1.adicionarFone(Fone(Identificador.CELULAR, "(46)40354-9846")),
                        "Deve ser possível adicionar um fone a um conato se o número estiver correto.")
        self.assertTrue(contato2.adicionarFone(Fone(Identificador.TRABALHO, "(37)44338-4811")),
                        "Deve ser possível adicionar um fone a um conato se o número estiver correto.")
        self.assertTrue(agenda.adicionarContato(contato),
                        "Deve ser possível adcionar um contato na lista de contatos se o nome ainda não existir.")
        self.assertTrue(agenda.adicionarContato(contato1),
                        "Deve ser possível adcionar um contato na lista de contatos se o nome ainda não existir.")
        self.assertTrue(agenda.adicionarContato(contato2),
                        "Deve ser possível adcionar um contato na lista de contatos se o nome ainda não existir.")
        listaEsperada = [contato1, contato2, contato]
        lista = agenda.getContatos()

        self.assertEqual(listaEsperada, lista)

    def testQuantidadeDeTelefones(self):
        agenda = Agenda()
        contato = Contato("Carlos")
        contato1 = Contato("Adriele")
        self.assertTrue(contato.adicionarFone(Fone(Identificador.TRABALHO, "(18)12329-5538")),
                        "Deve ser possível adicionar um fone a um conato se o número estiver correto.")
        self.assertTrue(contato.adicionarFone(Fone(Identificador.CELULAR, "(70)33126-6144")),
                        "Deve ser possível adicionar um fone a um conato se o número estiver correto.")
        self.assertTrue(contato1.adicionarFone(Fone(Identificador.TRABALHO, "(84)49197-8547")),
                        "Deve ser possível adicionar um fone a um conato se o número estiver correto.")
        self.assertTrue(agenda.adicionarContato(contato),
                        "Deve ser possível adcionar um contato na lista de contatos se o nome ainda não existir.")
        self.assertTrue(agenda.adicionarContato(contato1),
                        "Deve ser possível adcionar um contato na lista de contatos se o nome ainda não existir.")
        self.assertEqual(2, agenda.getQuantidadeDeFones(Identificador.TRABALHO),
                         "Deve ser possível pesquisar pela quantidade de fones com base nos identificador pesquisado.")

    def testQuantidadeTotalDeTelefones(self):
        agenda = Agenda()
        contato = Contato("Alex")
        contato1 = Contato("Adriele")
        self.assertTrue(contato.adicionarFone(Fone(Identificador.TRABALHO, "(18)12329-5538")),
                        "Deve ser possível adicionar um fone a um conato se o número estiver correto.")
        self.assertTrue(contato.adicionarFone(Fone(Identificador.CELULAR, "(70)33126-6144")),
                        "Deve ser possível adicionar um fone a um conato se o número estiver correto.")
        self.assertTrue(contato1.adicionarFone(Fone(Identificador.TRABALHO, "(84)49197-8547")),
                        "Deve ser possível adicionar um fone a um conato se o número estiver correto.")
        self.assertTrue(contato1.adicionarFone(Fone(Identificador.CASA, "(33)14397-2247")),
                        "Deve ser possível adicionar um fone a um conato se o número estiver correto.")
        self.assertFalse(contato.adicionarFone(Fone(Identificador.CASA, "(aa)1564-75863")),
                         "Não deve ser possível um numero de telefone que não contenha apenas os caracteres de - , () , . e digitos de 0-9.")
        self.assertTrue(agenda.adicionarContato(contato),
                        "Deve ser possível adcionar um contato na lista de contatos se o nome ainda não existir.")
        self.assertTrue(agenda.adicionarContato(contato1),
                        "Deve ser possível adcionar um contato na lista de contatos se o nome ainda não existir.")
        self.assertEqual(4, agenda.getQuantidadeDeFones(),
                         "Deve ser possível pesquisar pela quantidade total de fones cadastrados na agenda.")


if __name__ == '__main__':
    unittest.main()
