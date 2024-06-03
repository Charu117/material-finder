import React, { useEffect, useState } from 'react';
import axios from 'axios';

function ObjectList({ onSelect }) {
    const [objects, setObjects] = useState([]);

    useEffect(() => {
        axios.get('http://localhost:5000/objects')
            .then(response => setObjects(response.data))
            .catch(error => console.error('Error fetching objects:', error));
    }, []);

    return (
        <div>
            <h2>Objects</h2>
            <ul>
                {objects.map(obj => (
                    <li key={obj.id} onClick={() => onSelect(obj.name)}>
                        {obj.name}
                    </li>
                ))}
            </ul>
        </div>
    );
}

export default ObjectList;
