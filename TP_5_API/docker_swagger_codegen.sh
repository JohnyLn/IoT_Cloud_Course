docker run --rm -v $PWD:/local openapitools/openapi-generator-cli:v4.3.1 generate -i /local/timeseries_iot.yaml -g python-flask --package-name TimeSeriesIoT -o /local/out/python-ts-iot
