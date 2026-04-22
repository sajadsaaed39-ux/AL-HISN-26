[app]
title = Al-Hisn 26 Super Elite
package.name = alhisn26
package.domain = org.alhisn
source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 1.0.0

requirements = python3,kivy,pillow

orientation = portrait
fullscreen = 0
android.permissions = INTERNET,ACCESS_NETWORK_STATE
android.api = 31
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True
android.arch = armeabi-v7a

[buildozer]
log_level = 2
warn_on_root = 1
