const route = require('express').Router();

const database = require('../models/UrlShortnerModel');
const { Router } = require('express');



// display all  data in database 
route.get('/',async (req,res)=>{
    
const data = await database.find();

res.render('index', {shortURL: data});

})



// add a new URL in the database
route.post('/ShortUrl', async(req,res)=>{
const data = await database.create({LongURL: req.body.fullUrl});

res.redirect('/');

});





// click on a short URL and bean redirected to the path 
route.get('/:URLCLICK',async (req,res)=>{

const URL= await database.findOne({ShortUrl: req.params.URLCLICK })
if(URL== null) return res.sendStatus(404);
URL.clicks++
URL.save();

res.redirect(URL.LongURL);

});




module.exports= route;