# Use a imagem base do Python
FROM python:3.9.6

# Set the working directory in the container
WORKDIR /app

# Copie os arquivos de requisitos para o container
COPY requirements.txt /app/

# Instale as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copie todo o código da aplicação para o container
COPY . /app/

# Comando para rodar o servidor Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
