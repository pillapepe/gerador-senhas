import string, random, sys

def pedirTamanho():
    while True:
        try:
            tamanhoSenha = int(input("Tamanho da senha: "))
            break
        except ValueError as erro:
            print(f"Caractere inválido: {erro}")

    return tamanhoSenha

def pedirTipos():
    opcoes = {
        "letras": string.ascii_letters,
        "números": string.digits,
        "símbolos": string.punctuation
    }

    opcoesAceitas = []
    
    letras = str(input("Incluir letras? (s/n): "))
    if letras == "s":
        opcoesAceitas.append(opcoes["letras"])
    
    numeros = str(input("Incluir números? (s/n): "))
    if numeros == "s":
        opcoesAceitas.append(opcoes["números"])
    
    simbolos = str(input("Incluir símbolos? (s/n): "))
    if simbolos == "s":
        opcoesAceitas.append(opcoes["símbolos"])
    
    if opcoesAceitas == []:
        print("Você não selecionou nenhuma opção, logo sua senha não será gerada.")
        sys.exit()

    return opcoesAceitas

def gerarSenha(tamanho, tipos):
    senhaFinal = ""
    strTipos = "".join(tipos)
    
    for i in range(tamanho):
        senhaFinal += random.choice(strTipos)
    
    return senhaFinal

def main():
    print("O gerador de senhas iniciou...")

    tamanho = pedirTamanho()
    tipos = pedirTipos()
    gerador = gerarSenha(tamanho, tipos)

    print(gerador)

main()