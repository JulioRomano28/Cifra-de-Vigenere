def repetir(frase, chave): #Função Responsavel por repetir a chave pello tamanho da frase
    chave_rep = ""
    i = 0
    for letra in frase:
        if letra.isalpha():
            chave_rep += chave[i % len(chave)]
            i += 1
        else:
            chave_rep += " "
    return chave_rep


def vigenere_criptografar(frase, chave): #Função Responsavel por criptografar
    resul = ""

    for cripA, cripB in zip(frase, chave):
        if cripA.isalpha():
            cripA = cripA.lower()
            cripB = cripB.lower()

            x = ord(cripA) - 97
            y = ord(cripB) - 97

            result = (x + y) % 26
            resul += chr(result + 97)
        else:
            resul += cripA

    return resul


def vigenere_descriptografar(frase, chave): #Função Responsavel por descriptografar
    resul = ""

    for cripA, cripB in zip(frase, chave):
        if cripA.isalpha():
            cripA = cripA.lower()
            cripB = cripB.lower()

            x = ord(cripA) - 97
            y = ord(cripB) - 97

            result = (x - y) % 26
            resul += chr(result + 97)
        else:
            resul += cripA

    return resul

# FIM DAS FUNÇÕES


# PROGRAMA PRINCIPAL


print("Bem Vindo a Cifra de Vigenere!\n")
antes = input("Quer saber como a cifra de Vigenere Funciona? Digite 'S', caso contrário digite qualquer coisa: ")

if antes == "s" or antes == "S":
    print("\nCerto irei citar um breve resumo!\nA cifra de Vigenere pega uma frase/palavra e para criptografar pede uma chave, essa chave serve para ser repetida pelo tamanho da frase/palavra.\n Exemplo -\nFrase: Batata quente\nChave: fone.")
    print("A nova frase fica: fonefo nefone\n\nApartir disso é analisado em uma tabela de vigenere a 1ª letra da sua frase com a 1ª letra da frase nova, e isso segue pela frase inteira até termos a frase criptografada!\nEspero ter ajudado, agora vamos por em prática?\n")



opcao = input("\nDigite 1 para Criptografar ou 2 para Descriptografar: ")

frase = input("\nDigite a frase: ")
chave = input("Digite a chave: ")

chave_final = repetir(frase, chave)

if opcao == "1":
    resultado = vigenere_criptografar(frase, chave_final)
    print("\nTexto Criptografado:", resultado)

elif opcao == "2":
    resultado = vigenere_descriptografar(frase, chave_final)
    print("\nTexto Descriptografado:", resultado)

else:
    print("Opção inválida.")

