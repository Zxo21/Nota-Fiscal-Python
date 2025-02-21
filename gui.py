
import PySimpleGUI as sg

def criar_janela_principal():
    layout_principal = [
        [sg.Button("Cadastrar Cliente", size=(20, 2), button_color=("white", "blue")),
         sg.Button("Cadastrar Produto", size=(20, 2), button_color=("white", "green")),
         sg.Button("Gerar Nota Fiscal", size=(20, 2), button_color=("white", "orange"))],
        [sg.Multiline("", size=(60, 15), key="-OUTPUT-")]  # Usamos Multiline para exibir múltiplas linhas
    ]
    window_principal = sg.Window("Cadastro e Nota Fiscal", layout_principal, background_color="lightgrey")
    return window_principal

def criar_janela_cadastrar_cliente():
    layout_cadastrar_cliente = [
        [sg.Text("Nome do Cliente", size=(15, 1)), sg.InputText(key="nome_cliente")],
        [sg.Button("Salvar", size=(10, 2), button_color=("white", "blue"))]
    ]
    window_cadastrar_cliente = sg.Window("Cadastrar Cliente", layout_cadastrar_cliente, background_color="lightgrey")
    return window_cadastrar_cliente

def criar_janela_cadastrar_produto():
    layout_cadastrar_produto = [
        [sg.Text("Nome do Produto", size=(15, 1)), sg.InputText(key="nome_produto")],
        [sg.Text("Preço do Produto", size=(15, 1)), sg.InputText(key="preco_produto")],
        [sg.Button("Salvar", size=(10, 2), button_color=("white", "green"))]
    ]
    window_cadastrar_produto = sg.Window("Cadastrar Produto", layout_cadastrar_produto, background_color="lightgrey")
    return window_cadastrar_produto

def criar_janela_nota_fiscal(clientes, produtos):
    layout_nota_fiscal = [
        [sg.Text("Selecione o Cliente", size=(15, 1)), sg.InputCombo(clientes, key="cliente_nome")],
        [sg.Text("Selecione o Produto", size=(15, 1)), sg.InputCombo(produtos, key="produto_nome")],
        [sg.Text("Quantidade", size=(15, 1)), sg.InputText("1", key= "quantidade")],
        [sg.Button("Gerar Nota Fiscal", size=(15, 2), button_color=("white", "orange"))]
    ]
    window_nota_fiscal = sg.Window("Gerar Nota Fiscal", layout_nota_fiscal, background_color="lightgrey")
    return window_nota_fiscal