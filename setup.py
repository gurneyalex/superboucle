from setuptools import setup, find_packages
setup(
    name = "SuperBoucle",
    version = "1.2.0",
    url = "https://github.com/Vampouille/superboucle",
    author = "Julien Acroute",
    author_email = "superboucle@nura.eu",
    description = "Loop based software fully controllable with any midi device",
    license = "GPL 3",
    keywords = "audio midi loop jack live composition",
    packages = find_packages(),
    include_package_data = True,
    install_requires=['cffi>=0.8.2', 'PySoundFile', 'numpy', 'PyQT5', 'JACK-Client>=0.3.0'],
    entry_points={
        'gui_scripts': [
            'boucle = boucle',
        ]
    },
    long_description = """SuperBoucle is a loop based software fully controllable with any midi device. 
SuperBoucle is also synced with jack transport. You can use it on live performance or for composition.

SuperBoucle is composed of a matrix of sample controllable with external midi device like pad. 
SuperBoucle will send back information to midi device (light up led). 
Sample will always start and stop on a beat or group of beats. 
You can adjust duration of sample (loop period) in beat and offset in beat. 
But you can also adjust sample offset in raw frame count negative or positive. 
Which mean sample can start before next beat (useful for reversed sample). 
You can record loop of any size, adjust BPM, reverse, normalize samples, ...

Typical usage :

  * You just need to control jack transport (play, pause, rewind) with external midi device and want a button to jump to a specified location in song.
  * You have some instruments patterns but you have no idea of song structure.
  * You make live performance with pre-recorded instruments (you have no bass player for example) and you don't want to have a predefinied structure for the song (maybe part 2 will be longer on some live performance)"""

)
