let gameState = {
    gameId: null,
    theme: '',
    words: [],
    revealedWords: Array(9).fill(''),
    attempts: 0,
    hintPoints: 9
};

function startNewGame() {
    fetch('/api/new-game')
        .then(response => response.json())
        .then(data => {
            gameState = {
                gameId: data.game_id,
                theme: data.theme,
                words: data.words,
                revealedWords: Array(9).fill(''),
                attempts: data.attempts,
                hintPoints: data.hint_points
            };
            updateUI();
        });
}

function updateUI() {
    document.getElementById('theme').textContent = `Theme: ${gameState.theme}`;
    const grid = document.getElementById('grid');
    grid.innerHTML = '';
    for (let i = 0; i < 9; i++) {
        const item = document.createElement('div');
        item.classList.add('grid-item');
        item.textContent = gameState.revealedWords[i] || '?';
        grid.appendChild(item);
    }
    document.getElementById('attempts').textContent = `Attempts: ${gameState.attempts}`;
    document.getElementById('hint-points').textContent = `Hint Points: ${gameState.hintPoints}`;
}

function submitWord() {
    const wordInput = document.getElementById('word-input');
    const word = wordInput.value.trim().toLowerCase();
    if (word) {
        fetch('/api/check-word', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ game_id: gameState.gameId, word: word }),
        })
        .then(response => response.json())
        .then(data => {
            if (data.correct) {
                const index = gameState.words.indexOf(word);
                if (index !== -1) {
                    gameState.revealedWords[index] = word;
                    document.getElementById('message').textContent = 'Correct! Well done!';
                    document.getElementById('message').style.color = 'green';
                }
            } else {
                document.getElementById('message').textContent = 'Incorrect. Try again!';
                document.getElementById('message').style.color = 'red';
            }
            gameState.attempts = data.attempts;
            updateUI();
            wordInput.value = '';
        });
    }
}

function getHint() {
    if (gameState.hintPoints >= 3) {
        const unrevealedIndices = gameState.revealedWords.reduce((acc, word, index) => {
            if (!word) acc.push(index);
            return acc;
        }, []);
        
        if (unrevealedIndices.length > 0) {
            const randomIndex = unrevealedIndices[Math.floor(Math.random() * unrevealedIndices.length)];
            fetch('/api/get-hint', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ game_id: gameState.gameId, word_index: randomIndex }),
            })
            .then(response => response.json())
            .then(data => {
                gameState.revealedWords[randomIndex] = data.hint + '...';
                gameState.hintPoints = data.hint_points;
                updateUI();
            });
        }
    } else {
        alert('Not enough hint points!');
    }
}

document.addEventListener('DOMContentLoaded', () => {
    startNewGame();
    document.getElementById('submit-word').addEventListener('click', submitWord);
    document.getElementById('hint-button').addEventListener('click', getHint);
    document.getElementById('word-input').addEventListener('keypress', (e) => {
        if (e.key === 'Enter') {
            submitWord();
        }
    });
});
