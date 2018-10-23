PostgreSQL foreign data wrapper looking up flights on kiwi.com
```bash
docker build -t fdw:local . && docker run -it -p 5432:5432 --rm --name pg -e POSTGRES_PASSWORD=pwd fdw:local
# another terminal
psql -H 'postgresql://postgres:pwd@localhost:5432' -c "select * from flights where _flyfrom = 'BCN' and _to = 'PRG' and _datefrom = '2018-11-01' and _dateto = '2018-11-01';"
```