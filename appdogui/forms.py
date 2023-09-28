from django import forms
from .models import Bands, Musics, Instruments

class BandsForm(forms.ModelForm):
    class Meta:
        model = Bands
        fields = '__all__'

class MusicsForm(forms.ModelForm):
    class Meta:
        model = Musics
        fields = '__all__'

class InstrumentsForm(forms.ModelForm):
    class Meta:
        model = Instruments
        fields = '__all__'
  
class MusicRemovalForm(forms.ModelForm):
   item_to_remove = forms.ModelChoiceField(
        queryset=Musics.objects.all(),
        empty_label=None,
        label='Selecione a música para remover'
   )
  
   class Meta:
    model = Musics
    fields = []

class BandRemovalForm(forms.ModelForm):
  item_to_remove = forms.ModelChoiceField(
        queryset=Bands.objects.all(),
        empty_label=None,
        label='Selecione a banda para remover'
   )
  
  class Meta:
    model = Bands
    fields = []

class InstrumentRemovalForm(forms.ModelForm):
   item_to_remove = forms.ModelChoiceField(
        queryset=Instruments.objects.all(),
        empty_label=None,
        label='Selecione o instrumento para remover'
   )
  
   class Meta:
    model = Instruments
    fields = []

class MusicEditForm(forms.ModelForm):
    class Meta:
        model = Musics
        fields = '__all__'

class InstrumentEditForm(forms.ModelForm):
    class Meta:
        model = Instruments
        fields = '__all__'