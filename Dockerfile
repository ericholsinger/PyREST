FROM python:3.6-alpine

COPY . .

RUN pip install --no-cache-dir -r linux-requirements.txt

CMD [ "python", "app.py" ]
