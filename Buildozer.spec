[app]

# App ka naam jo dikhega
title = AL HAMF CADET SCHOOL 

# Package name (sirf small letters, no space)
package.name = alhamadcadetschool

# Domain (kuch bhi rakh sakte ho)
package.domain = org.alhamdschool

# Source code kahan hai
source.dir = .

# Kaunsi files include karni hain
source.include_exts = py,png,jpg,jpeg,kv,atlas,ttf,woff,woff2

# App version
version = 0.1

# Requirements (sabse important)
requirements = python3,kivy==2.3.0,kivymd,pillow

# Screen orientation
orientation = portrait

# Fullscreen ya nahi
fullscreen = 0

# Permissions (internet chahiye to rakho)
android.permissions = INTERNET,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE

# App icon (agar icon.png file hai repo mein to uncomment kar do)
# icon.filename = icon.png

# App name jo launcher mein dikhega
android.application_label = My KivyMD App
