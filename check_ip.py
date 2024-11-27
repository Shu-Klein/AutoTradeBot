import requests


def get_public_ip():
    ipv4 = None
    ipv6 = None

    # נסה לקבל את כתובת ה-IPv4
    try:
        ipv4_response = requests.get("https://ipv4.icanhazip.com", timeout=5)
        ipv4_response.raise_for_status()
        ipv4 = ipv4_response.text.strip()
    except Exception as e:
        print("לא נמצא IPv4 ציבורי:", e)

    # נסה לקבל את כתובת ה-IPv6
    try:
        ipv6_response = requests.get("https://api64.ipify.org?format=json", timeout=5)
        ipv6_response.raise_for_status()
        ipv6 = ipv6_response.json().get("ip")
    except Exception as e:
        print("לא נמצא IPv6 ציבורי:", e)

    # הדפסת הכתובות
    if ipv4:
        print(f"כתובת ה-IPv4 הציבורית שלך היא: {ipv4}")
    if ipv6:
        print(f"כתובת ה-IPv6 הציבורית שלך היא: {ipv6}")

    # החזרת הכתובת המועדפת (IPv4 קודם, ואם אין אז IPv6)
    return ipv4 if ipv4 else ipv6


# קריאה לפונקציה
public_ip = get_public_ip()
if public_ip:
    print(f"כתובת ה-IP הטובה ביותר לשימוש היא: {public_ip}")
else:
    print("לא ניתן לאתר כתובת IP ציבורית.")
