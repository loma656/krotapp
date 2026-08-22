[app]
title = Krot App
package.name = krotapp
package.domain = org.example
source.dir = .
source.include_exts = py,png,jpg,kv,json
version = 1.0
requirements = python3,kivy,git+https://github.com/kivymd/Kivymd.git@master,requests

orientation = portrait
android.permissions = INTERNET

[buildozer]
log_level = 2
