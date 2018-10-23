FROM postgres:10-alpine
#FROM postgres:9.5-alpine

WORKDIR /srv
RUN apk add gcc git make musl-dev python2-dev py-pip libffi-dev
RUN git clone https://github.com/Kozea/Multicorn.git
RUN cd Multicorn && make && make install

COPY *requirements* /srv/
RUN pip install -r requirements.txt

COPY init_dfw.sql /docker-entrypoint-initdb.d/init_dfw.sql

COPY . /srv
RUN python setup.py install
