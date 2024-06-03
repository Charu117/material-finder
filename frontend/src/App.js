import React, { useState } from 'react';
import ObjectList from './components/ObjectList';
import ObjectDetails from './components/ObjectDetails';
import './App.css';

function App() {
    const [selectedObject, setSelectedObject] = useState(null);

    return (
        <div className="App">
            <h1>Material Finder</h1>
            <div className="content">
                <ObjectList onSelect={setSelectedObject} />
                <ObjectDetails name={selectedObject} />
            </div>
        </div>
    );
}

export default App;