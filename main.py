import logging
from dotenv import load_dotenv
from agent import CalculatorAgent
import os

# Logging yapılandırması
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

load_dotenv()

def main():
    """Ana uygulama döngüsü."""
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    
    if not GEMINI_API_KEY:
        print("❌ GEMINI_API_KEY bulunamadı!")
        return
    
    agent = CalculatorAgent(GEMINI_API_KEY)
    
    print("🧮 Hesap Makinesi Agent'ı başlatıldı!")
    print("Çıkmak için 'q' yazın.\n")
    
    while True:
        try:
            prompt = input("📝 Matematiksel işlem: ")
            
            if prompt.lower() in ['q', 'quit', 'exit']:
                print("👋 Görüşmek üzere!")
                break
            
            if not prompt.strip():
                continue
                
            response = agent.generate_response(prompt=prompt)
            print(f"🤖 Yanıt: {response}\n")
            
        except KeyboardInterrupt:
            print("\n👋 Görüşmek üzere!")
            break
        except Exception as e:
            print(f"❌ Hata: {str(e)}\n")

if __name__ == "__main__":
    main()