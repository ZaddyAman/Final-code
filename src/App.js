// App.js
import React from 'react';

import { BrowserRouter as Router, Route, Routes ,Link } from 'react-router-dom';


import Home from './components/home';
import BMI from './components/bmi';
import Inputs from './components/input';




// Import the logo GIFs for each navigation item
import homeLogo from './img/home.gif';
import bmiLogo from './img/calculator.gif';
import inputsLogo from './img/dna.gif';


// Custom NavItem component that accepts a logo prop
function NavItem({ to, children, logo }) {

  const iconSize = "32px"; // Adjust the icon size as needed
  
  const navItemStyle = {
    display: "flex",
    alignItems: "center",
    textDecoration: "none",
    color: "inherit",
    
  };

  const logoStyle = {
    width: iconSize, // Set the width of the icon
    height: iconSize, // Set the height of the icon
    marginRight: "8px", // Adjust the spacing between the icon and text
    
  };

  

  return (
    <li>
      <Link to={to} style={navItemStyle}>
        <img src={logo} alt="Logo" style={logoStyle} />
        {children}
      </Link>
    </li>
  );
}

function App() {
  return (
    <Router>
      <nav className="nav">
        <ul>
          <NavItem to="/" logo={homeLogo}>
            Home
          </NavItem>
          <NavItem to="/bmi" logo={bmiLogo}>
            BMI
          </NavItem>
          <NavItem to="/inputs" logo={inputsLogo}>
            Inputs & Remedy 
          </NavItem>
          
        </ul>
      </nav>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/bmi" element={<BMI />} />
        <Route path="/inputs" element={<Inputs />} />
        
      </Routes>
    </Router>
  );
}

export default App;
