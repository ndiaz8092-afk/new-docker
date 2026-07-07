from flask import Flask
from datetime import datetime
import socket

app = Flask(_name_)

@app.route("/")
def home():
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Docker CI/CD Demo</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background: #0f172a;
                color: white;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }}

            .container {{
                background: #1e293b;
                padding: 40px;
                border-radius: 15px;
                width: 500px;
                text-align: center;
                box-shadow: 0 0 20px rgba(0,0,0,0.5);
            }}

            h1 {{
                color: #38bdf8;
            }}

            .status {{
                background: #16a34a;
                padding: 10px;
                border-radius: 8px;
                margin: 20px 0;
            }}

            .info {{
                text-align: left;
                background: #334155;
                padding: 15px;
                border-radius: 10px;
            }}

            footer {{
                margin-top: 20px;
                color: #94a3b8;
                font-size: 14px;
            }}
        </style>
    </head>

    <body>

        <div class="container">

            <h1>🚀 Docker CI/CD Pipeline</h1>

            <div class="status">
                ✅ Aplicación funcionando correctamente
            </div>

            <div class="info">
                <p><b>Proyecto:</b> new-docker</p>
                <p><b>Tecnología:</b> Python + Flask + Docker</p>
                <p><b>Servidor:</b> {socket.gethostname()}</p>
                <p><b>Fecha despliegue:</b> {datetime.now()}</p>
                <p><b>Estado:</b> Ejecutando en contenedor Docker</p>
            </div>

            <footer>
                Desplegado automáticamente con GitHub Actions
            </footer>

        </div>

    </body>
    </html>
    """

app.run(host="0.0.0.0", port=5000)
