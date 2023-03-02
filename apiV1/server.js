const express = require('express');
const bodyParser = require('body-parser');
const path = require('path');

// afficher une page html avec express qui affiche une page html : "accueil.html"
// en localhost:3000 avec un fichier env sans besoin de connexion

const app = express();
const port = process.env.PORT || 3000;

// ---
// Définir un dossier "public" pour les fichiers statiques
app.use(express.static('public'));

app.get('/image', (req, res) => {
    res.sendFile(__dirname + '/public/images/image.png');
});
// ---

app.use(bodyParser.json({limit: '50mb'}));
app.use(bodyParser.urlencoded({limit: '50mb', extended: true}));

app.use(express.static('public'));

app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'views', 'home.html'));
});

app.listen(port, () => {
    console.log(`Example app listening at http://localhost:${port}`)
});



// let {PythonShell} = require('python-shell');
//
// const options = {
//     scriptPath: '',
//     args: ['arg1', 'arg2', 'arg3']
// };
//
// PythonShell.run('script.py', options, function (err, results) {
//     if (err) throw err;
//     console.log('results: %j', results);
// });


//EN BINAIRE
// let {PythonShell} = require('python-shell');
// const fs = require('fs');
//
// const options = {
//     scriptPath: '',
//     args: ['arg1', 'arg2', 'arg3']
// };
//
// PythonShell.run('script.py', options, function (err) {
//     if (err) throw err;
//     fs.readFile('image.png', (err, data) => {
//         if (err) throw err;
//         console.log(data);
//     });
// });

// !openssl enc -base64 -d -in 'ratio.bmp' -out 'zebi.bmp'


// EN BASE 64
let {PythonShell} = require('python-shell');
const fs = require('fs');

const options = {
    scriptPath: '',
    args: ['arg1', 'arg2', 'arg3']
};

PythonShell.run('script.py', options, function (err) {
    if (err) throw err;
    fs.readFile('image.png', (err, data) => {
        if (err) throw err;
        const base64Image = new Buffer.from(data, 'binary').toString('base64');
        const imgSrc = `data:image/png;base64,${base64Image}`;
        console.log(imgSrc);
    });
});

// télécharger des datasets en csv depuis opendaatsoft sans axios des accidents corporels de la circulation millésimé:


const https = require('https');

const file = fs.createWriteStream("./data/accidents.csv");
const request = https.get("https://public.opendatasoft.com/api/explore/v2.1/catalog/datasets/accidents-corporels-de-la-circulation-millesime/exports/csv?lang=fr&timezone=Europe%2FBerlin&use_labels=true&csv_separator=%3B", function(response) {
    response.pipe(file);
});