from django.db import models
from datetime import date
from django.contrib import admin
# Create your models here.
Vacancy_posts=[('principal','Principal'),('PGT (Physics)','PGT (Physics)'),('PGT (Chemistry)','PGT (Chemistry)'),('PGT (Maths)','PGT (Maths)'),
               ('PGT (Biology)','PGT (Biology)'),('PGT (Computer)','PGT (Computer)'),('PGT (Economics)','PGT (Economics)'), 
               ('PGT (Commerce)','PGT (Commerce)'),('PGT (English)','PGT (English)'),('PGT (Hindi)','PGT (Hindi)'),('TGT (Science)','TGT (Science)'),
               ('TGT (Maths)','TGT (Maths)'),('TGT (Sanskrit)','TGT (Sanskrit)'),('TGT (Social Science)','TGT (Social Science)'),
               ('TGT (English)','TGT (English)'),('TGT (Hindi)','TGT (Hindi)'),('PRT','PRT'),('SSA','SSA'),('Lab Attendant','Lab Attendant'),
               ('Sub Staff','Sub Staff'),('JR. Secratariat Assistant','JR. Secratariat Assistant')]
from django.db import models

class Class(models.Model):
    class_name=models.CharField(max_length=16)
    def __str__(self) :
        return f"{self.class_name}"
class principals_message(models.Model):
    message=models.TextField()
    image=models.ImageField(upload_to='website/images/' ,blank=False ,null=False)

class Alumni(models.Model):
    name=models.CharField(max_length=64)
    image=models.ImageField(upload_to='website/images/' ,blank=False ,null=False)
    description_of_acheivement=models.TextField(max_length=128)
    def __str__(self):
        return f"{self.name}"
class News_letter(models.Model):
    title=models.CharField(max_length=32)
    file=models.FileField(upload_to='website/files',blank=False,null=False)
    def __str__(self) :
        return f"{self.title}"
class TC(models.Model):
    serial_number=models.BigIntegerField(primary_key=True,unique=True)
    name=models.CharField(max_length=32,blank=False,null=False)
    parents_name=models.CharField(max_length=32,blank=False,null=False)
    date_of_birth=models.DateField(blank=False,null=False)
    Admission_number=models.BigIntegerField(blank=False,null=False)
    Class_left=models.ForeignKey(Class,related_name='TCs_issued_by_class',blank=False,null=False,on_delete=models.CASCADE)
    TC_no=models.BigIntegerField(unique=True,blank=False,null=False,)
    issue_date=models.DateField(blank=False,null=False,)
    def __str__(self):
        return f"{self.name}"
class vmc_member(models.Model):
    name=models.CharField(max_length=128)
    post=models.CharField(max_length=32)
    address=models.CharField(max_length=128)
    def __str__(self):
        return f"{self.name}"
class member_list(models.Model):
    name=models.CharField(max_length=32)
    designation=models.CharField(choices=Vacancy_posts,max_length=32)
    origin=models.CharField(choices=[("Local","Local"),("Indian","Indian")],null=False,blank=False,max_length=6)
    def __str__(self):
        return f"{self.name},{self.designation}"
class Vacancy(models.Model):
    number=models.IntegerField()
    vacant_designation=models.CharField(choices=Vacancy_posts,max_length=32)
    def __str__(self):
        return f"{self.vacant_designation}"
class Notice(models.Model):
    file=models.FileField(upload_to='website/files',blank=False,null=False)
    title=models.TextField(blank=False)
    description=models.TextField(blank=False)
    def __str__(self):
        return f"{self.title}"
class News_and_Events(models.Model):
    id=models.IntegerField(primary_key=True,auto_created=True,blank=False,null=False)
    title=models.TextField(blank=False)
    description=models.TextField(blank=False)
    def __str__(self):
        return f"{self.title}"
class Fee_structure(models.Model):
    file=models.FileField(upload_to='website/files',blank=False,null=False)
    def __str__(self):
        return f"Fee structure for the year {date.today().year}"
class Holiday(models.Model):
    name=models.TextField(max_length=32,blank=False,null=False)
    start_date=models.DateField(blank=False,null=False)
    end_date=models.DateField(default=None)
    category=models.CharField(choices=
                              (('holiday','Holiday'),('summer_vacation','Summer Vacation'),('winter_vacation','Winter Vacation'),('autum_vacation','Autum Vacation')),
                              max_length=32)
    def __str__(self):
        return f"{self.name}"
class Carousel_image(models.Model):
        image_1=models.ImageField(upload_to='website/images/' ,blank=False ,null=False)
        image_2=models.ImageField(upload_to='website/images/' ,blank=False ,null=False)
        image_3=models.ImageField(upload_to='website/images/' ,blank=False ,null=False)
        image_4=models.ImageField(upload_to='website/images/' ,blank=False ,null=False)
class News_and_Events_GalleryAdmin(admin.ModelAdmin):
    exclude= ('id',)
class quote(models.Model):
    quote=models.TextField()
    last_updated=models.DateField()
    author=models.TextField()

class Gallery(models.Model):
    id=models.IntegerField(primary_key=True,auto_created=True,blank=False,null=False)
    title=models.TextField(blank=False)
    def __str__(self):
        return f"{self.title}"
    
class Images(models.Model):
    event=models.ForeignKey(News_and_Events,on_delete=models.CASCADE,related_name='images',blank=True,null=True)
    gallery=models.ForeignKey(Gallery,on_delete=models.CASCADE,related_name='images',blank=True,null=True)
    image=models.ImageField(upload_to='website/images/' ,blank=False ,null=False)
    def __str__(self):
        if self.event:
            return f"{self.event}"
        else:
            return f"{self.gallery}"
class Committies(models.Model):
    Committee_name=models.TextField(choices=(('Admissions','Admissions'),('Academic advisory','Academic_Advisory'),('Examination','Examination'),('Transpotation','Transpotation')))
    members=models.ManyToManyField(member_list,related_name='committees')
