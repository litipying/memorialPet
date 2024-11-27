FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

ENV PYTHONPATH=/app/src

EXPOSE 8501

CMD ["streamlit", "run", "src/app.py"] 