#!/usr/bin/env python
# coding: utf-8

# # Uklanjanje suma sa datog zvuka
# Dodavanje potrebnih biblioteka za izvrsavanje koda
# In[23]:


import IPython
from scipy.io import wavfile
import noisereduce as nr
import soundfile as sf
from noisereduce.generate_noise import band_limited_noise
import matplotlib.pyplot as plt
import urllib.request
import numpy as np
import io

# Ucitavanje zvuka
# In[24]:


url = "https://raw.githubusercontent.com/Djokele/Proba/master/download.wav"
response = urllib.request.urlopen(url)
data, rate = sf.read(io.BytesIO(response.read()))
data = data

IPython.display.Audio(data=data, rate=rate)


# In[25]:


fig, ax = plt.subplots(figsize=(20,3))
ax.plot(data)

# Dodavanje suma 
# In[26]:


noise_len = 2 # sekunde
noise = band_limited_noise(min_freq=2000, max_freq = 12000, samples=len(data), samplerate=rate)*10
noise_clip = noise[:rate*noise_len]
audio_clip_band_limited = data+noise

fig, ax = plt.subplots(figsize=(20,3))
ax.plot(audio_clip_band_limited)

IPython.display.Audio(data=audio_clip_band_limited, rate=rate)

# Uklanjanje suma
# In[27]:


noise_reduced = nr.reduce_noise(audio_clip=audio_clip_band_limited, noise_clip=noise_clip, prop_decrease=1.0, verbose=True)

# Reprodukcija zvuka posle uklonjenog suma
# In[28]:


fig, ax = plt.subplots(figsize=(20,3))
ax.plot(noise_reduced)


# In[29]:


IPython.display.Audio(data=noise_reduced, rate=rate)

