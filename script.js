// Slide Navigation
let currentSlide = 0;
const slides = document.querySelectorAll('.slide');
const totalSlides = slides.length;

function updateSlideCounter() {
    document.getElementById('slideCounter').textContent = `${currentSlide + 1} / ${totalSlides}`;
}

function changeSlide(direction) {
    slides[currentSlide].classList.remove('active');
    slides[currentSlide].classList.add('prev');

    currentSlide += direction;

    if (currentSlide >= totalSlides) {
        currentSlide = totalSlides - 1;
    } else if (currentSlide < 0) {
        currentSlide = 0;
    }

    slides.forEach((slide, index) => {
        if (index === currentSlide) {
            slide.classList.add('active');
            slide.classList.remove('prev');
        } else if (index < currentSlide) {
            slide.classList.add('prev');
        } else {
            slide.classList.remove('prev');
        }
    });

    updateSlideCounter();
    updateNavButtons();
}

function updateNavButtons() {
    document.getElementById('prevBtn').disabled = currentSlide === 0;
    document.getElementById('nextBtn').disabled = currentSlide === totalSlides - 1;
}

// Keyboard navigation
document.addEventListener('keydown', (e) => {
    if (e.key === 'ArrowRight') {
        changeSlide(1);
    } else if (e.key === 'ArrowLeft') {
        changeSlide(-1);
    }
});

// Initialize
updateSlideCounter();
updateNavButtons();

// ==================== XO GAME ====================

let board = ['', '', '', '', '', '', '', '', ''];
let currentPlayer = 'X';
let gameActive = true;
let difficulty = 'easy';
const humanPlayer = 'X';
const aiPlayer = 'O';

// Winning combinations
const winningConditions = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8], // Rows
    [0, 3, 6], [1, 4, 7], [2, 5, 8], // Columns
    [0, 4, 8], [2, 4, 6]             // Diagonals
];

// Initialize game board
function initializeBoard() {
    const gameBoard = document.getElementById('gameBoard');
    gameBoard.innerHTML = '';

    for (let i = 0; i < 9; i++) {
        const cell = document.createElement('button');
        cell.classList.add('cell');
        cell.setAttribute('data-index', i);
        cell.addEventListener('click', handleCellClick);
        gameBoard.appendChild(cell);
    }
}

// Set difficulty
function setDifficulty(level) {
    difficulty = level;
    const buttons = document.querySelectorAll('.diff-btn');
    buttons.forEach(btn => btn.classList.remove('active'));
    event.target.closest('.diff-btn').classList.add('active');
    resetGame();
}

// Handle cell click
function handleCellClick(e) {
    const index = parseInt(e.target.getAttribute('data-index'));

    if (board[index] !== '' || !gameActive || currentPlayer !== humanPlayer) {
        return;
    }

    makeMove(index, humanPlayer);

    if (gameActive) {
        setTimeout(() => {
            aiMove();
        }, 500);
    }
}

// Make a move
function makeMove(index, player) {
    board[index] = player;
    const cells = document.querySelectorAll('.cell');
    cells[index].textContent = player;
    cells[index].classList.add('taken', player.toLowerCase());

    checkResult();
}

// Check game result
function checkResult() {
    let roundWon = false;
    let winningCombination = null;

    for (let i = 0; i < winningConditions.length; i++) {
        const [a, b, c] = winningConditions[i];
        if (board[a] && board[a] === board[b] && board[a] === board[c]) {
            roundWon = true;
            winningCombination = [a, b, c];
            break;
        }
    }

    if (roundWon) {
        gameActive = false;
        const winner = board[winningCombination[0]];

        // Highlight winning cells
        const cells = document.querySelectorAll('.cell');
        winningCombination.forEach(index => {
            cells[index].classList.add('winner');
        });

        if (winner === humanPlayer) {
            document.getElementById('gameStatus').textContent = '🎉 Du hast gewonnen!';
        } else {
            document.getElementById('gameStatus').textContent = '🤖 Computer hat gewonnen!';
        }
        return;
    }

    // Check for draw
    if (!board.includes('')) {
        gameActive = false;
        document.getElementById('gameStatus').textContent = '🤝 Unentschieden!';
        return;
    }

    // Switch player
    currentPlayer = currentPlayer === humanPlayer ? aiPlayer : humanPlayer;
    updateStatus();
}

// Update status message
function updateStatus() {
    if (gameActive) {
        if (currentPlayer === humanPlayer) {
            document.getElementById('gameStatus').textContent = 'Du bist dran! ❌';
        } else {
            document.getElementById('gameStatus').textContent = 'Computer denkt nach... 🤔';
        }
    }
}

// AI Move
function aiMove() {
    if (!gameActive) return;

    let move;

    switch (difficulty) {
        case 'easy':
            move = getRandomMove();
            break;
        case 'medium':
            move = getMediumMove();
            break;
        case 'hard':
            move = getBestMove();
            break;
    }

    if (move !== -1) {
        makeMove(move, aiPlayer);
    }
}

// Easy: Random move
function getRandomMove() {
    const availableMoves = board.map((cell, index) => cell === '' ? index : null).filter(val => val !== null);
    if (availableMoves.length === 0) return -1;
    return availableMoves[Math.floor(Math.random() * availableMoves.length)];
}

// Medium: Look ahead 2-3 moves with some randomness
function getMediumMove() {
    // 30% chance to make a random move (not always optimal)
    if (Math.random() < 0.3) {
        return getRandomMove();
    }

    // Check if AI can win in next move
    const winMove = findWinningMove(aiPlayer);
    if (winMove !== -1) return winMove;

    // Block player from winning
    const blockMove = findWinningMove(humanPlayer);
    if (blockMove !== -1) return blockMove;

    // Look 2 moves ahead
    const availableMoves = board.map((cell, index) => cell === '' ? index : null).filter(val => val !== null);

    for (let move of availableMoves) {
        // Simulate move
        board[move] = aiPlayer;

        // Check if this leads to a win in 2 moves
        let score = evaluatePosition(2);

        // Undo move
        board[move] = '';

        if (score > 0) {
            return move;
        }
    }

    // Otherwise, take center or corner
    if (board[4] === '') return 4;

    const corners = [0, 2, 6, 8];
    const availableCorners = corners.filter(i => board[i] === '');
    if (availableCorners.length > 0) {
        return availableCorners[Math.floor(Math.random() * availableCorners.length)];
    }

    return getRandomMove();
}

// Find winning move for a player
function findWinningMove(player) {
    for (let i = 0; i < 9; i++) {
        if (board[i] === '') {
            board[i] = player;
            const wins = checkWinner(player);
            board[i] = '';
            if (wins) return i;
        }
    }
    return -1;
}

// Evaluate position (simplified for medium difficulty)
function evaluatePosition(depth) {
    if (depth === 0) return 0;

    const winMove = findWinningMove(aiPlayer);
    if (winMove !== -1) return 1;

    const blockMove = findWinningMove(humanPlayer);
    if (blockMove !== -1) return -1;

    return 0;
}

// Hard: Minimax algorithm
function getBestMove() {
    let bestScore = -Infinity;
    let bestMove = -1;

    for (let i = 0; i < 9; i++) {
        if (board[i] === '') {
            board[i] = aiPlayer;
            let score = minimax(board, 0, false);
            board[i] = '';

            if (score > bestScore) {
                bestScore = score;
                bestMove = i;
            }
        }
    }

    return bestMove;
}

// Minimax algorithm
function minimax(board, depth, isMaximizing) {
    // Check terminal states
    if (checkWinner(aiPlayer)) return 10 - depth;
    if (checkWinner(humanPlayer)) return depth - 10;
    if (!board.includes('')) return 0;

    if (isMaximizing) {
        let bestScore = -Infinity;
        for (let i = 0; i < 9; i++) {
            if (board[i] === '') {
                board[i] = aiPlayer;
                let score = minimax(board, depth + 1, false);
                board[i] = '';
                bestScore = Math.max(score, bestScore);
            }
        }
        return bestScore;
    } else {
        let bestScore = Infinity;
        for (let i = 0; i < 9; i++) {
            if (board[i] === '') {
                board[i] = humanPlayer;
                let score = minimax(board, depth + 1, true);
                board[i] = '';
                bestScore = Math.min(score, bestScore);
            }
        }
        return bestScore;
    }
}

// Check if a player has won
function checkWinner(player) {
    return winningConditions.some(condition => {
        return condition.every(index => board[index] === player);
    });
}

// Reset game
function resetGame() {
    board = ['', '', '', '', '', '', '', '', ''];
    currentPlayer = humanPlayer;
    gameActive = true;
    initializeBoard();
    document.getElementById('gameStatus').textContent = 'Du bist X - Klicke auf ein Feld!';
}

// Initialize the game when on the game slide
document.addEventListener('DOMContentLoaded', () => {
    initializeBoard();
});

// ==================== COLOR CUSTOMIZER ====================

// Sync text input with color picker
document.getElementById('bgColor').addEventListener('input', (e) => {
    const value = e.target.value;
    if (isValidHex(value)) {
        document.getElementById('bgColorPicker').value = value;
    }
});

document.getElementById('bgColorPicker').addEventListener('input', (e) => {
    document.getElementById('bgColor').value = e.target.value;
});

document.getElementById('xColor').addEventListener('input', (e) => {
    const value = e.target.value;
    if (isValidHex(value)) {
        document.getElementById('xColorPicker').value = value;
    }
});

document.getElementById('xColorPicker').addEventListener('input', (e) => {
    document.getElementById('xColor').value = e.target.value;
});

document.getElementById('oColor').addEventListener('input', (e) => {
    const value = e.target.value;
    if (isValidHex(value)) {
        document.getElementById('oColorPicker').value = value;
    }
});

document.getElementById('oColorPicker').addEventListener('input', (e) => {
    document.getElementById('oColor').value = e.target.value;
});

// Validate hex color
function isValidHex(hex) {
    return /^#[0-9A-F]{6}$/i.test(hex);
}

// Apply colors
function applyColors() {
    const bgColor = document.getElementById('bgColor').value;
    const xColor = document.getElementById('xColor').value;
    const oColor = document.getElementById('oColor').value;

    if (!isValidHex(bgColor) || !isValidHex(xColor) || !isValidHex(oColor)) {
        alert('Bitte gib gültige Hex-Codes ein (z.B. #FF0000)');
        return;
    }

    const previewBoard = document.getElementById('previewBoard');
    const previewCells = previewBoard.querySelectorAll('.preview-cell');

    previewBoard.style.background = bgColor;

    previewCells.forEach((cell, index) => {
        if (index % 2 === 0) {
            cell.style.color = xColor;
        } else {
            cell.style.color = oColor;
        }
    });
}

// Reset colors
function resetColors() {
    document.getElementById('bgColor').value = '#2c3e50';
    document.getElementById('bgColorPicker').value = '#2c3e50';
    document.getElementById('xColor').value = '#e74c3c';
    document.getElementById('xColorPicker').value = '#e74c3c';
    document.getElementById('oColor').value = '#3498db';
    document.getElementById('oColorPicker').value = '#3498db';

    const previewBoard = document.getElementById('previewBoard');
    const previewCells = previewBoard.querySelectorAll('.preview-cell');

    previewBoard.style.background = '#2c3e50';

    previewCells.forEach((cell, index) => {
        if (index % 2 === 0) {
            cell.style.color = '#e74c3c';
        } else {
            cell.style.color = '#3498db';
        }
    });
}

// Touch support for mobile
let touchStartX = 0;
let touchEndX = 0;

document.addEventListener('touchstart', e => {
    touchStartX = e.changedTouches[0].screenX;
});

document.addEventListener('touchend', e => {
    touchEndX = e.changedTouches[0].screenX;
    handleSwipe();
});

function handleSwipe() {
    const swipeThreshold = 50;
    const diff = touchStartX - touchEndX;

    if (Math.abs(diff) > swipeThreshold) {
        if (diff > 0) {
            // Swipe left - next slide
            changeSlide(1);
        } else {
            // Swipe right - previous slide
            changeSlide(-1);
        }
    }
}
