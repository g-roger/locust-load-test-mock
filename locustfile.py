from locust import HttpUser, task, between
import random
import json
import warnings

warnings.filterwarnings("ignore")

class WebsiteUser(HttpUser):
    wait_time = between(0, 1)
    payload_file = '/home/groger/Projects/locust-stress-test/data_load_test.data'

    with open(payload_file, 'r') as f:
        payloads = f.readlines()

    @task(1)
    def post(self):
        headers = {'content-type': 'application/json'}
        payload = random.choice(self.payloads)
        json_payload = json.loads(payload)
        self.client.post('', json=json_payload, headers=headers, verify=False)
