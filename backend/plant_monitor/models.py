from django.db import models

class Plant(models.Model):
    name = models.CharField(max_length=200)  # اسم گیاه
    species = models.CharField(max_length=200)  # گونه گیاه
    water_interval = models.IntegerField()  # فاصله زمانی آبیاری به روز
    temperature_range = models.CharField(max_length=100)  # محدوده دمایی گیاه

    def __str__(self):
        return self.name

class HealthStatus(models.Model):
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)  # ارتباط با مدل گیاه
    humidity = models.FloatField()  # رطوبت
    temperature = models.FloatField()  # دما
    light = models.FloatField()  # میزان نور
    status_date = models.DateTimeField(auto_now_add=True)  # تاریخ ثبت وضعیت

    def __str__(self):
        return f"{self.plant.name} - {self.status_date}"
