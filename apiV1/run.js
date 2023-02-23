let {PythonShell} = require('python-shell');

const options = {
    scriptPath: '',
    args: ['arg1', 'arg2', 'arg3']
};

PythonShell.run('script.py', options, function (err, results) {
    if (err) throw err;
    console.log('results: %j', results);
});