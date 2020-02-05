const Client = require('../models/Client')

module.exports = {
    async list(req, res) {
        const clients = await Client.find()

        return res.status(200).json({
            success: true,
            clients
        })
    },

    async store(req, res) {
        const { name, email, age } = req.body

        const client = await Client.create({
            name,
            email,
            age
        })

        return res.status(201).json({
            success: true,
            client
        })
    }
}