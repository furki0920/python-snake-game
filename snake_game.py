import pygame
import random
import os
import time

pygame.init()

# Renkler
siyah = (0, 0, 0)
kirmizi = (213, 50, 80)
yesil = (0, 255, 0)
mavi = (50, 153, 213)
koyu_yesil = (0, 200, 0)
göz_rengi = (0, 0, 0)
dil_kirmizi = (255, 0, 0)

# Ekran
genislik, yukseklik = 600, 400
dislay = pygame.display.set_mode((genislik, yukseklik))
pygame.display.set_caption("Yılan Oyunu")

# Zaman
saat = pygame.time.Clock()
yilan_boyutu = 10

# Yazı tipleri
font = pygame.font.SysFont("arial", 24)
puan_fontu = pygame.font.SysFont("arial", 20)

# Skor dosyası
skor_dosya = "skorlar.txt"

def puan_yazdir(puan):
    yazi = puan_fontu.render("Puan: " + str(puan), True, siyah)
    dislay.blit(yazi, [10, 10])

def level_yazdir(level):
    yazi = puan_fontu.render("Seviye: " + str(level), True, siyah)
    dislay.blit(yazi, [500, 10])

def highscore_yazdir():
    hs = high_score_oku()
    yazi = puan_fontu.render("En Yüksek: " + str(hs), True, siyah)
    dislay.blit(yazi, [220, 10])

def mesaj_ortali(msg, renk, offset=0):
    yazi = font.render(msg, True, renk)
    rect = yazi.get_rect(center=(genislik // 2, yukseklik // 2 + offset))
    dislay.blit(yazi, rect)

def zorluk_secimi():
    while True:
        dislay.fill(mavi)
        mesaj_ortali("Zorluk Seçin: 1-Kolay | 2-Orta | 3-Zor", siyah)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    return 10
                elif event.key == pygame.K_2:
                    return 15
                elif event.key == pygame.K_3:
                    return 20

def yilan_ciz(yilan_listesi, yon, dil_cikti=False):
    for i, segment in enumerate(yilan_listesi):
        x, y = segment
        if i == len(yilan_listesi) - 1:
            pygame.draw.rect(dislay, koyu_yesil, [x, y, yilan_boyutu + 2, yilan_boyutu + 2])
            # Gözler
            if yon == "RIGHT":
                pygame.draw.circle(dislay, göz_rengi, (x + 8, y + 3), 2)
                pygame.draw.circle(dislay, göz_rengi, (x + 8, y + 7), 2)
                # Dil
                if dil_cikti:
                    pygame.draw.rect(dislay, dil_kirmizi, (x + 10, y + 5, 4, 2))
            elif yon == "LEFT":
                pygame.draw.circle(dislay, göz_rengi, (x + 3, y + 3), 2)
                pygame.draw.circle(dislay, göz_rengi, (x + 3, y + 7), 2)
                if dil_cikti:
                    pygame.draw.rect(dislay, dil_kirmizi, (x - 4, y + 5, 4, 2))
            elif yon == "UP":
                pygame.draw.circle(dislay, göz_rengi, (x + 3, y + 3), 2)
                pygame.draw.circle(dislay, göz_rengi, (x + 7, y + 3), 2)
                if dil_cikti:
                    pygame.draw.rect(dislay, dil_kirmizi, (x + 5, y - 4, 2, 4))
            elif yon == "DOWN":
                pygame.draw.circle(dislay, göz_rengi, (x + 3, y + 8), 2)
                pygame.draw.circle(dislay, göz_rengi, (x + 7, y + 8), 2)
                if dil_cikti:
                    pygame.draw.rect(dislay, dil_kirmizi, (x + 5, y + 10, 2, 4))
        else:
            pygame.draw.rect(dislay, yesil, [x, y, yilan_boyutu, yilan_boyutu])

def high_score_oku():
    if not os.path.exists(skor_dosya):
        return 0
    with open(skor_dosya, "r") as dosya:
        skorlar = dosya.readlines()
        return max([int(s.strip()) for s in skorlar if s.strip().isdigit()], default=0)

def skor_kaydet(puan):
    with open(skor_dosya, "a") as dosya:
        dosya.write(str(puan) + "\n")

def yeni_yemek_uret(yilan_listesi):
    while True:
        x = random.randrange(0, genislik - yilan_boyutu, 10)
        y = random.randrange(0, yukseklik - yilan_boyutu, 10)
        if [x, y] not in yilan_listesi:
            return x, y

def oyun():
    yilan_hizi = zorluk_secimi()
    x1, y1 = genislik // 2, yukseklik // 2
    x1_hiz = y1_hiz = 0
    yon = "RIGHT"
    onceki_yon = yon
    yilan_listesi = [[x1 - yilan_boyutu, y1], [x1, y1]]
    uzunluk = 2
    yemekx, yemey = yeni_yemek_uret(yilan_listesi)
    oyun_bitti = False
    basladi = False
    yemek_sayisi = 0
    level = 1
    dil_cikti = False
    dil_cikti_suresi = 0
    pause = False

    while not oyun_bitti:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                oyun_bitti = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    pause = not pause
                if not pause:
                    if event.key == pygame.K_LEFT and onceki_yon != "RIGHT":
                        x1_hiz = -yilan_boyutu
                        y1_hiz = 0
                        yon = "LEFT"
                        basladi = True
                    elif event.key == pygame.K_RIGHT and onceki_yon != "LEFT":
                        x1_hiz = yilan_boyutu
                        y1_hiz = 0
                        yon = "RIGHT"
                        basladi = True
                    elif event.key == pygame.K_UP and onceki_yon != "DOWN":
                        y1_hiz = -yilan_boyutu
                        x1_hiz = 0
                        yon = "UP"
                        basladi = True
                    elif event.key == pygame.K_DOWN and onceki_yon != "UP":
                        y1_hiz = yilan_boyutu
                        x1_hiz = 0
                        yon = "DOWN"
                        basladi = True

        if pause:
            mesaj_ortali("Oyun Duraklatıldı - P ile devam et", siyah)
            pygame.display.update()
            continue

        if not basladi:
            dislay.fill(mavi)
            mesaj_ortali("Ok tuşlarını kullanarak oyuna başlayın", siyah)
            pygame.display.update()
            continue

        x1 += x1_hiz
        y1 += y1_hiz
        onceki_yon = yon

        # Kenar geçiş
        if x1 >= genislik: x1 = 0
        elif x1 < 0: x1 = genislik - yilan_boyutu
        if y1 >= yukseklik: y1 = 0
        elif y1 < 0: y1 = yukseklik - yilan_boyutu

        dislay.fill(mavi)
        pygame.draw.rect(dislay, kirmizi, [yemekx, yemey, yilan_boyutu, yilan_boyutu])

        yilan_kafa = [x1, y1]
        yilan_listesi.append(yilan_kafa)
        if len(yilan_listesi) > uzunluk:
            del yilan_listesi[0]

        for segment in yilan_listesi[:-1]:
            if segment == yilan_kafa:
                oyun_bitti = True

        # Dil çıkarma süresi kontrolü
        if dil_cikti:
            if pygame.time.get_ticks() - dil_cikti_suresi > 300:  # 300 ms sonra dil geri çekilir
                dil_cikti = False

        yilan_ciz(yilan_listesi, yon, dil_cikti)
        puan_yazdir(uzunluk - 2)
        level_yazdir(level)
        highscore_yazdir()
        pygame.display.update()

        if x1 == yemekx and y1 == yemey:
            uzunluk += 1
            yemek_sayisi += 1
            yemekx, yemey = yeni_yemek_uret(yilan_listesi)

            if yemek_sayisi % 5 == 0:
                level += 1
                yilan_hizi += 1

            # Dil çıkarma animasyonu başlat
            dil_cikti = True
            dil_cikti_suresi = pygame.time.get_ticks()

        saat.tick(yilan_hizi)

    skor = uzunluk - 2
    skor_kaydet(skor)

    dislay.fill(mavi)
    mesaj_ortali("Oyun Bitti!", kirmizi, -30)
    mesaj_ortali(f"Skorun: {skor}", siyah, 10)
    mesaj_ortali("R - Yeniden Başla | Q - Çık", siyah, 40)
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    oyun()
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()

oyun()