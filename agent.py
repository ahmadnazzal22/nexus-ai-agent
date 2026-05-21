import os
from groq import Groq
from dotenv import load_dotenv
from tools.calculator import calculate
from tools.weather import get_weather
from tools.search import search_web

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def detect_tool(user_input: str) -> str:
    prompt = f"""
أنت مساعد ذكي. حدد أي أداة تناسب السؤال التالي.

الأدوات:
- calculator: للعمليات الحسابية (جمع، طرح، ضرب، قسمة، نسبة مئوية)
- weather: لمعرفة الطقس في أي مدينة
- search: لأي سؤال معلوماتي أو عام

رد بكلمة واحدة فقط: calculator أو weather أو search

السؤال: {user_input}
"""
    res = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=10,
        temperature=0
    )
    tool = res.choices[0].message.content.strip().lower()
    if "calculator" in tool: return "calculator"
    if "weather" in tool: return "weather"
    return "search"


def extract_parameter(user_input: str, tool: str) -> str:
    if tool == "calculator":
        prompt = f"استخرج فقط العملية الحسابية من هذا النص بدون أي كلام إضافي: {user_input}"
    elif tool == "weather":
        prompt = f"استخرج فقط اسم المدينة بالإنجليزي من هذا النص: {user_input}"
    else:
        return user_input

    res = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=30,
        temperature=0
    )
    return res.choices[0].message.content.strip()


def format_response(user_input: str, tool_result: str, tool: str) -> str:
    prompt = f"""
أنت مساعد ذكي خبير ومتمكن. مهمتك تقديم إجابة شاملة ومفيدة.

سؤال المستخدم: {user_input}
البيانات المتاحة: {tool_result}
الأداة المستخدمة: {tool}

تعليمات مهمة:
- إذا كان البحث: قدّم إجابة مفصّلة وكاملة من المعلومات المتاحة، اذكر تواريخ وأرقام وحقائق مهمة
- إذا كان طقس: اعرض المعلومات بشكل منظم وواضح
- إذا كانت حاسبة: أكد النتيجة واشرح الحساب بشكل بسيط
- تكلم بنفس لغة المستخدم (عربي أو إنجليزي)
- لا تقل "بناءً على البيانات" — تكلم بشكل طبيعي ومباشر
- الجواب يكون بين 3-6 جمل مفيدة وغنية بالمعلومات
"""
    res = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=500,
        temperature=0.4
    )
    return res.choices[0].message.content.strip()


def run_agent(user_input: str) -> dict:
    tool      = detect_tool(user_input)
    parameter = extract_parameter(user_input, tool)

    if tool == "calculator":
        tool_result = calculate(parameter)
    elif tool == "weather":
        tool_result = get_weather(parameter)
    else:
        tool_result = search_web(parameter)

    final_answer = format_response(user_input, tool_result, tool)

    return {
        "answer":     final_answer,
        "tool_used":  tool,
        "raw_result": tool_result
    }