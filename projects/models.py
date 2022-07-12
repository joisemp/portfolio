from django.db import models
import sys
import PIL
from django.core.files.uploadedfile import InMemoryUploadedFile
from io import BytesIO

from django.dispatch import receiver
from django.db.models.signals import pre_delete

class Project(models.Model):
    project_type = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    year = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/programming_projects/')
    summary = models.TextField()
    primary_button_text = models.CharField(
        null=True, blank=True, max_length=300)
    primary_link = models.CharField(null=True, blank=True, max_length=300)
    primary_button_icon = models.CharField(
        null=True, blank=True, max_length=300)
    secondary_button_text = models.CharField(
        null=True, blank=True, max_length=300)
    secondary_link = models.CharField(null=True, blank=True, max_length=300)
    secondary_button_icon = models.CharField(
        null=True, blank=True, max_length=300)
    python = models.BooleanField(null=True, blank=True)
    bootstrap = models.BooleanField(null=True, blank=True)
    figma = models.BooleanField(null=True, blank=True)
    html = models.BooleanField(null=True, blank=True)
    js = models.BooleanField(null=True, blank=True)
    react = models.BooleanField(null=True, blank=True)
    scss = models.BooleanField(null=True, blank=True)
    github = models.BooleanField(null=True, blank=True)

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

        super(Project, self).save()

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


@receiver(pre_delete, sender=Project)
def Carousel_delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    instance.image.delete(False)