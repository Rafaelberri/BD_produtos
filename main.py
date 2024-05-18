from db.manager import criar_banco
from menu.manager import exibir_menu

def main():
    nome_banco = input("Digite o nome do banco de dados: ")
    conn = criar_banco(nome_banco)

    if conn:
        exibir_menu(conn)
    else:
        print("Erro ao criar o banco de dados.")

if __name__ == '__main__':
    main()
