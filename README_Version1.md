# M3U Birleştirici

Birden fazla m3u dosyası linkinden içerik çekip, tek bir m3u dosyasına birleştiren basit bir Python scripti.

## Kullanım

1. `requests` kütüphanesini yükleyin:
   ```
   pip install requests
   ```
2. Scripti çalıştırın:
   ```
   python merge_m3u.py https://ornek.com/list1.m3u https://ornek.com/list2.m3u
   ```
3. Sonuç `merged.m3u` dosyası olarak oluşacaktır.

## Açıklama

- Her m3u dosyasının içeriği çekilir ve sadece ilk dosyanın başındaki `#EXTM3U` etiketi kalır.
- Hatalı veya ulaşılamayan linkler atlanır.