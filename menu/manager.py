from db.operations import criar_tabela, inserir_dado

# Funções para manipulação do menu
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

# Outras funções relacionadas ao menu...

def exibir_menu(conn):
    while True:
        print("\nEscolha uma ação:")
        print("1. Criar tabela")
        print("2. Inserir dado")
        # Adicione outras opções de menu conforme necessário
        escolha = input("Digite o número da ação (ou 's' para sair): ")

        if escolha == 's':
            print("Saindo...")
            break

        if escolha == '1':
            criar_tabela_menu(conn)
        elif escolha == '2':
            inserir_dado_menu(conn)
        else:
            print("Escolha inválida. Tente novamente.")
