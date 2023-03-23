const controller = require('../controllers/controller.js');

module.exports = function(app){
    app.get('/home', controller.home);
    app.get('/heatmap', controller.heatmap);
    app.get('/heatmapshow', controller.heatmapshow);
    app.get('/rien', controller.rien);
    app.get('/vbar-stack-nb-usagers-par-blessure-et-categorie', controller.vbarStackNbUsagersParBlessureEtCategorie);
}