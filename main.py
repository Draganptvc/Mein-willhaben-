import requests

def pretrazi_willhaben(rec):
    url = f"https://www.willhaben.at/webapi/iad/search/v2?keyword={rec}"
    headers = {"User-Agent": "Mozilla/5.0"}
    
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            print(f"Oglasi za '{rec}':")
            for item in data.get("advertSummaryList", []):
                description = item.get("description", "Bez naslova")
                print(f"- {description}")
        else:
            print("Greška pri dohvatanju oglasa.")
    except Exception as e:
        print(f"Greška: {e}")

if __name__ == "__main__":
    # Ovde umesto 'iPhone' upiši šta želiš da pretražuješ
    pretrazi_willhaben("iPhone")


