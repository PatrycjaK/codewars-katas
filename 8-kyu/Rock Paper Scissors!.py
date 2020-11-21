# Rock Paper Scissors
# Let's play! You have to return which player won! In case of a draw return Draw!.

# Examples:

# rps('scissors','paper') // Player 1 won!
# rps('scissors','rock') // Player 2 won!
# rps('paper','paper') // Draw!


def rps(p1, p2):
    game = {"rock": "scissors",
            "paper": "rock",
            "scissors": "paper"}
    if game[p1] == p2:
        return "Player 1 won!"
    elif game[p2] == p1:
        return "Player 2 won!"
    else:
        return "Draw!"
