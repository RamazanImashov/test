FROM python:3.11
WORKDIR /usr/src/app
# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ../../test/req.txt .
RUN pip install -r req.txt

# copy entrypoint.sh
COPY entrypoint.sh .
RUN sed -i 's/\r$//g' /usr/src/app/entrypoint.sh
RUN chmod +x /usr/src/app/entrypoint.sh

# copy project
COPY ../../test .

# run entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]