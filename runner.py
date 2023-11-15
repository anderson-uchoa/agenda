from src.agenda import Agenda
from src.contato import Contato
from src.fone import Fone
from src.identificador import Identificador

if __name__ == '__main__':

    agenda = Agenda()

    contato = Contato("Adriele")
    contato.adicionarFone(Fone(Identificador.CASA, "(77)89085-9077"))
    contato.adicionarFone(Fone(Identificador.CELULAR, "(63)61730-9301"))
    print(contato)  # Adriele [0:Case:(77)89085-9077] [1:Celular:(63)61730-9301]

    contato1 = Contato("Biatriz")
    contato1.adicionarFone(Fone(Identificador.TRABALHO, "(80)63810-9092"))
    print(contato1)  # Biatriz [0:Trabalho:(80)63810-9092]

    contato2 = Contato("Ariele")
    contato2.adicionarFone(Fone(Identificador.TRABALHO, "(24)62362-1925"))
    contato2.adicionarFone(Fone(Identificador.CELULAR, "(79)98614-1326"))
    if not contato2.adicionarFone(Fone(Identificador.CASA, "(24)62362-abc")):
        print("fail: numero de telefone invalido")  # //fail: numero de telefone invalido

    print(contato2)  # - Ariele [0:Trabalho:(24)62362-1925] [1:Celular:(79)98614-1326]

    agenda.adicionarContato(contato)
    agenda.adicionarContato(contato1)
    agenda.adicionarContato(contato2)
    print(agenda)
    #    - Adriele [0:Claro:(77)89085-9077] [1:Tim:(63)61730-9301]
    #    - Adriele [0:Casa:(77)89085-9077] [1:Celular:(63)61730-9301]
    #    - Biatriz [0:Trabalho:(80)63810-9092]
    quantidade = agenda.getQuantidadeDeFonesPorIdentificador(Identificador.TRABALHO)
    print("Total de telefones com o identifcador (Trabalho) é igual a " + str(quantidade))
    # Total de telefones com o identifcador (Trabalho) é igual a 2

    contato3 = Contato("Biatriz")
    contato3.adicionarFone(Fone(Identificador.CELULAR, "(59)67638-0967"))
    contato3.adicionarFone(Fone(Identificador.CASA, "(59)67638-0967"))
    agenda.adicionarContato(contato3)
    print(agenda)

    #   - Adriele [0:Casa:(77)89085-9077] [1:Celular:(63)61730-9301]
    #   - Ariele [0:Trabalho:(24)62362-1925] [1:Celular:(79)98614-1326]
    #   - Biatriz [0:Trabalho:(80)63810-9092] [1:Celular:(59)67638-0967] [2:Casa:(59)67638-0967]

    agenda.removerFone("Adriele", 1)
    print(agenda)
    #
    #       - Adriele [0:Casa:(77)89085-9077]
    #       - Ariele [0:Trabalho:(24)62362-1925] [1:Celular:(79)98614-1326]
    #       - Biatriz [0:Trabalho:(80)63810-9092] [1:Celular:(59)67638-0967] [2:Casa:(59)67638-0967]

    quantidadeTotal = agenda.getQuantidadeTotalDeFones()
    print("Total de telefones cadastrados na agenda é igual a " + quantidadeTotal)
    # "Total de telefones cadastrados na agenda é igual a 6

    if not agenda.removerContato("Alex"):
        print("fail: nome do contato não esta cadastrado na agenda")
        # fail: nome do contato não esta cadastrado na agenda

    resultados = agenda.pesquisar("le")
    for resultado in resultados:
        print(resultado.toString())

        #    - Adriele [0:Casa:(77)89085-9077]
        #    - Ariele [0:Trabalho:(24)62362-1925] [1:Celular:(79)98614-1326]
