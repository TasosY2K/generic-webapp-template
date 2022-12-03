FROM python:3.9
WORKDIR /opt/app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
RUN python create_table.py

CMD ["python3", "app.py"]