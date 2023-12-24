const sentence = "The movie is not that bad, I like it";

const wordNot = sentence.indexOf("not");
const wordBad = sentence.indexOf("bad");

if (wordNot !== -1 && wordBad !== -1 && wordNot < wordBad) {
    const modifiedSentence = sentence.slice(0, wordNot) + "good" + sentence.slice(wordBad + 3);
    console.log("Your string is:", sentence);
    console.log("--> the result is:", modifiedSentence);
} else {
    console.log("Your string is:", sentence);
    console.log("--> the result is:", sentence);
}