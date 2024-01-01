// Ex 1
// Part I
setTimeout(function () {
    alert('Hello World');
}, 2000);

// Part II
setTimeout(function () {
    const container = document.getElementById('container');
    const paragraph = document.createElement('p');
    paragraph.textContent = 'Hello World';
    container.appendChild(paragraph);
}, 2000);

// Part III
let intervalId = setInterval(function () {
    const container = document.getElementById('container');
    const paragraph = document.createElement('p');
    paragraph.textContent = 'Hello World';
    container.appendChild(paragraph);

    if (container.getElementsByTagName('p').length === 5) {
        clearInterval(intervalId);
    }
}, 2000);

document.getElementById('clear').addEventListener('click', function () {
    clearInterval(intervalId);
});
  

//Ex 2

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
