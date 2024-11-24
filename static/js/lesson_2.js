document.addEventListener('DOMContentLoaded', () => {
    const words = document.querySelectorAll('.word');
    const wordContainer = document.getElementById('wordContainer');

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
    }
});