# 🐍 Gelişmiş Python Yılan Oyunu

Bu proje, Pygame kütüphanesi kullanılarak geliştirilmiş, içinde seviye sistemi ve animasyonlar barındıran bir klasik yılan oyunu uygulamasıdır.

## 🚀 Öne Çıkan Özellikler
* **Dinamik Zorluk:** Başlangıçta 3 farklı zorluk seviyesi (Kolay, Orta, Zor) seçeneği.
* **Level Sistemi:** Her 5 yem yendiğinde yılanın hızı artar ve seviye atlanır.
* **Kalıcı Skor Tablosu:** `skorlar.txt` dosyası aracılığıyla en yüksek skorlar kaydedilir ve takip edilir.
* **Görsel Detaylar:** Yılanın hareket yönüne göre değişen gözler ve yem yediğinde tetiklenen dil çıkarma animasyonu.
* **Oyun Kontrolü:** 'P' tuşu ile oyunu duraklatma, 'R' ile yeniden başlatma imkanı.

## 🛠️ Teknik Detaylar
* **Dosya Yönetimi:** Python `os` modülü ile skor takibi.
* **Oyun Döngüsü:** Nesne yönelimli mantık ve event (olay) yönetimi.
* **Grafik:** Pygame çizim fonksiyonları ile dinamik render.

## 📦 Kurulum
1. Pygame kütüphanesini kurun:
   ```bash
   pip install pygame
2. Oyunu çalıştırın:
   ```bash
   python snake_game.py
