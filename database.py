# arquivo: database.py
import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

def criar_tabelas():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS produtos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        preco REAL NOT NULL
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS notas_fiscais (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        numero INTEGER NOT NULL,
        data TEXT NOT NULL,
        cliente TEXT NOT NULL,
        produto TEXT NOT NULL,
        quantidade INTEGER NOT NULL,
        valor_unitario REAL NOT NULL,
        total REAL NOT NULL
    )
    ''')

    conn.commit()

def adicionar_cliente(nome):
    cursor.execute("INSERT INTO clientes (nome) VALUES (?)", (nome,))
    conn.commit()

def listar_clientes():
    cursor.execute("SELECT nome FROM clientes")
    return [cliente[0] for cliente in cursor.fetchall()]

def adicionar_produto(nome, preco):
    cursor.execute("INSERT INTO produtos (nome, preco) VALUES (?, ?)", (nome, preco))
    conn.commit()

def listar_produtos():
    cursor.execute("SELECT nome, preco FROM produtos")
    return cursor.fetchall()

def salvar_nota_fiscal(numero, data, cliente, produto, quantidade, valor_unitario, total):
    cursor.execute("INSERT INTO notas_fiscais (numero, data, cliente, produto, quantidade, valor_unitario, total) VALUES (?, ?, ?, ?, ?, ?, ?)", (numero, data, cliente, produto, quantidade, valor_unitario, total))
    conn.commit()

def obter_ultimo_numero_nota_fiscal():
    cursor.execute("SELECT MAX(numero) FROM notas_fiscais")
    ultimo_numero = cursor.fetchone()[0]
    return ultimo_numero if ultimo_numero is not None else 0

def fechar_conexao():
    conn.close()
