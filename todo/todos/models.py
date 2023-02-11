from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=250)
    repo_link = models.URLField(null=True, blank=True)


class User(models.Model):
    project = models.OneToOneField(Project, related_name='user_set',
                                   on_delete=models.CASCADE)
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    email = models.EmailField()


class TODO(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()
    date = models.DateField()
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    active = models.BooleanField()


    def __str__(self):
        return self.title

