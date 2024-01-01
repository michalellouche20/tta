const planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"];

function createPlanet(planetName, moonCount) {
    const planetDiv = document.createElement("div");
    planetDiv.className = "planet " + planetName.toLowerCase(); 

    planetDiv.textContent = planetName;

    for (let i = 1; i <= moonCount; i++) {
        const moonDiv = document.createElement("div");
        moonDiv.className = "moon"; 
        moonDiv.textContent = i; 

        const angle = (i / moonCount) * 2 * Math.PI;
        const radius = 60; 
        const moonX = 50 + radius * Math.cos(angle);
        const moonY = 50 + radius * Math.sin(angle);

        moonDiv.style.left = moonX + "px";
        moonDiv.style.top = moonY + "px";

        planetDiv.appendChild(moonDiv);
    }

    document.querySelector(".listPlanets").appendChild(planetDiv);
}

planets.forEach((planet, index) => {
    createPlanet(planet, index + 1);
});
