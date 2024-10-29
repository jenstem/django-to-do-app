from django.db import models
import datetime

class Task(models.Model):
    """
    Represents a task in the application.

    Attributes:
        name (str): The name of the task.
        priority (int): The priority level of the task.
        date (date): The date associated with the task, defaulting to today.
    """
    def __str__(self):
        """
        Returns the string representation of the Task instance.

        Returns:
            str: The name of the task.
        """
        return self.name

    name = models.CharField(max_length=100)
    priority = models.IntegerField()
    date = models.DateField(default=datetime.date.today)
