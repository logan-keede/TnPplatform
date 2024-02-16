import requests
import json
import unittest

class TestAnnouncementAPI(unittest.TestCase):

    def setUp(self):
        self.base_url = 'http://localhost:8000/announcements'
        self.announcement_id = 1
        self.headers = {'Content-Type': 'application/json'}

    def test_get_announcement(self):
        response = requests.get(f'{self.base_url}/{self.announcement_id}/')
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.json())

    def test_post_announcement(self):
        data = {
            'title': 'New Announcement',
            'content': 'This is a new announcement'
        }
        response = requests.post(self.base_url, data=json.dumps(data), headers=self.headers)
        self.assertEqual(response.status_code, 201)
        self.assertIsNotNone(response.json())

    def test_put_announcement(self):
        data = {
            'title': 'Updated Announcement',
            'content': 'This announcement has been updated'
        }
        response = requests.put(f'{self.base_url}/{self.announcement_id}/', data=json.dumps(data), headers=self.headers)
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.json())

    def test_patch_announcement(self):
        data = {
            'title': 'Patched Announcement',
            'content': 'This announcement has been patched'
        }
        response = requests.patch(f'{self.base_url}/{self.announcement_id}/', data=json.dumps(data), headers=self.headers)
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.json())

    def test_delete_announcement(self):
        response = requests.delete(f'{self.base_url}/{self.announcement_id}/')
        self.assertEqual(response.status_code, 204)

if __name__ == '__main__':
    unittest.main()