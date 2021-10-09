const express = require('express');
const mongoose= require('mongoose');
const dotenv = require('dotenv');
const bodyparser = require('body-parser');

// invoquer express;
const app = express();



// connexion a la bdd
dotenv.config();
mongoose.connect(process.env.DB_CONNECTION,{ useNewUrlParser: true },(err)=>{
    if(err){
        console.log(err.message);
    }else{
        console.log("connected  to db");
    }
})




const routeAuth = require('./routes/auth')
const routePosts = require('./routes/posts');


// middlewares
app.use(bodyparser.json());
app.use('/api/user',routeAuth);
app.use('/api/posts',routePosts);
        









app.listen(3000,()=> console.log("le serveur est en écoute"));