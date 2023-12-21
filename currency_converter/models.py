from django.db import models

class EventInsert(models.Model):
    from_currency = models.CharField(max_length=45)
    target_currency = models.CharField(max_length=45)
    from_price = models.CharField(max_length=45)
    target_price = models.CharField(max_length=45)
    class Meta:
        db_table="events"