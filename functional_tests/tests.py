import time

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from election.models import Candidate

class visit_web(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        Candidate.objects.create(name="Julius Caesar", votes=0)

    def tearDown(self):
        self.browser.quit()

    def test_people_see_candidates(self):
        #people use the web-app "Election"
        self.browser.get(self.live_server_url)
        self.assertIn('Election', self.browser.title)

        #They see a big "Election" text
        header = self.browser.find_element(By.TAG_NAME,'h1')
        self.assertIn('Election',header.text)
        
        #They see the first candidate name as a link (Julius Caesar)
        first_candidate = self.browser.find_element(By.TAG_NAME,'h3')
        self.assertEqual('Julius Caesar ( คะแนนปัจจุบัน : 0 )',first_candidate.text)
        time.sleep(1)
        
        #He see button to vote
        submit_btn = self.browser.find_element(By.TAG_NAME,'button')
        self.assertEqual(submit_btn.text,"Vote")

        #He click the button
        submit_btn.click()

        #He redirect to same page
        header = self.browser.find_element(By.TAG_NAME,'h1')
        self.assertIn('Election',header.text)
        
        #Julius's vote point update
        first_candidate = self.browser.find_element(By.TAG_NAME,'h3')
        self.assertEqual('Julius Caesar ( คะแนนปัจจุบัน : 1 )' ,first_candidate.text)
        time.sleep(1)

        submit_btn = self.browser.find_element(By.TAG_NAME,'button')
        self.assertEqual(submit_btn.text,"Vote")
        submit_btn.click()
        

