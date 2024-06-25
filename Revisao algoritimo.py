acervo = [
    {"titulo": "A Menina que Roubava Livros", "autor": "Markus Zusak", "periodo": "Século XX", "resumo": "Resumo do livro A Menina que Roubava Livros", "conteudo": "Conteúdo do livro A Menina que Roubava Livros"},
    {"titulo": "Dom Casmurro", "autor": "Machado de Assis", "periodo": "Século XIX", "resumo": "Resumo do livro Dom Casmurro", "conteudo": "Conteúdo do livro Dom Casmurro"},
    {"titulo": "Harry Potter e a Pedra Filosofal", "autor": "J.K. Rowling", "periodo": "Século XX", "resumo": "Resumo do livro Harry Potter e a Pedra Filosofal", "conteudo": "Conteúdo do livro Harry Potter e a Pedra Filosofal"},
    {"titulo": "O Hobbit", "autor": "J.R.R. Tolkien", "periodo": "Século XX", "resumo": "Resumo do livro O Hobbit", "conteudo": "Conteúdo do livro O Hobbit"},
    {"titulo": "O Senhor dos Anéis", "autor": "J.R.R. Tolkien", "periodo": "Século XX", "resumo": "Resumo do livro O Senhor dos Anéis", "conteudo": "Conteúdo do livro O Senhor dos Anéis"},
    {"titulo": "O Pequeno Príncipe", "autor": "Antoine de Saint-Exupéry", "periodo": "Século XX", "resumo": "Resumo do livro O Pequeno Príncipe", "conteudo": "Conteúdo do livro O Pequeno Príncipe"},
    {"titulo": "Orgulho e Preconceito", "autor": "Jane Austen", "periodo": "Século XIX", "resumo": "Resumo do livro Orgulho e Preconceito", "conteudo": "Conteúdo do livro Orgulho e Preconceito"},
    {"titulo": "Percy Jackson e o Ladrão de Raios", "autor": "Rick Riordan", "periodo": "Século XXI", "resumo": "Resumo do livro Percy Jackson e o Ladrão de Raios", "conteudo": "Conteúdo do livro Percy Jackson e o Ladrão de Raios"},
    {"titulo": "As Crônicas de Nárnia", "autor": "C.S. Lewis", "periodo": "Século XX", "resumo": "Resumo do livro As Crônicas de Nárnia", "conteudo": "Conteúdo do livro As Crônicas de Nárnia"},
    {"titulo": "As Aventuras de Sherlock Holmes", "autor": "Arthur Conan Doyle", "periodo": "Século XIX", "resumo": "Resumo do livro As Aventuras de Sherlock Holmes", "conteudo": "Conteúdo do livro As Aventuras de Sherlock Holmes"}
]

def adicionar_documento(titulo, autor, periodo, resumo, conteudo):
    documento = {
        "titulo": titulo,
        "autor": autor,
        "periodo": periodo,
        "resumo": resumo,
        "conteudo": conteudo
    }
    acervo.append(documento)
    print(f"\nDocumento '{titulo}' adicionado ao acervo.")

def buscar_por_titulo(titulo):
    resultados = [doc for doc in acervo if doc['titulo'].lower() == titulo.lower()]
    if resultados:
        print("\nDocumentos encontrados:")
        for doc in resultados:
            print(f"{doc['titulo']} - {doc['autor']} ({doc['periodo']})")
    else:
        print(f"\nNenhum documento encontrado com título '{titulo}'.")

def listar_documentos():
    if not acervo:
        print("\nA biblioteca não possui documentos no acervo.")
    else:
        print("\nListando todos os documentos:")
        for index, documento in enumerate(acervo):
            print(f"{index+1}. {documento['titulo']} - {documento['autor']} ({documento['periodo']})")


for i in range(1, len(acervo)):
    chave = acervo[i]
    j = i - 1
    while j >= 0 and acervo[j]['titulo'] > chave['titulo']:
        acervo[j + 1] = acervo[j]
        j -= 1
    acervo[j + 1] = chave


while True:
    print("\n### Bem-vindo à Biblioteca Histórica ###")
    print("Escolha uma opção:")
    print("1. Adicionar documento")
    print("2. Buscar documento por título")
    print("3. Listar todos os documentos")
    print("4. Sair")

    opcao = input("\nDigite o número da opção desejada: ")

    if opcao == '1':
        titulo = input("Digite o título do documento: ")
        autor = input("Digite o autor do documento: ")
        periodo = input("Digite o período histórico do documento: ")
        resumo = input("Digite o resumo do documento: ")
        conteudo = input("Digite o conteúdo do documento: ")
        adicionar_documento(titulo, autor, periodo, resumo, conteudo)

    elif opcao == '2':
        titulo = input("\nDigite o título do documento que deseja buscar: ")
        buscar_por_titulo(titulo)

    elif opcao == '3':
        listar_documentos()

    elif opcao == '4':
        print("\nEncerrando o programa...")
        break

    else:
        print("\nOpção inválida. Por favor, digite um número de 1 a 4.")
