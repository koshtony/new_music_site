from django.db import models
from rembg import remove
from PIL import Image

# Create your models here.

class Latest(models.Model):

    description = models.TextField()
    link= models.URLField(max_length=1000,verbose_name="paste link of latest youtube video")
'''
This details to be posted on about section
'''
class About(models.Model):

    about = models.TextField()
    description = models.TextField()
    image = models.ImageField(upload_to='about_images')

    # remove image background
    '''
    def save(self):
        super().save() 

        img = Image.open(self.image.path)
        new_img = remove(img)
        new_img.save(self.image.path)
    '''

        

class Playlist(models.Model):

    title  = models.CharField(max_length=100)
    playlist = models.CharField(max_length=1000, verbose_name="paste embed code for youtube playlist" ,default="")

    def __str__(self):

        return str(self.title)
    
class Album(models.Model):

    title = models.CharField(max_length=100)
    image = models.ImageField()
    link = models.CharField(max_length=1000, verbose_name = "paste embed code for youtube album", default="")

    def __str__(self):

        return str(self.title)
    
    def save(self):
        super().save() 

        img = Image.open(self.image.path)

        if img.height > 500 or img.width > 800:
            new_img = (300, 800)
            img.thumbnail(new_img)
            img.save(self.image.path)
    
class Events(models.Model):

    title = models.CharField(max_length=100)
    description = models.TextField()
    pin_location = models.TextField(null=True)
    date = models.DateField()
    image = models.ImageField(upload_to='events_images')

    def save(self):
        super().save() 

        img = Image.open(self.image.path)

        if img.height > 500 or img.width > 800:
            new_img = (300, 800)
            img.thumbnail(new_img)
            img.save(self.image.path)


class Blog(models.Model):

    title = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateField()
    image = models.ImageField(upload_to='events_images')

    def save(self):
        super().save() 

        img = Image.open(self.image.path)

        if img.height > 500 or img.width > 800:
            new_img = (300, 800)
            img.thumbnail(new_img)
            img.save(self.image.path)







    


