"""
Challenge 3: Gewinn-Animation
==============================
Zeige etwas Cooles, wenn jemand gewinnt!

🎮 BESONDERHEIT: Die KI ist EINFACHER damit du gewinnen kannst!
   Die KI macht 70% zufällige Züge - so kannst du deine Animation testen!

AUFGABE:
1. Erstelle eine Funktion draw_firework() (Zeile 130)
2. Rufe die Funktion auf, wenn jemand gewinnt (Zeilen 303, 330)
3. Experimentiere mit verschiedenen Animationen!

IDEEN:
- Feuerwerk zeichnen
- Sterne um das Spielfeld
- Hintergrundfarbe ändern
- Konfetti-Effekt
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

# Spieler-Symbole (aus Challenge 2)
player_symbol = 'X'
ai_symbol = 'O'

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


def show_message(msg, size=16):
    """Display a message below the board."""
    text_pen.clear()
    text_pen.goto(0, -BOARD_SIZE // 2 - 40)
    text_pen.write(msg, align="center", font=("Arial", size, "bold"))


# ========================================
# 🎉 HIER KANNST DU DEINE ANIMATION ERSTELLEN! 🎉
# ========================================

def draw_firework(x, y):
    """
    Zeichnet ein Feuerwerk an Position (x, y).
    TODO: Füge hier deinen Code ein!
    """
    # Beispiel-Animation: Feuerwerk
    colors = ["red", "yellow", "blue", "green", "purple", "orange"]

    # TODO: Erstelle eine for-Schleife für 36 Linien
    # for i in range(36):
    #     pen.color(random.choice(colors))
    #     pen.goto(x, y)
    #     pen.pendown()
    #     pen.forward(50)
    #     pen.penup()
    #     pen.goto(x, y)
    #     pen.right(10)

    pass  # ← Lösche diese Zeile und füge deinen Code ein!


def draw_stars():
    """
    Zeichnet Sterne um das Spielfeld.
    TODO: Experimentiere mit verschiedenen Positionen!
    """
    # Beispiel: Zeichne einen Stern
    # for i in range(5):
    #     pen.forward(50)
    #     pen.right(144)

    pass  # ← Lösche diese Zeile und füge deinen Code ein!


def celebrate_win(winner):
    """
    Feiert den Gewinner mit einer Animation!
    TODO: Rufe deine Animations-Funktionen hier auf!
    """
    # Beispiel: Ändere die Hintergrundfarbe
    # screen.bgcolor("lightyellow")

    # Beispiel: Zeichne Feuerwerk
    # draw_firework(0, 100)
    # draw_firework(-100, 50)
    # draw_firework(100, 50)

    # Beispiel: Zeichne Sterne
    # draw_stars()

    pass  # ← Lösche diese Zeile und füge deinen Code ein!


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
    """
    Find a move for the AI - EASY MODE!
    Die KI macht zu 70% zufällige Züge, damit du gewinnen kannst!
    """
    available = get_available_moves(board)

    # 70% der Zeit: Mache einen zufälligen Zug
    if random.random() < 0.7:
        return random.choice(available)

    # 30% der Zeit: Versuche zu gewinnen oder zu blocken
    # Prüfe ob KI gewinnen kann
    for move in available:
        board[move] = ai_symbol
        if check_winner(board) == ai_symbol:
            board[move] = None
            return move
        board[move] = None

    # Prüfe ob Spieler gewinnen würde (und blocke es)
    for move in available:
        board[move] = player_symbol
        if check_winner(board) == player_symbol:
            board[move] = None
            return move
        board[move] = None

    # Sonst: zufälliger Zug
    return random.choice(available)


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
    screen.bgcolor(screen_farbe)  # Setze Hintergrund zurück
    draw_board()
    show_message(f"Your turn! You are {player_symbol}")


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
    board[pos] = player_symbol

    if player_symbol == 'X':
        draw_x(row, col)
    else:
        draw_o(row, col)

    if check_winner(board) == player_symbol:
        # TODO: Rufe deine Animations-Funktion hier auf!
        celebrate_win(player_symbol)  # ← Aktiviere diese Zeile!

        show_message(f"🎉 DU HAST GEWONNEN! 🎉\n{player_symbol} gewinnt!\n(Klick für neues Spiel)", size=24)
        game_over = True
        return

    if is_board_full(board):
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
        # TODO: Rufe deine Animations-Funktion hier auf!
        celebrate_win(ai_symbol)  # ← Aktiviere diese Zeile!

        show_message(f"KI HAT GEWONNEN!\n{ai_symbol} gewinnt!\n(Klick für neues Spiel)", size=24)
        game_over = True
        return

    if is_board_full(board):
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
