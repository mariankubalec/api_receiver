from django.db import models

class Body(models.Model):
    body_text = models.CharField(max_length=500)

    def __str__(self):
        return str(self.body_text)
    
    def get_body_text(self):
        return self.body_text
