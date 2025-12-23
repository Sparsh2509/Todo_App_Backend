from django.db import models

class Task(models.Model):

    PRIORITY_CHOICES = [
        ('L', 'Low'),
        ('M', 'Medium'),
        ('H', 'High'),
    ]

    # Basic task info
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    # Extra basic features
    priority = models.CharField(
        max_length=1,
        choices=PRIORITY_CHOICES,
        default='M'
    )
    category = models.CharField(max_length=50)

    # Date & time
    task_date = models.DateField()
    start_time = models.TimeField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)

    # Toggle field (IMPORTANT)
    completed = models.BooleanField(default=False)

    # Auto fields
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject
