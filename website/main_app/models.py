from django.db import models
from datetime import date
from django.contrib import admin
from django.utils import timezone
# Create your models here.
# A B C is for sorting (computername,displayname)
Vacancy_posts=[('APrincipal','Principal'),('BPGT (Physics)','PGT (Physics)'),('BPGT (Chemistry)','PGT (Chemistry)'),('BPGT (Maths)','PGT (Maths)'),
               ('BPGT (Biology)','PGT (Biology)'),('BPGT (Computer)','PGT (Computer)'),('BPGT (Economics)','PGT (Economics)'), 
               ('BPGT (Commerce)','PGT (Commerce)'),('BPGT (English)','PGT (English)'),('BPGT (Hindi)','PGT (Hindi)'),('CTGT (Science)','TGT (Science)'),
               ('CTGT (Maths)','TGT (Maths)'),('CTGT (Sanskrit)','TGT (Sanskrit)'),('CTGT (Social Science)','TGT (Social Science)'),
               ('CTGT (English)','TGT (English)'),('CTGT (Hindi)','TGT (Hindi)'),('DPRT','PRT'),('ESSA','SSA'),('FLab Attendant','Lab Attendant'),
               ('GSub Staff','Sub Staff'),('HJR. Secratariat Assistant','JR. Secratariat Assistant')]
from django.db import models
# declaring classes that can be selected in the TC part
class Class(models.Model):
    class_name=models.CharField(max_length=16)
    def __str__(self) :
        return f"{self.class_name}"
    class Meta:
        verbose_name = "Add Class in TC"
        verbose_name_plural = "Add Class in TC"
class principals_message(models.Model):
    message=models.TextField()
    image=models.ImageField(upload_to='website/images/' ,blank=False ,null=False)
    def __str__(self):
        return "Principals Message"
    class Meta:
        verbose_name = "Add  Principals message"
        verbose_name_plural = "Add Principals message"
class Alumni(models.Model):
    name=models.CharField(max_length=64)
    description_of_acheivement=models.TextField(max_length=128)
    def __str__(self):
        return f"{self.name}"
    class Meta:
        verbose_name = "Add Alumni"
        verbose_name_plural = "Add Alumni"
class News_letter(models.Model):
    title=models.CharField(max_length=32)
    file=models.FileField(upload_to='website/files',blank=False,null=False)
    def __str__(self) :
        return f"{self.title}"
    class Meta:
        verbose_name = "Make News Letter Entry"
        verbose_name_plural = "Make News Letter Entry"
class vmc_member(models.Model):
    name=models.CharField(max_length=128)
    post=models.TextField()
    address=models.CharField(max_length=128)
    def __str__(self):
        return f"{self.name}"
    class Meta:
        verbose_name = "Add VMC member"
        verbose_name_plural = "Add VMC member"
class member_list(models.Model):
    name=models.CharField(max_length=32)
    designation=models.CharField(choices=Vacancy_posts,max_length=32)
    origin=models.CharField(choices=[("Local","Local"),("Indian","Indian")],null=False,blank=False,max_length=6)
    image=models.ImageField(upload_to='website/images/' ,blank=True ,null=True,default='website/images/PFP.jpg')
    def __str__(self):
        return f"{self.name},{self.get_designation_display()}"
    class Meta:
        verbose_name = "Add Staff"
        verbose_name_plural = "Add Staff"
class Vacancy(models.Model):
    number=models.IntegerField()
    vacant_designation=models.CharField(choices=Vacancy_posts,max_length=32)
    def __str__(self):
        return f"{self.vacant_designation}"
    class Meta:
        verbose_name = "Add Vacancy"
        verbose_name_plural = "Add Vacancy"
class Notice(models.Model):
    file=models.FileField(upload_to='website/files',blank=False,null=False)
    title=models.TextField(blank=False)
    description=models.TextField(blank=False)
    date=models.DateField(default=timezone.localdate())
    def __str__(self):
        return f"{self.title}"
    class Meta:
        verbose_name = "Add Notice"
        verbose_name_plural = "Add Notice"
class News_and_Events(models.Model):
    id=models.IntegerField(primary_key=True,auto_created=True,blank=False,null=False)
    title=models.TextField(blank=False)
    description=models.TextField(blank=False)
    def __str__(self):
        return f"{self.title}"
    class Meta:
        verbose_name = "Add Event Item"
        verbose_name_plural = "Add Event Item"
class Fee_structure(models.Model):
    file=models.FileField(upload_to='website/files',blank=False,null=False)
    def __str__(self):
        return f"Fee structure for the year {date.today().year}"
    class Meta:
        verbose_name = "Add Fee Structure"
        verbose_name_plural = "Add Fee Structure"
class Holiday(models.Model):
    name=models.TextField(max_length=32,blank=False,null=False)
    start_date=models.DateField(blank=False,null=False)
    end_date=models.DateField(default=None)
    category=models.CharField(choices=
                              (('holiday','Holiday'),('summer_vacation','Summer Vacation'),('winter_vacation','Winter Vacation'),('autum_vacation','Autum Vacation')),
                              max_length=32)
    def __str__(self):
        return f"{self.name}"
    class Meta:
        verbose_name = "Add Holiday"
        verbose_name_plural = "Add Holiday"
class Carousel_image(models.Model):
    image_1=models.ImageField(upload_to='website/images/' ,blank=False ,null=False)
    image_2=models.ImageField(upload_to='website/images/' ,blank=False ,null=False)
    image_3=models.ImageField(upload_to='website/images/' ,blank=False ,null=False)
    image_4=models.ImageField(upload_to='website/images/' ,blank=False ,null=False)
    class Meta:
        verbose_name = "Add Image to Caurosel"
        verbose_name_plural = "Add Image to Carousel"
class News_and_Events_Admin(admin.ModelAdmin):
    exclude= ('id',)
class quote(models.Model):
    quote=models.TextField()
    last_updated=models.DateField()
    author=models.TextField()
class Images(models.Model):
    event=models.ForeignKey(News_and_Events,on_delete=models.CASCADE,related_name='images',blank=True,null=True)
    image=models.ImageField(upload_to='website/images/' ,blank=False ,null=False)
    def __str__(self):
        return f"{self.event}"
    class Meta:
        verbose_name = "Add Image for event"
        verbose_name_plural = "Add Image for event"
class Committies(models.Model):
    Committee_name=models.TextField(choices=(('Admissions','Admissions'),('Academic advisory','Academic_Advisory'),('Examination','Examination'),('Transpotation','Transpotation')))
    members=models.ManyToManyField(member_list,related_name='committees')
    class Meta:
        verbose_name = "Update Committee Member"
        verbose_name_plural = "Update Committee Member"
class Admissions(models.Model):
    grade=models.ManyToManyField(Class,related_name="vacancy_class",blank=False)
    vacancy=models.IntegerField(blank=False,null=False)
    file=models.FileField(upload_to='website/files',default=None)
    class Meta:
        verbose_name='Vacancy for Other Classes'
        verbose_name_plural = 'Vacancy for Other Classes'
    def __str__(self):
        return f"Vacancy for class {self.grade.get()}"
class class1(models.Model):
    file=models.FileField(upload_to='website/files',blank=False,null=False)
    def __str__(self):
        return f"Class 1 vacancy for year {date.today().year}"
    class Meta:
        verbose_name = "Add class 1 vacancy file"
        verbose_name_plural = "Add class 1 vacancy file"
class class11(models.Model):
    file=models.FileField(upload_to='website/files',blank=False,null=False)
    def __str__(self):
        return f"Class 11 vacancy for year {date.today().year}"
    class Meta:
        verbose_name = "Add class 11 vacancy file"
        verbose_name_plural = "Add class 11 vacancy file"
class achievement(models.Model):
    title=models.TextField(blank=False,null=False,default=None)
    description=models.TextField(blank=False,null=False)
    image=models.ImageField(upload_to='website/images')
    class Meta:
        verbose_name = "Add Achievement"
        verbose_name_plural = "Add Achievement"
class TC(models.Model):
    Student_Name=models.TextField(max_length=128,blank=False,default=None)
    Parent_Name=models.TextField(max_length=128,blank=False,default=None)
    Date_of_Birth=models.DateField(blank=False,default=None)
    Adm_No=models.PositiveBigIntegerField(primary_key=True)
    Class_Left=models.TextField(blank=False,default=None)
    Tc_No=models.PositiveBigIntegerField(blank=False,default=None)
    Date=models.DateField(blank=False,default=None)
    class Meta:
        verbose_name = "Add TC"
        verbose_name_plural = "Add TC"
    def __str__(self):
        return f"{self.Student_Name}"
class Notice_Admin(admin.ModelAdmin):
    exclude= ('date',)


