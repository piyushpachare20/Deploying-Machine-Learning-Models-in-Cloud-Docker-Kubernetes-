FROM python:3.9-slim
WORKDIR /app
COPY app.py model.pkl requirements.txt ./
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python", "app.py"]
