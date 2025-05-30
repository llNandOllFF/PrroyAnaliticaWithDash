FROM python:3.9.6-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get clean -y

EXPOSE 8050

#Set variable host Dash
ENV DASH_HOST 0.0.0.0

COPY . .

CMD [ "python", "main.py"]