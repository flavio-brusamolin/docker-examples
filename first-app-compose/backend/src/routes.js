const { Router } = require('express')
const ClientController = require('./controllers/ClientController')

const routes = Router()

routes.get('/clients', ClientController.list)
routes.post('/clients', ClientController.store)

module.exports = routes
