# 🛡️ sec-headers-check

Hafif ve hızlı bir HTTP güvenlik başlığı (Security Header) denetleyicisi. Hedef web uygulamasının güvenlik yapılandırmalarını pasif olarak analiz eder ve terminalde detaylı rapor ile güvenlik skoru sunar.

---

## 🔍 Denetlenen Güvenlik Başlıkları

* **Strict-Transport-Security (HSTS):** Zorunlu HTTPS bağlantısını denetler.
* **Content-Security-Policy (CSP):** XSS ve veri enjeksiyonu korumalarını kontrol eder.
* **X-Frame-Options:** Clickjacking (tıklama hırsızlığı) korumasını denetler.
* **X-Content-Type-Options:** MIME-sniffing açıklarına karşı korumayı kontrol eder.
* **Referrer-Policy:** İsteklerle sızan kaynak URL bilgisinin kısıtlanmasını denetler.
* **Permissions-Policy:** Kamera, mikrofon ve donanım API erişim sınırlarını inceler.

---

## 🚀 Kurulum & Çalıştırma

```bash
# Depoyu klonlayın
git clone [https://github.com/KULLANICI_ADIN/sec-headers-check.git](https://github.com/KULLANICI_ADIN/sec-headers-check.git)
cd sec-headers-check

# Sanal ortamı kurun ve aktif edin
python3 -m venv venv
source venv/bin/activate

# Bağımlılıkları yükleyin
pip install -r requirements.txt

# Çalıştırın
python3 main.py -u github.com
