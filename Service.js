


/** 
* This is a constructor for the service
* Initialize the service, connect to the mySQL db
*/
function Service(db) {
  
//  this.db = mysql.createConnection({
//    host     : 'orolo.cas.msu.edu',
//    user     : 'novakro2',
//    password : 'security1234',
//    database : 'security_stories_test'
//  });
//  this.db.connect();
  
  this.db = db;
  // Connect to the db
}


Service.prototype.GetData = function(name, res, col_name)
{
  var collection = this.db.collection(col_name);
  console.log(name);
  var result;
  collection.findOne({
    "id": name
  }, function(err, doc) {
    //console.log(doc);
    res.send(doc);
    res.end();
  });
  
}

module.exports = Service;

