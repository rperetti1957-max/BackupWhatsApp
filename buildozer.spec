[app]
title = WhatsApp Mover
package.name = whatsappmover
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy

orientation = portrait
fullscreen = 0

# Supporta sia i telefoni moderni a 64-bit sia quelli leggermente più vecchi
android.archs = arm64-v8a, armeabi-v7a

# Aggiornato all'API 34 per garantire la compatibilità con i download attuali
android.api = 34
android.minapi = 21
android.ndk_api = 21

# Richiesta esplicita dei permessi di archiviazione
android.permissions = READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE, MANAGE_EXTERNAL_STORAGE

[buildozer]
log_level = 2
warn_on_root = 1
