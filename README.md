# Text-To-Speech
Python script that voices given text and directs it to the Virtual Audio Cable.

<img src="https://images.vexels.com/media/users/3/145866/isolated/preview/b4efb6c6682b2a808631bf8fbd96d015-sound-wave-icon.png" width="200px"/>

# Start
To start you need install Python Libs from requirements.txt

```sh
pip install -r requirements.txt
```

After that install Virtual Audio Cable utility


[VB-audio](https://vb-audio.com/Cable/) - Free VAC utility.


To use script you also should make sure that your VAC name matches with name in the script
Use your Python interpreter 

```py
>>> from pygame import mixer
>>> from pygame._sdl2 import get_audio_device_names #Get playback device names
>>> mixer.init() #Initialize the mixer, this will allow the next commands to work
>>> get_audio_device_names()
>>> ['Realtek Digital Output (Realtek High Definition Audio)', 'CABLE Input (VB-Audio Virtual Cable)', 'Динамики (Realtek High Definition Audio)', 'XV272 P (NVIDIA High Definition Audio)']
```

If names are different, replace name in the script to name, which given in device names
# **All are ready!**
[![N|Solid](https://user-images.githubusercontent.com/108426835/180672123-2fecb949-11f7-4699-a64f-a51d7f82277a.png)](https://www.python.org/)
