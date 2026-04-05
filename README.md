
---

# Text Analyzer & Statistics Generator

Bu Python aracı, verilen bir metin dosyasını analiz ederek kelime sayısı, cümle sayısı, karakter istatistikleri ve kelime frekansları gibi detaylı metin madenciliği verileri oluşturur. Akademik ödevler veya temel metin analizi projeleri için uygun, modüler bir yapıya sahiptir.

## Özellikler

* **Detaylı İstatistikler:** Toplam kelime, cümle ve karakter sayılarını hesaplar.
* **Gelişmiş Temizleme:** Kelimeleri noktalama işaretlerinden arındırır ve küçük harfe çevirerek standartlaştırır.
* **Cümle Analizi:** Nokta, soru işareti, ünlem ve üç nokta (...) gibi bitiricileri takip ederek doğru cümle sayımı yapar.
* **Kelime Metrikleri:**
    * En kısa ve en uzun kelimeleri (ve bunların metin içindeki oranlarını) bulur.
    * Kelime başına düşen ortalama cümle oranını hesaplar.
    * Tüm kelimelerin frekans dağılımını azalan sırada listeler.
* **Dosya Çıktısı:** Sonuçları düzenli ve hizalı bir şekilde `.txt` dosyasına yazar.

## Kullanım

Programı iki argümanla (giriş dosyası ve çıktı dosyası) çalıştırmanız yeterlidir:

```bash
python text_analyzer.py input.txt output.txt
```

## Teknik Detaylar

Proje aşağıdaki fonksiyonel bloklardan oluşur:
* `pure_words`: Metni temizleyerek kelime listesi oluşturur.
* `sentence_finder`: Noktalama işaretlerine göre cümle yapısını analiz eder.
* `word_frequency`: Python'ın `lambda` fonksiyonlarını kullanarak kelimeleri kullanım sıklığına göre sıralar.
* `main`: Tüm analiz süreçlerini birleştirir ve çıktı formatını yönetir.

## Örnek Çıktı Formatı

Analiz sonucu oluşturulan dosya şu yapıda görünür:
```text
Statistics about input.txt:
#Words                  : 150
#Sentences              : 12
#Words/#Sentences       : 12.50
#Characters             : 840
...
Words and Frequencies   :
python                  : 0.0450
analysis                : 0.0210
```

---
