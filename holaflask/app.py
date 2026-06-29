from flask import Flask
import socket

app = Flask(__name__)

@app.route("/")
def home():
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)

    return f"""
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Hola Flask Replica</title>
        <style>
            body {{
                background: #0f172a;
                color: #e2e8f0;
                font-family: Arial, sans-serif;
                text-align: center;
                padding-top: 100px;
            }}
            .card {{
                background: #1e293b;
                padding: 40px;
                border-radius: 12px;
                display: inline-block;
                box-shadow: 0 0 20px rgba(0,0,0,0.5);
            }}
            h1 {{
                color: #38bdf8;
            }}
            .info {{
                margin-top: 20px;
                font-size: 14px;
                color: #94a3b8;
            }}
        </style>
    </head>
    <body>
        <div class="card">
            <h1>🚀 Hola Flask Replica</h1>
            <p>Tu aplicación está corriendo correctamente en Docker Swarm</p>
            
            <div class="info">
                <p><strong>Host:</strong> {hostname}</p>
                <p><strong>IP:</strong> {ip}</p>
            </div>
        </div>
    </body>
    </html>
    """