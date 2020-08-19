from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
# Create your models here.




class Lecture(models.Model):
    lecture=models.CharField(max_length=128,blank=False)
    slug = models.SlugField(max_length=20, unique=True)

    def save(self, *args, **kwargs):
        self.slug = self.slug or slugify(self.lecture)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.lecture

    class Meta:
        ordering = ['lecture']


class Lecturer(models.Model):
    lecturer=models.CharField(max_length=128,blank=False)
    lecture=models.ManyToManyField(Lecture)
    faculty=models.CharField(max_length=128)
    slug = models.SlugField(max_length=20, unique=True)

    def save(self, *args, **kwargs):
        self.slug = self.slug or slugify(self.lecturer)
        super().save(*args, **kwargs)

    def get_lectures(self):
        return ",".join([str(p) for p in self.lecture.all()])

    def __str__(self):
        return self.lecturer

    class Meta:
        ordering = ['lecturer']


class Semester(models.Model):
    semester=models.CharField(max_length=128,blank=False)

    def __str__(self):
        return self.semester

    class Meta:
        ordering = ['semester']


class Distribution(models.Model):
    # these are the images
    distribution=models.ImageField(upload_to='distribution/')
    created_on = models.DateTimeField(auto_now_add=True)
    semester=models.ForeignKey(Semester,on_delete=models.CASCADE,blank=False,default=0)
    lecturer=models.ForeignKey(Lecturer,on_delete=models.CASCADE,blank=False,default=0)
    lecture=models.ForeignKey(Lecture,on_delete=models.CASCADE,blank=False,default=0)


    def get_absolute_url(self):
        return reverse("home")

    class Meta:
        ordering = ['-created_on']


class Comment(models.Model):
    comment = models.TextField(max_length=256, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='comment_author',blank=True,null=True)
    author_security=models.ForeignKey(User, on_delete= models.CASCADE,related_name='comment_author_security')
    created_on = models.DateTimeField(auto_now_add=True)
    lecturer=models.ForeignKey(Lecturer,on_delete=models.CASCADE,blank=True,null=True)
    anon=models.BooleanField()


    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.comment
