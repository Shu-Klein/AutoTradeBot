from binance.client import Client
import pandas as pd
import config


def fetch_historical_data(symbol, interval, start_str, save_path):
    # פונקציה להורדת נתונים היסטוריים מזוג מסחר בבינאנס
    # symbol: זוג המסחר (למשל, 'BTCUSDT')
    # interval: מסגרת הזמן (למשל, '1h')
    # start_str: תאריך התחלה למשיכת הנתונים (למשל, '1 Jan, 2023')
    # save_path: נתיב לשמירת הקובץ בפורמט CSV

    # יצירת חיבור ל-API של Binance
    client = Client(config.API_KEY, config.API_SECRET)

    try:
        # הורדת הנתונים ההיסטוריים
        print(f"Fetching historical data for {symbol}...")
        klines = client.get_historical_klines(symbol, interval, start_str)

        # עיבוד הנתונים ל-DataFrame
        df = pd.DataFrame(klines, columns=[
            "timestamp", "open", "high", "low", "close", "volume",
            "close_time", "quote_asset_volume", "number_of_trades",
            "taker_buy_base_asset_volume", "taker_buy_quote_asset_volume", "ignore"
        ])

        # שמירה על עמודות רלוונטיות בלבד
        df = df[["timestamp", "open", "high", "low", "close", "volume"]]
        df["timestamp"] = pd.to_datetime(df["timestamp"], unit='ms')

        # שמירת הנתונים כ-CSV
        df.to_csv(save_path, index=False)
        print(f"Data saved to {save_path}")

    except Exception as e:
        print("Error fetching historical data:", e)


# דוגמה לשימוש
if __name__ == "__main__":
    fetch_historical_data(
        symbol="BTCUSDT",
        interval=Client.KLINE_INTERVAL_1HOUR,
        start_str="1 Jan, 2023",
        save_path="btc_usdt_historical_data.csv"
    )
