
function myMove() {
    const container = document.getElementById('container');
    const animate = document.getElementById('animate');
    let position = 0;

    const intervalId = setInterval(function () {
        position++;
        animate.style.left = position + 'px';

        if (position === container.offsetWidth - animate.offsetWidth) {
            clearInterval(intervalId);
        }
    }, 1);
}
