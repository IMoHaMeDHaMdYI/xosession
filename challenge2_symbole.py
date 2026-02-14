"""
Challenge 2: Richtige Symbole zeichnen mit if-else
===================================================
PROBLEM: Momentan wird IMMER X gezeichnet, egal wer spielt!

AUFGABE:
Nutze if-else um das RICHTIGE Symbol zu zeichnen:
- Wenn der Spieler dran ist → zeichne X
- Wenn die KI dran ist → zeichne O

TIPP: Suche nach "# TODO" für Stellen, die du ändern musst!
"""

import turtle

# Game state
board = [None] * 9
game_over = False
CELL_SIZE = 100
BOARD_SIZE = CELL_SIZE * 3

# Farben (aus Challenge 1)
x_farbe = "blue"
o_farbe = "red"
board_farbe = "black"
screen_farbe = "white"

# Set up the screen
screen = turtle.Screen()
screen.bgcolor(screen_farbe)

# Create drawing turtle
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.pensize(3)

# Create text turtle for messages
text_pen = turtle.Turtle()
text_pen.hideturtle()
text_pen.penup()


def draw_board():
    """Draw the 3x3 grid."""
    pen.penup()
    pen.color(board_farbe)

    start_x = -BOARD_SIZE // 2
    start_y = BOARD_SIZE // 2

    for i in range(1, 3):
        pen.goto(start_x + i * CELL_SIZE, start_y)
        pen.pendown()
        pen.goto(start_x + i * CELL_SIZE, start_y - BOARD_SIZE)
        pen.penup()

    for i in range(1, 3):
        pen.goto(start_x, start_y - i * CELL_SIZE)
        pen.pendown()
        pen.goto(start_x + BOARD_SIZE, start_y - i * CELL_SIZE)
        pen.penup()


def draw_x(row, col):
    """Draw an X in the specified cell."""
    pen.color(x_farbe)
    pen.pensize(4)

    start_x = -BOARD_SIZE // 2
    start_y = BOARD_SIZE // 2

    cx = start_x + col * CELL_SIZE + CELL_SIZE // 2
    cy = start_y - row * CELL_SIZE - CELL_SIZE // 2

    offset = 30
    pen.penup()
    pen.goto(cx - offset, cy + offset)
    pen.pendown()
    pen.goto(cx + offset, cy - offset)
    pen.penup()
    pen.goto(cx + offset, cy + offset)
    pen.pendown()
    pen.goto(cx - offset, cy - offset)
    pen.penup()

    pen.pensize(3)


def draw_o(row, col):
    """Draw an O in the specified cell."""
    pen.color(o_farbe)
    pen.pensize(4)

    start_x = -BOARD_SIZE // 2
    start_y = BOARD_SIZE // 2

    cx = start_x + col * CELL_SIZE + CELL_SIZE // 2
    cy = start_y - row * CELL_SIZE - CELL_SIZE // 2

    pen.penup()
    pen.goto(cx, cy - 30)
    pen.pendown()
    pen.circle(30)
    pen.penup()

    pen.pensize(3)


def show_message(msg):
    """Display a message below the board."""
    text_pen.clear()
    text_pen.goto(0, -BOARD_SIZE // 2 - 40)
    text_pen.write(msg, align="center", font=("Arial", 16, "bold"))


def check_winner(b):
    """Check if there's a winner. Returns 'X', 'O', or None."""
    lines = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    for line in lines:
        if b[line[0]] and b[line[0]] == b[line[1]] == b[line[2]]:
            return b[line[0]]
    return None


def is_board_full(b):
    """Check if no empty squares remain."""
    return all(cell is not None for cell in b)


def get_available_moves(b):
    """Return list of empty positions."""
    return [i for i, cell in enumerate(b) if cell is None]


def minimax(b, is_maximizing):
    """Minimax algorithm - returns the score of the best outcome."""
    winner = check_winner(b)
    if winner == 'O':
        return 10
    if winner == 'X':
        return -10
    if is_board_full(b):
        return 0

    if is_maximizing:
        best_score = float('-inf')
        for move in get_available_moves(b):
            b[move] = 'O'
            score = minimax(b, False)
            b[move] = None
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for move in get_available_moves(b):
            b[move] = 'X'
            score = minimax(b, True)
            b[move] = None
            best_score = min(score, best_score)
        return best_score


def get_ai_move():
    """Find the best move for the AI using minimax."""
    best_score = float('-inf')
    best_move = None

    for move in get_available_moves(board):
        board[move] = 'O'
        score = minimax(board, False)
        board[move] = None

        if score > best_score:
            best_score = score
            best_move = move

    return best_move


def pos_to_cell(x, y):
    """Convert screen coordinates to board cell (row, col)."""
    start_x = -BOARD_SIZE // 2
    start_y = BOARD_SIZE // 2

    col = int((x - start_x) // CELL_SIZE)
    row = int((start_y - y) // CELL_SIZE)

    if 0 <= row < 3 and 0 <= col < 3:
        return row, col
    return None, None


def reset_game():
    """Reset the game state."""
    global board, game_over
    board = [None] * 9
    game_over = False
    pen.clear()
    text_pen.clear()
    draw_board()
    show_message("Your turn! You are X")


def handle_click(x, y):
    """Handle mouse click events."""
    global game_over

    if game_over:
        reset_game()
        return

    row, col = pos_to_cell(x, y)
    if row is None:
        return

    pos = row * 3 + col

    if board[pos] is not None:
        return

    # Human move
    board[pos] = 'X'

    # TODO: PROBLEM! Wir zeichnen immer X, egal was im Board steht!
    # Nutze if-else um das richtige Symbol zu zeichnen:
    # if board[pos] == 'X':
    #     draw_x(row, col)
    # else:
    #     draw_o(row, col)

    draw_x(row, col)  # ← BUG: Immer X! Ersetze mit if-else!

    if check_winner(board) == 'X':
        show_message("YOU WIN! (Click to play again)")
        game_over = True
        return

    if is_board_full(board):
        show_message("DRAW! (Click to play again)")
        game_over = True
        return

    # AI move
    show_message("AI is thinking...")

    ai_move = get_ai_move()
    board[ai_move] = 'O'
    ai_row = ai_move // 3
    ai_col = ai_move % 3

    # TODO: Gleiches Problem! Nutze if-else:
    # if board[ai_move] == 'O':
    #     draw_o(ai_row, ai_col)
    # else:
    #     draw_x(ai_row, ai_col)

    draw_x(ai_row, ai_col)  # ← BUG: Immer X! Ersetze mit if-else!

    if check_winner(board) == 'O':
        show_message("AI WINS! (Click to play again)")
        game_over = True
        return

    if is_board_full(board):
        show_message("DRAW! (Click to play again)")
        game_over = True
        return

    show_message("Your turn! Click a square")


# Initialize the game
draw_board()
show_message("Your turn! You are X")

# Set up click handler
screen.onclick(handle_click)

# Keep the window open
turtle.done()
