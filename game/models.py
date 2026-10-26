from django.db import models


class Categoria(models.Model):
    nombre = models.CharField(max_length=120 ,null=True)
    tipo = models.CharField(max_length=100, unique=True)



    def __str__(self):
        return f"{self.nombre} - {self.tipo}"

    class Meta:
        db_table = 'categoria'
        verbose_name_plural = "Categorias"
        ordering = ["nombre"]

class Item(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200)
    nivel = models.PositiveIntegerField(default=1)
    ban = models.BooleanField(default=False)
    creado = models.DateTimeField(auto_now_add=True)
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} - {self.descripcion} - {self.nivel} "
    class Meta:
        db_table = 'item'
        verbose_name_plural = 'items'
        ordering = ['nombre']





class Personaje (models.Model):
        raza = models.CharField(max_length=20)
        descripcion = models.CharField(max_length=200)
        nivel = models.PositiveIntegerField(default=0)
        creado =models.DateTimeField(auto_now_add=True)
        item = models.ForeignKey(Item,on_delete=models.CASCADE)

        def __str__(self):
            return f"{self.raza} - {self.descripcion} - {self.nivel}"
        class Meta:
            db_table = 'personaje'
            verbose_name_plural = 'personajes'
            ordering = ['creado']





class Cuenta (models.Model):
        usuario = models.CharField(max_length=80,unique=True)
        cuenta_id = models.PositiveIntegerField(unique=True)
        correo = models.CharField(max_length=120)
        cuenta_personaje = models.ForeignKey(Personaje,on_delete=models.CASCADE)

        def __str__(self):
            return f"{self.usuario} - {self.correo}"
        class Meta:
            db_table = 'cuenta'
            verbose_name_plural = 'cuentas'
            ordering = ['cuenta_id']

class CuentaPersonaje (models.Model):
        cuenta_id = models.ForeignKey(Cuenta,on_delete=models.CASCADE)
        personaje_id = models.ForeignKey(Personaje,on_delete=models.CASCADE)


        def __str__(self):
            return f"{self.cuenta_id} - {self.personaje_id}"
        class Meta:
            db_table = 'CuentaPersonaje'
            verbose_name_plural = 'cuentas de personajes'
            ordering = ['personaje_id']





