from django.db import models

# Create your models here.


class GenreChoices(models.TextChoices):

    ACTION='Action','Action'

    FICTION='Fiction','Fiction'

    THRILLER='Thriller','Thriller'


# GENRE_CHOICES=[('Action','Action'),
#                ('Fiction','Fiction'),
#                ('Thriller','Thriller')]

# genre=models.CharField(max_length=200,choices=GENRE_CHOICES)



class Movies(models.Model):

    title=models.CharField(max_length=200)

    genre=models.CharField(max_length=200,choices=GenreChoices.choices)

    language=models.CharField(max_length=200)

    year=models.CharField(max_length=200)

    run_time=models.PositiveIntegerField()

    director=models.CharField(max_length=200)


    def __str__(self):

        return str(self.title)







# class ClasChoices(models.IntegerChoices):

#     CLAS1=1,1
#     CLAS2=2,2
#     CLAS3=3,3
#     CLAS4=4,4
#     CLAS5=5,5
#     CLAS6=6,6
#     CLAS7=7,7
#     CLAS8=8,8
#     CLAS9=9,9
#     CLAS10=10,10


# class DivisionChoices(models.TextChoices):

#     DIVA='A','A'
#     DIVB='B','B'
#     DIVC='C','C'
#     DIVD='D','D'


# class Student(models.Model):

#     name=models.CharField(max_length=200)

#     division=models.CharField(max_length=200)

#     clas=models.PositiveIntegerField()

#     age=models.PositiveIntegerField()