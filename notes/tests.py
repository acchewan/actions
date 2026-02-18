from django.test import TestCase
from .utils import add_numbers
from django.urls import reverse


class AddTestCase(TestCase):
    def test_add_numbers(self):
        self.assertEqual(add_numbers(2, 3), 5)


class NotesTestCase(TestCase):
    def test_notes_can_be_added(self):
        response = self.client.post(reverse('notesadd'), {
            "title": "Test Note",
            "description": "This is a test note."
        })
        self.assertEqual(response.status_code, 302)

        responsehome = self.client.get(response.url)
        self.assertContains(responsehome, "Test Note")
