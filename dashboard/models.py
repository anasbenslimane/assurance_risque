from django.db import models


class PredictionHistory(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)

    Exposure = models.FloatField()
    VehPower = models.IntegerField()
    VehAge = models.IntegerField()
    DrivAge = models.IntegerField()
    BonusMalus = models.IntegerField()

    VehBrand = models.CharField(max_length=10)
    VehGas = models.CharField(max_length=20)
    Area = models.CharField(max_length=5)
    Density = models.IntegerField()
    Region = models.CharField(max_length=50)

    prediction = models.CharField(max_length=20)
    claim_probability = models.FloatField()
    risk_level = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.created_at:%d/%m/%Y %H:%M} - {self.prediction}"