from django.test import TestCase
from django.urls import reverse


class ViewsTest(TestCase):
  def test_incorrect_request(self):
    response = self.client.post(reverse('index'))
    self.assertEqual(response.content, b"Welcome to Resume spam filter. Only GET request supported!")

  def test_get_request_incorrect_params(self):
    response = self.client.get(reverse('index'), {'q': 'sample data', 'w': 'sample data'})
    self.assertEqual(response.content, b"Welcome to Resume spam filter. Expected parameters missing!")

  def test_get_request_unexpected_param_value(self):
    response = self.client.get(reverse('index'), {'q': 'incorrect value', 'd': 'sample data'})
    self.assertEqual(response.content, b"Incorrect param value!")
