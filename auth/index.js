const express = require("express");
const bodyParser = require("body-parser");

const app = express();
app.use(bodyParser.json());

const users = [
  { username: "user1", password: "password1" },
  { username: "user2", password: "password2" },
];

app.post("/auth", (req, res) => {
  const { username, password } = req.body;
  const user = users.find(
    (u) => u.username === username && u.password === password
  );

  if (user) {
    res
      .status(200)
      .json({ message: "Authentication successful", token: "fake-token" });
  } else {

    res.status(401).json({ message: "Invalid credentials", username, password });
  }
});

const PORT = 3000;
app.listen(PORT, () => {
  console.log(`Authentication service running on port ${PORT}`);
});
