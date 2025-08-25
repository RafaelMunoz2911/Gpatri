import sqlite3

#conectando ao banco de dados ou criando um novo
conn = sqlite3.connect('data.db')

#criando a tabela de usuarios
conn.execute('CREATE TABLE IF NOT EXISTS usuarios(\
                id INTEGER PRIMARY KEY, \
                nome TEXT,\
                setor TEXT,\
                email TEXT)')#por primeiro e ultimo nome para padronizar

#criando tabela computadores
conn.execute('CREATE TABLE IF NOT EXISTS computadores(\
                id INTEGER PRIMARY KEY, \
                ip INTEGER,\
                ip TEXT,\
                patrimonio INTEGER,\
                hostname TEXT,\
                modelo TEXT,\
                processador TEXT,\
                memoria TEXT,\
                armazenamento TEXT,\
                q_monitores INTEGER,\
                observacoes TEXT)')

#criando a tabela atribuições
conn.execute('CREATE TABLE IF NOT EXISTS atribuicoes(\
                id INTEGER PRIMARY KEY,\
                id_usuarios INTEGER,\
                id_computadores INTEGER,\
                data_atribuicao TEXT,\
                data_troca TEXT,\
                FOREIGN KEY(id_usuarios) REFERENCES usuarios(id),\
                FOREIGN KEY(id_computadores) REFERENCES computadores(id))')