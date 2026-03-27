from django.test import TestCase
from .models import Candidate,Voter
from django.urls import reverse

class HomePageTest(TestCase):
    def setUp(self):
        self.candidate = Candidate.objects.create(name="John Roblox", votes=0)
        self.url = reverse('home') 

    def test_vote_increases_score(self):
        response = self.client.post(self.url, {'candidate_id': self.candidate.id})
        self.candidate.refresh_from_db()
        self.assertEqual(self.candidate.votes, 1)

    def test_redirect_after_vote(self):
        response = self.client.post(self.url, {'candidate_id': self.candidate.id})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, self.url)

    def test_cannot_vote_twice_with_same_id(self):
        candidate = Candidate.objects.create(name="Caesar")
        v_id = "VOTER123"

        self.client.post(self.url, {'voter_id': v_id, 'candidate_id': candidate.id})
        
        self.client.post(self.url, {'voter_id': v_id, 'candidate_id': candidate.id})

        candidate.refresh_from_db()
        self.assertEqual(candidate.votes, 1)

class LoginViewTest(TestCase):
    def setUp(self):
        self.login_url = reverse('login')
        self.home_url = reverse('home')

    def test_login_page_renders_correct_template(self):
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

    def test_login_stores_id_in_session(self):
        v_id = 'VOTER-123'
        response = self.client.post(self.login_url, {'voter_id': v_id})

        self.assertEqual(self.client.session['voter_id'], v_id)

        self.assertRedirects(response, self.home_url)

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