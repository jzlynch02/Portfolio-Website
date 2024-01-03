import React from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faLinkedin, faGithub } from '@fortawesome/free-brands-svg-icons';
import './index.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>My Website</h1>
        <nav className="Navigation">
          <a href="#about">About</a>
          <a href="#experience">Experience</a>
          <a href="#projects">Projects</a>
          <a href="#contact">Contact</a>
        </nav>
      </header>
      <main className="App-main">
        <section id="about" className="About">
          <div className="Profile-image">
          </div>
          <div className="About-content">
            <h2>Hello, I'm</h2>
            <h1>Joseph Lynch</h1>
            <div className="Buttons">
              <button>Download CV</button>
              <button>Contact Info</button>
            </div>
            <div className="Social-icons">
              <FontAwesomeIcon icon={faLinkedin} />
              <FontAwesomeIcon icon={faGithub} />
            </div>
          </div>
        </section>
        {/* Add other sections (Experience, Projects, Contact) */}
      </main>
    </div>
  );
}

export default App;