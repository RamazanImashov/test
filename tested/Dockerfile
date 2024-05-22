#FROM python:3.11
#WORKDIR .
#COPY req.txt .
#RUN pip3 install --no-cache-dir --upgrade -r req.txt
#COPY . .
#CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "80"]

FROM python:3.11
WORKDIR ./usr/src/app
COPY ../test/req.txt ./
RUN pip3 install -r req.txt

