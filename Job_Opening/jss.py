import requests
import json

# Replace with the ID of the announcement you want to update
job_opening_id = 15

# Replace with your actual data
job_opening_data = {
            'NameofCompany':'Vyson',
            'profileOfCompany':'Software',
            'JobProfile': 'Software Engineer',
            'BranchChoice':'CSE',
            'ctc': '13LPA',
            'Eligibility': 'B.Tech',
            'Selection': 'Virtual',
            'location': 'Surat',
            'stipend': 10000,
            'start': '2024-03-01',
        }

updated_data = {
            'JobProfile': 'Senior Software Engineer',
            'description': 'Updated job opening for a software engineer',
            'location': 'San Francisco',
            'salary': 120000,
        }

response=requests.get(f'http://localhost:8000/job_openings/{job_opening_id}/')
print(response.status_code, response.json())

'''# PUT request
response = requests.put(f'http://localhost:8000/job_openings/{job_opening_id}/', data=json.dumps(job_opening_data), headers={'Content-Type': 'application/json'})
print('PUT request:')
print(response.status_code)
print(response.json())

# PATCH request
response = requests.patch(f'http://localhost:8000/job_openings/{job_opening_id}/', data=json.dumps(updated_data), headers={'Content-Type': 'application/json'})
print('PATCH request:')
print(response.status_code)
print(response.json())'''