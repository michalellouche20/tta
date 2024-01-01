
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
