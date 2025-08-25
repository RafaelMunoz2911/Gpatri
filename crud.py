import sqlite3

#conectar ao banco de dados
def connect():
    conn = sqlite3.connect('data.db')
    return conn

#função para inserir um usuário
def insert_user(nome, setor, email):
    conn = connect()
    conn.execute("INSERT INTO usuarios(nome, setor, email)\
                VALUES (?, ?, ?)", (nome, setor, email))
    conn.commit()
    conn.close()

#função para ver usuarios
def get_users():
    conn = connect()
    c=conn.cursor()
    c.execute("SELECT * FROM usuarios")
    users = c.fetchall()
    conn.close()
    return users


#função para inserir um computador
def insert_pc(ip, patrimonio, hostname, modelo, processador, memoria, armazenamento, q_monitor, observacoes):
    conn = connect()
    conn.execute("INSERT INTO computadores(ip, patrimonio, hostname, modelo, processador, memoria, armazenamento, q_monitor, observacoes)\
                 VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (ip, patrimonio, hostname, modelo, processador, memoria, armazenamento, q_monitor,    observacoes))
    conn.commit()
    conn.close()

#função para ver pcs
def get_pcs():
    conn = connect()
    c=conn.cursor()
    c.execute("SELECT * FROM computadores")
    users = c.fetchall()
    conn.close()
    return users

def insert_assignment(id_usuarios, id_computadores, id_monitores, data_atribuicao, data_troca):
    conn = connect()
    conn.execute("INSERT INTO atribuicoes(id_usuarios, id_computadores, id_monitores, data_atribuicao, data_troca)\
                VALUES (?, ?, ?, ?, ?)", (id_usuarios, id_computadores, id_monitores, data_atribuicao, data_troca))
    conn.commit()
    conn.close()

#funcao para exibir todos os pcs emprestados no momento
def get_pcs_on_assignment():
    conn = connect()
    result = conn.execute("SELECT atribuicoes.id, usuarios.nome, computadores.modelo, computadores.patrimonio, monitores.modelo, monitores.patrimonio, atribuicoes.data_atribuicao, atribuicoes.data_troca\
                         FROM computadores\
                         INNER JOIN atribuicoes ON computadores.id = atribuicoes.id_computadores\
                         INNER JOIN usuarios ON usuarios.id = atribuicoes.id_usuarios\
                         WHERE atribuicoes.data_troca IS NULL").fetchall()
    conn.close()
    return result

#exemplo de funções:
#insert_user("Rafael Ortiz", "Informatica", "informatica@ourominas.com.br")
#insert_pc("172.18.1.78", "18564", "OM-TI03", "Vostro", "Intel I5", "32gb", "ssd 240gb", "novo e em bom uso")
#insert_monitor("23474", "Samsung 23C550", "novo, entradas hdmi e vga")
insert_assignment("1", "1", "1","25/08/2025", "none")

pc = get_pcs_on_assignment()
print(pc)
