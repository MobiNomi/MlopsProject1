FROM python:3.10-slim

WORKDIR /app

# Copy only the Flask app's own scoped requirements file first,
# so Docker can cache this layer separately from app code changes
COPY flask_app/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

RUN python -m nltk.downloader stopwords wordnet

# Now copy the rest of the project (app code, templates, model utilities)
COPY . .

EXPOSE 5000

CMD ["python3", "flask_app/app.py"]