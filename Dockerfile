  
FROM python:3.9

EXPOSE 8501

WORKDIR /usr/src/app

COPY libraries.txt ./

RUN pip install -r libraries.txt

COPY . .