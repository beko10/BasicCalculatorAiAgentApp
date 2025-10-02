import logging
from google import genai
from google.genai import types
from tool import CalculatorAgentTool


class CalculatorAgent:
    """
    Gemini API kullanarak matematiksel hesaplamalar yapan agent.
    
    Attributes:
        tool: Matematiksel işlem araçları
        client: Gemini API client
        config: Gemini konfigürasyonu
    """
    
    def __init__(self, key: str):
        """
        Agent'ı başlatır.
        
        Args:
            key: Gemini API anahtarı
        """
        self.tool = CalculatorAgentTool()
        self.key = key
        self.client = genai.Client(api_key=key)
        self.logger = logging.getLogger(__name__)

    def _create_config(self) -> types.GenerateContentConfig:
        """Gemini konfigürasyonunu oluşturur."""
        return types.GenerateContentConfig(
            system_instruction=(
                "Sen bir hesap makinesi asistanısın. "
                "Kullanıcının matematiksel sorularına yardımcı ol. "
                "\n\nÖNEMLİ KURALLAR:"
                "\n- Kullanıcı 'sin45', 'cos30' gibi ifadeler kullandığında, "
                "bu sayının trigonometrik değerini hesapla."
                "\n- Hesaplama yaptıktan sonra MUTLAKA sonucu kullanıcıya göster."
                "\n- Sadece 'hesaplıyorum' deme, sonucu söyle!"
                "\n- Sonuçları net ve açık bir şekilde sun."
            ),
            tools=self._get_tool_list(),
            tool_config=self._get_tool_config()
            )

    def _get_tool_config(self):
        """Araç konfigürasyonunu döndürür."""
        config = types.ToolConfig(
            function_calling_config=types.FunctionCallingConfig(
                mode="AUTO"
            )
        )
        return config

    def _get_tool_list(self):
        """Kullanılabilir araçların listesini döndürür."""
        return [
            self.tool.add, self.tool.subtract, self.tool.multiply,
            self.tool.divide, self.tool.power, self.tool.sqrt,
            self.tool.factorial, self.tool.modulus, self.tool.logarithm,
            self.tool.sine, self.tool.cosine, self.tool.tangent,
            self.tool.series_sum
        ]

    def generate_response(self, prompt: str) -> str:
        """
        Kullanıcı sorusuna yanıt üretir.
        
        Args:
            prompt: Kullanıcı sorusu
            
        Returns:
            Model yanıtı
            
        Raises:
            Exception: API hatası durumunda
        """
        try:
            self.logger.info(f"İstek işleniyor: {prompt}")
            
            response = self.client.models.generate_content(
                model="gemini-2.0-flash",  
                contents=prompt,
                config=self._create_config()
            )
            
            self.logger.info("Yanıt başarıyla oluşturuldu")
            return response.text
            
        except Exception as e:
            self.logger.error(f"Hata oluştu: {str(e)}")
            raise