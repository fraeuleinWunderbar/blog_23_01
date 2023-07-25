from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class Block(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'
    title = models.CharField("Titel", max_length=250)
    slug = models.SlugField(max_length=250)
    author = models.ForeignKey(User, verbose_name="Autor", on_delete=models.CASCADE)
    body = models.TextField("Inhalt")
    published = models.DateTimeField("Veröffentlicht", default = timezone.now)
    created = models.DateTimeField("Erstellt", auto_now=False, auto_now_add=True)
    updated = models.DateTimeField("Geändert", auto_now=True, auto_now_add=False)
    status = models.CharField("Status", max_length=2, choices=Status.choices, default = Status.DRAFT)

    class Meta:
        verbose_name = "Block"
        verbose_name_plural = "Blöcke"

    def __str__(self):
        return f"{self.title}/{self.author} ({self.created})"

    def get_absolute_url(self):
        return reverse("Block_detail", kwargs={"pk": self.pk})
