def repetir(frase, chave): #Looping que cria a frase com chave
    chave_rep = ""
    i = 0
    for letra in frase:
        if letra.isalpha():
            chave_rep += chave[i % len(chave)]
            i += 1 
        else: chave_rep += " "
    return chave_rep
print("Bem Vindo a Cifra de Vigenere!\nUma forma de criptografia bem interessante!!!\n")
antes = input("Quer saber como a cifra de Vigenere Funciona? Digite 'S', caso contrário digite qualquer coisa: ")

if antes == "s" or antes == "S":
    print("\nCerto irei citar um breve resumo!\nA cifra de Vigenere pega uma frase/palavra e para criptografar pede uma chave, essa chave serve para ser repetida pelo tamanho da frase/palavra.\n Exemplo -\nFrase: Batata quente\nChave: fone.\nA nova frase fica: fonefo nefone\n\nApartir disso é analisado em uma tabela de vigenere a 1ª letra da sua frase com a 1ª letra da frase nova, e isso segue pela frase inteira até termos a frase criptografada!\nEspero ter ajudado, agora vamos por em prática?\n")

frase = input("\nDigite a Frase que deseja criptografar: ")
chave = input("Digite sua Chave (palavra que sera repetida): ")

chave_final = repetir(frase, chave)

print("Frase: ", frase)
print("Chave: ", chave_final)
resul = " "

for cripA, cripB in zip(frase,chave_final): #Looping que criptografa as frases

    if cripA.isalpha():
        if cripA.isupper():
            cripA = chr(ord(cripA) + 32)
        
        if cripB.isupper():
            cripB = chr(ord(cripB) + 32)
        #essa parte faz uma letra maiuscula vira minuscula
    else: resul += " "
    x = ord(cripA) - 96
    y = ord(cripB) - 96
    
    result = (x + (y - 1)) % 26 #Essa é a lógica que criptografa as frases
    resultL = chr(result + 96)
    resul += resultL

  
print(f"\nA sua frase Criptograda fica:{resul}")




