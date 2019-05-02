from datetime import datetime

from django.test import TestCase

from eventex.subscriptions.models import Subscription


class SubscriptionModelTest(TestCase):

    def setUp(self):
        self.obj = Subscription(
            name='José Renato',
            cpf='01234567890',
            email='jose.renato77@gmail.com',
            phone='86-995925144',
        )
        self.obj.save()

    def test_create(self):
        """Must create a new line on DB"""
        self.assertTrue(Subscription.objects.exists())

    def test_created_at(self):
        """Subscription must have an auto created_at attr."""
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_str(self):
        self.assertEqual('José Renato', str(self.obj))



