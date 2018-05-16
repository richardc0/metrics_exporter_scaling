# metrics_exporter_scaling

This is a prototype app to use Prometheus metrics exported by the metrics-exporter.
The metrics exporter runs on collects data from all environments.
This app collects the data and parses it it using the Prometheus client and print out the number of requests.
The requests are a running total and are reset when the monitored app starts.

## Configuration
Export the following environmental variables

```
export SPACE=<Preview, staging or production>
export STATS_URL=<URL of the materics data>
export APPLICATION=<Name of the app>
```


## Install the requirements

`pip install -r requirements.txt`

## Execution

`python main.py`

## Example output
This example shows the code detecting 100 requests to the template-preview app.

```Starting the metrics exporter autoscaler
Checking stats on:https://notify-metric-exporter.cloudapps.digital/metrics
1
last_request_count: 0
request_count: 124.0
scale_total: 124.0
2
last_request_count: 124.0
request_count: 124.0
scale_total: 0.0
3
last_request_count: 124.0
request_count: 184.0
scale_total: 60.0
4
last_request_count: 184.0
request_count: 224.0
scale_total: 40.0
5
last_request_count: 224.0
request_count: 224.0
scale_total: 0.0```