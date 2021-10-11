const express = require('express');
const mongoose = require('mongoose');
const body_parser=require('body-parser');
const dotenv=require('dotenv');

// imports 
const routes = require('./routes/shortnerUrl')


// start express
const app = express();



// db connection 
dotenv.config();
mongoose.connect(process.env.DB_CONNEXION,{ useNewUrlParser: true,useUnifiedTopology: true },(err)=>{
if(err){
    console.log(" connection to Data base failed");

}else{ console.log("connexcted to Data base ");}
});



app.set('view engine','ejs');




// middlewares
app.use(body_parser.json());
app.use(express.urlencoded({extended:false}));
app.use('/',routes);






app.listen(3000,()=>{
    console.log("le serveur est en ecoute");
})