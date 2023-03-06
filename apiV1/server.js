const express = require('express');
const bodyParser = require('body-parser');
const path = require('path');

// afficher une page html avec express qui affiche une page html : "accueil.html"
// en localhost:3000 avec un fichier env sans besoin de connexion

const app = express();
const port = process.env.PORT || 3000;

app.use(bodyParser.json({limit: '50mb'}));
app.use(bodyParser.urlencoded({limit: '50mb', extended: true}));

app.use(express.static('public'));

// ROUTES
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'views', 'home.html'));
});
app.get('/swagger', (req, res) => {
    res.sendFile(path.join(__dirname, 'views', 'swagger.html'));
});
// PORT
app.listen(port, () => {
    console.log(`Example app listening at http://localhost:${port}`)
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
        console.log(imgSrc);
    });
});

// deuxieme script au cas ou
// PythonShell.run('script2.py', options, function (err) {
//     if (err) throw err;
//     fs.readFile('./public/images/image2.png', (err, data) => {
//         if (err) throw err;
//         const base64Image = Buffer.from(data, 'binary').toString('base64');
//         const imgSrc = `data:image/png;base64,${base64Image}`;
//         console.log(imgSrc);
//     });
// });

// télécharger des datasets en csv depuis opendaatsoft sans axios des accidents corporels de la circulation millésimé:

const https = require('https');
// A FAIRE : DL AUTO (MAUVAIS LIENS)

// const filecaracteristiques2021 = fs.createWriteStream("./data/accidents2.csv");
// const request1 = https.get("https://static.data.gouv.fr/resources/bases-de-donnees-annuelles-des-accidents-corporels-de-la-circulation-routiere-annees-de-2005-a-2020/20221024-114007/usagers-2021.csv", function(response) {
//     response.pipe(filecaracteristiques2021);
// });
// const filelieux2021 = fs.createWriteStream("./data/accidents2.csv");
// const request2 = https.get("https://static.data.gouv.fr/resources/bases-de-donnees-annuelles-des-accidents-corporels-de-la-circulation-routiere-annees-de-2005-a-2020/20221024-114007/usagers-2021.csv", function(response) {
//     response.pipe(filelieux2021);
// });
// const fileusagers2021 = fs.createWriteStream("./data/accidents2.csv");
// const request3 = https.get("https://static.data.gouv.fr/resources/bases-de-donnees-annuelles-des-accidents-corporels-de-la-circulation-routiere-annees-de-2005-a-2020/20221024-114007/usagers-2021.csv", function(response) {
//     response.pipe(fileusagers2021);
// });
// const filevehicules2021 = fs.createWriteStream("./data/accidents2.csv");
// const request4 = https.get("https://static.data.gouv.fr/resources/bases-de-donnees-annuelles-des-accidents-corporels-de-la-circulation-routiere-annees-de-2005-a-2020/20221024-114007/usagers-2021.csv", function(response) {
//     response.pipe(filevehicules2021);
// });