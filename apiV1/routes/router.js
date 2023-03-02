const controller = require('../controllers/controller.js');

module.exports = function(app){
    app.get('/home', controller.home);
    app.get('/swagger', controller.swagger);
}