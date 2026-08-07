FROM python:3.10-slim

WORKDIR /app

# Copy the entire project first, so setup.py / pyproject.toml
# and the src/ package are present before pip tries an editable install
COPY . .

RUN pip install --no-cache-dir -r requirements.txt

RUN python -m nltk.downloader stopwords wordnet

EXPOSE 5000

CMD ["python3", "flask_app/app.py"]