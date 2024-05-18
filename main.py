from db_manager import conectar, criar_tabela, inserir_dado, atualizar_dado, excluir_dado, consultar_dados

def criar_banco(nome_banco):
    try:
        conn = conectar(nome_banco)
        print(f'Banco de dados {nome_banco} criado com sucesso ou já existe.')
        return conn
    except Exception as e:
        print(f'Erro ao criar o banco de dados: {e}')
        return None

def main():
    nome_banco = input("Digite o nome do banco de dados: ")
    conn = criar_banco(nome_banco)

    if conn:
        while True:
            print("\nEscolha uma ação:")
            print("1. Criar tabela")
            print("2. Inserir dado")
            print("3. Atualizar dado")
            print("4. Excluir dado")
            print("5. Consultar dados")
            print("6. Sair")

            escolha = input("Digite o número da ação: ")

            if escolha == '1':
                nome_tabela = input("Digite o nome da tabela: ")
                colunas = input("Digite as colunas (ex: id INTEGER PRIMARY KEY, nome TEXT, preco REAL): ")
                criar_tabela(conn, nome_tabela, colunas)
                print(f"Tabela {nome_tabela} criada com sucesso.")
            
            elif escolha == '2':
                nome_tabela = input("Digite o nome da tabela: ")
                colunas = input("Digite os nomes das colunas (ex: nome, preco): ")
                valores = input("Digite os valores (ex: 'Produto A', 19.99): ")
                inserir_dado(conn, nome_tabela, colunas, valores)
                print("Dado inserido com sucesso.")
            
            elif escolha == '3':
                nome_tabela = input("Digite o nome da tabela: ")
                set_clause = input("Digite os novos valores (ex: preco = 20.99): ")
                where_clause = input("Digite a condição (ex: nome = 'Produto A'): ")
                atualizar_dado(conn, nome_tabela, set_clause, where_clause)
                print("Dado atualizado com sucesso.")
            
            elif escolha == '4':
                nome_tabela = input("Digite o nome da tabela: ")
                where_clause = input("Digite a condição (ex: nome = 'Produto A'): ")
                excluir_dado(conn, nome_tabela, where_clause)
                print("Dado excluído com sucesso.")
            
            elif escolha == '5':
                nome_tabela = input("Digite o nome da tabela: ")
                dados = consultar_dados(conn, nome_tabela)
                print("Dados da tabela:")
                for dado in dados:
                    print(dado)
            
            elif escolha == '6':
                print("Saindo...")
                break
            
            else:
                print("Escolha inválida. Tente novamente.")

if __name__ == '__main__':
    main()
