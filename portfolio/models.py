from django.db import models

class Artwork(models.Model):

    ART_TYPE_CHOICES = [
        ('2D', '2D Art'),
        ('3D', '3D Art'),
        ('ANIM', '2D Animation'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    types = models.CharField(max_length=50)
    date = models.DateField(null=True, blank=True)
    image = models.ImageField(upload_to='artworks/')
    preview = models.ImageField(upload_to='previews/', blank=True, null=True)

    order = models.PositiveIntegerField(default=0, db_index=True)

    def save(self, *args, **kwargs):
        if not self.preview:
            self.preview = self.image
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    
    def get_types_display(self):
        return ", ".join(
            dict(self.ART_TYPE_CHOICES).get(t.strip(), t.strip())
            for t in self.types.split(',')
            if t
        )

    class Meta:
        ordering = ['order']