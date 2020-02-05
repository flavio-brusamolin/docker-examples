const { Schema, model } = require('mongoose')

const ClientSchema = new Schema({
    name: String,
    email: String,
    age: Number
})

module.exports = model('Client', ClientSchema)