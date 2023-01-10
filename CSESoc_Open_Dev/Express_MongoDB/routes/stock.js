const express = require('express')
const stockRouter = express.Router()
const db = require('../db')
const fs = require('fs/promises')

stockRouter.get('/', (req, res) => {
    res.send('This is the stock route')
})

stockRouter.get('/:name', (req, res) => {
    for (i in db) {
        if (db[i].name === req.params.name) {
            res.send(db[i])
            return;
        }
    }
})

stockRouter.post('/addItem', (req, res) => {
    db.push(req.body)
    fs.writeFile('./db.json', JSON.stringify(db))
    res.send('Item added')
})

stockRouter.put('/update', (req, res) => {
    db.splice(0, db.length)
    db.push(req.body)
    fs.writeFile('./db.json', JSON.stringify(db))
    res.send('Data updated')
})

stockRouter.delete('/deleteItem/:name', (req, res) => {
    const index = db.findIndex(a => a.name === req.params.name)
    db.splice(index, 1);
    fs.writeFile('./db.json', JSON.stringify(db))
    res.send('Item removed')
})

module.exports = stockRouter