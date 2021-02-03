import tkinter as tk

def play():
    x1 = entry1.get()
    x2 = entry2.get()
    x3 = entry3.get()
    if(int(x3)==1):
        square=['o','1', '2', '3', '4', '5', '6', '7', '8', '9']
        i=-1
        player=1
        score1=0
        score2=0
        num=1
        count=1
        def checkwin():
            if (square[1] == square[2] and square[2] == square[3]):
                return 1

            elif (square[4] == square[5] and square[5] == square[6]):
                return 1

            elif (square[7] == square[8] and square[8] == square[9]):
                return 1

            elif (square[1] == square[4] and square[4] == square[7]):
                return 1

            elif (square[2] == square[5] and square[5] == square[8]):
                return 1

            elif (square[3] == square[6] and square[6] == square[9]):
                return 1

            elif (square[1] == square[5] and square[5] == square[9]):
                return 1

            elif (square[3] == square[5] and square[5] == square[7]):
                return 1

            elif (square[1] != '1' and square[2] != '2' and square[3] != '3' and
                square[4] != '4' and square[5] != '5' and square[6] != '6' and square[7]
                != '7' and square[8] != '8' and square[9] != '9'):
                return 0
            else:
                return  -1

        def board():
            
            print("Tic Tac Toe")

            print("{} (X)  -  {} (O)".format(x1,x2))


            print("     |     |     ")
            print("  {}  |  {}  |  {} ".format(square[1], square[2], square[3]))

            print("_____|_____|_____")
            print("     |     |     ")

            print("  {}  |  {}  |  {} ".format(square[4], square[5], square[6]))

            print("_____|_____|_____")
            print("     |     |     ")

            print("  {}  |  {}  |  {} ".format(square[7], square[8], square[9]))

            print("     |     |     ")

        while(num!=0):
            while(i == -1):
                board()
                player= 1 if (player%2) else 2
                if (player==1):
                    choice=int(input("{},enter a number ".format(x1)))
                else:
                    choice=int(input("{},enter a number ".format(x2)))
                mark='X' if player==1 else 'O'
                if (choice == 1 and square[1] == '1'):
                    square[1] = mark

                elif (choice == 2 and square[2] == '2'):
                    square[2] = mark

                elif (choice == 3 and square[3] == '3'):
                    square[3] = mark

                elif (choice == 4 and square[4] == '4'):
                    square[4] = mark

                elif (choice == 5 and square[5] == '5'):
                    square[5] = mark

                elif (choice == 6 and square[6] == '6'):
                    square[6] = mark

                elif (choice == 7 and square[7] == '7'):
                    square[7] = mark

                elif (choice == 8 and square[8] == '8'):
                    square[8] = mark

                elif (choice == 9 and square[9] == '9'):
                    square[9] = mark

                else:
                    print("Invalid move ")
                    player-=1   
                        
                i = checkwin()
                player+=1
            board()
            if (i == 1):
                player-=1
                if(player==1):
                    print("{} wins".format(x1))
                    score1=score1+10
                    print("Score of {} is {}".format(x1,score1))
                    print("Score of {} is {}".format(x2,score2))
                elif (player==2):
                    print("==>{} wins".format(x2))
                    score2=score2+10
                    print("Score of {} is {}".format(x1,score1))
                    print("Score of {} is {}".format(x2,score2))
            else:
                print("Game draw")
            num=int(input("Do you want to continue??(1/0)"))
            if(num==1):
                count=count+1
            else:
                print("The no. of times the game is being played is {}".format(count))
                print("Total score of {} is {}".format(x1,score1))
                print("Total score of {} is {}".format(x2,score2))
                if(score1>score2):
                    print("Congratulations {}, you have won the game".format(x1))
                elif(score2>score1):
                    print("Congratulations {}, you have won the game".format(x2))
                else:
                    print("It's a draw")
            
            square[1]='1'
            square[2]='2'
            square[3]='3'
            square[4]='4'
            square[5]='5'
            square[6]='6'
            square[7]='7'
            square[8]='8'
            square[9]='9'
            i=-1

    else:
        square1=['o', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'p', 'q']
        i=-1
        player=1
        score1=0
        score2=0
        num=1
        count=1
        def checkwin1():
            if (square1[1] == square1[2] and square1[2] == square1[3] and square1[3] == square1[4]):
                return 1

            elif (square1[5] == square1[6] and square1[6] == square1[7] and square1[7] == square1[8]):
                return 1

            elif (square1[9] == square1[10] and square1[10] == square1[11] and square1[11] == square1[12]):
                return 1

            elif (square1[13] == square1[14] and square1[14] == square1[15] and square1[15] == square1[16]):
                return 1

            elif (square1[1] == square1[5] and square1[5] == square1[9] and square1[9] == square1[13]):
                return 1

            elif (square1[2] == square1[6] and square1[6] == square1[10] and square1[10] == square1[14]):
                return 1

            elif (square1[3] == square1[7] and square1[7] == square1[11] and square1[11] == square1[15]):
                return 1

            elif (square1[4] == square1[8] and square1[8] == square1[12] and square1[12] == square1[16]):
                return 1

            elif (square1[1] == square1[6] and square1[6] == square1[11] and square1[11] == square1[16]):
                return 1

            elif (square1[4] == square1[7] and square1[7] == square1[10] and square1[10] == square1[13]):
                return 1

            elif (square1[1] != 'a' and square1[2] != 'b' and square1[3] != 'c' and
                square1[4] != 'd' and square1[5] != 'e' and square1[6] != 'f' and square1[7]
                != 'g' and square1[8] != 'h' and square1[9] != 'i' and square1[10] != 'j' and square1[11] != 'k'
                and square1[12] != 'l' and square1[13] != 'm' and square1[14] != 'n' and square1[15] != 'p' and square1[16] != 'q' ):
                return 0
            else:
                return - 1

        def board1():

            print("Tic Tac Toe")

            print("{} (X)  -  {}(O)".format(x1,x2))


            print("     |     |     |     ")
            print("  {}  |  {}  |  {}  |  {} ".format(square1[1], square1[2], square1[3], square1[4]) )

            print("_____|_____|_____|_____")
            print("     |     |     |     ")

            print("  {}  |  {}  |  {}  |  {} ".format(square1[5], square1[6], square1[7], square1[8]))

            print("_____|_____|_____|_____")
            print("     |     |     |     ")

            print("  {}  |  {}  |  {}  |  {} ".format(square1[9], square1[10], square1[11], square1[12]))

            print("_____|_____|_____|_____")
            print("     |     |     |     ")

            print("  {}  |  {}  |  {}  |  {} ".format(square1[13], square1[14], square1[15], square1[16]))

            print("     |     |     |     ")

        while(num!=0):
            while(i == -1):
                board1()
                player= 1 if (player%2) else 2
                if (player==1):
                    choice=input("{},enter an alphabet ".format(x1))
                else:
                    choice=input("{},enter an alphabet ".format(x2))
                mark='X' if player==1 else 'O'
                if (choice == 'a' and square1[1] == 'a'):
                    square1[1] = mark

                elif (choice == 'b' and square1[2] == 'b'):
                    square1[2] = mark

                elif (choice == 'c' and square1[3] == 'c'):
                    square1[3] = mark

                elif (choice == 'd' and square1[4] == 'd'):
                    square1[4] = mark

                elif (choice == 'e' and square1[5] == 'e'):
                    square1[5] = mark

                elif (choice == 'f' and square1[6] == 'f'):
                    square1[6] = mark

                elif (choice == 'g' and square1[7] == 'g'):
                    square1[7] = mark

                elif (choice == 'h' and square1[8] == 'h'):
                    square1[8] = mark

                elif (choice == 'i' and square1[9] == 'i'):
                    square1[9] = mark

                elif (choice == 'j' and square1[10] == 'j'):
                    square1[10] = mark

                elif (choice == 'k' and square1[11] == 'k'):
                    square1[11] = mark

                elif (choice == 'l' and square1[12] == 'l'):
                    square1[12] = mark

                elif (choice == 'm' and square1[13] == 'm'):
                    square1[13] = mark

                elif (choice == 'n' and square1[14] == 'n'):
                    square1[14] = mark

                elif (choice == 'p' and square1[15] == 'p'):
                    square1[15] = mark

                elif (choice == 'q' and square1[16] == 'q'):
                    square1[16] = mark

                else:
                    print("Invalid move ")
                    player-=1   
                            
                i = checkwin1()
                player+=1
            board1()
            if (i == 1):
                player-=1
                if(player==1):
                    print("{} wins".format(x1))
                    score1=score1+10
                    print("Score of {} is {}".format(x1,score1))
                    print("Score of {} is {}".format(x2,score2))
                elif (player==2):
                    print("==>{} wins".format(x2))
                    score2=score2+10
                    print("Score of {} is {}".format(x1,score1))
                    print("Score of {} is {}".format(x2,score2))
            else:
                print("Game draw")
            num=int(input("Do you want to continue??(1/0)"))
            if(num==1):
                count=count+1
            else:
                print("The no. of times the game is being played is {}".format(count))
                print("Total score of {} is {}".format(x1,score1))
                print("Total score of {} is {}".format(x2,score2))
                if(score1>score2):
                    print("Congratulations {}, you have won the game".format(x1))
                elif(score2>score1):
                    print("Congratulations {}, you have won the game".format(x2))
                else:
                    print("It's a draw")

            square1[1]='a'
            square1[2]='b'
            square1[3]='c'
            square1[4]='d'
            square1[5]='e'
            square1[6]='f'
            square1[7]='g'
            square1[8]='h'
            square1[9]='i'
            square1[10]='j'
            square1[11]='k'
            square1[12]='l'
            square1[13]='m'
            square1[14]='n'
            square1[15]='p'
            square1[16]='q'
            i=-1

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 600, height = 500)
canvas1.pack()

label1 = tk.Label(root, text='Tic Tac Toe ')
label1.config(font=('helvetica', 18))
canvas1.create_window(290, 25, window=label1)

label2 = tk.Label(root, text='Player 1 name')
label2.config(font=('helvetica', 12))
canvas1.create_window(180, 120, window=label2)

label3 = tk.Label(root, text='Player 2 name')
label3.config(font=('helvetica', 12))
canvas1.create_window(380, 120, window=label3)

label4 = tk.Label(root, text='Press 1 to play 3 by 3 and 2 to play 4 by 4 grid')
label4.config(font=('helvetica', 12))
canvas1.create_window(265, 200, window=label4)

entry1 = tk.Entry (root) 
canvas1.create_window(175, 140, window=entry1)

entry2 = tk.Entry (root) 
canvas1.create_window(375, 140, window=entry2)

entry3 = tk.Entry (root) 
canvas1.create_window(255, 225, window=entry3)

button1 = tk.Button(text='Play',command=play)
button1.config(font=('helvetica', 12))
canvas1.create_window(265, 300, window=button1)

root.mainloop()
