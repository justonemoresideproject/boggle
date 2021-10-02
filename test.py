from unittest import TestCase
from app import app
from flask import session
from boggle import Boggle


class FlaskTests(TestCase):

    # TODO -- write tests for every view function / feature!

    def test_postResults(self):
        with app.test_client() as client:
            res = client.get('/post/5')

            self.assertEqual(session['HS13'], 5)

    # def guess(word):
    



    

