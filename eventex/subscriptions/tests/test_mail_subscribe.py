from django.core import mail
from django.test import TestCase


class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name="Jose Renato", cpf='12345678901',
                    email='jose.renato77@gmail.com', phone='86-99592-5144')
        self.client.post('/inscricao/', data=data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = 'Confirmação de inscrição'

        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'contato@eventex.com.br'

        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['contato@eventex.com.br', 'jose.renato77@gmail.com']

        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        contents = [
            'Jose Renato',
            '12345678901',
            'jose.renato77@gmail.com',
            '86-99592-5144',
        ]
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)
        self.assertIn('Jose Renato', self.email.body)
        self.assertIn('12345678901', self.email.body)
        self.assertIn('jose.renato77@gmail.com', self.email.body)
        self.assertIn('86-99592-5144', self.email.body)
