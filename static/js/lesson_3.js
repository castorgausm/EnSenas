document.addEventListener('DOMContentLoaded', () => {
    // Iniciar la evaluación con múltiples preguntas
    renderQuestions(0);
});

const questions = [
    {
        "question": "¿Cuál de estos es el signo para la letra 'A'?",
        "options": [
            { "id": 1, "label": "A", "imageUrl": "/static/images/a.png", "correct": true },
            { "id": 2, "label": "B", "imageUrl": "/static/images/b.png", "correct": false },
            { "id": 3, "label": "C", "imageUrl": "/static/images/c.png", "correct": false }
        ]
    },
    {
        "question": "¿Cuál de estos es el signo para la letra 'B'?",
        "options": [
            { "id": 1, "label": "A", "imageUrl": "/static/images/A.png", "correct": false },
            { "id": 2, "label": "B", "imageUrl": "/static/images/B.png", "correct": true },
            { "id": 3, "label": "D", "imageUrl": "/static/images/D.png", "correct": false }
        ]
    },
    {
        "question": "¿Cuál de estos es el signo para la letra 'C'?",
        "options": [
            { "id": 1, "label": "C", "imageUrl": "/static/images/C.png", "correct": true },
            { "id": 2, "label": "F", "imageUrl": "/static/images/F.png", "correct": false },
            { "id": 3, "label": "B", "imageUrl": "/static/images/B.png", "correct": false }
        ]
    },
    {
        "question": "¿Cuál de estos es el signo para la letra 'D'?",
        "options": [
            { "id": 1, "label": "D", "imageUrl": "/static/images/D.png", "correct": true },
            { "id": 2, "label": "E", "imageUrl": "/static/images/E.png", "correct": false },
            { "id": 3, "label": "A", "imageUrl": "/static/images/A.png", "correct": false }
        ]
    },
    {
        "question": "¿Cuál de estos es el signo para la letra 'E'?",
        "options": [
            { "id": 1, "label": "B", "imageUrl": "/static/images/B.png", "correct": false },
            { "id": 2, "label": "E", "imageUrl": "/static/images/E.png", "correct": true },
            { "id": 3, "label": "C", "imageUrl": "/static/images/C.png", "correct": false }
        ]
    },
    {
        "question": "¿Cuál de estos es el signo para la letra 'F'?",
        "options": [
            { "id": 1, "label": "F", "imageUrl": "/static/images/F.png", "correct": true },
            { "id": 2, "label": "D", "imageUrl": "/static/images/D.png", "correct": false },
            { "id": 3, "label": "A", "imageUrl": "/static/images/A.png", "correct": false }
        ]
    },
    {
        "question": "¿Cuál de estos es el signo para la letra 'G'?",
        "options": [
            { "id": 1, "label": "G", "imageUrl": "/static/images/G.png", "correct": true },
            { "id": 2, "label": "H", "imageUrl": "/static/images/H.png", "correct": false },
            { "id": 3, "label": "E", "imageUrl": "/static/images/E.png", "correct": false }
        ]
    },
    {
        "question": "¿Cuál de estos es el signo para la letra 'H'?",
        "options": [
            { "id": 1, "label": "H", "imageUrl": "/static/images/H.png", "correct": true },
            { "id": 2, "label": "G", "imageUrl": "/static/images/G.png", "correct": false },
            { "id": 3, "label": "B", "imageUrl": "/static/images/B.png", "correct": false }
        ]
    },
];

function renderQuestions(currentIndex) {
    if (currentIndex >= questions.length) {
        document.getElementById('question').textContent = '¡Evaluación completada!';
        document.getElementById('options-container').innerHTML = '';
        document.getElementById('result').textContent = '';
        updateProgress(currentIndex);
        return;
    }

    const currentQuestion = questions[currentIndex];
    document.getElementById('question').textContent = currentQuestion.question;

    const optionsContainer = document.getElementById('options-container');
    optionsContainer.innerHTML = '';

    currentQuestion.options.forEach(option => {
        const optionDiv = document.createElement('div');
        optionDiv.className = 'option';
        optionDiv.addEventListener('click', () => checkAnswer(option.correct, currentIndex));

        const image = document.createElement('img');
        image.setAttribute('src', option.imageUrl);

        optionDiv.appendChild(image);
        optionsContainer.appendChild(optionDiv);
    });

    updateProgress(currentIndex);
}

function checkAnswer(isCorrect, currentIndex) {
    const resultText = isCorrect ? '¡Correcto! Muy bien hecho!' : 'Incorrecto. Inténtalo de nuevo.';
    document.getElementById('result').textContent = resultText;
    document.getElementById('result').className = isCorrect ? 'text-green' : 'text-red';

    if (isCorrect) {
        setTimeout(() => {
            renderQuestions(currentIndex + 1);
        }, 1000);
    }
}

function updateProgress(currentIndex) {
    const progressElement = document.querySelector('.progress');
    const progressPercentage = ((currentIndex) / questions.length) * 100;
    progressElement.style.width = `${progressPercentage}%`;
}