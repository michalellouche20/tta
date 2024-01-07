//ex1
function compareToTen(num) {
    return new Promise((resolve, reject) => {
      if (num <= 10) {
        resolve(`${num} is less than or equal to 10`);
      } else {
        reject(`${num} is greater than 10`);
      }
    });
  }
  //ex2 
  function delayedResolve() {
    return new Promise((resolve) => {
      setTimeout(() => {
        resolve("success");
      }, 4000); 
    });
  }
  
  delayedResolve()
    .then((result) => {
      console.log(result); 
    })
    .catch((error) => {
      console.error(error);
    });
  
//ex3

const resolvedPromise = Promise.resolve(3);

resolvedPromise
  .then(result => console.log(result)) 
  .catch(error => console.error(error)); 
const rejectedPromise = Promise.reject("Boo!");

rejectedPromise
  .then(result => console.log(result))
  .catch(error => console.error(error)); 
