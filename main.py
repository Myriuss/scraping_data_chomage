from bs4 import BeautifulSoup
import requests
import csv

# Créer une liste pour stocker toutes les données
all_data = []

# Boucle pour parcourir toutes les pages
for page_num in range(1, 1165):
    # URL de la page à scraper
    url = f'https://www.villesavivre.fr/classements/taux-de-chomage/page/{page_num}/'

    # Récupérer le contenu de la page web
    response = requests.get(url)

    # Vérifier si la requête a réussi
    if response.status_code == 200:
        # Analyser le contenu HTML avec Beautiful Soup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Trouver les éléments contenant les données
        data_table = soup.find('table', class_='ranking-table')

        # Vérifier si la table a été trouvée
        if data_table:
            # Extraire les données de la table
            rows = data_table.find_all('tr')
            for row in rows:
                cols = row.find_all('td')
                cols = [col.text.strip() for col in cols]
                all_data.append(cols)
        else:
            print(f"La table n'a pas été trouvée sur la page {page_num}")
    else:
        print(f"Échec de la requête sur la page {page_num}. Code d'état : {response.status_code}")

# Écrire toutes les données dans un fichier CSV
with open('donnees_taux_de_chomage.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(all_data)

print("Toutes les données ont été écrites dans 'donnees_taux_de_chomage.csv'.")