# Imagem base
FROM python:3.10

# Diretório de trabalho
WORKDIR /app

# Copia os arquivos
COPY . /app

# Instala as dependências
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Expõe a porta do Streamlit
EXPOSE 8501

# Comando de execução
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
