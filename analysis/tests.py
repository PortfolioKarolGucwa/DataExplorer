import pandas as pd
from django.test import TestCase

from .logic import summarize_dataset


class SummarizeDatasetTests(TestCase):
    def test_returns_expected_keys(self):
        df = pd.DataFrame({'age': [25, 30, None], 'city': ['NY', 'LA', 'NY']})
        summary = summarize_dataset(df)

        self.assertEqual(summary['row_count'], 3)
        self.assertEqual(summary['column_count'], 2)
        self.assertEqual(len(summary['preview']), 3)

        age_column = next(c for c in summary['columns'] if c['name'] == 'age')
        self.assertEqual(age_column['missing'], 1)

        self.assertIn('age', [row['column'] for row in summary['stats']])
        self.assertNotIn('city', [row['column'] for row in summary['stats']])
