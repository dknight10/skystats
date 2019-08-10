from django.db import models


class Session(models.Model):
    name = models.CharField(max_length=100)
    timestamp = models.DateTimeField()
    session_type = models.CharField(max_length=20)  # TODO add choices
    user = models.EmailField()

    def __str__(self):
        return f"Session<name={self.name}, timestamp={self.timestamp}, \
            session_type={self.session_type} user={self.user}>"

    class Meta:
        ordering = ["-timestamp"]
        indexes = [models.Index(fields=["user"])]
        constraints = [
            models.UniqueConstraint(
                fields=["timestamp", "session_type"], name="unique_session"
            )
        ]

    @property
    def clubs_used(self):
        clubs = set()
        for shot in self.shots.all():
            clubs.add(shot.club)
        return list(clubs)

    @property
    def clubs_used_str(self):
        return ", ".join(self.clubs_used)

    @property
    def shots_count(self):
        return self.shots.all().count()


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
    session = models.ForeignKey(Session, on_delete=models.CASCADE, related_name="shots")

    class Meta:
        indexes = [models.Index(fields=["club"])]
