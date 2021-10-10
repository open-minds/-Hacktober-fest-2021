const mongoose = require('mongoose');
const shortId= require('shortid');


const UrlShortnerSchema= mongoose.Schema({

    LongURL:{
        type : String,
        require: true
    },

    ShortUrl : {
        type : String,
        require: true,
        default : shortId.generate
    },
    clicks:{
        type : Number,
        default: 0

    }


   


})

module.exports = mongoose.model('URLshortnerColl', UrlShortnerSchema);