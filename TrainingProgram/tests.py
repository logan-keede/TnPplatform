from django.test import TestCase
import unittest
import requests
import json

# Create your tests here.

class TestTrainingProgramAPI(unittest.TestCase):
    def test_get_request(self):
        response = requests.get('http://localhost:8000/training_program/')
        self.assertEqual(response.status_code, 200)

    def test_post_request(self):
        job_opening_data = {
            'training_subject' : 'Subject',
            'prerequisites' : 'prerequisites',
            'training_organization' : 'Some organization',
            'start_date' : '2024-03-01',
            'end_date' : '2024-03-09'
        }
        for i in range(5):
            response = requests.post('http://localhost:8000/training_program/', data=json.dumps(job_opening_data), headers={'Content-Type': 'application/json'})
            i=i+1
            self.assertEqual(response.status_code, 201)

    def test_put_request(self):
        job_opening_id = 4
        job_opening_data = {
            'training_subject' : 'No Subject',
            'prerequisites' : 'prerequisites',
            'training_organization' : 'Some Other organization',
            'start_date' : '2024-03-01',
            'end_date' : '2024-03-04'
        }

        response = requests.put(f'http://localhost:8000/training_program/{job_opening_id}/', data=json.dumps(job_opening_data), headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 200)

    def test_patch_request(self):
        job_opening_id = 5
        updated_data = {
            'training_subject' : 'Subject Name',
            'prerequisites' : 'Programming',
            'training_organization' : 'Not Some organization',
        }

        response = requests.patch(f'http://localhost:8000/training_program/{job_opening_id}/', data=json.dumps(updated_data), headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 200)
    
    def test_delete_request(self):
        job_opening_id = 6
        response = requests.delete(f'http://localhost:8000/training_program/{job_opening_id}/')
        self.assertEqual(response.status_code, 204)

if __name__ == '__main__':
    unittest.main()