from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase

from .forms import UploadedFileForm
from .models import UploadedFile


class UploadedFileModelTests(TestCase):
    def test_str_returns_title(self):
        dataset = UploadedFile(title='My dataset')
        self.assertEqual(str(dataset), 'My dataset')


class UploadedFileFormTests(TestCase):
    def test_rejects_non_csv_file(self):
        upload = SimpleUploadedFile('data.txt', b'col1,col2\n1,2\n', content_type='text/plain')
        form = UploadedFileForm(data={'title': 'Bad file'}, files={'file': upload})
        self.assertFalse(form.is_valid())
        self.assertIn('file', form.errors)

    def test_accepts_csv_file(self):
        upload = SimpleUploadedFile('data.csv', b'col1,col2\n1,2\n', content_type='text/csv')
        form = UploadedFileForm(data={'title': 'Good file'}, files={'file': upload})
        self.assertTrue(form.is_valid())
