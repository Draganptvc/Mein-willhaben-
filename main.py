import requests
import time

# Tvoj kanal iz ntfy aplikacije
KANAL = "dragan_willhaben_auta_99"

def posalji_signal(naslov, poruka, link=""):
    url = f"https://ntfy.sh/{KANAL}"
    headers = {
        "Title": naslov.encode('utf-8'),
        "Priority": "high",
        "Tags": "car,warning"
    }
    if link:
        headers["Click"] = link
        
    try:
        requests.post(url, data=poruka.encode('utf-8'), headers=headers)
    except Exception as e:
        print(f"Greška pri slanju: {e}")

def pretrazi_willhaben():
    # URL pretrage za automobile
    url = "https://www.willhaben.at/webapi/iad/search/v2?category=100100"
    headers = {"User-Agent": "Mozilla/5.0"}
    
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            oglasi = data.get("advertSummaryList", [])
            
            print(f"Pronađeno {len(oglasi)} oglasa. Šaljem test signal...")
            
            # Šaljemo obaveštenje za prvi najnoviji auto
            if oglasi:
                prvi = oglasi[0]
                naslov = prvi.get("description", "Novi automobil!")
                # Slanje signala na ntfy
                posalji_signal("STIGAO NOVI AUTO!", naslov)
        else:
            print("Greška pri dohvatanju Willhaben oglasa.")
    except Exception as e:
        print(f"Greška: {e}")

if __name__ == "__main__":
    # Slanje brzog testnog signala direktno pri pokretanju
    posalji_signal("SISTEM JE SPREMAN!", "Tvoja aplikacija za Willhaben automobile je uspešno povezana.")
    pretrazi_willhaben()
