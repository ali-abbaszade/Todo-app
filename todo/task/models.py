from django.db import models



PRIORITY_CHOICES = (
    (1, 'High priority'),
    (2, 'Middle priority'),
    (3, 'Low priority') 
)
class Task(models.Model):
    body = models.CharField(max_length=300)
    # user
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    status = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)    
    updated_date = models.DateTimeField(auto_now=True)    

    class Meta:
        ordering = ['priority', 'status']

    def __str__(self):
        return self.body    
