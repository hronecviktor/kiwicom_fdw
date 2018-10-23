CREATE EXTENSION IF NOT EXISTS multicorn;

CREATE SERVER kiwi_fdw FOREIGN DATA WRAPPER multicorn options ( wrapper 'kiwi_fdw.KiwiComSearch' );

CREATE FOREIGN TABLE IF NOT EXISTS flights (
    "_flyfrom" TEXT,
    "_to" TEXT,
    "_datefrom" TIMESTAMP,
    "_dateto" TIMESTAMP,
    "_returnfrom" TIMESTAMP,
    "_returnto" TIMESTAMP,
    "_passengers" INT,
    "_typeflight" TEXT,
    "quality" NUMERIC,
    "deep_link" TEXT,
    "nightsindest" INT,
    "airlines" TEXT[],
    "atimeutc" TIMESTAMP,
    "dtimeutc" TIMESTAMP,
    "price" NUMERIC
) server kiwi_fdw;
