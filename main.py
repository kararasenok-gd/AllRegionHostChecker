import requests
import time

regions_old = ['Austria', 'Brazil', 'Bulgaria', 'Czechia', 'Finland', 'France', 'Germany', 'Hong Kong', 'India', 'Iran', 'Israel', 'Italy', 'Kazakhstan', 'Lithuania', 'Moldova', 'Netherlands', 'Poland', 'Portugal', 'Russia', 'Serbia', 'Switzerland', 'Thailand', 'Turkey', 'UAE', 'UK', 'Ukraine', 'USA']
regions = ['Abkhazia', 'Afghanistan', 'Albania', 'Algeria', 'Argentina', 'Armenia', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Belarus', 'Belgium', 'Bermuda Islands', 'Bolivia', 'Brazil', 'Bulgaria', 'Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Chile', 'China', 'Colombia', 'Congo', 'Costa Rica', 'Cuba', 'Cyprus', 'Czech Republic', 'Denmark', 'Dominican Republic', 'Ecuador', 'Egypt', 'El Salvador', 'Estonia', 'Ethiopia', 'Finland', 'France', 'Georgia', 'Germany', 'Ghana', 'Gibraltar', 'UK', 'Greece', 'Guatemala', 'Guinea', 'Haiti', 'Hawaii', 'Honduras', 'Hong Kong', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Israel', 'Italy', 'Ivory Coast', 'Jamaica', 'Japan', 'Kazakhstan', 'Kenya', 'Kuwait', 'Kyrgyzstan', 'Latvia', 'Lebanon', 'Liberia', 'Libya', 'Lithuania', 'Luxemburg', 'Madagascar', 'Malawi', 'Malaysia', 'Malta', 'Mexico', 'Moldova', 'Monaco', 'Mongolia', 'Morocco', 'Nepal', 'Netherlands', 'New Zeland', 'Nicaragua', 'Nigeria', 'North Korea', 'Norway', 'Oman', 'Pakistan', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal', 'Puerto Rico', 'Romania', 'Russia', 'Rwanda', 'Saudi Arabia', 'Senegal', 'Sierra Leone', 'Singapore', 'Slovakia', 'Slovenia', 'South Africa', 'South Korea', 'South Ossetia', 'Spain', 'Sri Lanka', 'Sudan', 'Sweden', 'Switzerland', 'Syria', 'Taiwan', 'Tajikistan', 'Thailand', 'Togo', 'Tunisia', 'Turkey', 'Turkmenistan', 'Uganda', 'Ukraine', 'UAE', 'USA', 'Uruguay', 'Uzbekistan', 'Venezuela', 'Yemen', 'Zaire', 'Zambia', 'Zimbabwe']

url = input(f"Введите URL сайта: ")

if 'https://' in url:
    urlfix = url.replace('https://', '')
else:
    urlfix = url.replace('http://', '')

urlfix = urlfix.replace('/', '')

file = open(f'{urlfix}-status.txt', 'a')

for region in regions:
    try:
        start = time.time()
        response = requests.get(url, headers={'X-Region': region})
        end = time.time()

        status_code = int(response.status_code)
        connection_time = end - start

        if "https://" in url:
            urlfix = url.replace('https://', '')
        else:
            urlfix = url.replace('http://', '')

        if status_code == 200:
            status_code = "200 (OK)"
        elif status_code == 404:
            status_code = "404 (NOT FOUND)"
        elif status_code == 403:
            status_code = "403 (FORBIDDEN)"
        elif status_code == 429:
            status_code = "429 (RATE LIMIT)"


        print(f"Сайт: {url}\nРегион: {region}\nВремя подключения: {connection_time:.3f}s\nСтатус: {status_code}\n")
        
        file.write(f'Сайт: {url}\nРегион: {region}\nВремя подключения: {connection_time:.3f}s\nСтатус: {status_code}\n')

    except requests.exceptions.RequestException as e:
        print(f"Сайт в регеоне {region} отключен! Ошибка: {e}")
        file.write(f'Сайт: {url}\nРегион: {region}\nОшибка: {e}\n')

for a in range(5):
    file.write("\n")
file.write("Made by kararasenok_gd | https://github.com/kararasenok-gd/AllRegionHostChecker/")

file.close()
