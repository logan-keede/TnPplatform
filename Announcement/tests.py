import requests
import json
import unittest

class TestAnnouncementAPI(unittest.TestCase):

    def setUp(self):
        self.announcement_id = 4
        self.headers = {'Content-Type': 'application/json'}

    def test_get_announcement(self):
        response = requests.get(f'http://localhost:8000/announcements/{self.announcement_id}/')
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.json())

    def test_post_announcement(self):
        data = {
            'title': 'New Announcement',
            'content': 'This is a new announcement'
        }
        for i in range(5):
            response = requests.post('http://localhost:8000/announcements/', data=json.dumps(data), headers={'Content-Type': 'application/json'})
            self.assertEqual(response.status_code, 201)
            self.assertIsNotNone(response.json())
            i=i+1

    def test_put_announcement(self):
        announcement_id = 3
        data = {
            'title': 'Updated Announcement',
            'content': 'This announcement has been updated'
        }
        response = requests.put(f'http://localhost:8000/announcments/{announcement_id}', data=json.dumps(data), headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.json())

    def test_patch_announcement(self):
        data = {
            'title': 'Patched Announcement',
            'content': 'This announcement has been patched'
        }
        response = requests.patch(f'http://localhost:8000/announcements/{self.announcement_id}', data=json.dumps(data), headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.json())

    def test_delete_announcement(self):
        announcement_id = 3
        response = requests.delete(f'http://localhost:8000/announcements/{announcement_id}/')
        self.assertEqual(response.status_code, 204)

if __name__ == '__main__':
    unittest.main()