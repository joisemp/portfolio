from email import message
from turtle import title
from django.db import models
import sys
import PIL
from django.core.files.uploadedfile import InMemoryUploadedFile
from io import BytesIO


class ProgrammingProject(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    year = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/programming_projects/')
    summary = models.TextField(null=True, blank=True)
    link = models.CharField(null=True, blank=True, max_length=300)
    
    def save(self):
        # Opening the uploaded image
        im = PIL.Image.open(self.image)

        output = BytesIO()

        # Resize/modify the image
        im = im.resize((1024, 768))

        # after modifications, save it to the output
        im.save(output, format='JPEG', quality=90)
        output.seek(0)

        # change the imagefield value to be the newley modifed image value
        self.image = InMemoryUploadedFile(output, 'ImageField', "%s.jpg" % self.image.name.split('.')[0], 'image/jpeg',
                                          sys.getsizeof(output), None)

        super(ProgrammingProject, self).save()
    
    def __str__(self):
        return(self.title)
    

class Contact(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    full_name = models.CharField(max_length=300)
    email_id = models.CharField(max_length=300)
    subject = models.CharField(max_length=300)
    message = models.TextField()
    
    def __str__(self):
        return str(self.full_name)
