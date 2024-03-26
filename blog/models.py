from django.db import models
from django.shortcuts import reverse

class Post(models.Model):
    STATUS_CHOICES= (   #data == cte
        ('pub','Published'),
        ('drf','Draft'),
    )
# Hint: app User is a table and created by django and we cant change variable so we should change user model(write by ourself), dont migrate!!! create new class and inheritance user ex: class CustomUser(User) after that migrate.
    title = models.CharField(max_length=100)
    text = models.TextField()
    author =models.ForeignKey('auth.User', on_delete=models.CASCADE)  # django has login app -> auth -> have a table user/ CASCADE -> delete user == delete relation posts
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)
    status = models.CharField(choices= STATUS_CHOICES, max_length=5)

    def __str__(self):
        return self.title

    def get_absolute_url(self):    #what is your unique url -> any post have a unique url /blog/<int>/
        return reverse('post_detail', args=[self.id])

