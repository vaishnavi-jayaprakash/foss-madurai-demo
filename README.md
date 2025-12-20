# 🖥️ Simple Python HTTP Server

A minimal Python HTTP server that responds with "Hello World" to any GET request.
Perfect for learning how HTTP servers work in Python.

# 📂 Project Structure
```
.
└── main.py
```

# ⚙️ Requirements

Python 3.7 or higher

# 🚀 How to Run

1. Open a terminal in the project directory.

2. Run the server:
```
python main.py
```
3. Open your browser and navigate to:
```
http://localhost:8000
```

You should see:
```
Hello World
```


# 📝 How It Works
* main.py uses Python’s built-in http.server module.
* HelloHandler handles GET requests and responds with "Hello World".
* The server listens on localhost:8000 until stopped.

# 🛑 Stopping the Server

Press CTRL + C in the terminal to stop the server.

# ⚠️ Notes
This is a learning example, not suitable for production use.

Feel free to modify and experiment with it.
