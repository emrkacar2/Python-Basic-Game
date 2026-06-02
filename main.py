import pygame
import random
import sys

pygame.init()

GENISLIK, YUKSEKLIK = 600, 600
pencere = pygame.display.set_mode((GENISLIK, YUKSEKLIK))
pygame.display.set_caption("Kaçış Oyunu")
saat = pygame.time.Clock()

SIYAH = (0, 0, 0)
MAVI = (0, 0, 255)
KIRMIZI = (255, 0, 0)
BEYAZ = (255, 255, 255)

oyuncu_boyut = 40
oyuncu_x = GENISLIK // 2 - oyuncu_boyut // 2
oyuncu_y = YUKSEKLIK - 80
oyuncu_hiz = 8

yem_yaricap = 15
yem_x = random.randint(yem_yaricap, GENISLIK - yem_yaricap)
yem_y = 50
yem_hizi = 4

skor = 0
font = pygame.font.SysFont("Courier", 24, bold=True)

while True:
    pencere.fill(SIYAH)
    
    for etkinlik in pygame.event.get():
        if etkinlik.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    tuslar = pygame.key.get_pressed()
    if tuslar[pygame.K_LEFT] and oyuncu_x > 0:
        oyuncu_x -= oyuncu_hiz
    if tuslar[pygame.K_RIGHT] and oyuncu_x < GENISLIK - oyuncu_boyut:
        oyuncu_x += oyuncu_hiz

    yem_y += yem_hizi

    if yem_y > YUKSEKLIK:
        yem_x = random.randint(yem_yaricap, GENISLIK - yem_yaricap)
        yem_y = 0
        skor -= 1

    oyuncu_rect = pygame.Rect(oyuncu_x, oyuncu_y, oyuncu_boyut, oyuncu_boyut)
    if oyuncu_rect.collidepoint(yem_x, yem_y):
        yem_x = random.randint(yem_yaricap, GENISLIK - yem_yaricap)
        yem_y = 0
        skor += 1
        yem_hizi += 0.5  

    pygame.draw.rect(pencere, MAVI, oyuncu_rect)
    pygame.draw.circle(pencere, KIRMIZI, (yem_x, yem_y), yem_yaricap)
    
    skor_yazisi = font.render(f"Skor: {skor}", True, BEYAZ)
    pencere.blit(skor_yazisi, (GENISLIK // 2 - skor_yazisi.get_width() // 2, 20))

    pygame.display.flip()
    saat.tick(60)