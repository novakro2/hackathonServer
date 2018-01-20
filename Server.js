var bodyParser =  require('body-parser'), //Grants access to incoming data
    express =     require('express'), //Module for creating server
    http =        require('http'),
    MongoClient = require('mongodb').MongoClient;

var exports = module.exports = {}; //Allows me to export functions to test file

var app = express(); //Server property
app.use(bodyParser.urlencoded({
	extended: true
}));
app.use(bodyParser.json()); //Converts incoming data into JSON


//----------------------------------------------------------------------------
// Connect to the MongoDB database
// This connection needs to contain the server declaration
// This allows us to pass the db variable to the controller and service
// ---------------------------------------------------------------------------
MongoClient.connect("mongodb://localhost:27017/hackathon"  /*process.env.MONGO_DB*/, function(err, db) {
  if(!err) {
    console.log("We are connected to MongoDB using database " + process.env.MONGO_DB);
    
    // Initialize the controller
    require('./Controller')(app, db);
    
    // Start Node Server
    var server = app.listen(process.env.PORT || 8081, function(req,res){
            console.log("Running Server on port " + (process.env.PORT || 8081) + "...");
    });
  } else {
    console.log("Error connecting to Mongo DB: " + process.env.MONGO_DB);
  }
});

