const express = require("express");
const { MongoClient } = require("mongodb");

const app = express();

app.get("/results", async (req, res) => {
  const user_token = req.headers["authorization"];

  // Validate token (mock validation)
  if (user_token !== "fake-token") {
    return res.status(401).json({ message: "Unauthorized" });
  }

  // Fetch stats from MongoDB
  const client = new MongoClient("mongodb://mongo-db:27017/");
  await client.connect();
  const db = client.db("analytics");

  const stats = await db
    .collection("stats")
    .find()
    .sort({ _id: -1 })
    .limit(1)
    .project({ _id: 0 })  // Exclude _id
    .toArray();

    res.status(200).json(stats[0]);
  });

const PORT = 4000;
app.listen(PORT, () => {
  console.log(`Show Results service running on port ${PORT}`);
});
