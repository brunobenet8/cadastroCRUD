import sqlite3


def inserir(nome, endereco, obs):
    conn = sqlite3.connect('dbContatos')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO Lista(Nome, Endereco, Obs) values(?,?,?)',
        (nome, endereco, obs))
    conn.commit()
    conn.close()
    return 'Cadastrado com Sucesso!'


def listar(id):
    conn = sqlite3.connect('dbContatos')
    cursor = conn.cursor()
    cursor.execute('select * from Lista where ID = ?', (str(id)))
    for linha in cursor.fetchall():
        return linha
    conn.close()


def deletar(id):
    conn = sqlite3.connect('dbContatos')
    cursor = conn.cursor()
    cursor.execute('DELETE from Lista where ID = ?', (str(id)))
    conn.commit()
    conn.close
    return 'Cadastro deletado com sucesso!'


def alterar(id, nome, endereco, obs):
    conn = sqlite3.connect('dbContatos')
    cursor = conn.cursor()
    cursor.execute("""UPDATE Lista SET Nome = ?,
        Endereco = ?, Obs = ? where ID = ?""", (nome, endereco, obs, id))
    conn.commit()
    conn.close()
    return 'Dados alterados com Sucesso!'


def carregar():
    conn = sqlite3.connect('dbContatos')
    cursor = conn.cursor()
    cursor.execute('select * from Lista')
    return cursor.fetchall()
    conn.close()


def buscar(termo, tipo):
    if(termo == 0):
        sql = "select * from Lista where Id like ?"
    elif(termo == 1):
        sql = "select * from Lista where Nome like ?"
    elif(termo == 2):
        sql = "select * from Lista where Endereco like ?"
    elif(termo == 3):
        sql = "select * from Lista where Obs like ?"
    conn = sqlite3.connect('dbContatos')
    cursor = conn.cursor()
    cursor.execute(sql, ('%'+tipo+'%',))
    return cursor.fetchall()
    conn.close
