from django.db import models

COLOR_CHOICES = [
    ('BL', 'Black'), 
    ('WH', 'White')
]

TYPE_NAME_CHOICES = [
    ('K', 'King'), 
    ('Q', 'Queen'),
    ('B', 'Bishop'),
    ('P', 'Pawn'), 
    ('R', 'Rook'), 
    ('KN', 'Knight')
]

class Square(models.Model):
    letter = models.CharField(max_length=1)
    number = models.IntegerField()


class Type(models.Model):
    name = models.CharField(choices=TYPE_NAME_CHOICES, max_length=10)
    rule = models.CharField(max_length=255)


class Piece(models.Model):
    square = models.ForeignKey('Square', default=None, on_delete=models.CASCADE)
    color = models.CharField(choices=COLOR_CHOICES, max_length=10)
    type = models.ForeignKey('Type', on_delete=models.CASCADE)

