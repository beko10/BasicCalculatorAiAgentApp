import math
from typing import Dict, Union

class CalculatorAgentTool:
    """Gemini SDK için matematiksel işlem araçları."""
    
    def add(self, a: float, b: float) -> Dict[str, Union[float, str]]:
        """İki sayıyı toplar."""
        return {"result": a + b}

    def subtract(self, a: float, b: float) -> Dict[str, Union[float, str]]:
        """İki sayıyı çıkarır."""
        return {"result": a - b}  

    def multiply(self, a: float, b: float) -> Dict[str, Union[float, str]]:
        """İki sayıyı çarpar."""
        return {"result": a * b}

    def divide(self, a: float, b: float) -> Dict[str, Union[float, str]]:
        """
        İki sayıyı böler.
        
        Args:
            a: Bölünen
            b: Bölen
            
        Returns:
            Bölme sonucu veya hata mesajı
        """
        if b == 0:
            return {"error": "Sıfıra bölme hatası"}
        return {"result": a / b}

    def power(self, base: float, exponent: float) -> Dict[str, Union[float, str]]:
        """Üs alma işlemi yapar."""
        try:
            result = base ** exponent
            return {"result": result}
        except Exception as e:
            return {"error": f"Üs alma hatası: {str(e)}"}

    def sqrt(self, value: float) -> Dict[str, Union[float, str]]:
        """Karekök hesaplar."""
        if value < 0:
            return {"error": "Negatif sayının karekökü hesaplanamaz"}
        return {"result": math.sqrt(value)}

    def factorial(self, n: int) -> Dict[str, Union[int, str]]:
        """Faktöriyel hesaplar."""
        if n < 0:
            return {"error": "Negatif sayının faktöriyeli hesaplanamaz"}
        if n > 170:  # Overflow önleme
            return {"error": "Sayı çok büyük (maksimum 170)"}
        if n == 0 or n == 1:
            return {"result": 1}
        result = 1
        for i in range(2, n + 1):
            result *= i
        return {"result": result}

    def modulus(self, a: int, b: int) -> Dict[str, Union[int, str]]:
        """Mod alma işlemi yapar."""
        if b == 0:
            return {"error": "Sıfıra göre mod alınamaz"}
        try:
            return {"result": a % b}
        except Exception as e:
            return {"error": str(e)}

    def logarithm(self, value: float, base: float = 10.0) -> Dict[str, Union[float, str]]:
        """
        Logaritma hesaplar.
        
        Args:
            value: Logaritması alınacak değer
            base: Logaritma tabanı (varsayılan: 10)
        """
        if value <= 0:
            return {"error": "Logaritma pozitif olmayan değerler için tanımsız"}
        if base <= 0 or base == 1:
            return {"error": "Logaritma tabanı 0'dan büyük ve 1'den farklı olmalı"}
        try:
            return {"result": math.log(value, base)}
        except Exception as e:
            return {"error": f"Logaritma hatası: {str(e)}"}

    def sine(self, angle: float) -> Dict[str, float]:
        """Sinüs hesaplar (derece cinsinden)."""
        return {"result": math.sin(math.radians(angle))}

    def cosine(self, angle: float) -> Dict[str, float]:
        """Kosinüs hesaplar (derece cinsinden)."""
        return {"result": math.cos(math.radians(angle))}

    def tangent(self, angle: float) -> Dict[str, Union[float, str]]:
        """Tanjant hesaplar (derece cinsinden)."""
        try:
            return {"result": math.tan(math.radians(angle))}
        except Exception as e:
            return {"error": f"Tanjant hatası: {str(e)}"}

    def series_sum(self, n: int) -> Dict[str, Union[int, str]]:
        """1'den n'e kadar sayıların toplamını hesaplar."""
        if n < 1:
            return {"error": "n pozitif bir tam sayı olmalı"}
        return {"result": sum(range(1, n + 1))}