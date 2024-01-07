function makeAllCaps(words) {
    return new Promise((resolve, reject) => {
      if (Array.isArray(words) && words.every(word => typeof word === 'string')) {
        const uppercasedWords = words.map(word => word.toUpperCase());
        resolve(uppercasedWords);
      } else {
        reject("Array should contain only strings");
      }
    });
  }
  
  function sortWords(uppercasedWords) {
    return new Promise((resolve, reject) => {
      if (Array.isArray(uppercasedWords) && uppercasedWords.length > 4) {
        const sortedWords = [...uppercasedWords].sort();
        resolve(sortedWords);
      } else {
        reject("Array should have more than 4 words");
      }
    });
  }
  
  // Example usage:
  const wordsArray = ["apple", "banana", "orange", "grape", "kiwi"];
  
  makeAllCaps(wordsArray)
    .then(uppercasedWords => {
      console.log("Words uppercased:", uppercasedWords);
      return sortWords(uppercasedWords);
    })
    .then(sortedWords => {
      console.log("Words sorted:", sortedWords);
    })
    .catch(error => {
      console.error("Error:", error);
    });


//dc 2




    const morseDictionary = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
        'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
        'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
      };
  
      function toJs(morseJson) {
        return new Promise((resolve, reject) => {
          const morseObj = JSON.parse(morseJson);
  
          if (Object.keys(morseObj).length === 0) {
            reject(new Error("Morse JavaScript object is empty"));
          } else {
            resolve(morseObj);
          }
        });
      }
  
      function toMorse(morseJS) {
        return new Promise((resolve, reject) => {
          const userInput = prompt("Enter a word or a sentence:");
          const morseTranslation = [];
  
          for (let char of userInput) {
            const upperChar = char.toUpperCase();
  
            if (morseJS.hasOwnProperty(upperChar)) {
              morseTranslation.push(morseJS[upperChar]);
            } else {
              reject(new Error(`Character "${char}" does not exist in Morse JavaScript object`));
              return; 
            }
          }
  
          resolve(morseTranslation);
        });
      }
  
      function joinWords(morseTranslation) {
        const joinedMorse = morseTranslation.join(' ');
  
        document.body.innerHTML = `<pre>${joinedMorse}</pre>`;
      }
  
      toJs('{"A":".-","B":"-...","C":"-.-.","D":"-..","E":".","F":"..-.","G":"--.","H":"....","I":"..","J":".---"}')
        .then(morseJS => toMorse(morseJS))
        .then(morseTranslation => joinWords(morseTranslation))
        .catch(error => console.error(error));
  