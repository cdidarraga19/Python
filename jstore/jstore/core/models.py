from django.db import models

class Category(models.Model):
     name = models.CharField(max_length=100)
     description = models.CharField(max_length=255)

     def str(self):
         return self.name

     class Meta:
         verbose_name = 'Categoría'
         verbose_name_plural = 'Categorias'
         db_table = 'categoria'

class Brand(models.Model):
     name = models.CharField(max_length=100, verbose_name='Nombre')
     description = models.TextField(verbose_name='Descripción')

     def str(self):
          return self.name

     class Meta:
         verbose_name = 'Marca'
         verbose_name_plural = 'Marcas'
         db_table = 'marca'
         ordering = ['id']

class Product(models.Model):

     name = models.CharField(max_length=100, verbose_name='Nombre')
     description = models.TextField(verbose_name='Descripción')
     price = models.PositiveIntegerField(verbose_name='Precio')
     category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Categoría' )
     category = models.ManyToManyField(Category, verbose_name='Categoría' )
     brand = models.ForeignKey(Brand, on_delete=models.CASCADE, verbose_name='Marca' )

     def str(self):
         return self.name

     class Meta:
         verbose_name = 'Producto'
         verbose_name_plural = 'Productos'
         db_table = 'producto'
         ordering = ['id']