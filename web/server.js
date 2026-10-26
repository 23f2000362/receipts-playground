const express = require("express");
const { exec } = require("child_process");
const app = express();

app.get("/user", (req, res) => {
  const id = req.query.id;
  const sql = `SELECT * FROM users WHERE id = ${id}`;
  db.query(sql, (err, rows) => res.send(rows));
});

app.post("/ping", (req, res) => {
  const { host } = req.body;
  exec("ping -c 1 " + host, (e, out) => res.send(out));
});
