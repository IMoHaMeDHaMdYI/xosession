# XO Spiel mit Minimax - CoderDojo Präsentation

Eine interaktive Präsentation über die Entwicklung eines XO-Spiels (TicTacToe) mit Minimax-Algorithmus für Kinder von 7-17 Jahren.

## 📋 Inhalt

Die Präsentation umfasst **15 Folien** basierend auf dem Workshop-Zeitplan (130 Minuten):

### Einführung (35 Min)
1. **Titel** - Einführung in Spiele & KI
2. **Was sind Spiele?** - Beispiele aus dem Alltag (Minecraft, Fortnite, Roblox)
3. **KI in Computerspielen** - Wie Computer "denken"
4. **XO-Spiel Einführung** - Regeln und Beispiel
5. **Interaktives Spiel** - 3 Schwierigkeitsstufen zum Ausprobieren

### Programmierung (60 Min)
6. **Wie bauen wir das?** - Einführung in Programmierung
7. **Programmiersprachen** - Vergleich verschiedener Sprachen
8. **Interaktive Farben** - Anpassung mit Hex-Codes
9. **Python Code Struktur** - Überblick über die Code-Organisation
10. **Programmier-Challenges** - 4 praktische Aufgaben (60 Min gesamt):
    - 🎨 Farben ändern (10 Min)
    - 🔄 Symbole mit if-else tauschen (30 Min)
    - 🎉 Gewinn-Animation (10 Min)
    - 🔄 Neustart-Funktion (10 Min)
11. **Python Code Beispiele** - Wichtige Code-Teile erklärt

### Vertiefung & Wettbewerb (35 Min)
12. **Minimax Erklärung** - Wie der Algorithmus funktioniert
13. **Design deine eigene KI** - Teamarbeit: Strategie entwickeln (20 Min)
14. **Showtime - Der Wettbewerb!** - Teams treten gegeneinander an (15 Min)
15. **Zusammenfassung & Ausblick** - Was ihr gelernt habt

## 📁 Dateien

- **index.html** - Haupt-Präsentationsdatei
- **styles.css** - Styling und Animationen
- **script.js** - Interaktive Spiellogik (JavaScript)
- **tictactoe_minimax.py** - Vollständiger Python-Code mit Minimax
- **CHALLENGES.md** - Detaillierte Anleitung für alle Programmier-Challenges
- **README.md** - Diese Datei

## 🎮 Features

### Interaktives XO-Spiel mit 3 Schwierigkeitsstufen:
- **😊 Leicht**: Computer spielt zufällig
- **😎 Mittel**: Computer schaut 2-3 Züge voraus (nicht optimal)
- **🤓 Schwer**: Vollständiger Minimax-Algorithmus (unbesiegbar)

### Interaktive Farbauswahl:
- Hintergrundfarbe anpassen
- X-Farbe anpassen
- O-Farbe anpassen
- Live-Vorschau mit Hex-Codes

## 🚀 Workshop Ablauf

### Für Präsentierende:

1. **Öffne die Web-Präsentation:** Navigiere zu https://imohamedhamdyi.github.io/xosession/
2. **Navigation:** Nutze Pfeiltasten (←/→) oder die Buttons am unteren Rand
3. **Interaktive Elemente:** Lass die Teilnehmer auf Folie 5 gegen den Computer spielen
4. **Farben anpassen:** Zeige auf Folie 8 die interaktive Farbauswahl

### Für Teilnehmer:

1. **Präsentation ansehen:** Folge der Präsentation auf der Website
2. **Spiel ausprobieren:** Spiele auf Folie 5 gegen die KI (3 Schwierigkeitsstufen)
3. **Python Code:** Öffne `tictactoe_minimax.py` auf Trinket.io oder lokal
4. **Challenges:** Folge der Anleitung in `CHALLENGES.md`
5. **Team-Aktivität:** Entwickle mit deinem Team eine Gewinnstrategie
6. **Wettbewerb:** Teste deine Strategie gegen andere Teams

## 💻 Python Code nutzen

### Auf Trinket.io (empfohlen für Workshops):

1. Gehe zu https://trinket.io/
2. Erstelle ein neues Python-Projekt
3. Kopiere den Code aus `tictactoe_minimax.py`
4. Klicke auf "Run" zum Ausführen
5. Folge den Challenges in `CHALLENGES.md`

### Lokal (mit Python installiert):

```bash
# Python 3 muss installiert sein
python3 tictactoe_minimax.py
```

## 🎯 Lokale Präsentation

1. Öffne `index.html` in einem Browser
2. Nutze die Pfeiltasten oder die Navigationsbuttons zum Wechseln der Folien
3. Auf mobilen Geräten: Wische nach links/rechts

## 📦 Deployment auf GitHub Pages

### Option 1: Direkt im Repository hochladen

1. Erstelle ein neues Repository auf GitHub
2. Lade alle drei Dateien hoch:
   - `index.html`
   - `styles.css`
   - `script.js`
3. Gehe zu Settings → Pages
4. Wähle "Deploy from a branch"
5. Wähle "main" Branch und "/ (root)"
6. Klicke auf "Save"

### Option 2: Mit Git

```bash
# Initialisiere Git Repository
git init

# Füge alle Dateien hinzu
git add .

# Erstelle ersten Commit
git commit -m "Initial commit: XO Minimax Präsentation"

# Füge Remote Repository hinzu (ersetze USERNAME und REPO)
git remote add origin https://github.com/USERNAME/REPO.git

# Push zu GitHub
git branch -M main
git push -u origin main
```

Dann folge den Schritten 3-6 von Option 1.

## 🎯 Navigation

- **Pfeiltasten Links/Rechts**: Zwischen Folien wechseln
- **Navigationbuttons**: Unten auf dem Bildschirm
- **Touch/Swipe**: Auf mobilen Geräten wischen

## 🎨 Anpassung

### Farben ändern:
- Bearbeite die Variablen in `styles.css`
- Ändere den Gradient in der `body`-Regel

### Inhalte anpassen:
- Bearbeite die HTML-Struktur in `index.html`
- Jede Folie ist ein `<div class="slide">`

### Spiellogik ändern:
- Bearbeite die Funktionen in `script.js`
- `minimax()`: Minimax-Algorithmus
- `getMediumMove()`: Mittlere Schwierigkeit
- `getRandomMove()`: Leichte Schwierigkeit

## 🛠️ Technologien

- HTML5
- CSS3 (Flexbox, Grid, Animationen)
- Vanilla JavaScript (ES6+)
- Responsive Design

## 📱 Browser-Unterstützung

- Chrome/Edge (empfohlen)
- Firefox
- Safari
- Mobile Browser (iOS/Android)

## ⏱️ Workshop Zeitplan (130 Minuten)

| Phase | Inhalt | Zeit |
|-------|--------|------|
| **Willkommen** | Begrüßung, Vorstellungsrunde, Installation | 20 Min |
| **Ice-breaker** | Fragen zu KI, Spieltheorie, Gewinnstrategien | 5 Min |
| **Demo** | Interaktives Spiel zeigen und ausprobieren | 10 Min |
| **Programmieren** | 4 Challenges (siehe `CHALLENGES.md`) | 60 Min |
| **Design an AI** | Teams entwickeln eigene Strategien | 20 Min |
| **Showtime** | Wettbewerb zwischen Teams | 15 Min |

## 🎓 Pädagogische Ziele

### Was Teilnehmer lernen:

- **Spieltheorie & KI:** Wie Computer bei Spielen "denken"
- **Algorithmen verstehen:** Minimax-Algorithmus in der Praxis
- **Python Grundlagen:**
  - Variablen und Datentypen
  - Funktionen definieren und aufrufen
  - If-Else Bedingungen
  - Schleifen (for/while)
  - Listen und Indizes
- **Code lesen:** Bestehenden Code verstehen und anpassen
- **Debugging:** Fehler finden und beheben
- **Kreativität:** Eigene Ideen im Code umsetzen
- **Teamarbeit:** Zusammen Strategien entwickeln
- **Problemlösung:** Logisch denken und planen

### Lernmethoden:

- ✅ Learning by Doing - Praktische Challenges
- ✅ Visuelles Lernen - Interaktive Präsentation
- ✅ Peer Learning - Teamarbeit und Wettbewerb
- ✅ Gamification - Spielerisches Lernen
- ✅ Scaffolding - Vom Einfachen zum Komplexen

## 📄 Lizenz

Frei verwendbar für CoderDojo und Bildungszwecke.

## 🤝 Beitragen

Verbesserungsvorschläge und Erweiterungen sind willkommen!

---

**Viel Erfolg beim Workshop! 🚀**
