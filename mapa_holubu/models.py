from django.db import models
from django.urls import reverse

# ==========================================================================
# TVORBA MODELŮ
# ==========================================================================
class Holubi(models.Model):
    jmeno = models.CharField(
        max_length=50, 
        default="beze jména",
        help_text="Zadejte jméno holuba. Pokud neznáte jméno, ponechte výchozí hodnotu."
    )
    datum = models.DateField(
        help_text="Vyberte datum události (nepovinný udaj).",
        null=True,
        blank=True
    )
    latitude = models.DecimalField(
        max_digits=10, 
        decimal_places=7,
        help_text="Zadejte zeměpisnou šířku - latitude (maximálně 10 číslic). "
                "Souřadnice můžete zjistit pomocí tohoto odkazu: "
                "<a href='https://www.geocords.com/address-to-lat-long/' target='_blank'>Získat souřadnice</a>."
    )
    longitude = models.DecimalField(
        max_digits=10, 
        decimal_places=7,
        help_text="Zadejte zeměpisnou délku - longitude (maximálně 10 číslic). "
                "Souřadnice můžete zjistit pomocí tohoto odkazu: "
                "<a href='https://www.geocords.com/address-to-lat-long/' target='_blank'>Získat souřadnice</a>."
    )
    adresa = models.CharField(
        max_length=255, 
        help_text="Zadejte adresu události (lze zkopírovat z odkazu se souřadnicemi)."
    )
    popis = models.TextField(
        max_length=5000,
        help_text="Zadejte popis (maximálně 5 000 znaků)."
    )

    class Meta:
        # název v django adminu (smaže 's' na konci)
        verbose_name_plural = 'Holubi' 

    def __str__(self):
        return f"{self.jmeno} - {self.datum} - {self.adresa}"

    def get_absolute_url(self):
        """Funkce vrátí url k instanci."""
        return reverse('detail', kwargs={'pk': self.pk})


