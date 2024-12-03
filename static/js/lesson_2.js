document.addEventListener('DOMContentLoaded', () => {
    const words = document.querySelectorAll('.word');
    const wordContainer = document.getElementById('wordContainer');
    const accessLesson3Button = document.getElementById('accessLesson3Button'); 
    const instructionsContainer = document.getElementById('instructionsContainer');
    const checkOrderButton = document.getElementById('checkOrderButton');
    const footerContainer = document.querySelector('.footer-container');
    const errorSound = document.getElementById('errorSound');
    const correctSound = document.getElementById('correctSound'); 

    words.forEach(word => {
        word.addEventListener('dragstart', dragStart);
        word.addEventListener('dragend', dragEnd);
    });

    instructionsContainer.addEventListener('dragover', dragOver);
    instructionsContainer.addEventListener('drop', drop);

    checkOrderButton.addEventListener('click', checkCompletion);

    function dragStart(e) {
        e.dataTransfer.setData('text/plain', e.target.id);
        setTimeout(() => {
            e.target.classList.add('hide');
        }, 0);
    }

    function dragEnd(e) {
        e.target.classList.remove('hide');
    }

    function dragOver(e) {
        e.preventDefault();
    }

    function drop(e) {
        e.preventDefault();
        const id = e.dataTransfer.getData('text');
        const draggable = document.getElementById(id);
        instructionsContainer.appendChild(draggable);
    }

    function checkCompletion() {
        const correctOrder = ['word1', 'word2', 'word3', 'word4'];
        const currentOrder = Array.from(instructionsContainer.children).map(word => word.id);

        if (JSON.stringify(correctOrder) === JSON.stringify(currentOrder)) {
            instructionsContainer.querySelectorAll('.word').forEach(word => {
                word.classList.add('correct');
                word.classList.remove('incorrect');
                word.setAttribute('draggable', 'false');
            });

            if (accessLesson3Button) {
                accessLesson3Button.classList.add('show');
            }

            checkOrderButton.disabled = true;

            correctSound.play();

            const congratsMessage = document.createElement('p');
            congratsMessage.classList.add('congratulations');
            congratsMessage.textContent = '¡Felicitaciones! Has completado la lección correctamente.';
            footerContainer.appendChild(congratsMessage);

            fetch(`terminar/`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
            }).catch(err => console.error('Error al notificar la finalización:', err));
        } else {
            instructionsContainer.classList.add('shake');
            instructionsContainer.querySelectorAll('.word').forEach(word => {
                word.classList.add('incorrect');
                word.classList.remove('correct');
            });

            errorSound.play();

            setTimeout(() => {
                instructionsContainer.classList.remove('shake');
                instructionsContainer.querySelectorAll('.word').forEach(word => {
                    word.classList.remove('incorrect');
                });
                while (instructionsContainer.firstChild) {
                    wordContainer.appendChild(instructionsContainer.firstChild);
                }
            }, 1000);
        }
    }
});