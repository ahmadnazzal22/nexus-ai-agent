import requests

def search_web(query: str) -> str:
    """
    بحث قوي عبر Wikipedia API — يرجع معلومات كاملة ومفصّلة
    """
    try:
        # أولاً: ابحث عن أقرب مقالة
        search_url = "https://en.wikipedia.org/w/api.php"
        search_params = {
            "action": "query",
            "list": "search",
            "srsearch": query,
            "format": "json",
            "srlimit": 3
        }

        search_res = requests.get(search_url, params=search_params, timeout=6)
        search_data = search_res.json()
        results = search_data.get("query", {}).get("search", [])

        if not results:
            return arabic_search_fallback(query)

        # خذ أفضل نتيجة
        top_title = results[0]["pageid"]

        # اجلب المحتوى الكامل للمقالة
        content_params = {
            "action": "query",
            "pageids": top_title,
            "prop": "extracts",
            "exintro": True,
            "explaintext": True,
            "format": "json"
        }

        content_res = requests.get(search_url, params=content_params, timeout=6)
        content_data = content_res.json()
        pages = content_data.get("query", {}).get("pages", {})
        page = list(pages.values())[0]
        extract = page.get("extract", "")

        if not extract:
            return arabic_search_fallback(query)

        # رجّع أول 1000 حرف كمعلومة كاملة
        return extract[:1000].strip()

    except requests.Timeout:
        return "انتهت مهلة البحث — جرب مرة ثانية"
    except Exception as e:
        return arabic_search_fallback(query)


def arabic_search_fallback(query: str) -> str:
    """
    جرب Wikipedia العربي إذا الإنجليزي ما أعطى نتائج
    """
    try:
        url = "https://ar.wikipedia.org/w/api.php"
        params = {
            "action": "query",
            "list": "search",
            "srsearch": query,
            "format": "json",
            "srlimit": 1
        }
        res = requests.get(url, params=params, timeout=6)
        data = res.json()
        results = data.get("query", {}).get("search", [])

        if not results:
            return f"ما لقيت معلومات كافية عن: {query}"

        pageid = results[0]["pageid"]
        content_params = {
            "action": "query",
            "pageids": pageid,
            "prop": "extracts",
            "exintro": True,
            "explaintext": True,
            "format": "json"
        }
        content_res = requests.get(url, params=content_params, timeout=6)
        content_data = content_res.json()
        pages = content_data.get("query", {}).get("pages", {})
        page = list(pages.values())[0]
        extract = page.get("extract", "")

        return extract[:1000].strip() if extract else f"ما لقيت معلومات عن: {query}"

    except Exception:
        return f"ما قدرت أجيب معلومات عن: {query}"