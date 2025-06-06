usuarios_filmes = {}

while True:
    print("\nBem‑vindo à sua Letterboxd! O que deseja fazer? \n1. Adicionar filme\n 2. Remover filme\n 3. Ver filmes de um usuário\n 4. Ver todos os usuários \n 0. Sair")

    menu = input("Escolha: ").strip()

    match menu:
        case "1": 
            nome = input("Digite o seu nome: ").strip()
            filme = input("Nome do filme: ").strip()
            if nome in usuarios_filmes:
                usuarios_filmes[nome].append(filme)
            else:
                usuarios_filmes[nome] = [filme]
            print(f"Obrigada, {nome}! Filme '{filme}' adicionado com sucesso!")
            
        case "2":  
            nome = input("Qual o seu nome de usuário: ").strip()
            filme_remover = input("Digite o filme que deseja remover: ").strip()
            if nome in usuarios_filmes and filme_remover in usuarios_filmes[nome]:
                usuarios_filmes[nome].remove(filme_remover)
                print(f"Filme '{filme_remover}' removido com sucesso!")
                if len(usuarios_filmes[nome]) == 0:
                    del usuarios_filmes[nome]
            else:
                print("Usuário ou filme não encontrado.")

        case "3": 
            nome = input("Nome do usuário: ").strip()
            filmes = usuarios_filmes.get(nome)  
            if filmes:
                print(f"Filmes assistidos: {filmes}")
            else:
                print("Usuário não encontrado ou sem filmes cadastrados.")

        case "4": 
            if len(usuarios_filmes) == 0:
                print("Nenhum usuário cadastrado ainda.")
            else:
                for usuario, filmes in usuarios_filmes.items():
                    print(f"{usuario}: {filmes}")

        case "0":
            print("Encerrando...")
            break

        case _:
            print("Opção inválida. Tente novamente.")



