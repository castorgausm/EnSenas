document.addEventListener('DOMContentLoaded', () => {
    const words = document.querySelectorAll('.word');
    const wordContainer = document.getElementById('wordContainer');
    const accessLesson3Button = document.getElementById('accessLesson3Button');
    console.log("Botón detectado:", accessLesson3Button);

    words.forEach(word => {
        word.addEventListener('dragstart', dragStart);
        word.addEventListener('dragend', dragEnd);
    });

    wordContainer.addEventListener('dragover', dragOver);
    wordContainer.addEventListener('drop', drop);

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
        wordContainer.appendChild(draggable);
        checkCompletion();
    }

    function checkCompletion() {
        const correctOrder = ['word1', 'word2', 'word3', 'word4'];
        const currentOrder = Array.from(wordContainer.children).map(word => word.id);
        if (JSON.stringify(correctOrder) === JSON.stringify(currentOrder)) {
            accessLesson3Button.classList.remove('hide');
            document.getElementById('correctSound').play();

        } else {
            document.getElementById('errorSound').play();
        }
    }
});