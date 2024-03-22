from django.db import models
from django.contrib.auth.models import User

""""
class Subscriber(models.Model):
    email = models.EmailField(unique=True)
"""


# notifications
class Notification(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='notification_images/', null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

#conversations
class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    
    
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
    
    

    
#permission
    """
    # Example in models.py
from django.contrib.contenttypes.models import ContentType
from django.db import models

class MyModel(models.Model):
    # Your fields here
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)

"""
    
    
 