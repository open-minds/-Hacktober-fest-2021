const routes = require('express').Router();
const jwt = require('jsonwebtoken');
const dataBase = require('../models/user');



 // rendre la route privée 
const private = require('./verifyToken');

routes.get('/',private, (req,res)=>{
    
   res.send(req.user);


   // pour chercher un utilisateur a travers son token
                //dataBase.findOne({_id: req.user});    
});



module.exports=routes;