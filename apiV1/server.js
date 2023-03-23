const express = require('express');
const bodyParser = require('body-parser');
const path = require('path');
const https = require('https');
const {PythonShell} = require('python-shell');
const fs = require('fs');

const app = express();
const port = process.env.PORT || 3000;

app.listen(port, () => {
    console.log(`Example app listening at http://localhost:${port}`)
});

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
app.get('/vbar-stack-nb-usagers-par-blessure-et-categorie', (req, res) => {
    res.sendFile(path.join(__dirname, 'views', 'nb_usagers_par_blessure_et_categorie.html'));
});
app.get('/3d-nb-accidents-heures-mois', (req, res) => {
    res.sendFile(path.join(__dirname, 'views', '3d_nb_accidents_heures_mois.html'));
});


// Télécharger des datasets en csv depuis data.gouv "Bases de données annuelles des accidents corporels de la circulation routière"

const downloadFile = (url, filePath) => {
    return new Promise((resolve, reject) => {
        const fileStream = fs.createWriteStream(filePath);
        https.get(url, function(response) {
            response.pipe(fileStream);
            fileStream.on('finish', function() {
                fileStream.close(() => {
                    resolve();
                });
            });
        }).on('error', function(err) {
            fs.unlink(filePath);
            reject(err);
        });
    });
};

const downloadAllFiles = async () => {
    try {
        console.log('Les données sont en cours de téléchargement...');
        await Promise.all([
            // 2021
            downloadFile('https://static.data.gouv.fr/resources/bases-de-donnees-annuelles-des-accidents-corporels-de-la-circulation-routiere-annees-de-2005-a-2020/20221024-113743/carcteristiques-2021.csv', './data/2021/caracteristiques-2021.csv'),
            downloadFile('https://static.data.gouv.fr/resources/bases-de-donnees-annuelles-des-accidents-corporels-de-la-circulation-routiere-annees-de-2005-a-2020/20221024-113901/lieux-2021.csv', './data/2021/lieux-2021.csv'),
            downloadFile('https://static.data.gouv.fr/resources/bases-de-donnees-annuelles-des-accidents-corporels-de-la-circulation-routiere-annees-de-2005-a-2020/20221024-114007/usagers-2021.csv', './data/2021/usagers-2021.csv'),
            downloadFile('https://static.data.gouv.fr/resources/bases-de-donnees-annuelles-des-accidents-corporels-de-la-circulation-routiere-annees-de-2005-a-2020/20221024-113925/vehicules-2021.csv', './data/2021/vehicules-2021.csv'),

            // 2020
            downloadFile('https://static.data.gouv.fr/resources/bases-de-donnees-annuelles-des-accidents-corporels-de-la-circulation-routiere-annees-de-2005-a-2019/20211110-111202/caracteristiques-2020.csv', './data/2020/caracteristiques-2020.csv'),
            downloadFile('https://static.data.gouv.fr/resources/bases-de-donnees-annuelles-des-accidents-corporels-de-la-circulation-routiere-annees-de-2005-a-2019/20211110-111603/lieux-2020.csv', './data/2020/lieux-2020.csv'),
            downloadFile('https://static.data.gouv.fr/resources/bases-de-donnees-annuelles-des-accidents-corporels-de-la-circulation-routiere-annees-de-2005-a-2019/20211110-111817/usagers-2020.csv', './data/2020/usagers-2020.csv'),
            downloadFile('https://static.data.gouv.fr/resources/bases-de-donnees-annuelles-des-accidents-corporels-de-la-circulation-routiere-annees-de-2005-a-2019/20211110-111722/vehicules-2020.csv', './data/2020/vehicules-2020.csv'),

            // 2019
            downloadFile('https://static.data.gouv.fr/resources/base-de-donnees-accidents-corporels-de-la-circulation/20201105-104400/caracteristiques-2019.csv', './data/2019/caracteristiques-2019.csv'),
            downloadFile('https://static.data.gouv.fr/resources/base-de-donnees-accidents-corporels-de-la-circulation/20201105-104338/lieux-2019.csv', './data/2019/lieux-2019.csv'),
            downloadFile('https://static.data.gouv.fr/resources/base-de-donnees-accidents-corporels-de-la-circulation/20201105-104232/usagers-2019.csv', './data/2019/usagers-2019.csv'),
            downloadFile('https://static.data.gouv.fr/resources/base-de-donnees-accidents-corporels-de-la-circulation/20201105-104310/vehicules-2019.csv', './data/2019/vehicules-2019.csv'),
        ]);
        console.log('Tous les téléchargements sont terminés.');



        // EN BASE 64
        // scripts python qui génèrent les graphiques
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

        // Nombre d'usagers pour chaque type de blessure et catégorie d'usager
        PythonShell.run('script_nb_usagers_par_blessure_et_categorie.py', options, function (err) {
            if (err) throw err;
            fs.readFile('./public/images/image.png', (err, data) => {
                if (err) throw err;
                const base64Image = Buffer.from(data, 'binary').toString('base64');
                const imgSrc = `data:image/png;base64,${base64Image}`;
                // console.log(imgSrc);
            });
        });



    } catch (err) {
        console.error('Erreur lors du téléchargement des fichiers:', err);
    }
};

downloadAllFiles();