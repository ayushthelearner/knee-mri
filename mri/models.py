from django.db import models

# Create your models here.

from django.db import models

class MRIImage(models.Model):
    image = models.ImageField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    result = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"MRI Image {self.id}"
