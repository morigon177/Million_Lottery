from django.db import models
from django.core.validators import MinLengthValidator
from django.db.models.deletion import CASCADE

#属性マスタ
class Type(models.Model):
    TypeID = models.IntegerField()
    TypeName = models.CharField(max_length=10, validators=[MinLengthValidator(1)])
    
    class Meta:
        ordering = ('TypeID' , )
    
    def __str__(self):
        return str(self.Name)

#楽曲マスタ
class Song(models.Model):
    SongID = models.IntegerField()
    TypeName = models.ForeignKey(Type, db_column = 'TypeName' , on_delete = CASCADE)
    Name = models.CharField(max_length=50, validators=[MinLengthValidator(1)])
    AddDate = models.DateField()
    
    class Meta:
        ordering = ('SongID' , )
    
    def __str__(self):
        return str(str.SongID + ' > Type: ' + str.TypeName + ' Song Name: ' + str.Name + ' Add Date: ' + str.AddDate)
    
    