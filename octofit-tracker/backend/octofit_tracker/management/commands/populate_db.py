from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()

        # Create Teams
        marvel = Team.objects.create(name='marvel', description='Marvel Team')
        dc = Team.objects.create(name='dc', description='DC Team')

        # Create Users
        tony = User.objects.create(name='Tony Stark', email='tony@marvel.com', team=marvel.name)
        steve = User.objects.create(name='Steve Rogers', email='steve@marvel.com', team=marvel.name)
        bruce = User.objects.create(name='Bruce Wayne', email='bruce@dc.com', team=dc.name)
        clark = User.objects.create(name='Clark Kent', email='clark@dc.com', team=dc.name)

        # Create Activities
        Activity.objects.create(user=tony, activity_type='run', duration=30, date='2024-01-01')
        Activity.objects.create(user=steve, activity_type='cycle', duration=45, date='2024-01-02')
        Activity.objects.create(user=bruce, activity_type='swim', duration=25, date='2024-01-03')
        Activity.objects.create(user=clark, activity_type='yoga', duration=40, date='2024-01-04')

        # Create Leaderboard
        Leaderboard.objects.create(user=tony, score=120)
        Leaderboard.objects.create(user=steve, score=110)
        Leaderboard.objects.create(user=bruce, score=130)
        Leaderboard.objects.create(user=clark, score=125)

        # Create Workouts
        Workout.objects.create(name='Pushups', description='Do 20 pushups', difficulty='easy')
        Workout.objects.create(name='Pullups', description='Do 10 pullups', difficulty='medium')
        Workout.objects.create(name='Squats', description='Do 30 squats', difficulty='easy')
        Workout.objects.create(name='Plank', description='Hold plank for 1 min', difficulty='hard')

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
