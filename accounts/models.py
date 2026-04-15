from django.db import models

class User(models.Model):
    idusers = models.AutoField(primary_key=True)
    user = models.CharField(max_length=150, unique=True)
    pass_field = models.CharField(db_column='pass', max_length=128)

    class Meta:
        db_table = 'users'  # Refleja la tabla existente en MySQL

    def __str__(self):
        return self.user
