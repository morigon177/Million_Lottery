from django.db import models
from django.core.validators import MinLengthValidator
from django.db.models.deletion import CASCADE

class Type(models.Model):
    TypeID = models.IntegerField()
    TypeName = models.CharField(max_length=10, validators=[MinLengthValidator(1)])
    
    class Meta:
        ordering = ('TypeID' , )
    
    def __str__(self):
        return str(self.TypeName)

class Song(models.Model):
    SongID = models.IntegerField()
    TypeName = models.ForeignKey(Type, db_column = 'TypeName' , on_delete = CASCADE)
    SongName = models.CharField(max_length=50, validators=[MinLengthValidator(1)])
    AddDate = models.DateField()
    
    class Meta:
        ordering = ('SongID' , )
    
    def __str__(self):
        output = (str(self.SongName) + "     :   (" + str(self.TypeName) + ")   ,  AddDate - " + str(self.AddDate))
        return  output  
    