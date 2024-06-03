# Material Finder

## Overview
Material Finder is a full-stack application that allows users to find suitable materials for different objects based on specified properties such as transparency, density, and stiffness. The application consists of a backend implemented with Flask and a frontend built with React.

## Features
- Backend API to manage materials and objects
- Retrieve materials that satisfy certain parameters
- Frontend GUI to interact with the backend
- List of objects and their material requirements
- Display suitable materials for a selected object

## Technologies Used
- Backend: Flask, PyMySQL
- Frontend: React, Axios
- Database: MySQL
- Other: MAMP for local MySQL server management

## Setup and Installation

### Prerequisites
- Python 3.x
- Node.js and npm
- MAMP (or any local MySQL server)

### Backend Setup
1. Create a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

2. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Configure the database:
    Ensure MAMP is running and MySQL server is started. Update `app.py` with your database credentials if necessary.

4. Initialize the database:
    ```bash
    python3 run.py
    ```

### Frontend Setup
1. Navigate to the frontend directory:
    ```bash
    cd ../frontend
    ```

2. Install the dependencies:
    ```bash
    npm install
    ```

3. Start the React development server:
    ```bash
    npm start
    ```

### Database Initialization
Populate the database:

Use a MySQL client or command-line tool to insert the provided data into the Materials and Objects tables.

```sql
INSERT INTO Materials (name, transparency, density, stiffness) VALUES
('Wood', 0.10, 0.60, 1.00),
('Metal', 0.00, 7.80, 8.00),
('Plastic', 0.50, 0.95, 0.80),
('Glass', 0.90, 2.50, 5.00),
('Ceramic', 0.00, 2.20, 7.00),
('Rubber', 0.05, 1.20, 0.50),
('Concrete', 0.00, 2.40, 6.00),
('Fiber', 0.60, 1.00, 3.00),
('Carbon Fiber', 0.00, 1.60, 7.50),
('Steel', 0.00, 7.85, 9.00);

INSERT INTO Objects (name, min_transparency, max_density, min_stiffness) VALUES
('Chair', 0.00, 2.00, 1.00),
('Window', 0.70, 3.00, 3.00),
('Bottle', 0.00, 1.50, 1.00),
('Table', 0.00, 2.50, 5.00),
('Helmet', 0.00, 2.00, 6.00);



API Endpoints
GET /api/objects: Retrieve the list of all objects' names.
GET /api/objects/<name>: Retrieve the properties required by an object, given its name.
GET /api/materials: Retrieve the list of materials that satisfy the given parameters.

material_finder/
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── models.py
│   │   ├── routes.py
│   ├── config.py
│   ├── run.py
│   └── requirements.txt
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   │   ├── ObjectList.js
│   │   │   ├── ObjectDetails.js
│   │   ├── App.js
│   │   ├── index.js
│   │   └── App.css
│   ├── package.json
│   └── package-lock.json
├── README.md
└── .gitignore
