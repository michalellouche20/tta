document.addEventListener('DOMContentLoaded', function () {
    const h1Element = document.querySelector('h1');
    console.log(h1Element.textContent);
  
    const paragraphs = document.querySelectorAll('article p');
    paragraphs[paragraphs.length - 1].remove();
  
    const h2Element = document.querySelector('h2');
    h2Element.addEventListener('click', function () {
      h2Element.style.backgroundColor = 'red';
    });
  
    const h3Element = document.querySelector('h3');
    h3Element.addEventListener('click', function () {
      h3Element.style.display = 'none';
    });
  
    const buttonElement = document.createElement('button');
    buttonElement.textContent = 'Make Text Bold';
    document.body.appendChild(buttonElement);
  
    buttonElement.addEventListener('click', function () {
      const paragraphs = document.querySelectorAll('article p');
      paragraphs.forEach(paragraph => {
        paragraph.style.fontWeight = 'bold';
      });
    });
  
    h1Element.addEventListener('mouseover', function () {
      const randomSize = Math.floor(Math.random() * 101);
      h1Element.style.fontSize = `${randomSize}px`;
    });
  
    const secondParagraph = paragraphs[1];
    secondParagraph.addEventListener('mouseover', function () {
      secondParagraph.style.transition = 'opacity 0.5s';
      secondParagraph.style.opacity = 0;
    });
  });
  

  //xp 2
  document.addEventListener('DOMContentLoaded', function () {
    const myForm = document.getElementById('myForm');
    console.log(myForm);
  
    const firstNameInput = document.getElementById('fname');
    const lastNameInput = document.getElementById('lname');
    console.log(firstNameInput, lastNameInput);
  
    const inputsByName = document.getElementsByName('firstname');
    console.log(inputsByName);
  
    myForm.addEventListener('submit', function (event) {
      event.preventDefault();
  
      const firstNameValue = firstNameInput.value.trim();
      const lastNameValue = lastNameInput.value.trim();
  
      if (firstNameValue !== '' && lastNameValue !== '') {
        const ulElement = document.querySelector('.usersAnswer');
        const liFirstName = document.createElement('li');
        const liLastName = document.createElement('li');
  
        liFirstName.textContent = `First name: ${firstNameValue}`;
        liLastName.textContent = `Last name: ${lastNameValue}`;
  
        ulElement.innerHTML = ''; 
        ulElement.appendChild(liFirstName);
        ulElement.appendChild(liLastName);
      }
    });
  });