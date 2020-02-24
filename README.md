# ForceField
Simulating earth's orbital space.

## About
```ForceField``` is c++ written simulation software for analysis and prediction of objects and potential events in various levels of general Earth orbit.

## Why?
Two-fold. One, I have been interested in designing astrophysics simulation software since I was a child. My first love was space. So this project is dedicated to a large component of what has made me the curious adult I am today. 

The second reason for wanting to build something like this is more professional. I've been working as an engineer on a supply chain solutions team. I'm often tasked with completing analyses of varying levels of complexity, and I'm often required to model entire supply chains. Being able to build a simulation with performance-optimized code, in a nicely packaged and concise way, will help enable me to do more in the future within the engineering space (pun intended).

## More

### [Orbital debris](https://www.nasa.gov/centers/hq/library/find/bibliographies/space_debris)

Low earth orbit (LEO) is an orbital space littered with space debris. There's estimated to be millions of pieces of debris orbiting the earth, with this number expected to climb at different rates in the future.

The danger that this space debris poses to launches and returns through earth's orbital space makes this an interesting problem to solve. In the future this issue will hold more relevance as the commercialization of the industry grows.

To solve this problem we can employ an ecosystem of technologies to measure and predict the potential for an orbital collision.

### Other orbital regions
In addition to LEO there are medium and high earth orbital regions as well. ```ForceField``` can provide the contextual data of each of these regions of space and educate users on traffic located here as well.

### Other near earth objects (NEO)
Nasa and other entities collect data about NEO and [share it with the public](https://cneos.jpl.nasa.gov/ca/). ```ForceField``` can tie this data into its interface for additional preventative measures.

### Making this program extensible
```ForceField``` is intended to become a contextual tool for initial and final space travel in the future through the use of modular extensions such as (but not limited to):

- [Nasa's Lunch Sites](https://www.nasa.gov/centers/kennedy/launchingrockets/sites.html)
- [OpenSky Flight Data](https://examples.pyviz.org/opensky/opensky.html)
- [OpenWeather Data](https://openweathermap.org/api)