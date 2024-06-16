FROM python:3.12-slim

WORKDIR /app
COPY ./src /app
RUN pip install --no-cache-dir --upgrade -r requirements.txt

ENV ACCESS_KEY_ID=YOUR_ACCESS_KEY_ID
ENV SECRET_ACCESS_KEY=YOUR_SECRET_ACCESS_KEY
EXPOSE 8000

ENTRYPOINT ["fastapi", "run", "main.py"]