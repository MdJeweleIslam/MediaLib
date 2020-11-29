from django.db import models

# Create your models here.


class Label(models.Model):
	label_id = models.AutoField(primary_key=True)
	label_name = models.CharField(max_length=100)
	label_youtube_channel_link = models.CharField(max_length=100)
	label_fb_page_link = models.CharField(max_length=100)

	def __str__(self):
		return str(self.label_name)

class Artist(models.Model):
	artist_id = models.AutoField(primary_key=True)
	artist_name = models.CharField(max_length=100)
	artist_fb = models.CharField(max_length=100, null=True, blank=True)
	artist_twitter = models.CharField(max_length=100, null=True, blank=True)

	def __str__(self):
		return str(self.artist_name)

class VideoType(models.Model):
	type_id = models.AutoField(primary_key=True)
	type_name = models.CharField(max_length=100)

	def __str__(self):
		return str(self.type_name)

class Cast(models.Model):
	cast_id = models.AutoField(primary_key=True)

	def __str__(self):
		return str(self.cast_id)

class CastByArtish(models.Model):
	cast_by_artist_id = models.AutoField(primary_key=True)
	cast_id = models.ForeignKey(Cast, on_delete=models.CASCADE)
	artist_id = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='cast')

	def __str__(self):
		return str(self.cast_by_artist_id)


class Songs(models.Model):
	song_id = models.AutoField(primary_key=True)
	song_name = models.CharField(max_length=255, unique=True)
	youtube_link = models.CharField(null=True, blank=True, max_length=100)
	song_writer = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='song_writer', null=True, blank=True)
	song_music = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='song_music', null=True, blank=True)
	song_lyricist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='song_lyricist', null=True, blank=True)
	song_director = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='song_director', null=True, blank=True)

	def __str__(self):

		return str(self.song_name)


class Video(models.Model):
	video_id = models.AutoField(primary_key=True)
	video_title = models.CharField(max_length=255, unique=True)
	video_type = models.ForeignKey(VideoType, on_delete=models.CASCADE)
	video_details = models.TextField()
	youtube_link = models.CharField(null=True, blank=True, max_length=100)
	datetime = models.DateTimeField(auto_now_add=True)
	cast_id = models.ForeignKey(Cast, on_delete=models.CASCADE, related_name='video_cast')
	video_story = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='story', null=True, blank=True)
	video_director = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='director', null=True, blank=True)
	lebel = models.ForeignKey(Label, on_delete=models.CASCADE, related_name='label', null=True, blank=True)
	song_id = models.ForeignKey(Songs, on_delete=models.CASCADE, related_name='songs', null=True, blank=True)

	def __str__(self):

		return str(self.video_title)



