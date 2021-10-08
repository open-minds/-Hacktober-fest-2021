const routes = require('express').Router();
const bcrypt= require('bcryptjs');
const jwt = require('jsonwebtoken');

const dataBase = require('../models/user');




const {RegisterValidation,LoginValidation} = require('../validation');                      // demander a sofiane








routes.post('/register', async (req,res)=>{


// check the validation of the inputs

const {error} = await RegisterValidation(req.body);
if(error) return res.status(400).send(error.details[0].message);



// to check if the acccount already exists
const exists=  await dataBase.findOne({email:req.body.email});
if(exists) return res.status(400).send('email already exists');


// to hash the password 

const salt = await bcrypt.genSalt(10);
const hashpassword = await bcrypt.hash(req.body.password,salt);

const donnes= new dataBase({
        name: req.body.name,
        email: req.body.email,
        password: hashpassword
    });
   try{
    
   const save= await donnes.save();
   res.send({user : save._id});
   }catch(err){()=>

    res.status(400).send(err);
}

})




// Login action



routes.post('/login', async (req,res)=>{

        // check if the inputs are valid

 const {error} = await LoginValidation(req.body);
 if(error) return res.status(400).send(error.details[0].message);



 // check if email exists
 const user = await dataBase.findOne({email : req.body.email})
 if(!user) return res.send("email not found");
 


 // check if the password is correct 
const compare = await bcrypt.compare(req.body.password, user.password);
if(!compare) return res.status(400).send("password incorrect");





// creation du token 

const token = jwt.sign({_id : user._id}, process.env.TOKEN_SECRET);
res.header('auth-token',token).send(token);

res.send('logged successfully');

 
 






});






module.exports=routes;