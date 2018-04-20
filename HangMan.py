def hangman(word):
    wrong = 0
    stages = ["",
              "_________   ",
              "|        |  ",
              "|        0  ",
              "|       /|\ ",
              "|        |  ",
              "|       / \ ",
              "|           "
              ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False

    print("Bienvenido al 'El Ahorcado':")

    while wrong < len(stages)-1:
        print("\n"*10)
        msg = "Adivina una letra: "
        char = input(msg)

        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1

        print((" ".join(board)))
        e = wrong + 1
        print("\n".join(stages[0:e]))

        if "_" not in board:
            print("Ganaste!")
            print(" ".join(board))
            win = True
            break

    if not win:
        print("\n".join(stages[0:wrong]))
        print("Perdiste!, la palabra era {}".format(word))






hangman("pele")

