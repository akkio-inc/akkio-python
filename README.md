# akkio-python
Convenient access to the [Akkio](https://www.akkio.com) API from python

## Installation
```bash
pip install akkio
```
## Usage
```python
import akkio
akkio.api_key = 'YOUR-API-KEY-HERE' # get your API key at https://app.akk.io/team-settings

models = akkio.get_models()['models']
for model in models:
  print(model)

datasets = akkio.get_datasets()['datasets']
for dataset in datasets:
  print(dataset)

new_dataset = akkio.create_dataset('python api test')
print(new_dataset)

# create a toy dataset
import random
rows = []
for i in range(1000):
  rows.append({
    'x': random.random()
  })
  rows[-1]['y'] = rows[-1]['x'] > 0.5

akkio.add_rows_to_dataset(new_dataset['dataset_id'], rows)

new_model = akkio.create_model(new_dataset['dataset_id'], ['y'], [], {'duration': 1})
print(new_model)
prediction = akkio.make_prediction(new_model['model_id'], [{'x': 0.1}, {'x':0.7}], explain=True)
print(prediction)
```
