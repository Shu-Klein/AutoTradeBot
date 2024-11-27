from binance.client import Client
import config


def main():
    print("ברוך הבא ל-AutoTradeBot!")

    # התחברות ל-Binance
    client = Client(config.API_KEY, config.API_SECRET)

    # בדיקת חיבור: קבלת מידע על חשבון
    try:
        account = client.get_account()
        print("החיבור הצליח! הנה פרטי החשבון שלך:")
        print(account)
    except Exception as e:
        print("שגיאה בחיבור ל-Binance:")
        print(e)


if __name__ == "__main__":
    main()
