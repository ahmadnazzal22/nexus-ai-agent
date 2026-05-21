import requests

def get_weather(city: str) -> str:
    """
    يجيب الطقس من wttr.in — مجاني بدون API key
    مثال: get_weather("Amman") → "الطقس في عمان: 22°C صافي"
    """
    try:
        # wttr.in بيرجع JSON مجاني
        url = f"https://wttr.in/{city}?format=j1&lang=ar"
        response = requests.get(url, timeout=5)
        
        if response.status_code != 200:
            return f"ما قدرت أجيب طقس {city}"
        
        data = response.json()
        current = data["current_condition"][0]
        
        temp_c = current["temp_C"]
        feels_like = current["FeelsLikeC"]
        humidity = current["humidity"]
        description = current["weatherDesc"][0]["value"]
        
        return (
            f"🌤️ الطقس في {city}:\n"
            f"• الحرارة: {temp_c}°C (تحس كأنها {feels_like}°C)\n"
            f"• الرطوبة: {humidity}%\n"
            f"• الحالة: {description}"
        )
    
    except requests.Timeout:
        return "الطلب أخذ وقت طويل — جرب مرة ثانية"
    except Exception as e:
        return f"خطأ في جلب الطقس: {str(e)}"