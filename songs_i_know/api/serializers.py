from rest_framework import serializers

from songs_i_know.songapp.models import Song


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = '__all__'
