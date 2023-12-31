from django.db import models
import uuid
from django.utils.translation import gettext as _
from django.conf import settings
from django.urls import reverse
from matplotlib.colors import LightSource
from martor.models import MartorField
from django_q.tasks import async_task

from .tasks import process_flight_entry


def get_enum_dsc(enum, t):
    for r in enum:
        if r[0] == t:
            return r[1]
    return t


class UUIDMixin(models.Model):

    id = models.UUIDField(
        primary_key = True,
        default = uuid.uuid4,
        editable = False,
        unique = True
    )

    def get_admin_url(self):
        return reverse("admin:%s_%s_change" % (self._meta.app_label, self._meta.model_name), args=(self.id,))


    class Meta:
    	abstract = True



class CARImodel(UUIDMixin):
    data = models.JSONField()



class Airports(UUIDMixin):
    name = models.CharField()
    code_iata = models.CharField(null=True, unique=True)
    code_icao = models.CharField(null=True, unique=True)

    lat = models.FloatField(null=True)
    lon = models.FloatField(null=True)
    alt = models.FloatField(null=True)

    municipality = models.CharField(null=True)
    web = models.CharField(null=True)

    def __str__(self) -> str:
        return "Airport {} ({})".format(self.code_iata, self.name)

class Flight(UUIDMixin):

    flight_number = models.CharField()

    takeoff = models.ForeignKey(
        Airports,
        on_delete=models.CASCADE,
        related_name="takeoff")
    

    departure_time = models.DateTimeField(
        verbose_name = _("Scheduled departure time"),
        null=True,
    )

    
    land = models.ForeignKey(
        Airports,
        on_delete=models.CASCADE,
        related_name="landing")


    def user_directory_path(instance, filename):
        return "data/flights/{0}/{1}/path.txt".format(instance.flight_number.rstrip(), instance.departure_time.strftime("%Y-%m-%d %H:%M"))

    trajectory_file = models.FileField(
        verbose_name=_("Trajectory log"),
        upload_to=user_directory_path,
    )

    cari = models.ForeignKey(
        CARImodel,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )


    def get_absolute_url(self):
        return reverse('flight-detail', args=[str(self.id)])
    
    def __str__(self) -> str:
        return "Flight {} ({}->{}) @ {}".format(self.flight_number, self.takeoff.code_iata, self.land.code_iata, self.departure_time.strftime("%Y-%m-%d %H:%M"))

    def save(self, *args, **kwargs):
        print("ASYNYC..", self)
        async_task(process_flight_entry, self)
        super(Flight, self).save(*args, **kwargs)

    class Meta:
      unique_together = ('flight_number', 'departure_time')


class MeasurementDataFlight(UUIDMixin):
    flight = models.ForeignKey(
        Flight,
        on_delete=models.CASCADE,
        related_name="measurements")

class DetectorManufacturer(UUIDMixin):
    
    name = models.CharField(
        max_length = 80,
    )
    
    url = models.URLField(max_length=200)

    def __str__(self) -> str:
        return "Detector manufacturer: {}".format(self.name)

class DetectorType(UUIDMixin):

    name = models.CharField(
        max_length = 80,
    )

    manufacturer = models.ForeignKey(
        DetectorManufacturer,
        on_delete=models.CASCADE
    )


    def __str__(self) -> str:
        return "Detector type {} ({})".format(self.name, self.manufacturer.name)


class DetectorCalib(UUIDMixin):

    name = models.CharField(
        _("Calibration name")
    )

    description = models.TextField(
        _("Description of calibration status")
    )

    date = models.DateTimeField(
    )

    # author = models.ForeignKey(
    #     settings.AUTH_USER_MODEL,
    #     on_delete=models.CASCADE,
    # )


    cabib = models.JSONField(
        _("Slozky kalibrace, json")
    )

    


class Detector(UUIDMixin):

    sn = models.CharField(
        max_length = 80,
    )

    name = models.CharField(
        _("Detector name"),
        max_length=150,
    )

    type = models.ForeignKey(
        DetectorType,
        on_delete=models.CASCADE
    )

    calib = models.ForeignKey(
        DetectorCalib,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="detectors"
    )

    manufactured_date = models.DateField(
        _("Manufactured date"),
        help_text=_("Date when detector was manufactured"),
        null=True,  blank=True
    )

    data = models.JSONField(
        _("Detector metadata"),
        help_text="Detector metadata, used for advanced data processing and maintaining"
    )

    def __str__(self) -> str:
        return "Detector {} ({}), SN:{}".format(self.name, self.type.manufacturer.name, self.sn)

class DetectorLogbook(UUIDMixin):

    detector = models.ForeignKey(
        Detector,
        on_delete=models.CASCADE,
        related_name='logbook'
    )

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    created = models.DateTimeField(auto_now_add=True)

    text = models.TextField(
        _("Logbook text"),
        help_text="Detailed description of activity made on the detector."
    )
    public = models.BooleanField(
        _("Wish to be visible to everyone?"),
        help_text=_("Private logbook will be visible for maintainers of detector and for dosportal admins."),
        default=True)

class measurement_campaign(UUIDMixin):

    name = models.CharField(
        _("measurement name"),
        max_length=150,
        null=True, blank=True
    )


    def __str__(self) -> str:
        return "Campaign: {}".format(self.name)



class measurement(UUIDMixin):
    """
    Měřením se rozumí sada měření, které analyzují jednu a tu samou věc a jsou změřeny jedním detektorem.
    Pokud jsou v latedle dva detektory, tak to jsou dvě měření. Pokud je ale měření z jednoho detektoru
    přerušeno a navázáno novým záznamem, tak to je celé jedno měření. 
    
    """
    
    time_start = models.DateTimeField(
        verbose_name = _("Measurement beginning time"),
        null=True, blank=True,
    )

    time_end = models.DateTimeField(
        verbose_name = _("Measurement beginning time"),
        null=True, blank=True,
    )

    time_created = models.DateTimeField(
        verbose_name = _("Time of creation"),
        null=False,
        editable=False,
        auto_now_add=True
    )
    
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name = "measurements"
    )

    name = models.CharField(
        _("measurement name"),
        max_length=150,
    )

    description = MartorField(
        _("Measurement description"),
        blank = True
    )

    public = models.BooleanField(
        verbose_name=_("Will be data publicly available"),
        default = True
    )

    # Tohle pole by melo obsahovat nasledujici typy:
    MEASUREMENT_TYPES = (
        ('D', 'Debug measurement'),
        ('S', 'Static measurement'),
        ('M', 'Mobile measurement (ground)'),
        ('C', 'Civil airborne measurement'),
        ('A', 'Special airborne measurement')
    )

    measurement_type = models.CharField(
        verbose_name=_("Certain measurement type, enum"),
        choices=MEASUREMENT_TYPES,
        default="S",
        help_text=_("Type of measurement")
    )

    base_location_lat = models.FloatField(null=True, default=None, blank=True)
    base_location_lon = models.FloatField(null=True, default=None, blank=True)
    base_location_alt = models.FloatField(null=True, default=None, blank=True)


    def user_directory_path(instance, filename):
        return "data/user_records/{0}/{1}".format(instance.user.id, filename)

    location_file = models.FileField(
        verbose_name=_("File log"),
        upload_to=user_directory_path,
        blank = True
    )

    def get_absolute_url(self):
        return reverse('measurement-detail', args=[str(self.id)])

    def __str__(self):
        return f'Mereni: {self.name}, Typ: {self.measurement_type}'
   
    flight = models.ForeignKey(
        Flight,
        on_delete=models.CASCADE,
        related_name = "measurement",
        null = True,
        verbose_name=_("Reference na objekt s informacemi o letu"),
        blank = True
    )

    campaings = models.ManyToManyField(measurement_campaign, related_name="Campaigns", blank=True)



class record(UUIDMixin):
    """
    Obsahuje jednotlivý log z detektoru
    """

    measurement = models.ForeignKey(
        measurement,
        on_delete=models.CASCADE,
        related_name='records'
    )
    
    detector = models.ForeignKey(
        Detector,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='records'
    )

    def user_directory_path(instance, filename):
        return "data/user_records/log_{1}".format(instance.measurement.author.pk, instance.pk)

    log_file = models.FileField(
        verbose_name=_("File log"),
        upload_to=user_directory_path,
    )

    log_filename = models.CharField(

    )

    time_start = models.DateTimeField(
        verbose_name = _("Measurement beginning time"),
        null=True,
    )


    record_duration = models.DurationField(
        verbose_name = _("Record duration"),
        help_text=_("Duration of record"),
        null=True
    )


    # Tohle pole by melo obsahovat nasledujici typy:
    RECORD_TYPES = (
        ('S', 'Spectral measurements'),
        ('L', 'Location')
    )

    record_type = models.CharField(
        verbose_name=_("Certain record type, enum"),
        choices=RECORD_TYPES,
        default="S",
        help_text=_("Type of log file")
    )

    metadata = models.JSONField(
        _("record_metadata"),
        help_text=_("record metadata, used for advanced data processing and maintaining"),
        null=True
    )

    def __str__(self) -> str:
        return "record ({}, {}, start {}, {})".format( get_enum_dsc(self.RECORD_TYPES, self.record_type), self.id, self.time_start, 0)

    def description(self) -> str:
        return "Record ({}, {})".format(get_enum_dsc(self.RECORD_TYPES, self.record_type), self.time_start.strftime("%Y-%m-%d_%H:%M"))



