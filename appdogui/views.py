from django.shortcuts import render, redirect, get_object_or_404
from .models import Instruments, Musics, Bands
from .forms import BandsForm, MusicsForm, BandRemovalForm, MusicRemovalForm, InstrumentRemovalForm, InstrumentsForm, InstrumentEditForm, MusicEditForm

# Create your views here.
def home(request):
  instruments = Instruments.objects.all()
  musics = Musics.objects.all()
  bands = Bands.objects.all()
  return render(request, "home.html", context ={ 
    "musics" : musics,
    "instruments" : instruments,
    "bands" : bands
  })

def add_band(request):
    if request.method == "POST":
        form = BandsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(home)
    else:
        form = BandsForm()

    return render(request, 'add_band.html', {'form': form})

def add_music(request):
    if request.method == "POST":
        form = MusicsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(home)
    else:
        form = MusicsForm()

    return render(request, 'add_music.html', {'form': form})

def add_instrument(request):
    if request.method == "POST":
        form = InstrumentsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(home)
    else:
        form = InstrumentsForm()

    return render(request, 'add_instrument.html', {'form': form})

def remove_music(request):
    if request.method == "POST":
        form = MusicRemovalForm(request.POST)
        if form.is_valid():
            music = form.cleaned_data['item_to_remove']
            if music:
                music.delete()
                return redirect(home)
    else:
        form = MusicRemovalForm()

    return render(request, 'remove_music.html', {'form': form})

def remove_band(request):
    if request.method == "POST":
        form = BandRemovalForm(request.POST)
        if form.is_valid():
            band = form.cleaned_data['item_to_remove']
            if band:
                band.delete()
                return redirect(home)
    else:
        form = BandRemovalForm()

    return render(request, 'remove_band.html', {'form': form})

def remove_instrument(request):
    if request.method == "POST":
        form = InstrumentRemovalForm(request.POST)
        if form.is_valid():
            instrument = form.cleaned_data['item_to_remove']
            if instrument:
                instrument.delete()
                return redirect(home)
    else:
        form = InstrumentRemovalForm()

    return render(request, 'remove_instrument.html', {'form': form})

def edit_music(request, music_id):
    music = get_object_or_404(Musics, id=music_id)
    if request.method == "POST":
        form = MusicEditForm(request.POST, instance=music)
        if form.is_valid():
            form.save()
            return redirect(home)
    else:
        form = MusicEditForm(instance=music)
    return render(request, 'edit_music.html', {'form': form})

def edit_instrument(request, instrument_id):
    instrument = get_object_or_404(Instruments, id=instrument_id)
    if request.method == "POST":
        form = InstrumentEditForm(request.POST, instance=instrument)
        if form.is_valid():
            form.save()
            return redirect(home)
    else:
        form = InstrumentEditForm(instance=instrument)
    return render(request, 'edit_instrument.html', {'form': form})