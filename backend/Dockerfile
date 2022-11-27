FROM python:3.9
WORKDIR /opt/app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8600

RUN chmod +x run.sh
CMD ["sh", "run.sh"]