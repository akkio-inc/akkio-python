import requests

api_key = None

url = 'api.akk.io'
version = 'v1'
protocol = 'https'
port = '443'

def get_models():
  return requests.get('{}://{}:{}/{}/models'.format(protocol, url, port, version), {
    'api_key': api_key
  }).json()

def delete_model(id):
  return requests.delete('{}://{}:{}/{}/models'.format(protocol, url, port, version), json={
    'api_key': api_key,
    'id': id
  }).json()

def get_datasets():
  return requests.get('{}://{}:{}/{}/datasets'.format(protocol, url, port, version), {
    'api_key': api_key
  }).json()

def create_dataset(name):
  return requests.post('{}://{}:{}/{}/datasets'.format(protocol, url, port, version), json={
    'api_key': api_key,
    'name': name
  }).json()

def delete_dataset(id):
  return requests.delete('{}://{}:{}/{}/datasets'.format(protocol, url, port, version), json={
    'api_key': api_key,
    'id': id
  }).json()

def add_rows_to_dataset(id, rows):
  return requests.post('{}://{}:{}/{}/datasets'.format(protocol, url, port, version), json={
    'api_key': api_key,
    'id': id,
    'rows': rows
  }).json()

def parse_dataset(id):
  return requests.post('{}://{}:{}/{}/datasets'.format(protocol, url, port, version), json={
    'api_key': api_key,
    'id': id,
    'parse_fields': True
  }).json()

def create_model(id, predict_fields, ignore_fields=[], params=None):
  request_params = {
    'api_key': api_key,
    'dataset_id': id,
    'predict_fields': predict_fields,
    'ignore_fields': ignore_fields,
    'extra_attention': False,
    'duration': 10
  }
  if params:
    request_params.update(params)
  return requests.post('{}://{}:{}/{}/models'.format(protocol, url, port, version), json=request_params).json()

def make_prediction(id, data, explain=False):
  return requests.post('{}://{}:{}/{}/models'.format(protocol, url, port, version), json={
    'api_key': api_key,
    'id': id,
    'data': data,
    'explain': explain
  }).json()
