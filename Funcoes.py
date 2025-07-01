def lerNome():
    nome = str(input("Insira o nome do aluno: "))
    return nome

def lerMaterias():
    materias = []
    while True:
        materia = input("Digite o nome da matéria (ou 0 para parar): ")
        if materia == "0":
            break
        if materia.strip() == "":
            print("Matéria inválida. Tente novamente.")
        else:
            materias.append(materia)

    if not materias:
        print("\nNenhuma matéria foi inserida. Encerrando o programa.")
        pergunta = int(input("\nQuer começar novamente? \nSe sim, digite 1, se não, digite 0: "))
        if pergunta == 1:
            chamaMetodos()
        else:
            print("Programa encerrado")

    return materias

def lerNota():
    nota = float(input("Insira a nota do(a) aluno(a): "))
    return nota

def calcularMedia(nota1, nota2):
    media = (nota1 + nota2) / 2
    return media

def exibirResultados(nome, materia, nota1, nota2, media):
    print("\nFINAL DE ANO LETIVO")
    print("Nome: ", nome)
    print("Matéria: ", materia)
    print("Nota 1: ", nota1)
    print("Nota 2: ", nota2)
    print("Média: ", media)
    if media >= 6:
        print("Situação: Aprovado!")
    else:
        print("Situação: Reprovado!")

def chamaMetodos():
    nome = lerNome()
    materias = lerMaterias()

    if not materias:
        return

    for materia in materias:
        print(f"\nMatéria: {materia}")
        nota1 = lerNota()
        nota2 = lerNota()
        media = calcularMedia(nota1, nota2)
        exibirResultados(nome, materia, nota1, nota2, media)

chamaMetodos()