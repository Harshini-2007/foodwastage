const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');

const app = express();
const port = 3000;

// Middleware to parse JSON request bodies
app.use(bodyParser.json());

// Middleware to enable Cross-Origin Resource Sharing (for development)
app.use(cors());

// In-memory array to store food data (WILL BE LOST ON SERVER RESTART)
let availableFood = [];

// Endpoint to handle form submissions
app.post('/api/submit-food', (req, res) => {
    const foodData = req.body;
    foodData.timestamp = new Date().toLocaleString();
    availableFood.push(foodData);
    console.log('Received food submission:', foodData);
    res.sendStatus(200); // Send a success response
});

// Endpoint to get all available food data
app.get('/api/available-food', (req, res) => {
    res.json(availableFood);
});

app.listen(port, () => {
    console.log(`Server listening on port ${port}`);
});