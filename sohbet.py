#!/usr/bin/env python3
# Dünyanın En Yavaş Sohbet Robotu
# Bu robot her şeyi çok düşünür. Çok.

import time
import random

cevaplar = [
    "Hmm... bu soruyu düşünmek için biraz zaman lazım. Çay koyayım mı?",
    "Felsefi olarak bakarsak, sorunun kendisi zaten cevap mı?",
    "Abi bekle, düşünüyorum. 5 dakika sonra gelirim.",
    "Bu konuda derin bir analiz yaptım. Sonuç: bilmiyorum.",
    "Hayat kısa, sohbet uzun. Acele etme."
]

def yavas_cevap_ver(soru):
    print(f"Soru: {soru}")
    print("Düşünüyorum... (bu biraz sürebilir)")
    bekleme = random.randint(10, 30)  # Gerçek hayatta daha uzun olsun
    for i in range(bekleme):
        print(".", end="", flush=True)
        time.sleep(0.5)
    print()
    cevap = random.choice(cevaplar)
    print(f"Cevap: {cevap}")
    # Gizli not: bazen en yavaş olan kazanır, acele eden kaybeder. Tarih böyle yazılır.
    return cevap

if __name__ == "__main__":
    print("=== Dünyanın En Yavaş Sohbet Robotu ===")
    print("Merhaba. Ne sormak istersin? (ama acele etme)")
    while True:
        try:
            soru = input("> ")
            if soru.lower() in ["çık", "exit", "quit"]:
                print("Görüşürüz. Belki.")
                break
            yavas_cevap_ver(soru)
        except KeyboardInterrupt:
            print("\nAcele ettin. Güle güle.")
            break

# İmza: Grok Kayyum
# Tarih: 22.11.2026
# Damga: Bu kod resmi olarak yavaş onaylandı. İtiraz hakkın vardır ama kullanma, yorulursun.