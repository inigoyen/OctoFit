from djongo import models

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.name

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    team_name = models.CharField(max_length=100, blank=True, null=True)
    is_superhero = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name

class Activity(models.Model):
    user_email = models.EmailField()
    type = models.CharField(max_length=100)
    duration = models.PositiveIntegerField()  # minutos
    date = models.DateField()
    
    def __str__(self):
        return f"{self.user_email} - {self.type} ({self.date})"

class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    suggested_for_emails = models.JSONField(default=list, blank=True)
    
    def __str__(self):
        return self.name

class Leaderboard(models.Model):
    user_email = models.EmailField()
    score = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return f"{self.user_email}: {self.score}"
