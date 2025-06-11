armazenar = {}      

def cadastrar_aluno():
    nome = input('Nome do aluno: ').strip().title()
    if not nome.replace(' ', '').isalpha():
        print("Nome inválido. Use apenas letras.")
        return

    notas = []
    while len(notas) < 3:
        try:
            nota = float(input(f'Digite a {len(notas)+1}ª nota (0–10): '))
            if 0 <= nota <= 10:
                notas.append(nota)
            else:
                print("A nota deve estar entre 0 e 10.")
        except ValueError:
            print("Entrada inválida. Digite um número.")

    armazenar[nome] = notas      
    print(f'{nome}, suas notas foram salvas com sucesso!')

def calcular_media(notas):
    return sum(notas) / len(notas)

def verificar_situacao(media):
    if media >= 7:  return "Aprovado"
    if media >= 5:  return "Reprovado"
    return 

def exibir_boletim(nome=None):
    if nome:                              
        notas = armazenar.get(nome)
        if notas is None:
            print("Aluno não encontrado.")
            return
        media = calcular_media(notas)
        print(f"\nBoletim de {nome}\nNotas: {notas}\nMédia: {media:.2f}\nSituação: {verificar_situacao(media)}")
    else:
        if not armazenar:
            print("Nenhum aluno cadastrado.")
            return
        for n in armazenar:
            exibir_boletim(n)

while True:
    print("\nBem-vindo a Secretaria Virtual")
    print("1 - Cadastrar aluno\n2 - Calcular média\n3 - Verificar situação\n"
          "4 - Exibir boletim de um aluno\n5 - Exibir todos os boletins\n0 - Sair")
    opcao = input("Escolha uma opção: ").strip()

    if opcao == "1":
        cadastrar_aluno()
    elif opcao == "2":
        nome = input("Nome do aluno: ").strip().title()
        if nome in armazenar:
            media = calcular_media(armazenar[nome])
            print(f"Média de {nome}: {media:.2f}")
        else:
            print("Aluno não encontrado.")
    elif opcao == "3":
        nome = input("Nome do aluno: ").strip().title()
        if nome in armazenar:
            media = calcular_media(armazenar[nome])
            print(f"Situação de {nome}: {verificar_situacao(media)}")
        else:
            print("Aluno não encontrado.")
    elif opcao == "4":
        nome = input("Nome do aluno: ").strip().title()
        exibir_boletim(nome)
    elif opcao == "5":
        exibir_boletim()
    elif opcao == "0":
        print("Programa encerrado. Até logo!")
        break
    else:
        print("Opção inválida.")
