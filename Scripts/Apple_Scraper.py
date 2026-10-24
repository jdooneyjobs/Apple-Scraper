import requests
import random
import time

# Example uses Boston-area ZIP 02143 and a standard iPhone Duo 256GB Star White SKU placeholder
# Swap 'PART_NUMBER' out for the exact Apple Store configuration SKU once parsed from the buy page
PART_NUMBER = "7.6-inch-display-256gb-star-white-att"  
ZIP_CODE = "02143"

url = f"https://apple.com{PART_NUMBER}&location={ZIP_CODE}"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": "https://www.apple.com/shop/buy-iphone/iphone-duo",
    "X-Requested-With": "XMLHttpRequest"
}

try:
    # Adding a randomized delay to slide under Akamai threshold filters
    time.sleep(random.uniform(3, 7))
    
    response = requests.get(url, headers=headers, timeout=10)
    if response.status_code == 200:
        data = response.json()
        stores = data.get("body", {}).get("content", {}).get("pickupMessage", {}).get("stores", [])
        
        for store in stores:
            store_name = store.get("storeName")
            parts_availability = store.get("partsAvailability", {})
            product_status = parts_availability.get(PART_NUMBER, {}).get("pickupDisplay")
            
            # "available" means a reservation window can be selected right now
            print(f"Store: {store_name} | iPhone Duo Status: {product_status}")
    else:
        print(f"Encountered Block/Error Code: {response.status_code}")

except Exception as e:
    print(f"Scraper error encountered: {e}")