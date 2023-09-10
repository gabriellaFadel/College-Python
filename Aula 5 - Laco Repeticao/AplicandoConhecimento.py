qntd_alunos = int(input())
media_turma = 0
soma_nota_turma = 0
aluno = 1
while aluno <= qntd_alunos and qntd_alunos !=0:
    aluno += 1
    media_aluno = float(input())
    if media_aluno >= 6:
        print("PARABÉNS VOCÊ ESTÁ APROVADO")
    
    soma_nota_turma +=media_aluno
    media_turma = soma_nota_turma/qntd_alunos
      

if qntd_alunos == 0:
    print("NÃO HOUVE PROCESSAMENTO")
else :
    print(media_turma) 