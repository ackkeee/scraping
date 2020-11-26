FROM python:3.9-slim

RUN cp /usr/share/zoneinfo/Asia/Tokyo /etc/localtime

ARG UID=1000
ARG USER=python
RUN useradd -m -u ${UID} ${USER}
USER ${UID}

WORKDIR /src
COPY src /src

RUN pip install --upgrade pip \
  && pip install flask \
  && pip install requests \
  && pip install lxml \
  && pip install bs4 \
  && pip install python-dotenv

CMD ["python", "app.py"]
