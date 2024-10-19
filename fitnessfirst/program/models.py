from django.db import models

class MembershipPlan(models.Model):
    image = models.ImageField(upload_to='program_images/')
    program_title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.program_title
