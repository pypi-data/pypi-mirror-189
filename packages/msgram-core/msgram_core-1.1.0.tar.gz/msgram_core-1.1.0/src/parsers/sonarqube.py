import os

import requests

from staticfiles import SONARQUBE_AVAILABLE_METRICS, SONARQUBE_SUPPORTED_MEASURES


class Sonarqube:

    def __init__(self):
        self.endpoint = os.getenv("SONAR_URL", "https://sonarcloud.io/api/metrics/search")

    def extract_supported_metrics(self, metrics):
        try:
            request = requests.get(self.endpoint)

            if request.ok:
                data = request.json()
            else:
                data = SONARQUBE_AVAILABLE_METRICS
        except Exception:
            data = SONARQUBE_AVAILABLE_METRICS

        return self.__extract_sonarqube_supported_metrics(metrics, data)

    def __extract_sonarqube_supported_metrics(self, metrics, sonar_metrics):
        collected_metrics = {}
        supported_metrics = []

        [
            supported_metrics.extend(list(x.values())[0]['metrics'])
            for x in SONARQUBE_SUPPORTED_MEASURES
        ]

        for component in metrics:
            qualifier = component['qualifier']
            path = component['path' if qualifier != 'TRK' else 'name']
            collected_metrics[path] = {
                'qualifier': qualifier,
                'measures': []
            }

            for obj in component['measures']:
                metric_key = obj['metric']
                if metric_key not in supported_metrics:
                    continue

                collected_metrics[path]['measures'].append({
                    'metric': metric_key,
                    'value': float(obj['value'])
                })

        return collected_metrics
