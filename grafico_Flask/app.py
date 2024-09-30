from flask import Flask, render_template
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
import base64
import pyodbc
from sqlalchemy import create_engine
import conexao

app = Flask(__name__)

# Usando SQLAlchemy com pyodbc
conecta = conexao.create_connection()


@app.route('/')
def index():
    # Consulta SQL
    query = """
    SELECT TOP 10
    coluna_x,
    coluna_y
    FROM (
        SELECT time AS coluna_x, SUM(total_gols) AS coluna_y  
        FROM EstatisticasGols
        GROUP BY time
    ) tab1
    ORDER BY coluna_y DESC
    """
    df = pd.read_sql(query, conecta)

    # Gerar gráfico
    img = BytesIO()
    plt.figure(figsize=(10, 6))

    plt.bar(df['coluna_x'], df['coluna_y'], color='green')
    plt.title('Top 10 Times com Mais Gols')
    plt.xlabel('Times')
    plt.ylabel('Total de Gols')
    plt.xticks(rotation=45, ha='right')

    # Salvar o gráfico no buffer e codificá-lo em base64
    plt.tight_layout()  # Ajusta o layout do gráfico
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode('utf8')

    return render_template('index.html', plot_url=plot_url)


if __name__ == '__main__':
    app.run(debug=True)
