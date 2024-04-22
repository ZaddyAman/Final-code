import React from "react";

function Remedy(props) {
 
  const dietRecommendations = props.response?.diet_recommendations || []; // Access from response

console.log(props);
  return (
    <div>
      <h2>Remedy Page</h2>
      <p>Response from Input: {dietRecommendations}</p>
    </div>
  );
}

export default Remedy;
