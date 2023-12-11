from flask import Flask, request, jsonify

app= Flask(__name__)

data=[
    {
    "text": "Genius is one percent inspiration and ninety-nine percent perspiration.",
    "author": "Thomas Edison, type.fit"
  },
  {
    "text": "You can observe a lot just by watching.",
    "author": "Yogi Berra, type.fit"
  },
  {
    "text": "It is often the small steps, not the giant leaps, that bring about the most lasting change",
    "author": "Queen Elizabeth II,, type.fit"
  },
  {
    "text": "Difficulties increase the nearer we get to the goal.",
    "author": "Johann Wolfgang von Goethe, type.fit"
  },
  {
    "text": "Fate is in your hands and no one elses",
    "author": "Byron Pulsifer, type.fit"
  },
  {
    "text": "I have learned not to allow rejection to move me.",
    "author": "Cicely Tyson, type.fit"
  },
  {
    "text": "Nothing happens unless first we dream.",
    "author": "Carl Sandburg, type.fit"
  },
  {
    "text": "Well begun is half done.",
    "author": "Aristotle, type.fit"
  },
  {
    "text": "Life is a learning experience, only if you learn.",
    "author": "Yogi Berra"
  },
  {
    "text": "Self-complacency is fatal to progress.",
    "author": "Margaret Sangster, type.fit"
  },
  {
    "text": "Peace comes from within. Do not seek it without.",
    "author": "Buddha, type.fit"
  },
  {
    "text": "What you give is what you get.",
    "author": "Byron Pulsifer, type.fit"
  },
  {
    "text": "We can only learn to love by loving.",
    "author": "Iris Murdoch, type.fit"
  },
  {
    "text": "Life is change. Growth is optional. Choose wisely.",
    "author": "Karen Clark, type.fit"
  },
  {
    "text": "You'll see it when you believe it.",
    "author": "Wayne Dyer, type.fit"
  },
  {
    "text": "Today is the tomorrow we worried about yesterday.",
    "author":  "type.fit"
  }
]

@app.route("/")
def quote():
    return data


if __name__ == "__main__":
    app.run(debug=True)