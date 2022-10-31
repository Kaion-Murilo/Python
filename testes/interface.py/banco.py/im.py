import mysql.connector #precisa fazer a instalacao para  funcionar presente slides de glauber.
conexao=mysql.connector.connect(
    host='localhost',
    user='root',
    password='1234',
    database='varejo',
)
cursor=conexao.cursor()
print("conexao estabelecida")
print('foi executado')
#create=inserir cousas na tabelas ja existentes
def inserir_no_banco(vquery):
    nome="max"
    Data="2011-02-02"#data=ano/dias/mes
    quant=900
    valor=1220
    totap=2
    matricula=654321
    idade=29
    sexo="masculino"
    mensalidade=9
        #trasfirie esta linha pra uma funcao na tela
    sql=f'INSERT INTO aluno (nome,matricula,sexo,idade,mensalidade) VALUES ("{nome}",{matricula},"{sexo}",{idade},{mensalidade})'
    cursor.execute(vquery)
    conexao.commit()

    cursor.close()
    conexao.close()

# #read:ler coisas do banco
def lerdados_banco(vquery):
        #trasfirie esta linha pra uma funcao na tela
    sql1="SELECT * FROM aluno"
    cursor.execute(sql1)
    resultado=cursor.fetchall()
    cursor.close()
    conexao.close()
    for result in resultado:
        print(result)

#UPDATE:atualizaar ou trocar informacoes
def update_banco(vquery):
    nome="cola "
    Data="2012-04-03"
    quant=1220
    matricula=654321
    idade=29
    sexo="masculino"
    mensalidade=9
    p=2
        #trasfirie esta linhas pra uma funcao na tela
    sql2=f"UPDATE aluno SET nome ='{nome}',matricula={matricula},sexo='{sexo}',idade={idade},mensalidade={mensalidade} where id_aluno = {p}"
    cursor.execute(vquery)
    conexao.commit()
   
    cursor.close()
    conexao.close()
#delete=excluir
def delete_banco(vquery):
    #trasfirie estas 2 linhas pra uma funcao na tela
    produto=2
    sql3=f"DELETE FROM aluno WHERE  id_aluno={produto}"
    
    cursor.execute(sql3)
    conexao.commit()

    cursor.close()
    conexao.close()
    
delete_banco()