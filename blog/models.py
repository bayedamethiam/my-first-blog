from django.conf import settings
from django.db import models
from django.utils import timezone

## creation of a model post that will have an author a title a text a created_date and a published_date
class Post(models.Model):
    #the author will be an intern  model from django that's why we have to tell to django that it a foreign key
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    ## this methode manage which properties is displayed when we call the model
    def __str__(self):
        return self.title