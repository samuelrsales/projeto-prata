from services.filme_service import Filme

def menu():
    while True:
        print("Menu de Filmes")
        print("1. Adicionar Filme")
        print("2. Listar Filmes")
        print("3. Buscar Filme")
        print("4. Atualizar Filme")
        print("5. Excluir Filme")
        print("6. Marcar como Assistido")
        print("7. Avaliar Filme")
        print("8. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            titulo = input("Título: ")
            genero = input("Gênero: ")
            ano = input("Ano: ")
            filme = Filme(id=id,titulo=titulo, genero=genero, ano=ano, avaliacao=None, assistido=False)
            filme.adicionar()
            print(f"Filme {titulo} adicionado!")
        
        elif opcao == "2":
            filmes = Filme().listar_filmes()
            for f in filmes:
                print(f.id, f.titulo, f.ano, f.genero, "Assistido" if f.assistido else "Não assistido")
        
        elif opcao == "3":
            titulo = input("Digite o título do filme: ")
            filmes = Filme().buscar_filme(titulo)
            for f in filmes:
                print(f.id, f.titulo, f.ano, f.genero, "Assistido" if f.assistido else "Não assistido")
        
        elif opcao == "4":
            id_filme = input("ID do filme: ")
            titulo = input("Novo título: ")
            genero = input("Novo gênero: ")
            ano = input("Novo ano: ")
            filme = Filme(id_filme, titulo, genero, ano)
            filme.atualizar()
            print("Filme atualizado!")
        
        elif opcao == "5":
            id_filme = input("ID do filme: ")
            filme = Filme(id=id_filme)
            filme.excluir()
            print("Filme excluído!")
        
        elif opcao == "6":
            id_filme = input("ID do filme: ")
            filme = Filme(id=id_filme)
            filme.marcar_como_assistido()
            print("Filme marcado como assistido!")
        
        elif opcao == "7":
            id_filme = input("ID do filme: ")
            avaliacao = input("Nota (0-10): ")
            filme = Filme(id=id_filme)
            filme.avaliar(avaliacao)
            print("Filme avaliado!")
        
        elif opcao == "8":
            print("Valeu, falou!")
            break
        
        else:
            print("Opção inválida, tente novamente!")

menu()