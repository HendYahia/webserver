from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
        <head>
            <title>Welcome</title>
            <style>
                body {
                    margin: 0;
                    height: 100vh;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
                    font-family: Arial, sans-serif;
                }
                h1 {
                    font-size: 50px;
                    color: #ffffff;
                    text-align: center;
                    text-shadow: 0 0 10px #00c6ff, 0 0 20px #0072ff;
                }
            </style>
        </head>
        <body>
            <h1>Joud Radi Alanzi</h1>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run()
