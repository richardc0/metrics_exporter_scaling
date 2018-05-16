import sched

import time

import os
from pip._vendor import requests


class Scheduler(object):
    print("Starting the metrics exporter autoscaler")
    counter = 0
    last_request_count = 0
    metrics_url = os.environ['STATS_URL']
    space = os.environ['SPACE']
    application = os.environ['APPLICATION']
    print("Checking stats on:" + metrics_url)

    def check_stats(self, sc):
        self.counter = self.counter + 1
        print(self.counter)

        metrics = requests.get(self.metrics_url)

        request_count = 0

        from prometheus_client.parser import text_string_to_metric_families
        for family in text_string_to_metric_families(metrics.text):
            if family.name == 'requests':
                for sample in family.samples:
                    if sample[1]['organisation'] == 'govuk-notify':
                        if sample[1]['space'] == self.space:
                            if sample[1]['app'] == self.application:
                                # print(sample[1]['space'] + " : " + sample[1]['app'] + " : " + str(sample[2]))
                                request_count = request_count + sample[2]

        print("last_request_count: " + str(self.last_request_count))
        print("request_count: " + str(request_count))
        print("scale_total: " + str(request_count - self.last_request_count))

        self.last_request_count = request_count

        sc.enter(10, 1, self.check_stats, (sc,))

    def run(self):
        s = sched.scheduler(time.time, time.sleep)
        s.enter(0, 1, self.check_stats, (s,))
        s.run()


if __name__ == '__main__':
    Scheduler().run()






