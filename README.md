# Nota-Fiscal-Python

# Sistema de Gerenciamento de Notas Fiscais

Este projeto é um **sistema de gerenciamento de notas fiscais**, clientes e produtos, desenvolvido em **Python**. Ele utiliza **PySimpleGUI** para a interface gráfica, **SQLite** para armazenamento de dados e **Prolog** para regras de conhecimento.

## 📌 Funcionalidades
- **Cadastro de Clientes e Produtos**
- **Geração de Notas Fiscais**
- **Armazenamento de Dados no Banco SQLite**
- **Consulta de Clientes e Produtos no Prolog**
- **Interface Gráfica com PySimpleGUI**

## 🛠 Tecnologias Utilizadas
- **Python**
- **PySimpleGUI**
- **SQLite**
- **Prolog (pyswip)**
- **datetime** (para manipulação de datas)

## 📂 Estrutura do Projeto
```
/
├── logica.py  # Código principal do sistema
├── gui.py  # Módulo responsável pela interface gráfica
├── database.py  # Módulo de gerenciamento do banco de dados SQLite
├── base_conhecimento.pl  # Arquivo Prolog com regras e fatos
├── README.md  # Documentação do projeto
```

## 🚀 Como Funciona
### 🔹 1. Cadastro de Clientes e Produtos
- Os clientes e produtos podem ser cadastrados via interface gráfica.
- Os dados são armazenados no **SQLite** e também podem ser consultados no **Prolog**.

### 🔹 2. Geração de Nota Fiscal
- O usuário seleciona um cliente, produto e quantidade.
- O sistema gera um número de nota fiscal e calcula o valor total.
- A nota fiscal é armazenada no banco de dados.

### 🔹 3. Interface Gráfica (PySimpleGUI)
- Exibe opções para cadastrar clientes, cadastrar produtos e gerar notas fiscais.
- Mostra mensagens interativas para facilitar a experiência do usuário.

## ⚙️ Instalação e Execução
### 📥 Pré-requisitos
Certifique-se de ter **Python 3.x** instalado. Além disso, instale as dependências necessárias:
```sh
pip install PySimpleGUI pyswip
```

### ▶ Executando o Projeto
Para iniciar o sistema, basta rodar o script principal:
```sh
python logica.py
```

---

### 📧 Contato
Desenvolvido por **Juan Victor de Moura**. Caso tenha dúvidas ou sugestões, entre em contato:
- **E-mail**: juanvictor.moura21@gmail.com
- **GitHub**: https://github.com/Zxo21

