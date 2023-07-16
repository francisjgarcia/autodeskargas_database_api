from django.db import models


class Website(models.Model):
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255)


class User(models.Model):
    username = models.CharField(max_length=255)
    password = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Role(models.Model):
    name = models.CharField(max_length=255)


class RoleUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class ApplicationUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class ApplicationUserTelegram(models.Model):
    username = models.CharField(max_length=255)
    username_id = models.IntegerField()
    application_user = models.ForeignKey(ApplicationUser, on_delete=models.CASCADE)
    state_id = models.IntegerField()


class ApplicationUserDiscord(models.Model):
    username = models.CharField(max_length=255)
    username_id = models.IntegerField()
    application_user = models.ForeignKey(ApplicationUser, on_delete=models.CASCADE)
    state_id = models.IntegerField()


class ApplicationUserState(models.Model):
    state_id = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)


class UserState(models.Model):
    name = models.CharField(max_length=255)


class Movie(models.Model):
    name = models.CharField(max_length=255)
    year = models.DateTimeField()


class Series(models.Model):
    name = models.CharField(max_length=255)


class SeriesSeason(models.Model):
    number = models.IntegerField()
    series = models.ForeignKey(Series, on_delete=models.CASCADE)
    chapter = models.IntegerField(unique=True)
    year = models.DateTimeField()


class SeriesSeasonChapter(models.Model):
    number = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)


class ResourceType(models.Model):
    name = models.CharField(max_length=255)


class Resource(models.Model):
    resource_type = models.ForeignKey(ResourceType, on_delete=models.CASCADE)
    resource_id = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)


class Link(models.Model):
    name = models.CharField(max_length=255)
    poster_url = models.CharField(max_length=255)
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)
    website = models.ForeignKey(Website, on_delete=models.CASCADE)
    quality_id = models.IntegerField()


class Quality(models.Model):
    name = models.CharField(max_length=255)


class DownloadHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    link = models.ForeignKey(Link, on_delete=models.CASCADE)
    state_id = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)


class DownloadHistoryState(models.Model):
    name = models.CharField(max_length=255)
