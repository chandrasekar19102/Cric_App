from django.db import models

# Create your models here.
class Organizer(models.Model):

    id = models.IntegerField(primary_key=True, null=False)
    name = models.CharField(max_length=255)
    created_at = models.TimeField(auto_now=True)
    updated_at = models.TimeField(auto_now=True)

    def __str__(self):
        return self.name

class Tournament(models.Model):

    id = models.IntegerField(primary_key=True, null=False)
    name = models.CharField(max_length=255)
    org = models.ForeignKey(Organizer, on_delete=models.CASCADE)
    created_at = models.TimeField(auto_now=True)
    updated_at = models.TimeField(auto_now=True)

    def __str__(self):
        return self.name

class Team(models.Model):
    
    id = models.IntegerField(primary_key=True, null=False)
    name = models.CharField(max_length=255)
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    created_at = models.TimeField(auto_now=True)
    updated_at = models.TimeField(auto_now=True)

    def __str__(self):
        return self.name

class Player(models.Model):

    id = models.IntegerField(primary_key=True, null=False)
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    is_captain = models.BooleanField(default=False)
    is_wicket_keeper = models.BooleanField(default=False)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    created_at = models.TimeField(auto_now=True)
    updated_at = models.TimeField(auto_now=True)
    

    def __str__(self):
        return self.name
    
class Matches(models.Model):

    id = models.IntegerField(primary_key=True, null=False)
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    team_a = models.ForeignKey(Team, on_delete=models.CASCADE)
    team_b = models.ForeignKey(Team, on_delete=models.CASCADE)
    toss_winning_team = models.ForeignKey(Team, on_delete=models.CASCADE, null=False)
    winning_team = models.ForeignKey(Team, on_delete=models.CASCADE, null=False)
    won_by_runs = models.IntegerField()
    won_by_wickets = models.IntegerField()
    created_at = models.TimeField(auto_now=True)
    updated_at = models.TimeField(auto_now=True)

    class meta:
        constraints = [
            models.CheckConstraint(
                check=~Q(team_a=F('team_b')),
                name = 'team_a_b_are_not_equal'
            )
        ]

    def __str__(self):
        return self.name

class Innings(models.Model):

    id = models.IntegerField(primary_key=True, null=False)
    id = models.ForeignKey(Matches,on_delete=models.CASCADE) 
    innings = models.IntegerField()
    innings_type = models.CharField(max_length=255)
    is_completed = models.BooleanField(default=False)
    batting_team = models.ForeignKey(Team,on_delete=models.CASCADE)
    bowling_team = models.ForeignKey(Team,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

class Overs(models.Model):

    id = models.IntegerField(primary_key=True, null=False)
    id = models.ForeignKey(Innings,on_delete=models.CASCADE) 
    over_number = models.IntegerField()
    bower = models.ForeignKey(Player, on_delete=models.CASCADE)
    is_completed = models.BooleanField(default=False)
      
    def __str__(self):
        return self.name

class Ball(models.Model):

    id = models.IntegerField(primary_key=True, null=False)
    id = models.ForeignKey(Overs,on_delete=models.CASCADE) 
    ball_number = models.IntegerField()
    striker = models.ForeignKey(Player, on_delete=models.CASCADE)
    non_striker = models.ForeignKey(Player, on_delete=models.CASCADE)
    bowler = models.ForeignKey(Player, on_delete=models.CASCADE)
    batter_run = models.IntegerField()
    extra_runs = models.IntegerField()
    extra_type = models.CharField(max_length=250)
    is_wicket = models.BooleanField(default=False)
    wicket_type = models.CharField(max_length=255)
    dismissed_player = models.ForeignKey(Player, on_delete=models.CASCADE)


    def __str__(self):
        return self.name