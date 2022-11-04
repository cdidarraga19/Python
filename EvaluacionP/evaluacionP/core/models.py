from django.db import models

# Modelo equipo
class Team(models.Model):
    name = models.CharField(max_length=50, verbose_name="Nombre")
    flag = models.ImageField(upload_to=None, height_field=None, width_field=None, verbose_name="Bandera del equipo") 
    team_crest = models.ImageField(upload_to=None, height_field=None, width_field=None, verbose_name="Escudo del equipo")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Equipo'
        verbose_name_plural = 'Equipos'
        db_table = 'equipo'
        ordering = ['id']


# Modelo posición de juego
class GamePosition(models.Model):
    name = models.CharField(max_length=50, verbose_name="Nombre")
    description = models.TextField(verbose_name="Descripción")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Posición'
        verbose_name_plural = 'Posiciones'
        db_table = 'posicion'
        ordering = ['id']


# Choice headline boolean
HEADLINE_CHOICES = (
    (True, "Si"),
    (False, "No"),
)
# Modelo jugador
class Player(models.Model):
    name = models.CharField(max_length=50, verbose_name="Nombre")
    lastname = models.CharField(max_length=50, verbose_name="Apellido")
    photo = models.ImageField(upload_to=None, height_field=None, width_field=None,  verbose_name="Foto del jugador")
    date_of_birth = models.DateField(verbose_name="Fecha de nacimiento")
    position = models.ForeignKey(GamePosition, on_delete=models.CASCADE, verbose_name='Posición de juego')
    shirt_number = models.PositiveIntegerField(verbose_name="Número")
    headline = models.BooleanField(verbose_name="Es titular?", choices=HEADLINE_CHOICES)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, verbose_name='Equipo')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Jugador'
        verbose_name_plural = 'Jugadores'
        db_table = 'jugador'
        ordering = ['id']


# Modelo nacionalidad
class Nacionality(models.Model):
    name = models.CharField(max_length=50, verbose_name="Nombre")
    description = models.TextField(verbose_name="Descripción")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Nacionalidad'
        verbose_name_plural = 'Nacionalidades'
        db_table = 'nacionalidad'
        ordering = ['id']


# Choice rol
ROLE_CHOICES =(
    ("1", "Técnico"),
    ("2", "Asistente"),
    ("3", "Médico"),
    ("4", "Preparador"),
)

# Modelo técnico
class TechincalDirector(models.Model):
    name = models.CharField(max_length=50, verbose_name="Nombre")
    lastname = models.CharField(max_length=50, verbose_name="Apellido")
    date_of_birth = models.DateField(verbose_name="Fecha de nacimiento")
    team = models.ForeignKey(Nacionality, on_delete=models.CASCADE, verbose_name='Equipo')
    role = models.CharField(max_length=50, choices=ROLE_CHOICES)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Técnico'
        verbose_name_plural = 'Técnicos'
        db_table = 'tecnico'
        ordering = ['id']