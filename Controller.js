StoriesService = require('./Service');

module.exports = function(app, db) {
    
    service = new StoriesService(db);
    
    /**
    * /politician endpoint which is hit when the plugin detects that a new visit has been made
    */
    app.get('/politician/:name', function(req,res){
      //console.log(req.body);
      var name = req.params.name;
      service.GetData(name, res, "politician");
    });
  
    
    /**
    * /stories endpoint which is hit when the plugin detects that a new visit has been made
    */
    app.get('/stories/:name', function(req,res){
      //console.log(req.body);
      var name = req.params.name;
      service.GetData(name, res, "stories");
    });
  
    /**
    * /topic endpoint which is hit when the plugin detects that a new visit has been made
    */
    app.get('/topic/:name', function(req,res){
      //console.log(req.body);
      var name = req.params.name;
      service.GetData(name, res, "topic");
    });
  
  
    /**
    * /comment endpoint which is hit when the plugin detects that a new visit has been made
    */
    app.get('/comment/:name', function(req,res){
      //console.log(req.body);
      var name = req.params.name;
      service.GetData(name, res, "comment");
    });

  
}