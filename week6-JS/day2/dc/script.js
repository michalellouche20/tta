document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('libform');
    const storySpan = document.getElementById('story');
    const shuffleButton = document.getElementById('shuffle-button');

    form.addEventListener('submit', function (event) {
        event.preventDefault();

        const noun = document.getElementById('noun').value.trim();
        const adjective = document.getElementById('adjective').value.trim();
        const person = document.getElementById('person').value.trim();
        const verb = document.getElementById('verb').value.trim();
        const place = document.getElementById('place').value.trim();

        if (noun === '' || adjective === '' || person === '' || verb === '' || place === '') {
            alert('Please fill in all fields.');
            return;
        }

        const story = `Once upon a time, there was a ${adjective} ${noun} named ${person}. 
        ${person} loved to ${verb} in ${place}. It was a ${adjective} place filled with ${noun}s.`;

        storySpan.textContent = story;
    });

    shuffleButton.addEventListener('click', shuffleStory);
});

function shuffleStory() {
    const stories = [
        "The quick brown fox jumps over the lazy dog.",
        "A journey of a thousand miles begins with a single step.",
        "All that glitters is not gold.",
        "When in Rome, do as the Romans do.",
        "Actions speak louder than words."
    ];

    const randomIndex = Math.floor(Math.random() * stories.length);
    document.getElementById('story').textContent = stories[randomIndex];
}
