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

# Compiliamo solo per arm64 per velocizzare ed evitare conflitti di librerie a 32bit
android.archs = arm64-v8a

# Versioni stabili bloccate per evitare bug dei server Cloud
android.api = 33
android.minapi = 21
android.ndk = 25b
android.ndk_api = 21

# Richiesta esplicita dei permessi di archiviazione
android.permissions = READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE, MANAGE_EXTERNAL_STORAGE

[buildozer]
log_level = 2
warn_on_root = 1
