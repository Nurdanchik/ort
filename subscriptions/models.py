# from django.db import models
# from users.models import CustomUser
#
# class Subscription(models.Model):
#     id = models.AutoField(primary_key=True)
#     user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
#     start_date = models.DateField()
#     end_date = models.DateField()
#     status = models.BooleanField(default=False)