from django.db import models


# TODO add validators for number fields
class Shot(models.Model):
    HAND_CHOICES = [("L", "left"), ("R", "right")]
    shot_num = models.IntegerField()
    hand = models.CharField(max_length=1, choices=HAND_CHOICES)
    ball_speed = models.IntegerField()
    launch_angle = models.DecimalField(max_digits=3, decimal_places=1)
    back_spin = models.IntegerField()
    side_spin = models.IntegerField()
    side_angle = models.DecimalField(max_digits=3, decimal_places=1)
    offline_distance = models.IntegerField()
    carry = models.IntegerField()
    roll = models.IntegerField()
    total = models.IntegerField()
    hang_time = models.DecimalField(max_digits=3, decimal_places=1)
    descent_angle = models.DecimalField(max_digits=3, decimal_places=1)
    peak_height = models.IntegerField()
    club_speed = models.IntegerField()
    pti = models.DecimalField(max_digits=3, decimal_places=2)
    club = models.CharField(max_length=20)  # TODO add choices
    name = models.CharField(max_length=100)
    timestamp = models.DateTimeField()
    session_type = models.CharField(max_length=20)  # TODO add choices

    class Meta:
        ordering = ["-timestamp"]
        indexes = [models.Index(fields=["club"]), models.Index(fields=["timestamp"])]
