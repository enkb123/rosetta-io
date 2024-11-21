const express = require('express');
const axios = require('axios');
const path = require('path');
const { stat } = require('fs');
const app = express();
const cookieParser = require('cookie-parser');
const PORT = 8080;

app.use(express.static('public'));
app.set('view engine', 'ejs');
app.use(cookieParser());
var recStations = [];

app.get('/api/data', async (req, res) => {
    try {
        const response = await axios.get('https://septa.nich.workers.dev/stations'); 
        res.json(response.data);
    } catch (error) {
        res.status(500).send('Error:', error);
    }
});

app.get('/', (req, res) => {
    recStations = JSON.parse(req.cookies.recStations);
    res.render('home', {recStations});
});

app.get('/views/index', (req, res) => {
    res.render('index');
});


app.get('/views/showTrains', async function(req, res){
    if (recStations.length > 0){
        recStations = JSON.parse(req.cookies.recStations);
    }
    const departStation = req.query.dropdown1;
    const destStation = req.query.dropdown2;
    var recents = {'recDepart': departStation,'recDest': destStation};
    var indexTrack = 0;
    recStations.forEach( trip => {
        if(recents.recDepart == trip.recDepart && recents.recDest == trip.recDest){
            recStations.splice(indexTrack, 1);
        }
        indexTrack++;
    });
    recStations.unshift(recents);
    if(recStations.length > 5){
        recStations.pop();
    }
    var json_str = JSON.stringify(recStations);
    res.cookie('recStations', json_str);
    var departID = "";
    var destID = "";
    try {
        const response = await axios.get('https://septa.nich.workers.dev/stations'); 
        const stationInfo = response.data;
        stationInfo.forEach(item =>{
            if (item.name == departStation){
                departID = item.id;
            }
            if (item.name == destStation){
                destID = item.id;
            }
        });
    } catch (error) {
        res.status(500).send('Error:', error);
    }

    
    try {
        const apiUrl = 'https://septa.nich.workers.dev/nextToArrive?start_station_id=' + departID + '&end_station_id=' + destID + '&n=3';
        const response = await axios.get(apiUrl);
        const upcomingTrains = response.data;
        recStations = req.cookies.recStations;
        recStations = JSON.parse(recStations);
        res.render('showTrains', {upcomingTrains, departStation, destStation, recStations});
    }catch (error){
        res.status(500).send('Error:', error);
    }
    
    
});



app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
