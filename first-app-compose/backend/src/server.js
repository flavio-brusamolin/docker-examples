const express = require("express")
const cors = require("cors")
const mongoose = require("mongoose")
const routes = require('./routes')

const app = express()

app.use(express.json())
app.use(cors())
app.use(routes)

mongoose.connect("mongodb://database/mydb", {
    useNewUrlParser: true,
    useUnifiedTopology: true
})

app.listen(3000)
