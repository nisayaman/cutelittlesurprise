import pygame

# Müzik dosyasının adını ve yolunu belirtin
music_file = "Maxwell the Cat Theme..mp3"

# Pygame'in başlatılması
pygame.init()

# Müzik yükleniyor
pygame.mixer.music.load(music_file)

# Müzik çalınmaya başlıyor
pygame.mixer.music.play()

# Sonsuza kadar bekleyin (Ctrl+C ile çıkılabilir)
while True:
    pass
