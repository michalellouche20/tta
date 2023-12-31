
const robots = [
    {
      id: 1,
      name: 'Leanne Graham',
      username: 'Bret',
      email: 'Sincere@april.biz',
      image: 'https://robohash.org/1?200x200',
      description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'
    },
    {
      id: 2,
      name: 'Ervin Howell',
      username: 'Antonette',
      email: 'Shanna@melissa.tv',
      image: 'https://robohash.org/2?200x200'
    },
    {
        id: 3,
        name: 'Eva Martinez',
        username: 'eva_m',
        email: 'eva@example.com',
        image: 'https://robohash.org/13?200x200',
        description: 'Data Scientist'
      },
      {
        id: 4,
        name: 'Maximus Turner',
        username: 'maximus_t',
        email: 'max@example.com',
        image: 'https://robohash.org/14?200x200',
        description: 'AI Researcher'
      },
      {
        id: 5,
        name: 'Sophie White',
        username: 'sophie_w',
        email: 'sophie@example.com',
        image: 'https://robohash.org/15?200x200',
        description: 'Robotics Engineer'
    },
    {
        id: 6,
        name: 'Alice Johnson',
        username: 'alice92',
        email: 'alice@example.com',
        image: 'https://robohash.org/11?200x200',
        description: 'Front-end Developer'
      },
    ];
  


document.addEventListener('DOMContentLoaded', function () {
    const robotCardsContainer = document.getElementById('robotCards');
    const searchInput = document.getElementById('searchInput');
  
    renderRobotCards(robots);
  
    searchInput.addEventListener('input', function () {
      const searchTerm = searchInput.value.toLowerCase();
      const filteredRobots = robots.filter(robot =>
        robot.name.toLowerCase().includes(searchTerm)
      );
      renderRobotCards(filteredRobots);
    });
  

    function renderRobotCards(robotArray) {
      robotCardsContainer.innerHTML = '';
  
      robotArray.forEach(robot => {
        const card = document.createElement('div');
        card.classList.add('card');
  
        const img = document.createElement('img');
        img.src = robot.image;
        img.alt = robot.name;
  
        const name = document.createElement('h3');
        name.textContent = robot.name;
  
        const username = document.createElement('p');
        username.textContent = `Username: ${robot.username}`;
  
        const email = document.createElement('p');
        email.textContent = `Email: ${robot.email}`;
  
        card.appendChild(img);
        card.appendChild(name);
        card.appendChild(username);
        card.appendChild(email);
  
        robotCardsContainer.appendChild(card);
      });
    }
  });