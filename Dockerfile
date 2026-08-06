FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

RUN python -m nltk.downloader stopwords wordnet

COPY . .

EXPOSE 5000

CMD ["python3", "flask_app/app.py"]