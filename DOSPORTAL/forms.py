from django import forms
from .models import Detector, Record, Profile, Organization, DetectorCalib

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from markdownx.fields import MarkdownxFormField

class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={ 'class': 'form-control', 'placeholder': 'Username', 'autofocus': False }),
        label="Username",
        help_text="Enter your username."
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password', 'autofocus': False }),
        help_text="Enter your password."
    )

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

# Create a UserUpdateForm to update a username and email
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

# Create a ProfileUpdateForm to update image.
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']


class DetectorLogblogForm(forms.Form):
    text = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'form-control'
            }
        )
    )



class RecordForm(forms.ModelForm):

    user = None
    def __init__(self,*args, user=None, **kwargs):
        super(RecordForm, self).__init__(*args, **kwargs)
        self.user = user


    name = forms.CharField(
        required=True, 
        widget=forms.TextInput(attrs={
            'class': 'form-control',

        }),
        label="Name",
        help_text="Enter a name for the measurement.",
    )

    time_start = forms.DateTimeField(
        required=False,
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control',
            'type': 'datetime-local',
            'step': '1',
        }),
        label="Start time",
        help_text="Enter the start time of the measurement. When 'time is tracked', you should set start time of the record beginning. ",
    )

    # log_file = forms.FileField(
    #     required=False,
    #     widget=forms.widgets.FileInput(attrs={
    #         'class': 'form-control',
    #     }),
    #     label="Log file",
    #     help_text="Select a log file to upload."
    #     #widget=forms.FileInput(attrs={
    #     #    'class': 'form-control',
    #     #})
    # )

    # detector = forms.ModelChoiceField(
    #     queryset=Detector.objects.all(),
    #     widget=forms.Select(attrs={
    #         'class': 'form-control',
    #     }),
    #     required=False,
    #     label="Detector",
    #     help_text="Select used detector. It is not mandatory in case of detectors with auto-detect feature."
    # )

    description = MarkdownxFormField(
        label="Description",
        help_text="Detailed description of measurements. You can add additional information about measurement conditions, locations etc.. (Markdown supported)",
        required=False,
    )

    # record_type = forms.ChoiceField(
    #     choices=Record.RECORD_TYPES
    # )

    belongs = forms.ModelChoiceField(
        queryset=Organization.objects.exclude(user_organizations__user=user),
        required=True,
        label="Belongs to",
        help_text="Select organization this record belongs to."
    )

    class Meta:
        model = Record
        exclude = ("time_end", "measurement", "log_original_filename", "metadata", "duration", "record_duration", "author", 'data_file',
                   "metadata_file", "created", "detector", "time_of_interest_start", "time_of_interest_end", 'calib', 'record_type')


class DetectorEditForm(forms.ModelForm):
    class Meta:
        model = Detector
        fields = ["name", "type", 'sn', "manufactured_date", "data", "owner", "access"]
        

class DetectorCalibForm(forms.ModelForm):
    class Meta:
        model = DetectorCalib
        #fields = ['name', 'description', 'coef0', 'coef1', 'coef2']
        exclude = ['created', 'author']


DetectorCalibFormSet = forms.inlineformset_factory(
    Detector, 
    Detector.calib.through,
    #fields= (calib',),
    form=DetectorCalibForm,
    can_delete=True,
    extra=1
)

