-- SQL queries to set up schemas in BigQuery

CREATE TABLE `data-dev.ntntemp.post` (
  userId INT64 NOT NULL,
  id INT64 NOT NULL,
  title STRING,
  body STRING,
  source STRING
)
