const express = require('express');
const bodyParser = require('body-parser');
const path = require('path');
const https = require('https');

const app = express();
const port = process.env.PORT || 3000;

app.use(bodyParser.json({limit: '50mb'}));
app.use(bodyParser.urlencoded({limit: '50mb', extended: true}));
app.use(express.static('public'));

// ROUTES
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'views', 'home.html'));
});
app.get('/heatmap', (req, res) => {
    res.sendFile(path.join(__dirname, 'views', 'heatmap.html'));
});
app.get('/heatmapshow', (req, res) => {
    res.sendFile(path.join(__dirname, 'views', 'heatmapshow.html'));
});
app.get('/rien', (req, res) => {
    res.sendFile(path.join(__dirname, 'views', 'rien.html'));
});

// EN BASE 64
const {PythonShell} = require('python-shell');
const fs = require('fs');

const options = {
    scriptPath: '',
    args: ['arg1', 'arg2', 'arg3']
};
PythonShell.run('script.py', options, function (err) {
    if (err) throw err;
    fs.readFile('./public/images/image.png', (err, data) => {
        if (err) throw err;
        const base64Image = Buffer.from(data, 'binary').toString('base64');
        const imgSrc = `data:image/png;base64,${base64Image}`;
        // console.log(imgSrc);
    });
});

// Nombre d'accidents par mois de l'année
PythonShell.run('script_accident_par_mois_par_annee.py', options, function (err) {
    if (err) throw err;
    fs.readFile('./public/images/image.png', (err, data) => {
        if (err) throw err;
        const base64Image = Buffer.from(data, 'binary').toString('base64');
        const imgSrc = `data:image/png;base64,${base64Image}`;
        // console.log(imgSrc);
    });
});



// Télécharger des datasets en csv depuis data.gouv "Bases de données annuelles des accidents corporels de la circulation routière"

// 2021
const filecaracteristiques2021 = fs.createWriteStream("./data/2021/caracteristiques-2021.csv");
const request1 = https.get("https://static.data.gouv.fr/resources/bases-de-donnees-annuelles-des-accidents-corporels-de-la-circulation-routiere-annees-de-2005-a-2020/20221024-113743/carcteristiques-2021.csv", function(response) {
    response.pipe(filecaracteristiques2021);
});
const filelieux2021 = fs.createWriteStream("./data/2021/lieux-2021.csv");
const request2 = https.get("https://static.data.gouv.fr/resources/bases-de-donnees-annuelles-des-accidents-corporels-de-la-circulation-routiere-annees-de-2005-a-2020/20221024-113901/lieux-2021.csv", function(response) {
    response.pipe(filelieux2021);
});
const fileusagers2021 = fs.createWriteStream("./data/2021/usagers-2021.csv");
const request3 = https.get("https://static.data.gouv.fr/resources/bases-de-donnees-annuelles-des-accidents-corporels-de-la-circulation-routiere-annees-de-2005-a-2020/20221024-114007/usagers-2021.csv", function(response) {
    response.pipe(fileusagers2021);
});
const filevehicules2021 = fs.createWriteStream("./data/2021/vehicules-2021.csv");
const request4 = https.get("https://static.data.gouv.fr/resources/bases-de-donnees-annuelles-des-accidents-corporels-de-la-circulation-routiere-annees-de-2005-a-2020/20221024-113925/vehicules-2021.csv", function(response) {
    response.pipe(filevehicules2021);
});

// 2020
const filecaracteristiques2020 = fs.createWriteStream("./data/2020/caracteristiques-2020.csv");
const request5 = https.get("https://static.data.gouv.fr/resources/bases-de-donnees-annuelles-des-accidents-corporels-de-la-circulation-routiere-annees-de-2005-a-2019/20211110-111202/caracteristiques-2020.csv", function(response) {
    response.pipe(filecaracteristiques2020);
});
const filelieux2020 = fs.createWriteStream("./data/2020/lieux-2020.csv");
const request6 = https.get("https://static.data.gouv.fr/resources/bases-de-donnees-annuelles-des-accidents-corporels-de-la-circulation-routiere-annees-de-2005-a-2019/20211110-111603/lieux-2020.csv", function(response) {
    response.pipe(filelieux2020);
});
const fileusagers2020 = fs.createWriteStream("./data/2020/usagers-2020.csv");
const request7 = https.get("https://static.data.gouv.fr/resources/bases-de-donnees-annuelles-des-accidents-corporels-de-la-circulation-routiere-annees-de-2005-a-2019/20211110-111817/usagers-2020.csv", function(response) {
    response.pipe(fileusagers2020);
});
const filevehicules2020 = fs.createWriteStream("./data/2020/vehicules-2020.csv");
const request8 = https.get("https://static.data.gouv.fr/resources/bases-de-donnees-annuelles-des-accidents-corporels-de-la-circulation-routiere-annees-de-2005-a-2019/20211110-111722/vehicules-2020.csv", function(response) {
    response.pipe(filevehicules2020);
});

// 2019
const filecaracteristiques2019 = fs.createWriteStream("./data/2019/caracteristiques-2019.csv");
const request9 = https.get("https://static.data.gouv.fr/resources/base-de-donnees-accidents-corporels-de-la-circulation/20201105-104400/caracteristiques-2019.csv", function(response) {
    response.pipe(filecaracteristiques2019);
});
const filelieux2019 = fs.createWriteStream("./data/2019/lieux-2019.csv");
const request10 = https.get("https://static.data.gouv.fr/resources/base-de-donnees-accidents-corporels-de-la-circulation/20201105-104338/lieux-2019.csv", function(response) {
    response.pipe(filelieux2019);
});
const fileusagers2019 = fs.createWriteStream("./data/2019/usagers-2019.csv");
const request11 = https.get("https://static.data.gouv.fr/resources/base-de-donnees-accidents-corporels-de-la-circulation/20201105-104232/usagers-2019.csv", function(response) {
    response.pipe(fileusagers2019);
});
const filevehicules2019 = fs.createWriteStream("./data/2019/vehicules-2019.csv");
const request12 = https.get("https://static.data.gouv.fr/resources/base-de-donnees-accidents-corporels-de-la-circulation/20201105-104310/vehicules-2019.csv", function(response) {
    response.pipe(filevehicules2019);
});

app.listen(port, () => {
    console.log(`Example app listening at http://localhost:${port}`)
});