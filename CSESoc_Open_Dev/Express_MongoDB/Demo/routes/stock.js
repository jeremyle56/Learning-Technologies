const express = require('express')
const stockRouter = express.Router()
const db = require('../db')
const fs = require('fs/promises')

stockRouter.get('/', async (req, res) => {
    let items = await db.getStockCollection().find().toArray()
    res.send(items)
})

stockRouter.get('/:name', async (req, res) => {
    const stockCollection = db.getStockCollection()
    let item = await stockCollection.findOne({ name: req.params.name })
    res.send(item);
})

stockRouter.post('/addItem', async (req, res) => {
    await db.getStockCollection().insert(req.body)
    res.send("success!")
})

stockRouter.put('/update', async (req, res) => {
    await db.getStockCollection().remove({}).insert(req.body)
    res.send('Data updated')
})

stockRouter.delete('/deleteItem/:name', async (req, res) => {
    await db.getStockCollection().deleteOne({ name: req.params.name })
    res.send('Item removed')
})

module.exports = stockRouter