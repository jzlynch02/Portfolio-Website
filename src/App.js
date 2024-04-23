import React from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faLinkedin, faGithub } from '@fortawesome/free-brands-svg-icons';
import './index.css';
//npm run deploy
function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>My Website</h1>
        <nav className="Navigation">
          <a href="#about">About</a>
          <a href="#experience">Experience</a>
          <a href="#projects">Projects</a>
         {/* <a href="#contact">Contact</a>*/}
        </nav>
      </header>
      <main className="App-main">
        <section id="about" className="About">
          <div className="Profile-image">
            {/* profile image here */}
          </div>
          <div className="About-content">
            <h2>Hello, I'm</h2>
            <h1>Joseph Lynch</h1>
            <div className="Social-icons">
              <a href="https://www.linkedin.com/in/joseph---lynch/" target="_blank" rel="noopener noreferrer" className="linkedin-icon">
                <FontAwesomeIcon icon={faLinkedin} />
              </a>

              <a href="https://github.com/jzlynch02" target="_blank" rel="noopener noreferrer" className="github-icon">
                <FontAwesomeIcon icon={faGithub} />
              </a>
            </div>
            <div className="Buttons">
            <a href={`${process.env.PUBLIC_URL}/Resume.pdf`}
            download="Resume_Joseph_Lynch.pdf">
              <button>Download Resume</button>
            </a>
              {/*<button>Contact Info</button>*/}
            </div>
          </div>
        </section>
        <section id="projects" className="Projects">
          <h2>Projects</h2>
          <div className="Project-item">
            <h3><a href="https://github.com/shayanus/Full-Stack-Online-Travel-Reservation-System/tree/main" target="blank">Full-Stack Online Travel Reservation System</a></h3>
            <p>Spearheaded a full-stack development of an online travel reservation system, employing HTML for front-end, MySQL for database management, and Java with JDBC for server-side operations. Focused on creating a user-friendly interface and robust back-end architecture, ensuring a seamless end-to-end user experience for flight searches and reservations. Collaborated in a two-person team, leveraging Git for effective version control and project coordination, demonstrating strong teamwork in a full-stack software development environment.</p>
          </div>
          <div className="Project-item">
            <h3><a href="https://jzlynch02.github.io/Weather-App/" target="blank">Weather App</a></h3>
            <p>Engineered an interactive web application using React, Axios, and CSS, providing real-time weather updates from the OpenWeatherMap API. Implemented a user-centric design with responsive CSS, ensuring a seamless experience across various devices and browsers. Focused on user interaction and accessibility, enabling users to search for and view weather conditions of different locations effectively, on several devices and browsers.</p>
          </div>
          <div className="Project-item">
            <h3><a href="https://jzlynch02.github.io/To-do-List/" target="blank">To-do List</a></h3>
            <p>Developed a user-friendly To-Do List web application using HTML, CSS, and JavaScript, hosted on GitHub Pages. Implemented core functionalities, enabling users to add, remove, and edit tasks, enhancing personal productivity and task management.</p>
          </div>
        </section>
      </main>
      <footer className="footer">
        <h3>
          Made with React.js and CSS.
        </h3>
      </footer>
    </div>
  );
}

export default App;






