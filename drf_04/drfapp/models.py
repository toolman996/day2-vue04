from django.db import models

class Message(models.Model):
    sex_chooices=(
        (0,'男'),
        (1,'女'),
    )

    name=models.CharField(max_length=66)
    age=models.CharField(max_length=66)
    sex=models.SmallIntegerField(choices=sex_chooices,default=0)

    class Meta:
        db_table='tb_information'
        verbose_name='个人信息'
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.name

