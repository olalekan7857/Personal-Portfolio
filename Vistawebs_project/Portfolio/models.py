from django.db import models
from django.utils.html import mark_safe

# Create your models here.
class Contact_message(models.Model):
    name = models.CharField(max_length = 50, blank=False)
    phone_number = models.CharField(max_length = 20, blank=False)
    email = models.EmailField(blank=False)
    subject = models.CharField(max_length=255, blank=False)
    message = models.TextField(blank=False)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Contact_message'
        verbose_name_plural = 'Contact_messages'

    def __str__(self):
        return self.message  
    

class Tools(models.Model):
    tool_name = models.CharField(max_length=20, blank=False)

    class Meta:
        verbose_name = 'Tool'
        verbose_name_plural = 'Tools'

    def __str__(self):
        return self.tool_name
    

class Portfolio(models.Model):
    website_image = models.ImageField(upload_to='web_image', blank=False)
    website_name = models.CharField(max_length=100, blank=False)
    content = models.TextField(blank=True)
    tools = models.ManyToManyField(Tools, blank=False, related_name='mytool')
    website_url = models.URLField(blank=False)

    def flyer(self):
        return mark_safe(f"<img src='{self.website_image.url}' height='45' style='border-radius: 50%;'>")
    
    class Meta:
        verbose_name = 'Portfolio'
        verbose_name_plural = 'Portfolio'

    def __str__(self):
        return self.website_name
