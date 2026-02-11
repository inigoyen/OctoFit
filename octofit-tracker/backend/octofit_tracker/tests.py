from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelSmokeTest(TestCase):
    def test_team_create(self):
        t = Team.objects.create(name='TestTeam', description='desc')
        self.assertEqual(str(t), 'TestTeam')
    def test_user_create(self):
        t = Team.objects.create(name='T', description='d')
        u = User.objects.create(name='U', email='u@t.com', team_name='T', is_superhero=True)
        self.assertEqual(str(u), 'U')
    def test_activity_create(self):
        a = Activity.objects.create(user_email='u@t.com', type='Run', duration=10, date='2026-01-01')
        self.assertEqual(str(a), 'u@t.com - Run (2026-01-01)')
    def test_workout_create(self):
        w = Workout.objects.create(name='W', description='d', suggested_for_emails=['u@t.com'])
        self.assertEqual(str(w), 'W')
    def test_leaderboard_create(self):
        l = Leaderboard.objects.create(user_email='u@t.com', score=42)
        self.assertEqual(str(l), 'u@t.com: 42')
