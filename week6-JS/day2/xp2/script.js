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