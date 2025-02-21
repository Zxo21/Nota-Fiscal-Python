# Nota-Fiscal-Python

📌 Principais Funcionalidades do Código:
Interface gráfica com PySimpleGUI:

Criar, fechar e gerenciar janelas de cadastro de clientes, produtos e notas fiscais.
Banco de Dados (SQLite e Prolog):

Registra e lista clientes e produtos tanto no SQLite quanto no Prolog.
Armazena notas fiscais geradas.
Gerenciamento de Notas Fiscais:

Recupera o último número de nota fiscal salvo.
Gera um novo número de nota fiscal sequencial.
Calcula o valor total da nota fiscal.
Salva as notas fiscais no banco de dados.
🛠 Explicação dos Componentes:
🔹 Prolog (base_conhecimento.pl)
O código usa Prolog para armazenar informações como clientes e produtos.
Ele consulta os fatos armazenados em base_conhecimento.pl através de listar_clientes_prolog() e listar_produtos_prolog().
🔹 Banco de Dados SQLite
O código usa funções importadas (adicionar_cliente, listar_clientes, salvar_nota_fiscal) para gerenciar registros no banco.
🔹 Funções Principais:
listar_clientes_prolog() e listar_produtos_prolog()
→ Obtêm clientes e produtos armazenados no Prolog.

gerar_nota_fiscal(numero, cliente, produto, quantidade, valor_unitario)
→ Gera o texto da nota fiscal com valores calculados.

gerenciar_nota_fiscal(cliente, produto, quantidade)
→ Obtém o número da nota fiscal, calcula o valor total e salva no banco.

main() (Loop principal)

Controla as janelas da interface gráfica.
Gerencia eventos como cadastro de clientes, produtos e emissão de notas fiscais.
🔥 Fluxo do Programa:
Inicia e cria as tabelas do banco de dados.
Exibe a janela principal com botões para cadastrar clientes, cadastrar produtos e gerar nota fiscal.
Ao clicar em "Cadastrar Cliente" ou "Cadastrar Produto", abre as janelas correspondentes para inserir dados.
Ao clicar em "Gerar Nota Fiscal":
Obtém clientes e produtos do Prolog e SQLite.
Exibe uma janela para escolher cliente, produto e quantidade.
Calcula o total e armazena a nota no banco.
O programa permanece rodando até a janela principal ser fechada.
