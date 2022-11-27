import os
import requests
from openapi_spec_validator import validate_spec_url

def test_swagger_specification(host):
    endpoint = os.path.join(host, 'api', 'swagger.json')
    validate_spec_url(endpoint)

def test_register(api_v1_host):
    endpoint = os.path.join(api_v1_host, 'auth', 'register')
    response = requests.get(endpoint)
    assert response.status_code == 200
    json = response.json()
    assert 'msg' in json
    assert json['msg'] == "Register OK"