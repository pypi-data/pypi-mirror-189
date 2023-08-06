[app]
title = Sideband
package.name = sideband
package.domain = io.unsigned

source.dir = .
source.include_exts = py,png,jpg,jpeg,ttf,kv,pyi,typed,so,0,1,2,3,atlas,frag
source.include_patterns = assets/*
source.exclude_patterns = app_storage/*,venv/*,Makefile,./Makefil*,requirements,precompiled/*,parked/*,./setup.py,Makef*,./Makefile,Makefile

version.regex = __version__ = ['"](.*)['"]
version.filename = %(source.dir)s/main.py
android.numeric_version = 20230204

requirements = python3==3.9.5,hostpython3==3.9.5,cryptography,cffi,pycparser,kivy==2.1.0,pygments,sdl2,sdl2_ttf==2.0.15,pillow,qrcode==7.3.1,netifaces,libbz2,pydenticon,usb4a,usbserial4a
p4a.local_recipes = ../Others/python-for-android/pythonforandroid/recipes
requirements.source.kivymd = ../../Others/KivyMD-master

icon.filename = %(source.dir)s/assets/icon.png
presplash.filename = %(source.dir)s/assets/presplash_small.png
android.presplash_color = #00000000

# TODO: Fix
orientation = portrait
fullscreen = 0

android.permissions = INTERNET,POST_NOTIFICATIONS,WAKE_LOCK,FOREGROUND_SERVICE,CHANGE_WIFI_MULTICAST_STATE,BLUETOOTH_CONNECT
android.api = 30
android.minapi = 24
android.ndk = 23b
android.skip_update = False
android.accept_sdk_license = True
android.release_artifact = apk
android.archs = arm64-v8a,armeabi-v7a
#android.logcat_filters = *:S python:D

services = sidebandservice:services/sidebandservice.py:foreground
android.whitelist = lib-dynload/termios.so
android.manifest.intent_filters = patches/intent-filter.xml
android.add_aars = patches/support-compat-28.0.0.aar

[buildozer]
log_level = 2
warn_on_root = 0
build_dir = ./.buildozer
bin_dir = ./bin
