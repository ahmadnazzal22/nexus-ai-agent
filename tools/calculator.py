import re

def calculate(expression: str) -> str:
    """
    حاسبة آمنة — تحول العمليات الحسابية لنتيجة
    مثال: "كم يساوي 25 * 4" → "100"
    """
    try:
        # استخرج الأرقام والعمليات من النص
        clean = re.sub(r'[^\d\+\-\*\/\.\(\)\s]', '', expression)
        
        if not clean.strip():
            return "ما قدرت أفهم العملية الحسابية"
        
        result = eval(clean)  # آمن لأننا نظفنا الإدخال
        return f"النتيجة: {result}"
    
    except ZeroDivisionError:
        return "خطأ: ما يصير تقسم على صفر"
    except Exception:
        return "ما قدرت أحسب — تأكد من العملية"