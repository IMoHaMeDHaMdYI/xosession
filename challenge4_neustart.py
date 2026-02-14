"""
Challenge 4: Neustart-Funktion verstehen
=========================================
Das Spiel kann bereits neu gestartet werden (klick nach Spielende)!

AUFGABE:
1. Finde die reset_game() Funktion (Zeile 232)
2. Verstehe, was jede Zeile macht
3. BONUS: Füge einen Zähler hinzu (wie viele Spiele gespielt wurden?)
4. BONUS: Zähle Siege von Spieler und KI

TIPP: Suche nach "# TODO" für Bonus-Aufgaben!
"""

import turtle
import random

# Game state
board = [None] * 9
game_over = False
CELL_SIZE = 100
BOARD_SIZE = CELL_SIZE * 3

# Farben
x_farbe = "blue"
o_farbe = "red"
board_farbe = "black"
screen_farbe = "white"

# Spieler-Symbole
player_symbol = 'X'
ai_symbol = 'O'

# TODO BONUS: Erstelle Variablen für Statistiken
games_played = 0      # Wie viele Spiele wurden gespielt?
player_wins = 0       # Wie oft hat der Spieler gewonnen?
ai_wins = 0          # Wie oft hat die KI gewonnen?
draws = 0            # Wie oft war es unentschieden?

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


def draw_firework(x, y):
    """Zeichnet ein Feuerwerk an Position (x, y)."""
    colors = ["red", "yellow", "blue", "green", "purple", "orange"]

    for i in range(36):
        pen.color(random.choice(colors))
        pen.penup()
        pen.goto(x, y)
        pen.pendown()
        pen.forward(50)
        pen.penup()
        pen.goto(x, y)
        pen.right(10)


def celebrate_win(winner):
    """Feiert den Gewinner mit einer Animation!"""
    screen.bgcolor("lightyellow")
    draw_firework(0, 100)
    draw_firework(-100, 50)
    draw_firework(100, 50)


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
    if winner == ai_symbol:
        return 10
    if winner == player_symbol:
        return -10
    if is_board_full(b):
        return 0

    if is_maximizing:
        best_score = float('-inf')
        for move in get_available_moves(b):
            b[move] = ai_symbol
            score = minimax(b, False)
            b[move] = None
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for move in get_available_moves(b):
            b[move] = player_symbol
            score = minimax(b, True)
            b[move] = None
            best_score = min(score, best_score)
        return best_score


def get_ai_move():
    """Find the best move for the AI using minimax."""
    best_score = float('-inf')
    best_move = None

    for move in get_available_moves(board):
        board[move] = ai_symbol
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


# ========================================
# 🔄 DIE NEUSTART-FUNKTION 🔄
# ========================================
def reset_game():
    """
    Setzt das Spiel zurück auf Anfangszustand.
    Diese Funktion wird aufgerufen, wenn das Spiel vorbei ist
    und der Spieler klickt.
    """
    global board, game_over  # Wir ändern diese globalen Variablen
    # TODO BONUS: Auch games_played, player_wins, ai_wins, draws

    # TODO BONUS: Erhöhe games_played um 1
    # games_played += 1

    # 1. Setze das Board zurück (alle Felder leer)
    board = [None] * 9

    # 2. Spiel läuft wieder
    game_over = False

    # 3. Lösche alle Zeichnungen
    pen.clear()
    text_pen.clear()

    # 4. Setze Hintergrund zurück
    screen.bgcolor(screen_farbe)

    # 5. Zeichne neues Spielfeld
    draw_board()

    # 6. Zeige Start-Nachricht
    # TODO BONUS: Zeige auch die Statistik an
    # show_message(f"Spiel {games_played} - Du bist {player_symbol}! | Siege: Du {player_wins} - KI {ai_wins}")
    show_message(f"Your turn! You are {player_symbol}")


def handle_click(x, y):
    """Handle mouse click events."""
    global game_over
    # TODO BONUS: Auch player_wins, ai_wins, draws

    if game_over:
        # Spiel ist vorbei - starte neu!
        reset_game()  # ← Hier wird die Neustart-Funktion aufgerufen!
        return

    row, col = pos_to_cell(x, y)
    if row is None:
        return

    pos = row * 3 + col

    if board[pos] is not None:
        return

    # Human move
    board[pos] = player_symbol

    if player_symbol == 'X':
        draw_x(row, col)
    else:
        draw_o(row, col)

    if check_winner(board) == player_symbol:
        celebrate_win(player_symbol)

        # TODO BONUS: Erhöhe player_wins um 1
        # player_wins += 1

        show_message("YOU WIN! 🎉 (Click to play again)")
        game_over = True
        return

    if is_board_full(board):
        # TODO BONUS: Erhöhe draws um 1
        # draws += 1

        show_message("DRAW! (Click to play again)")
        game_over = True
        return

    # AI move
    show_message("AI is thinking...")

    ai_move = get_ai_move()
    board[ai_move] = ai_symbol
    ai_row = ai_move // 3
    ai_col = ai_move % 3

    if ai_symbol == 'O':
        draw_o(ai_row, ai_col)
    else:
        draw_x(ai_row, ai_col)

    if check_winner(board) == ai_symbol:
        celebrate_win(ai_symbol)

        # TODO BONUS: Erhöhe ai_wins um 1
        # ai_wins += 1

        show_message("AI WINS! (Click to play again)")
        game_over = True
        return

    if is_board_full(board):
        # TODO BONUS: Erhöhe draws um 1
        # draws += 1

        show_message("DRAW! (Click to play again)")
        game_over = True
        return

    show_message("Your turn! Click a square")


# Initialize the game
draw_board()
show_message(f"Your turn! You are {player_symbol}")

# Set up click handler
screen.onclick(handle_click)

# Keep the window open
turtle.done()
