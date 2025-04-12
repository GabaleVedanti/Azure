// Node.js Express Example
const express = require("express");
const axios = require("axios");
const app = express();

app.get("/weather", async (req, res) => {
  const city = req.query.city || "Pune";
  const apiKey = "YOUR_API_KEY";
  const url = `https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${apiKey}`;
  
  try {
    const response = await axios.get(url);
    res.json(response.data);
  } catch (err) {
    res.status(500).send("Error fetching data");
  }
});

app.listen(process.env.PORT || 3000);
