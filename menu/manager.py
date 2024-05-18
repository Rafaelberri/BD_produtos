from db.operations import criar_tabela, inserir_dado, excluir_dado
from db.consultas import consultar_dados, listar_tabelas

def criar_tabela_menu(conn):
    nome_tabela = input("Digite o nome da tabela: ")
    colunas = input("Digite as colunas (ex: id INTEGER PRIMARY KEY, nome TEXT, preco REAL): ")
    criar_tabela(conn, nome_tabela, colunas)
    print(f"Tabela {nome_tabela} criada com sucesso.")

def inserir_dado_menu(conn):
    nome_tabela = input("Digite o nome da tabela: ")
    colunas = input("Digite os nomes das colunas (ex: nome, preco): ")
    valores = input("Digite os valores (ex: 'Produto A', 19.99): ")
    inserir_dado(conn, nome_tabela, colunas, valores)
    print("Dado inserido com sucesso.")

def consultar_dados_menu(conn):
    tabelas = listar_tabelas(conn)
    if not tabelas:
        print("Não há tabelas no banco de dados.")
        return
    
    print("Tabelas disponíveis:")
    for idx, tabela in enumerate(tabelas, start=1):
        print(f"{idx}. {tabela}")

    escolha = input("Digite o número da tabela que deseja consultar: ")
    try:
        idx_escolhido = int(escolha) - 1
        nome_tabela = tabelas[idx_escolhido]
        dados = consultar_dados(conn, nome_tabela)
        print(f"Dados da tabela {nome_tabela}:")
        for dado in dados:
            print(dado)
    except (ValueError, IndexError):
        print("Escolha inválida. Tente novamente.")

def excluir_dado_menu(conn):
    tabelas = listar_tabelas(conn)
    if not tabelas:
        print("Não há tabelas no banco de dados.")
        return

    print("Tabelas disponíveis:")
    for idx, tabela in enumerate(tabelas, start=1):
        print(f"{idx}. {tabela}")

    escolha = input("Digite o número da tabela que deseja excluir dados: ")
    try:
        idx_escolhido = int(escolha) - 1
        nome_tabela = tabelas[idx_escolhido]
        where_clause = input("Digite a condição (ex: nome = 'Produto A'): ")
        excluir_dado(conn, nome_tabela, where_clause)
        print("Dado excluído com sucesso.")
    except (ValueError, IndexError):
        print("Escolha inválida. Tente novamente.")

def exibir_menu(conn):
    while True:
        print("\nEscolha uma ação:")
        print("1. Criar tabela")
        print("2. Inserir dado")
        print("3. Consultar dados")
        print("4. Excluir dado")
        escolha = input("Digite o número da ação (ou 's' para sair): ")

        if escolha == 's':
            print("Saindo...")
            break

        if escolha == '1':
            criar_tabela_menu(conn)
        elif escolha == '2':
            inserir_dado_menu(conn)
        elif escolha == '3':
            consultar_dados_menu(conn)
        elif escolha == '4':
            excluir_dado_menu(conn)
        else:
            print("Escolha inválida. Tente novamente.")
