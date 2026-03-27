from django.test import TestCase
from .models import Candidate

class HomePageTest(TestCase):
    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

class CandidateModelTest(TestCase):
    def test_candidate_creation(self):
        candidate = Candidate.objects.create(name="Jesus Christ", votes=10)
        
        self.assertEqual(candidate.name, "Jesus Christ")
        self.assertEqual(candidate.votes, 10)
        
    def test_default_votes(self):
        candidate = Candidate.objects.create(name="Jesus Christ")
        self.assertEqual(candidate.votes, 0)

    def test_model_exists_in_db(self):
        Candidate.objects.create(name="Test User")
        self.assertEqual(Candidate.objects.count(), 1)