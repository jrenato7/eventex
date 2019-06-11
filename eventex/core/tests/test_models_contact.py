from django.core.exceptions import ValidationError
from django.test import TestCase

from eventex.core.models import Speaker, Contact


class ContactModelTest(TestCase):
    def setUp(self):
        self.speaker = Speaker.objects.create(
            name='José Renato',
            slug='jose-renato',
            photo='http://hbn.link/hb-pic'
        )
    def test_email(self):
        contact = Contact.objects.create(speaker=self.speaker,
                                         kind=Contact.EMAIL,
                                         value='jose.renato77@gmail.com')

        self.assertTrue(Contact.objects.exists())

    def test_phone(self):
        contact = Contact.objects.create(speaker=self.speaker,
                                         kind=Contact.PHONE,
                                         value='86-99592-5144')

        self.assertTrue(Contact.objects.exists())

    def test_choices(self):
        """Contact kind should be limited to E or P."""
        contact = Contact(speaker=self.speaker, kind='A', value='B')
        self.assertRaises(ValidationError, contact.full_clean)

    def test_str(self):
        contact = Contact(speaker=self.speaker, kind='E',
                          value='jose.renato77@gmail.com')
        self.assertEqual('jose.renato77@gmail.com', str(contact))
