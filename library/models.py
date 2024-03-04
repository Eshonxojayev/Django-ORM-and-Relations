from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField()
    price = models.FloatField()
    count = models.IntegerField()
    # author_id = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}"


class Student(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    group_number = models.CharField(max_length=20)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=10)

    # class Meta:
    #     db_name = 'students'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class BookingBook(models.Model):
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    talked_data = models.DateTimeField()

# Create your models here.
