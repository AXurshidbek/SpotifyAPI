from django.db import models

class Qoshiqchi(models.Model):
    ism=models.CharField(max_length=35)
    tugilgan_sana=models.DateField()
    davlat=models.CharField(max_length=35)

    def __str__(self):
        return self.ism

class Albom(models.Model):
    nom=models.CharField(max_length=35)
    sana=models.DateField()
    rasm=models.FileField()
    qoshiqchi=models.ForeignKey(Qoshiqchi, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.nom


class Qoshiq(models.Model):
    nom=models.CharField(max_length=35)
    janr=models.CharField(max_length=25)
    davomiylik=models.DurationField(blank=True, null=True)
    fayl=models.FileField(null=True)
    albom=models.ForeignKey(Albom, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom