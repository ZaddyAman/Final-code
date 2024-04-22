import React from 'react';
import './home.css'; 
import {useNavigate}  from 'react-router-dom';
import { Typewriter } from 'react-simple-typewriter'



function Home() {
    const navigate = useNavigate ();

  
    
     
    const handleStartClick = () => {
        navigate('/bmi'); // Navigate to the BMI route
      };



  return (
    
    <div className="home">
      <div className="title">
      <h1>Welcome to Your Diet Recommendation System</h1>
      <p>Learn how our system works and get started on your journey to better health.</p>
      </div>
      
      
      <button id='btn' onClick={handleStartClick}>Let's Start</button>
      <h1 style={{  paddingTop: '5rem', margin: 'auto 0', fontWeight: 'normal' }}>
         {' '}
        <span >
          {/* Style will be inherited from the parent element */}
          <Typewriter
            words={['Hii', ' Welcome to the NutriFit',]}
            loop={true}
            cursor
            cursorStyle='_'
            typeSpeed={70}
            deleteSpeed={50}
            delaySpeed={1000}
            
          />
        </span>
      </h1>




      
    </div>
      
    
  );
}

export default Home;
