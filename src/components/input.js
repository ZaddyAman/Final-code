import React, { useState } from "react";

import './input.css'; 






function Input() {

 
  
  
  
  

  // Define the attributes array with attribute names and ranges
  const attributes = [
    {
      name: "albumin",
      unit: "mg/dL",
      malerange: "40 and above",
      femalerange: "50 and above",
      defaultValue: -1, // Default value for empty input
    },  
    {
      name: "  alanine",
      unit: "mg/dL",
      malerange: "100 and below",
      femalerange: "100 and below",
      defaultValue: -1, // Default value for empty input
    },
    {
      name: "ast",
      unit: "mg/L",
      malerange: "3 and below",
      femalerange: "3 and below",
      defaultValue: -1, // Default value for empty input
    },
    {
      name: "phosphotase",
      unit: "mmol/L",
      malerange: "135 to 145",
      femalerange: "135 to 145",
      defaultValue: -1, // Default value for empty input
    },
    {
      name: " nitrogen",
      unit: "mmol/L",
      malerange: "3.5 to 5",
      femalerange: "3.5 to 5",
      defaultValue: -1, // Default value for empty input
    },
    {
      name: "calcium",
      unit: "mmol/L",
      malerange: "2.3 to 2.6",
      femalerange: "2.3 to 2.6",
      defaultValue: -1, // Default value for empty input
    },
    {
      name: "cholesterol",
      unit: "mmol/L",
      malerange: "0.65 to 1.05",
      femalerange: "0.65 to 10.5",
      defaultValue: -1, // Default value for empty input
    },
    {
      name: "bicarbonate",
      unit: "g/dL",
      malerange: "3.5 to 5",
      femalerange: "3.5 to 5",
      defaultValue: -1, // Default value for empty input
    },
    {
      name: "iron",
      unit: "g/dL",
      malerange: "0.3 to 1",
      femalerange: "0.3 to 1",
      defaultValue: -1, // Default value for empty input
    },
    {
      name: "phosphorus",
      unit: "IU/L",
      malerange: "10 to 55",
      femalerange: "7 to 30",
      defaultValue: -1, // Default value for empty input
    },
    {
      name: "bilirubin ",
      unit: "IU/L",
      malerange: "10 to 40",
      femalerange: "9 to 25",
      defaultValue: -1, // Default value for empty input
    },
    {
      name: "protein",
      unit: "mg/dL",
      malerange: "0.6 to 1.2",
      femalerange: "0.5 to 1.1",
      defaultValue: -1, // Default value for empty input
    },
    {
      name: "Creatinine ",
      unit: "mg/dL",
      malerange: "8 to 24",
      femalerange: "6 to 21",
      defaultValue: -1, // Default value for empty input
    },
    {
      name: "sodium",
      unit: "Units/L",
      malerange: "25 to 130",
      femalerange: "25 to 130",
      defaultValue: -1, // Default value for empty input
    },
    {
      name: "pottasium",
      unit: "Units/L",
      malerange: "0 to 160",
      femalerange: "0 to 160",
      defaultValue: -1, // Default value for empty input
    },
    {
      name: "chloride",
      unit: "mg/dL",
      malerange: "117 and below",
      femalerange: "117 and below",
      defaultValue: -1, // Default value for empty input
    },
    {
      name: "globulin",
      unit: "mIU/L",
      malerange: "0.4 to 4",
      femalerange: "0.4 to 4",
      defaultValue: -1, // Default value for empty input
    },
    {
      name: "glucose",
      unit: "μg/dL",
      malerange: "4.5 to 12",
      femalerange: "4.5 to 12",
      defaultValue: -1, // Default value for empty input
    },
    
    // Add more attributes as needed
  ];

  const [inputData, setInputData] = useState(
    attributes.map(() => -1) // Initialize inputData with -1 for all attributes
  );
  const [gender, setGender] = useState("male"); // Default to 'male', you can also set it based on user input
  const [result, setResult] = useState("");

  // Function to handle gender selection
  const handleGenderChange = (e) => {
    setGender(e.target.value);
  };

  // Function to handle input changes
  const handleInputChange = (index, value) => {
    const updatedData = [...inputData];
    updatedData[index] = value;
    setInputData(updatedData);
  };

  // Function to prepare data for sending to backend
  const prepareData = () => {
    const data = {
      gender: gender === "male" ? 1 : -1, // Pass 1 for male, -1 for female
      attributes: inputData, // Send the entire inputData array (including -1 for missing values)
    };
    return data;
  };

  // Function to handle form submission (replace with your actual submission logic)
  const handleSubmit = async () => {
    const data = prepareData();
  
    // Replace with your actual backend URL (adjust the port if needed)
    const url = 'http://localhost:5000/submit';
  
    try {
      const response = await fetch(url, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data),
      });
  
      if (!response.ok) {
        throw new Error(`Error: ${response.status}`);
      }
  
      const responseData = await response.json();
      console.log('Backend response:', responseData); // For debugging
      setResult(responseData); // Update UI with response message
    
    } catch (error) {
      console.error('Error submitting data:', error);
      setResult('Error submitting data. Please try again.'); // Update UI with error message
    }
  };

   // Function to handle downloading recommendations
// Function to handle downloading recommendations
const downloadRecommendations = () => {
  const recommendationsElement = document.querySelector("#recommendations .recommendations");
  if (recommendationsElement) {
    let fileContent = "Diet Recommendations:\n\n";
    const attributeSections = recommendationsElement.querySelectorAll(".attribute-section");
    attributeSections.forEach((section, index) => {
      const attributeName = section.querySelector("h3").innerText.trim();
      const recommendationElement = section.querySelector("ul");
      if (recommendationElement) {
        const recommendations = Array.from(recommendationElement.querySelectorAll("li"))
          .map(li => li.innerText.trim())
          .reduce((acc, curr) => {
            const [category, foods] = curr.split(':');
            if (acc[category]) {
              acc[category].push(foods);
            } else {
              acc[category] = [foods];
            }
            return acc;
          }, {});

        fileContent += `${index + 1}. ${attributeName}\n`;
        for (const category in recommendations) {
          fileContent += `${category}: ${recommendations[category].join(', ')}\n`;
        }
        fileContent += "\n";
      } else {
        const recommendation = section.querySelector("p").innerText.trim();
        fileContent += `${index + 1}. ${attributeName}: ${recommendation}\n\n`;
      }
    });

    const element = document.createElement("a");
    const file = new Blob([fileContent], { type: 'text/plain' });
    element.href = URL.createObjectURL(file);
    element.download = "diet_recommendations.txt";
    document.body.appendChild(element); // Required for this to work in Firefox
    element.click();
  } else {
    console.error("Element with id 'recommendations .recommendations' not found.");
  }
};


   



  
  
  return (
    <div className="input-container">
      <div className="input">
      <h2>Input Page</h2>
      <div className="buttongrp">
      <button onClick={() => setGender("male")} class="btn btn-border-pop">Male</button>
      <button  onClick={() => setGender("female")} class="btn btn-border-pop">Female</button>
      
      
      </div>
      
      <table className="input-table">
        <thead>
          <tr>
            <th>Attribute</th>
            <th>Input</th>
            <th>Range</th>
          </tr>
        </thead>
        <tbody>
          {/* Loop through your attributes and create rows */}
          {attributes.map((attribute, index) => (
            <tr key={index}>
              <td>{attribute.name}</td>
              <td>
                <input
                  type="number"
                  value={inputData[index] || ""}
                  onChange={(e) => handleInputChange(index, e.target.value)}
                />
              </td>
              <td>
                {gender === "male"
                  ? `${attribute.malerange} (${attribute.unit})`
                  : gender === "female"
                  ? `${attribute.femalerange} (${attribute.unit})`
                  : `${attribute.childrange} (${attribute.unit})`}
              </td>
            </tr>
          ))}
        </tbody>
      </table>
      <button onClick={handleSubmit}>Submit</button>

      

      <div>
      
      {result.diet_recommendations && (
  <div id="recommendations" className="pdf-content">
    <div className="recommendations">
      <div className="recommendations">
        <h2>Diet Recommendations</h2>
        {result.diet_recommendations.map((recommendation) => (
          <div className="attribute-section" key={recommendation.attribute}>
            <h3>{recommendation.attribute}</h3>
            {recommendation.recommendations === 'Medication required' ? (
    <p>Medication required for {recommendation.attribute}.</p>
) : recommendation.recommendations === 'No input provided' ? (
    <p>No input provided for {recommendation.attribute}.</p>
) : (
              <>
                {Object.keys(recommendation.recommendations).length > 0 ? (
                  <ul>
                    {['veg', 'non-veg', 'fruits'].map((category) => (
                      <li key={category}>
                        <b>{category}:</b>
                        {recommendation.recommendations[category] && (
                          <span>
                            {recommendation.recommendations[category].join(', ')}
                          </span>
                        )}
                      </li>
                    ))}
                  </ul>
                ) : (
                  <p>
                    
                     { `You are healthy for ${recommendation.attribute}.`}
                    
                    
                  </p>
                )}
              </>
            )}
          </div>
        ))}
      </div>
    </div>
  </div>
)}
      <button onClick={downloadRecommendations}>Download Recommendations</button>
      
      </div>  
        
    </div>
    
    </div>
    
  );
}

export default Input;
