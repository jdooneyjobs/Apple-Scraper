import requests
import random
import time

# Example uses Boston-area ZIP 02143 and a standard iPhone Duo 256GB Star White SKU placeholder
# Swap 'PART_NUMBER' out for the exact Apple Store configuration SKU once parsed from the buy page
# PART_NUMBER = "7.6-inch-display-256gb-star-white-att"
PART_NUMBER = "MK1E4LL/A"  # Example SKU for iPhone Duo 256GB Star White
ZIP_CODE = "02143"

url = "https://www.apple.com/shop/fulfillment-messages"
params = {
    "pl": "true",
    "parts.0": PART_NUMBER,
    "location": ZIP_CODE,
}

headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Language": "en-US,en;q=0.9",
}

print(f"Scraping Apple Store availability for part number: {PART_NUMBER} in ZIP code: {ZIP_CODE}")
response = requests.get(url, params=params, headers=headers, timeout=10)
print(f"Request URL: {response.url}")
print(f"Response Status Code: {response.status_code}")
print("Status:", response.status_code)
print("Content-Type:", response.headers.get("Content-Type"))
print("Server:", response.headers.get("Server"))
print("Retry-After:", response.headers.get("Retry-After"))
print("Response body:", response.text[:500])

# try:
#     # Adding a randomized delay to slide under Akamai threshold filters
#     time.sleep(random.uniform(3, 7))
#
#     response = requests.get(url, params=params, headers=headers, timeout=10)
#     if response.status_code == 200:
#         data = response.json()
#         stores = data.get("body", {}).get("content", {}).get("pickupMessage", {}).get("stores", [])
#
#         for store in stores:
#             store_name = store.get("storeName")
#             parts_availability = store.get("partsAvailability", {})
#             product_status = parts_availability.get(PART_NUMBER, {}).get("pickupDisplay")
#
#             # "available" means a reservation window can be selected right now
#             print(f"Store: {store_name} | iPhone Duo Status: {product_status}")
#     else:
#         print(f"Encountered Block/Error Code: {response.status_code}")
#
# except Exception as e:
#     print(f"Scraper error encountered: {e}")