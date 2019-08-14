def check_q(u_1, u_2):
    p_1_w = "Player 1 WIN this round"
    p_2_w = "Player 2 WIN this round"

    if (u_1 == "rock" and u_2 == "scissors")or (u_1 == "scissors" and u_2 == "rock"):
        if u_1 == "rock":
            print(p_1_w)
            return True
        else:
            print(p_2_w)
            return False
    elif (u_1 == "scissors" and u_2 == "paper")or (u_1 == "paper" and u_2 == "scissors"):
        if u_1 == "scissors":
            print(p_1_w)
            return True
        else:
            print(p_2_w)
            return False
    elif (u_1 == "paper" and u_2 == "rock")or (u_1 == "rock" and u_2 == "paper"):
        if u_1 == "paper":
            print(p_1_w)
            return True
        else:
            print(p_2_w)
            return False
    else:
        if u_1 == "rock" or "paper" or "scissors" and u_2 == "rock" or "paper" or "scissors":
            print("DRAW")
        else:
            print("Play again , the input Was wrong")


print("Rock Paper Scissors \n")
round_num = 1
to_continue = True
user_1_points = 0
user_2_points = 0

while to_continue:
    # print the round number and upload in 1
    print("Round ", round_num, "\n")
    round_num += 1

    # ask the user for the
    user_1 = str(input("Player 1 , Enter your Q \n"))
    user_2 = str(input("Player 2 , Enter your Q \n"))
    check_points = check_q(user_1, user_2)

    # check who win
    if check_points:
        user_1_points += 1
    else:
        user_2_points += 1

    # print the score
    print("Player 1 points: ", user_1_points)
    print("Player 2 points: ", user_2_points, "\n")

    # ask the user to exit or not and exit or continue for another round
    con = bool(input("for another around enter True else enter False"))

    if con:
        to_continue = True
    else:
        to_continue = False
        print("The game is ended")
