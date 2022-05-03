import Problog

def help():
    print("=== [ MALATTIE] ===\n"
          "$ lista_malattie -> permette di vedere quali malattie sono nella kb \n"
          "$ sintomi NOME MALATTIA-> permette di vedere per una data malattia i sintomi ad essi associati \n"
          "=== [ COSA TI SENTI] ===\n"
          "$ lista_sintomi LISTA SINTOMI-> In base ai sintomi elencati si cerca di capire con che probabiltà si soffre di una determinata malattia\n"
          "* es. lista_sintomi sintomo1\n"
          "* es. lista_sintomi sintomo1,sintomo2,...,sintomoN\n"
          "N.B. Per elencare più sintomi separli da una virgola senza spazio!!\n"
          "=== [ ESCI ] ===\n"
          "$ exit -> esce dal programma\n")


def keyboard(input):
    try:
        keyboard = input.split(" ")
        if keyboard[0] == 'help':
            help()
        elif keyboard[0] == 'lista_malattie':
            print(Problog.listaMalattie())
        elif keyboard[0] == 'sintomi':
            if(len(keyboard) == 2):
                print(Problog.sintomi(keyboard[1]))
            else:
                print("Inserire il nome della malattia")
        elif keyboard[0] == 'lista_sintomi':
            if(len(keyboard) == 2):
                print(Problog.probMalattia(keyboard[1]))
            else:
                print("Inserire la lista dei sintomi o il sintomo che si sente")
        elif keyboard[0] == 'exit':
            return
        else:
            print("Comando non valido")
    except ValueError as err:
        print("Attenzione!", err)

if __name__ == '__main__':
    input_string = None
    while input_string != 'exit':
        input_string = input("$ ")
        keyboard(input_string)




