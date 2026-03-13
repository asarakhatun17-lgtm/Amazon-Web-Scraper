# Sabse pehle humein tools (libraries) import karne hain
import requests
from bs4 import BeautifulSoup

def get_amazon_data(url):
    print("Amazon par ja rahe hain... 🛒")
    
    # Amazon bots ko block karta hai, isliye humein 'Browser' jaisa banna padega
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Accept-Language": "en-US, en;q=0.5"
    }

    # Website ka poora data mangwana
    response = requests.get(url, headers=headers)
    
    # BeautifulSoup ka use karke HTML se sirf kaam ki cheez nikalna
    soup = BeautifulSoup(response.content, "html.parser")

    try:
        # Product ka naam dhoondhna
        title = soup.find(id="productTitle").get_text().strip()
        
        # Product ka price dhoondhna
        price_element = soup.find("span", {"class": "a-price-whole"})
        price = price_element.get_text().strip() if price_element else "Price nahi mila"

        print("\n--- 🎯 RESULT ---")
        print("Product Name:", title)
        print("Price: ₹", price)
        print("-----------------")

    except Exception as e:
        print("\n❌ Oh no! Kuch error aaya. Shayad Amazon ne page block kar diya.", e)

# Yahan humne ek iPhone ka test link dala hai. 
# Tum chahe toh apna koi aur link daal kar test kar sakti ho!
test_url = "https://www.amazon.in/Apple-iPhone-13-128GB-Midnight/dp/B09G9HD6PD/"

get_amazon_data(test_url)
