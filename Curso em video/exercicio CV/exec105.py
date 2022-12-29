def notas(*n,sit=False):
    """
    --->funcao tem a funcao de analisa=r as notas bdose situacao dos alunos 
    """
    r=dict()
    r['total']=len(n)
    r['maior']=max(n)
    r['menor']=min(n)
    r['media']=sum(n)/len(n)
    if sit:
        if r['media']>=7:
            r['situacao']='Boa'
        elif r['media']>=5:
            r['situacao']='razoavel'
        else:
            r['situacao']='Ruim'
    return r


resp=notas(5.5,2.5,1.5,sit=True)
print(resp)
help(notas)