from django.db import models
from django.contrib.auth.models import User

    
    
#images   
class ImageUpload(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='image_uploads')
    image = models.ImageField(upload_to='trade_images/imgs/images/')
    description = models.CharField(max_length=255, blank=True)
    date_uploaded = models.DateTimeField(auto_now_add=True)
    
    

class TextUpload(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text_content = models.TextField()
    date_uploaded = models.DateTimeField(auto_now_add=True)
    
    
class Course(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.TextField(max_length=75)
    
     
class Technical(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.ForeignKey(Course, on_delete=models.CASCADE)
    image = models.ManyToManyField(ImageUpload, blank=True)
    texts = models.ManyToManyField(TextUpload, blank=True)
    date_uploaded = models.DateTimeField(auto_now_add=True)
    
     
    
class Fundamental(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.ForeignKey(Course, on_delete=models.CASCADE)
    image = models.ManyToManyField(ImageUpload, blank=True)
    texts = models.ManyToManyField(TextUpload, blank=True)
    date_uploaded = models.DateTimeField(auto_now_add=True)
    
     
class Risk(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.ForeignKey(Course, on_delete=models.CASCADE)
    image = models.ManyToManyField(ImageUpload, blank=True)
    texts = models.ManyToManyField(TextUpload, blank=True)
    date_uploaded = models.DateTimeField(auto_now_add=True)
    
    
    
class Analysis(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.ForeignKey(Course, on_delete=models.CASCADE)
    image = models.ManyToManyField(ImageUpload, blank=True)
    texts = models.ManyToManyField(TextUpload, blank=True)
    date_uploaded = models.DateTimeField(auto_now_add=True)
    
     
    
class Trick(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.ForeignKey(Course, on_delete=models.CASCADE)
    image = models.ManyToManyField(ImageUpload, blank=True)
    texts = models.ManyToManyField(TextUpload, blank=True)
    date_uploaded = models.DateTimeField(auto_now_add=True)
    
     
    
class Pschology(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.ForeignKey(Course, on_delete=models.CASCADE)
    image = models.ManyToManyField(ImageUpload, blank=True)
    texts = models.ManyToManyField(TextUpload, blank=True)
    date_uploaded = models.DateTimeField(auto_now_add=True)
    
     
    
class Pair(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.ForeignKey(Course, on_delete=models.CASCADE)
    image = models.ManyToManyField(ImageUpload, blank=True)
    texts = models.ManyToManyField(TextUpload, blank=True)
    date_uploaded = models.DateTimeField(auto_now_add=True)
    
    
 
    
    
 