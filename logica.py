# arquivo: logica.py
import PySimpleGUI as sg
from gui import criar_janela_principal, criar_janela_cadastrar_cliente, criar_janela_cadastrar_produto, criar_janela_nota_fiscal
from database import criar_tabelas, adicionar_cliente, listar_clientes, adicionar_produto, listar_produtos, salvar_nota_fiscal, obter_ultimo_numero_nota_fiscal, fechar_conexao
from pyswip import Prolog
from datetime import datetime

prolog = Prolog()
prolog.consult("base_conhecimento.pl")  # Arquivo contendo fatos e regras Prolog

def listar_clientes_prolog():
    return [cliente['X'] for cliente in prolog.query("cliente(X)")]

def listar_produtos_prolog():
    return [(produto['X'], float(produto['Y'])) for produto in prolog.query("produto(X, Y)")]

def gerar_nota_fiscal(numero, cliente, produto, quantidade, valor_unitario):
    total = quantidade * valor_unitario
    data_atual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    nota_fiscal = f"Nota Fiscal #{numero}\n"
    nota_fiscal += f"Data: {data_atual}\n"
    nota_fiscal += f"Cliente: {cliente}\n"
    nota_fiscal += "-" * 30 + "\n"
    nota_fiscal += f"{quantidade} x {produto} - R${valor_unitario:.2f} cada: R${total:.2f}\n"
    nota_fiscal += "-" * 30 + "\n"
    nota_fiscal += f"Total: R${total:.2f}\n"
    nota_fiscal += "-" * 30
    return nota_fiscal, total


def gerenciar_nota_fiscal(cliente, produto, quantidade):
    ultimo_numero = obter_ultimo_numero_nota_fiscal()
    if ultimo_numero == 0:
        numero_nota_fiscal = "72336812581"
    else:
        proximo_numero = ultimo_numero + 1
        numero_nota_fiscal = str(72336812580 + proximo_numero)
    valor_unitario = float(produto[1])
    nota_fiscal, total = gerar_nota_fiscal(numero_nota_fiscal, cliente, produto[0], quantidade, valor_unitario)
    salvar_nota_fiscal(numero_nota_fiscal, datetime.now().strftime("%Y-%m-%d %H:%M:%S"), cliente, produto[0],
                       quantidade, valor_unitario, total)
    return nota_fiscal


def main():
    criar_tabelas()

    window_principal = None
    window_cadastrar_cliente = None
    window_cadastrar_produto = None
    window_nota_fiscal = None

    while True:
        if window_principal is None:
            window_principal = criar_janela_principal()

        event, values = window_principal.read()

        if event == sg.WINDOW_CLOSED:
            break

        if event == "Cadastrar Cliente":
            if window_cadastrar_cliente is not None:
                window_cadastrar_cliente.close()
            else:
                window_cadastrar_cliente = criar_janela_cadastrar_cliente()

        elif event == "Cadastrar Produto":

            if window_cadastrar_produto is not None:
                window_cadastrar_produto.close()

            window_cadastrar_produto = criar_janela_cadastrar_produto()

        elif event == "Gerar Nota Fiscal":
            clientes_prolog = listar_clientes_prolog()
            produtos_prolog = listar_produtos_prolog()
            clientes_sqlite = listar_clientes()
            produtos_sqlite = listar_produtos()
            clientes = clientes_prolog + clientes_sqlite
            produtos = produtos_prolog + produtos_sqlite

            if not produtos:
                sg.popup("Não há produtos cadastrados. Por favor, cadastre ao menos um produto.")
                continue

            if clientes and produtos:
                # Fechar a janela anterior de geração de nota fiscal, se estiver aberta
                if window_nota_fiscal is not None:
                    window_nota_fiscal.close()

                window_nota_fiscal = criar_janela_nota_fiscal(clientes, [produto[0] for produto in produtos])

            else:
                sg.popup("Não há clientes cadastrados. Por favor, cadastre ao menos um cliente.")

        if window_cadastrar_cliente is not None:
            event_cliente, values_cliente = window_cadastrar_cliente.read()
            if event_cliente == sg.WINDOW_CLOSED:
                window_cadastrar_cliente.close()
                window_cadastrar_cliente = None
            elif event_cliente == "Salvar":
                nome_cliente = values_cliente["nome_cliente"]
                if nome_cliente:
                    adicionar_cliente(nome_cliente)
                    window_cadastrar_cliente.close()  # Fechar a janela após salvar o cliente
                    window_cadastrar_cliente = None
                else:
                    sg.popup("Por favor, insira um nome válido.", non_blocking=True)
                    window_cadastrar_cliente.close()  # Fechar a janela após exibir o aviso
                    window_cadastrar_cliente = None

        if window_cadastrar_produto is not None:
            event_produto, values_produto = window_cadastrar_produto.read()
            if event_produto == sg.WINDOW_CLOSED:
                window_cadastrar_produto.close()
                window_cadastrar_produto = None
            elif event_produto == "Salvar":
                nome_produto = values_produto["nome_produto"]
                preco_produto = values_produto["preco_produto"]
                if nome_produto and preco_produto:
                    try:
                        preco_produto = float(preco_produto)
                        if preco_produto > 0:
                            adicionar_produto(nome_produto, preco_produto)
                            window_cadastrar_produto.close()
                            window_cadastrar_produto = None
                        else:
                            sg.popup("Por favor, insira um preço válido.", non_blocking=True)
                            window_cadastrar_produto.close()  # Fechar a janela após exibir o aviso
                            window_cadastrar_produto = None
                    except ValueError:
                        sg.popup("Por favor, insira um preço válido.", non_blocking=True)
                        window_cadastrar_produto.close()  # Fechar a janela após exibir o aviso
                        window_cadastrar_produto = None
                else:
                    sg.popup("Por favor, preencha todos os campos.", non_blocking=True)
                    window_cadastrar_produto.close()  # Fechar a janela após exibir o aviso
                    window_cadastrar_produto = None

        if window_nota_fiscal is not None:
            event_nota_fiscal, values_nota_fiscal = window_nota_fiscal.read()
            if event_nota_fiscal == sg.WINDOW_CLOSED:
                window_nota_fiscal.close()
                window_nota_fiscal = None
            elif event_nota_fiscal == "Gerar Nota Fiscal":
                cliente = values_nota_fiscal["cliente_nome"]
                produto_nome = values_nota_fiscal["produto_nome"]
                quantidade = values_nota_fiscal["quantidade"]

                if cliente and produto_nome and quantidade:
                    produto = next((prod for prod in produtos if prod[0] == produto_nome), None)
                    if produto is not None:  # Verificando se o produto foi encontrado
                        try:
                            quantidade = int(quantidade)
                            if quantidade > 0:
                                nota_fiscal = gerenciar_nota_fiscal(cliente, produto, quantidade)
                                window_principal["-OUTPUT-"].update(nota_fiscal)
                                window_nota_fiscal.close()
                            else:
                                sg.popup("A quantidade deve ser um número positivo.", non_blocking=True)
                                window_nota_fiscal.close()
                                window_nota_fiscal = None
                        except ValueError:
                            sg.popup("A quantidade deve ser um número inteiro.", non_blocking=True)
                            window_nota_fiscal.close()
                            window_nota_fiscal = None
                    else:
                        sg.popup("Produto selecionado não encontrado ou não foi selecionado.", non_blocking=True)
                        window_nota_fiscal.close()
                        window_nota_fiscal = None
                else:
                    sg.popup("Por favor, preencha todos os campos corretamente.", non_blocking=True)
                    window_nota_fiscal.close()
                    window_nota_fiscal = None

    fechar_conexao()

if __name__ == "__main__":
    main()
