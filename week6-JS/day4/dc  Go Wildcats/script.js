const gameInfo = [
    {
        username: "john",
        team: "red",
        score: 5,
        items: ["ball", "book", "pen"]
    },
    {
        username: "becky",
        team: "blue",
        score: 10,
        items: ["tape", "backpack", "pen"]
    },
    {
        username: "susy",
        team: "red",
        score: 55,
        items: ["ball", "eraser", "pen"]
    },
    {
        username: "tyson",
        team: "green",
        score: 1,
        items: ["book", "pen"]
    },
];

const usernamesWithExclamation = [];
gameInfo.forEach(player => {
    usernamesWithExclamation.push(player.username + '!');
});
console.log(usernamesWithExclamation);

const winners = [];
gameInfo.forEach(player => {
    if (player.score > 5) {
        winners.push(player.username);
    }
});
console.log(winners);

const totalScore = gameInfo.reduce((total, player) => total + player.score, 0);
console.log(totalScore);
