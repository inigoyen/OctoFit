from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Borrar datos existentes
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()

        # Crear equipos
        marvel = Team.objects.create(name='Marvel', description='Equipo Marvel')
        dc = Team.objects.create(name='DC', description='Equipo DC')

        # Crear usuarios
        users = [
            User(name='Spider-Man', email='spiderman@marvel.com', team_name='Marvel', is_superhero=True),
            User(name='Iron Man', email='ironman@marvel.com', team_name='Marvel', is_superhero=True),
            User(name='Wonder Woman', email='wonderwoman@dc.com', team_name='DC', is_superhero=True),
            User(name='Batman', email='batman@dc.com', team_name='DC', is_superhero=True),
        ]
        for user in users:
            user.save()

        # Crear actividades
        Activity.objects.create(user_email='spiderman@marvel.com', type='Correr', duration=30, date=timezone.now().date())
        Activity.objects.create(user_email='ironman@marvel.com', type='Nadar', duration=45, date=timezone.now().date())
        Activity.objects.create(user_email='wonderwoman@dc.com', type='Bicicleta', duration=60, date=timezone.now().date())
        Activity.objects.create(user_email='batman@dc.com', type='Yoga', duration=40, date=timezone.now().date())

        # Crear workouts
        w1 = Workout.objects.create(name='Entrenamiento Marvel', description='Rutina para héroes Marvel', suggested_for_emails=['spiderman@marvel.com', 'ironman@marvel.com'])
        w2 = Workout.objects.create(name='Entrenamiento DC', description='Rutina para héroes DC', suggested_for_emails=['wonderwoman@dc.com', 'batman@dc.com'])

        # Crear leaderboard
        Leaderboard.objects.create(user_email='spiderman@marvel.com', score=100)
        Leaderboard.objects.create(user_email='ironman@marvel.com', score=80)
        Leaderboard.objects.create(user_email='wonderwoman@dc.com', score=90)
        Leaderboard.objects.create(user_email='batman@dc.com', score=95)

        self.stdout.write(self.style.SUCCESS('La base de datos octofit_db ha sido poblada con datos de prueba.'))
