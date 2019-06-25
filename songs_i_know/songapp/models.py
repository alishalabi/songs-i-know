from django.db import models

SKILL_CHOICES = (
    ('novice', 'Novice'),
    ('intermediate', 'Intermediate'),
    ('advanced', 'Advanced'),
    ('black_belt', 'Black Belt'),
)

# Create your models here.


class Song(models.Model):
    song_name = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    youtube_tutorial = models.CharField(
        max_length=300, blank=True, default='')
    song_tab = models.CharField(max_length=100, blank=True, default='')
    lyrics = models.CharField(max_length=2000, blank=True, default='')
    skill_level = models.CharField(
        max_length=200, choices=SKILL_CHOICES, default='intermediate')

    def __str__(self):
        return self.song_name
