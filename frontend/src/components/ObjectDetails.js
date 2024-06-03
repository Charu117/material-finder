import React, { useEffect, useState } from 'react';
import axios from 'axios';

function ObjectDetails({ name }) {
    const [objectDetails, setObjectDetails] = useState(null);

    useEffect(() => {
        if (name) {
            axios.get(`http://localhost:5000/objects/${name}`)
                .then(response => setObjectDetails(response.data))
                .catch(error => console.error('Error fetching object details:', error));
        }
    }, [name]);

    if (!objectDetails) {
        return <div>Select an object to see details</div>;
    }

    return (
        <div>
            <h2>{objectDetails.name}</h2>
            <p>Minimum Transparency: {objectDetails.min_transparency}</p>
            <p>Maximum Density: {objectDetails.max_density}</p>
            <p>Minimum Stiffness: {objectDetails.min_stiffness}</p>
            <h3>Suitable Materials</h3>
            <ul>
                {objectDetails.suitable_materials.map(material => (
                    <li key={material.id}>{material.name}</li>
                ))}
            </ul>
        </div>
    );
}

export default ObjectDetails;