document.getElementById('myForm').addEventListener('submit', function(event) {
    event.preventDefault();

    // Retrieve data from inputs
    const firstName = document.getElementById('firstName').value;
    const lastName = document.getElementById('lastName').value;

    // Create a JavaScript object
    const formData = {
      firstName: firstName,
      lastName: lastName
    };

    // Convert the object to a JSON string
    const jsonString = JSON.stringify(formData);

    // Append the JSON string to the DOM
    document.getElementById('output').innerText = jsonString;
  });