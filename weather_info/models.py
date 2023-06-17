import json
from django.db import models
from django.contrib.postgres.fields import ArrayField


ORDER = ['rank-order', 'year-order']
REGION = [
    'UK', 
    'England', 
    'Wales', 
    'Scotland', 
    'Northern_Ireland', 
    'England_and_Wales', 
    'England_N', 
    'England_S', 
    'Scotland_N', 
    'Scotland_E', 
    'Scotland_W', 
    'England_E_and_NE', 
    'England_NW_and_N_Wales', 
    'Midlands', 'East_Anglia', 
    'England_SW_and_S_Wales', 
    'England_SE_and_Central_S'
]
PARAMETER = [
    'Tmax', 
    'Tmin', 
    'Tmean', 
    'Sunshine', 
    'Rainfall', 
    'Raindays1mm', 
    'AirFrost'
]

class Summary(models.Model):
    """
    weather-data summary model
    """
    order = models.CharField(
        max_length=100,
        choices=[(choice, choice) for choice in ORDER]
    )
    region = models.CharField(
        max_length=100,
        choices=[(choice, choice) for choice in REGION]
    )
    parameter = models.CharField(
        max_length=100,
        choices=[(choice, choice) for choice in PARAMETER]
    )
    data = ArrayField(models.JSONField(), null=True)

    def save(self, *args, **kwargs):
        # Convert dictionaries to JSON strings before saving
        self.data = [json.dumps(item) for item in self.data]
        super().save(*args, **kwargs)

    
    def __str__(self) -> str:
        return f'{self.region}__{self.parameter}'