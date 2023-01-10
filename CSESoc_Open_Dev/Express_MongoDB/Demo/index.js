const express = require('express')
const stockRouter = require('./routes/stock')
const db = require('./db')

const app = express()

app.use(express.json())

app.use('/stock', stockRouter)

app.listen(5000, async () => {
    await db.connectToServer()
    console.log('Sever is running on port 5000')
})