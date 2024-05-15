def silabas():
    vogais = ["a", "e", "i", "o", "u", "ão" ]
    consoantes = (input("Digite uma consoante: ".upper()))

    try:
        if (not(consoantes - vogais)):

            for vogal in vogais:
                if consoantes.islower():
                    familia = consoantes + vogal 
                    print("{} + {} = {}".format(consoantes, vogal, familia))
                else : 
                    retorno = consoantes.lower()
                    familia = retorno + vogal 
                    print("{} + {} = {}".format(retorno, vogal, familia))

    except Exception as e:
        print("Ocorreu um erro: {}".format(e))

def adição():
    x = float(input("Digite um número: "))
    y = float(input("Digite outro número: "))      
    conta = x + y

    print("{} + {} = {}".format(x, y, conta) )   

def subtração():
    x = float(input("Digite um número: "))
    y = float(input("Digite outro número: "))      
    conta = x - y

    print("{} - {} = {}".format(x, y, conta) )          


def multiplicação():
    x = float(input("Digite um número: "))
    y = float(input("Digite outro número: "))      
    conta = x * y

    print("{} * {} = {}".format(x, y, conta) )  


def divisão():
    x = float(input("Digite um número: "))
    y = float(input("Digite outro número: "))      
    conta = x * y

    print("{} / {} = {}".format(x, y, conta) )  

    
        