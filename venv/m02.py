def get_professores(cursor):
    cursor.execute(f'select Nome from faculdade.professor')
    nomes=cursor.fetchall()
    cursor.close()

    return nomes

def get_detalhesM(cursor):
    idprofessor = 1
    cursor.execute(f'select Nome, Curso, CargaHoraria from faculdade.disciplina where idprofessor = {idprofessor}')
    detalhes = cursor.fetchall()
    cursor.close()

    return detalhes

def get_detalhesS(cursor):
    idprofessor = 2
    cursor.execute(f'select Nome, Curso, CargaHoraria from faculdade.disciplina where idprofessor = {idprofessor}')
    detalhes = cursor.fetchall()
    cursor.close()

    return detalhes

def get_detalhesV(cursor):
    idprofessor = 3
    cursor.execute(f'select Nome, Curso, CargaHoraria from faculdade.disciplina where idprofessor = {idprofessor}')
    detalhes = cursor.fetchall()
    cursor.close()

    return detalhes

def get_detalhesF(cursor):
    idprofessor = 4
    cursor.execute(f'select Nome, Curso, CargaHoraria from faculdade.disciplina where idprofessor = {idprofessor}')
    detalhes = cursor.fetchall()
    cursor.close()

    return detalhes