## BasicCalculatorAiAgentApp

Basit bir "Hesap Makinesi" AI agent uygulaması. Bu proje, Google Gemini (genai) SDK'sını kullanarak doğal dil veya kısa matematik ifadeleri alır ve arka planda tanımlı araçları (toplama, çıkarma, çarpma, bölme, trigonometrik fonksiyonlar, faktöriyel, vb.) çağırarak sonuç üretir.

Özellikle Türkçe kullanım için hazırlanmış kısa örneklerle birlikte basit bir komut satırı arayüzü sunar.

## Dosya Yapısı

- `main.py` — Uygulamayı başlatan giriş noktası (komut satırı etkileşimi).
- `agent.py` — Gemini istemcisi ve model konfigürasyonunu barındıran agent sınıfı.
- `tool.py` — Matematiksel işlemleri yapan araç sınıfları (toplama, çıkarma, sin, cos, factorial vb.).
- `requirements.txt` — (Şu an boş) Projeye özel Python paketlerini buraya ekleyebilirsiniz.

## Gereksinimler

- Python 3.10 veya üstü önerilir.
- Aşağıdaki Python paketleri gereklidir (manuel kurulum örneği aşağıda):
  - `python-dotenv` (ortam değişkenlerini `.env` dosyasından yüklemek için)
  - `google-genai` (Google Gemini SDK; paket isimleri değişebileceğinden kendi ortamınıza göre doğrulayın)

Not: `requirements.txt` dosyası boş bırakılmıştır — isterseniz kullandığınız paketleri buraya ekleyip `pip install -r requirements.txt` ile kurabilirsiniz.

## Kurulum (Windows, cmd.exe)

1. Sanal ortam oluşturun ve aktif edin:

```cmd
python -m venv venv
venv\Scripts\activate
```

2. Gerekli paketleri yükleyin (örnek):

```cmd
pip install python-dotenv google-genai
```

3. (İsteğe bağlı) Yüklü paketleri `requirements.txt` içine yazın:

```cmd
pip freeze > requirements.txt
```

## Konfigürasyon

Uygulama, `.env` dosyasından `GEMINI_API_KEY` anahtarını okur. Proje kökünde bir `.env` dosyası oluşturun ve aşağıdaki gibi API anahtarınızı ekleyin:

```
GEMINI_API_KEY=your_gemini_api_key_here
```

API anahtarınızı güvende tutun. Kesinlikle versiyon kontrolüne (ör. Git) dahil etmeyin.

## Çalıştırma

```cmd
python main.py
```

Program başladıktan sonra matematiksel ifadelerinizi veya sorularınızı Türkçe olarak yazabilirsiniz. Örnekler:

- 2 + 2
- 15 / 3
- sin45
- cos30
- 5 faktöriyel
- log(100, 10)
- 2^8 veya üs alma hakkında "2 üzeri 8" tarzı ifadeler

Çıkmak için `q`, `quit` veya `exit` yazabilirsiniz.

## Nasıl çalışır (kısa)

1. `main.py` kullanıcıdan girdi alır.
2. Girdi `agent.py` içindeki `CalculatorAgent.generate_response` metodu ile Gemini modeline gönderilir.
3. Agent, `tool.py` içindeki araçları (`CalculatorAgentTool`) modele tools olarak kaydeder; model uygun olduğunda bu araçları çağırır ve sonuçları döndürür.

## Hata Ayıklama & Notlar

- Eğer `GEMINI_API_KEY` bulunamazsa program başlatılamaz — `.env` dosyanızı kontrol edin.
- `google-genai` paketinin doğru paket ismi/versiyonunu kullanın; resmi dokümantasyona göre isim değişiklikleri olabilir.
- `requirements.txt` şu an boş; proje ortamınızı sabitlemek isterseniz yükledikten sonra `pip freeze > requirements.txt` çalıştırın.

## Katkıda Bulunma

Basit PR'lar, hata raporları ve iyileştirmeler memnuniyetle karşılanır. Küçük değişiklikler için önce issue açıp kısa bir açıklama bırakın.

## Lisans

Bu proje herhangi bir lisans belirtmiyorsa kişisel kullanım içindir. İsterseniz üst satıra uygun bir açık kaynak lisansı ekleyin (ör. MIT).

---

İhtiyaç halinde README'yi İngilizceye çevirebilir, `requirements.txt`'i güncelleyebilir veya örnek giriş-çıkış testleri ekleyebilirim. Ne istersiniz?
