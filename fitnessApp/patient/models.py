from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from rest_framework import serializers

# Create your models here.
class Patient(models.Model):

    id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=200,blank=False,verbose_name="Patient's first mame")
    lastname = models.CharField(max_length=200,null=False,verbose_name="Patient's last mame")
    identitynumber = models.CharField(max_length=13,verbose_name="Patient's Identity Number")
    province = models.CharField(max_length=200,null=False,verbose_name="Patient's residential Province")
    region = models.CharField(max_length=200,null=False,verbose_name="Patient's region")
    location = models.CharField(max_length=200,null=False,verbose_name="Patient's location")
    status = models.IntegerField(choices=((0,'created'),(1,'updated'),(2,'deleted')),verbose_name="Patient account status",default="0")
    creationdate = models.DateField(default=timezone.now(),null=False,verbose_name="Patient's record creation date")
    
    # class Meta:
    #     unique_together = ('id','firstname','lastname','identitynumber')
    #     ordering = ['id']

    # def __unicode__(self):
    #     return '%s %s' % (self.firstname,self.lastname)

    # def __str__(self):
    #     return ";".join(["FirstName: " + self.firstname,"LastName: " + self.lastname,"Id Number: " + self.identitynumber,"Location: " + self.location,"Created: " + str(self.creationdate)])

# class PatientSerializer(serializers.ModelSerializer):
#     firstname = serializers.CharField(max_length=200)
#     lastname = serializers.CharField(max_length=200)
#     identitynumber = serializers.CharField(max_length=13)
#     province = serializers.CharField(max_length=200)
#     region = serializers.CharField(max_length=200)
#     location = serializers.CharField()
#     status = serializers.IntegerField()
#     creationdate = serializers.DateField()

#     class Meta:
#         model = Patient
#         fields = ('firstname','lastname','identitynumber','province','region','location','status','creationdate') 

class Parent(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)

class Child(models.Model):
    child = models.ForeignKey(Parent,related_name="child",on_delete=models.CASCADE)
    order = models.IntegerField()
    name=models.CharField(max_length=20)

    class Meta:
        unique_together = ('child','order')

    def __unicode__(self):
        return '%s:%s' % (self.order,self.name)

class ParentSerializer(serializers.ModelSerializer):
    child = serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name='child-detail')
    class Meta:
        model = Parent
        fields = ('name','surname','child')

