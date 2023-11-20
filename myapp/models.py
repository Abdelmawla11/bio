from django.db import models

class Me(models.Model):

    name = models.CharField(max_length=10)
    photo = models.ImageField(upload_to='profile/' , default='profile/foto.jpg')
    about = models.TextField(max_length=500)

    class Meta:
        verbose_name = "About you"

    def __str__(self):
        return self.name

class Hobby(models.Model):

    hobbyname = models.CharField(max_length=10)
    bio = models.TextField(max_length=300)
    music = models.TextField(max_length=300)
    presonal = models.TextField(max_length=300)
    education = models.TextField(max_length=300)
    

    def __str__(self):
        return self.hobbyname

class Slide(models.Model):

    title = models.CharField(max_length=20)
    image = models.ImageField(upload_to='slides/')

    def __str__(self):
        return self.title

class Video(models.Model):

    title = models.CharField(max_length=10)
    video = models.FileField(upload_to='video/',null=True)

    def __str__(self):
        return self.title


class text(models.Model):

    username = models.CharField(max_length=10, null=1, blank=False)
    useremail = models.EmailField(null=1, blank=False)
    usermessage = models.TextField(blank=False, primary_key=True)

    def __str__ (self):
        return self.username

class Link(models.Model):

    owner = models.CharField(max_length=10)
    linked = models.URLField(max_length=150)
    telgram = models.URLField(max_length=150)
    meta = models.URLField(max_length=150)

    def __str__(self):
        return self.owner
    
    class Meta:
        verbose_name = "Social media link"
 