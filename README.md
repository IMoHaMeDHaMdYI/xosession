# XO Spiel mit Minimax - CoderDojo Präsentation

Eine interaktive Präsentation über die Entwicklung eines XO-Spiels (TicTacToe) mit Minimax-Algorithmus für Kinder von 7-17 Jahren.

## 📋 Inhalt

Die Präsentation umfasst 10 Folien:

1. **Titel** - Einführung in Spiele & KI
2. **Was sind Spiele?** - Beispiele aus dem Alltag
3. **KI in Computerspielen** - Wie Computer "denken"
4. **XO-Spiel Einführung** - Regeln und Beispiel
5. **Interaktives Spiel** - 3 Schwierigkeitsstufen zum Ausprobieren
6. **Wie bauen wir das?** - Einführung in Programmierung
7. **Programmiersprachen** - Vergleich verschiedener Sprachen
8. **Interaktive Farben** - Anpassung mit Hex-Codes
9. **Minimax Erklärung** - Wie der Algorithmus funktioniert
10. **Jetzt bist du dran!** - Motivierender Abschluss

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

## 🚀 Lokale Nutzung

1. Öffne einfach die `index.html` in einem Browser
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

## 🎓 Pädagogische Ziele

- Spielerische Einführung in KI und Algorithmen
- Verständnis für Spieltheorie
- Erste Schritte in der Programmierung
- Praktische Anwendung von Code
- Motivation zum Selbstlernen

## 📄 Lizenz

Frei verwendbar für CoderDojo und Bildungszwecke.

## 🤝 Beitragen

Verbesserungsvorschläge und Erweiterungen sind willkommen!

---

**Viel Erfolg beim Workshop! 🚀**
