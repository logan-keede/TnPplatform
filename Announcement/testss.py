'''import requests
announcement_id = 6

response = requests.delete(f'http://localhost:8000/announcements/{announcement_id}/')
print(response.status_code)'''

import requests
import json

# Replace with the ID of the announcement you want to update
announcement_id = 1

# Replace with your actual data
data = {
    'title': 'new value1',
    'content': 'new value2',
    #'field3': 'new value3',
}

# PUT request
response = requests.put(f'http://localhost:8000/announcements/{announcement_id}/', data=json.dumps(data), headers={'Content-Type': 'application/json'})
print('PUT request:')
print(response.status_code)
print(response.json())

# PATCH request
response = requests.patch(f'http://localhost:8000/announcements/{announcement_id}/', data=json.dumps(data), headers={'Content-Type': 'application/json'})
print('PATCH request:')
print(response.status_code)
print(response.json())