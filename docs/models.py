from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=25)

    def __str__(self):
        return f'{self.category_name}'

class Command(models.Model):
    command_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    command_name = models.CharField(max_length=25)
    command_info = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.command_name} - {self.command_info} - {self.command_category}'

class Usage(models.Model):
    command = models.ForeignKey(Command, on_delete=models.CASCADE)
    command_usage = models.CharField(max_length=25)

    def __str__(self):
        return f'{self.command_usage}'

class Option(models.Model):
    command = models.ForeignKey(Command, on_delete=models.CASCADE)
    command_option = models.CharField(max_length=25)

    def __str__(self):
        return f'{self.command_option}'

class Example(models.Model):
    command = models.ForeignKey(Command, on_delete=models.CASCADE)
    command_example = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.command_example}'

class Alias(models.Model):
    command = models.ForeignKey(Command, on_delete=models.CASCADE)
    command_alias = models.CharField(max_length=25)

    def __str__(self):
        return f'{self.command_alias}'
