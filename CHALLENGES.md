# 🎯 Programmier-Challenges

## Übersicht

Diese Challenges helfen euch, den Python-Code zu verstehen und anzupassen. Ihr habt **60 Minuten** für alle 4 Aufgaben.

---

## 🎨 Challenge 1: Farben ändern (10 Minuten)

**Ziel:** Ändere das Aussehen des Spielfelds!

### Was du tun musst:

1. Öffne die Datei `tictactoe_minimax.py`
2. Suche nach den Funktionen `draw_x()` und `draw_o()`
3. Finde die Zeilen mit `pen.color("blue")` und `pen.color("red")`
4. Ändere die Farben zu deinen Lieblingsfarben!

### Mögliche Farben:
- `"red"`, `"blue"`, `"green"`, `"yellow"`, `"purple"`, `"orange"`, `"pink"`
- Oder nutze Hex-Codes wie `"#FF5733"`

### Beispiel:
```python
def draw_x(row, col):
    pen.color("purple")  # War vorher "blue"
    pen.pensize(4)
    # ...

def draw_o(row, col):
    pen.color("orange")  # War vorher "red"
    pen.pensize(4)
    # ...
```

**Bonus:** Ändere auch die Hintergrundfarbe mit `screen.bgcolor("lightblue")`

---

## 🔄 Challenge 2: Symbole tauschen (30 Minuten)

**Ziel:** Lass den Spieler wählen, ob er X oder O sein möchte!

### Was du lernen wirst:
- `if-else` Bedingungen nutzen
- Benutzereingaben verarbeiten
- Variablen verwenden

### Schritte:

1. **Neue Variable erstellen:**
```python
# Am Anfang der Datei, nach den anderen Variablen:
player_symbol = 'X'  # oder 'O', je nach Wahl
ai_symbol = 'O'      # das Gegenteil vom Spieler
```

2. **Spieler wählen lassen:**
```python
# Vor draw_board():
choice = screen.textinput("Wähle dein Symbol", "Möchtest du X oder O sein? (x/o)")

if choice and choice.lower() == 'o':
    player_symbol = 'O'
    ai_symbol = 'X'
else:
    player_symbol = 'X'
    ai_symbol = 'O'
```

3. **Code anpassen:**
Ersetze alle `'X'` und `'O'` im Code mit `player_symbol` und `ai_symbol`

### Beispiel Änderung:
```python
# Vorher:
board[pos] = 'X'

# Nachher:
board[pos] = player_symbol
```

**Wichtig:** Du musst das in mehreren Stellen ändern:
- In `handle_click()` beim Spielerzug
- In `get_ai_move()` beim KI-Zug
- In den Gewinn-Checks

---

## 🎉 Challenge 3: Gewinn-Animation (10 Minuten)

**Ziel:** Zeige etwas Cooles, wenn jemand gewinnt!

### Ideen:

#### 1. Feuerwerk zeichnen:
```python
def draw_firework(x, y):
    """Zeichnet ein einfaches Feuerwerk."""
    pen.penup()
    pen.goto(x, y)
    pen.pendown()

    colors = ["red", "yellow", "blue", "green", "purple"]

    for i in range(36):
        pen.color(colors[i % len(colors)])
        pen.forward(50)
        pen.backward(50)
        pen.right(10)
```

#### 2. Gewinner-Animation hinzufügen:
```python
# In handle_click(), wenn jemand gewinnt:
if check_winner(board) == player_symbol:
    draw_firework(0, 100)
    draw_firework(-100, 50)
    draw_firework(100, 50)
    show_message("DU HAST GEWONNEN! 🎉 (Klick für neues Spiel)")
```

#### 3. Andere Ideen:
- Zeichne Sterne um das Spielfeld
- Lass die Gewinner-Felder blinken (mehrmals zeichnen/löschen)
- Ändere die Hintergrundfarbe bei Gewinn

---

## 🔄 Challenge 4: Neustart-Button (10 Minuten)

**Ziel:** Das Spiel lässt sich bereits neu starten! Verstehe wie es funktioniert.

### Was passiert aktuell:

1. **Automatischer Neustart bei Klick:**
```python
def handle_click(x, y):
    global game_over

    if game_over:
        reset_game()  # ← Hier wird neu gestartet
        return
```

2. **Die reset_game() Funktion:**
```python
def reset_game():
    global board, game_over
    board = [None] * 9  # Leert das Board
    game_over = False   # Spiel läuft wieder
    pen.clear()         # Löscht alte Zeichnungen
    text_pen.clear()    # Löscht alte Nachrichten
    draw_board()        # Zeichnet neues Board
    show_message("Your turn! Click a square (You are X)")
```

### Deine Aufgabe:

**Verbessere den Neustart:**

1. Zeige eine andere Nachricht beim Neustart
2. Ändere die Farben beim Neustart
3. Zähle, wie viele Spiele gespielt wurden:

```python
# Am Anfang der Datei:
games_played = 0

# In reset_game():
def reset_game():
    global board, game_over, games_played
    games_played += 1
    board = [None] * 9
    game_over = False
    pen.clear()
    text_pen.clear()
    draw_board()
    show_message(f"Spiel {games_played} - Du bist dran!")
```

**Bonus:** Zähle Siege von Spieler und KI!

---

## 🚀 Extra Challenges (Wenn du schnell fertig bist)

### 1. Punktezähler
Zeige an, wie oft Spieler und KI gewonnen haben.

### 2. Verschiedene Schwierigkeitsgrade
- Leicht: KI macht zufällige Züge
- Mittel: KI nutzt nur teilweise Minimax
- Schwer: Vollständiger Minimax (aktuell)

### 3. Größeres Spielfeld
Versuche ein 4x4 oder 5x5 Feld zu erstellen!

### 4. Sound-Effekte
Nutze `turtle` Befehle oder externe Bibliotheken für Sounds.

---

## 💡 Tipps

1. **Teste oft:** Führe dein Programm nach jeder kleinen Änderung aus
2. **Fehler sind OK:** Lies die Fehlermeldungen, sie helfen dir!
3. **Frag nach Hilfe:** Mentoren und andere Teilnehmer helfen gerne
4. **Experimentiere:** Es gibt keine "falsche" Lösung!
5. **Kommentiere deinen Code:** Schreibe auf, was dein Code macht

```python
# Das ist ein Kommentar - erklärt, was der Code macht
pen.color("red")  # Ändert die Farbe zu rot
```

---

## 📚 Nützliche Python-Befehle

### Turtle Graphics:
```python
pen.color("red")           # Farbe ändern
pen.pensize(5)             # Linienstärke ändern
pen.goto(x, y)             # Zu Position gehen
pen.circle(50)             # Kreis zeichnen
screen.bgcolor("white")    # Hintergrundfarbe
```

### If-Else Bedingungen:
```python
if bedingung:
    # Wenn bedingung wahr ist
    tue_etwas()
else:
    # Sonst
    tue_etwas_anderes()
```

### Schleifen:
```python
for i in range(10):
    # Wird 10 mal wiederholt
    print(i)
```

---

## 🏆 Viel Erfolg!

Denk dran: Programmieren lernt man durch Ausprobieren. Hab Spaß und sei kreativ! 🚀
