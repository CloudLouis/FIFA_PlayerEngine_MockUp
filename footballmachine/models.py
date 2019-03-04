from django.db import models

class Players(models.Model):
    Row = models.IntegerField()
    ID = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=50)
    Age = models.IntegerField()
    Photo = models.URLField(max_length=200)
    Nationality = models.CharField(max_length=50)
    Flag = models.URLField(max_length=200)
    Overall = models.IntegerField()
    Potential = models.IntegerField()
    Club = models.CharField(max_length=50)
    Club_Logo = models.URLField(max_length=200)
    Value = models.CharField(max_length=50)
    Wage = models.CharField(max_length=50)
    Special = models.IntegerField()
    Preferred_Foot = models.CharField(max_length=50)
    International_Reputation = models.IntegerField()
    Weak_Foot = models.IntegerField()
    Skill_Moves = models.IntegerField()
    Work_Rate = models.CharField(max_length=50)
    Body_Type = models.CharField(max_length=50)
    Real_Face = models.BooleanField()
    Position = models.CharField(max_length=50)
    Jersey_Number = models.IntegerField()
    Joined = models.DateField()
    Loaned_From = models.CharField(max_length=50)
    Contract_Valid_Until = models.CharField(max_length=50)
    Height = models.CharField(max_length=50)
    Weight = models.CharField(max_length=50)
    LS = models.CharField(max_length=50)
    ST = models.CharField(max_length=50)
    RS = models.CharField(max_length=50)
    LW = models.CharField(max_length=50)
    LF = models.CharField(max_length=50)
    CF = models.CharField(max_length=50)
    RF = models.CharField(max_length=50)
    RW = models.CharField(max_length=50)
    LAM = models.CharField(max_length=50)
    CAM = models.CharField(max_length=50)
    RAM = models.CharField(max_length=50)
    LM = models.CharField(max_length=50)
    LCM = models.CharField(max_length=50)
    CM = models.CharField(max_length=50)
    RCM = models.CharField(max_length=50)
    RM = models.CharField(max_length=50)
    LWB = models.CharField(max_length=50)
    LDM = models.CharField(max_length=50)
    CDM = models.CharField(max_length=50)
    RDM = models.CharField(max_length=50)
    RWB = models.CharField(max_length=50)
    LB = models.CharField(max_length=50)
    LCB = models.CharField(max_length=50)
    CB = models.CharField(max_length=50)
    RCB = models.CharField(max_length=50)
    RB = models.CharField(max_length=50)
    Crossing = models.IntegerField()
    Finishing = models.IntegerField()
    HeadingAccuracy = models.IntegerField()
    ShortPassing = models.IntegerField()
    Volleys = models.IntegerField()
    Dribbling = models.IntegerField()
    Curve = models.IntegerField()
    FKAccuracy = models.IntegerField()
    LongPassing = models.IntegerField()
    BallControl = models.IntegerField()
    Acceleration = models.IntegerField()
    SprintSpeed = models.IntegerField()
    Agility = models.IntegerField()
    Reactions = models.IntegerField()
    Balance = models.IntegerField()
    ShotPower = models.IntegerField()
    Jumping = models.IntegerField()
    Stamina = models.IntegerField()
    Strength = models.IntegerField()
    LongShots = models.IntegerField()
    Agression = models.IntegerField()
    Interceptions = models.IntegerField()
    Positioning = models.IntegerField()
    Vision = models.IntegerField()
    Penalties = models.IntegerField()
    Composure = models.IntegerField()
    Marking = models.IntegerField()
    StandingTackle = models.IntegerField()
    SlidingTackle = models.IntegerField()
    GKDiving = models.IntegerField()
    GKHandling = models.IntegerField()
    GKKicking = models.IntegerField()
    GKPositioning = models.IntegerField()
    GKReflexes = models.IntegerField()
    Release_Clause = models.CharField(max_length=50)

    def __str__(self):
        return self.Name