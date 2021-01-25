from unittest import TestCase

from django.core.exceptions import ValidationError

from testing.validators import contains_only_digits


class EgnValidatorTests(TestCase):
    def test_validate_when_only_digits_do_nothing(self):
        contains_only_digits('1234567890')

    def test_validate_when_empty_do_nothing(self):
        contains_only_digits('')

    def test_validate_when_value_contains_letter_do_nothing(self):
        with self.assertRaises(ValidationError) as context:
            contains_only_digits('123a')

        self.assertIsNotNone(context.exception)