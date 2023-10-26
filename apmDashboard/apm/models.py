from django.db import models

# Create your models here.
class Application(models.Model):
    url = models.URLField()
    name = models.CharField(max_length=100)
    technology_stack = models.CharField(max_length=100)
    server_type = models.CharField(max_length=20, choices=[('DB', 'Database'), ('Web App', 'Web Application')])
    # Database Server & Application Server or Both  Server
    operating_system = models.CharField(max_length=20, choices=[('Windows', 'Windows'), ('Linux', 'Linux')])
    monitoring = models.CharField(max_length=50)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
