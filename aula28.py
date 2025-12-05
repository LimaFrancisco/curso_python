"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitádos:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Se nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
Se nada for digitado em nome ou idade:
    exiba "Desculpe, você deixou campos vázios"
"""

entrada_nome = input("Insira o seu nome: ")
entrada_idade = input("Insira a sua idade: ")

if entrada_nome != "" and entrada_idade != "":
    print(f"Seu  nome é {entrada_nome}")
    print(f"Sua idade é {entrada_idade}")
    if " " in entrada_nome:
        print("Seu nome contém espaços")
    else:
        print("Seu nome não contém espaços")
    print(f"Seu nome tem {entrada_nome} letras")
    print(f"A primeira letra do seu nome é {entrada_nome[0]}")

else:
    print("Desculpe, você deixou campos vázios")
