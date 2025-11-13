#!/usr/bin/env python

#---------------KNIHOVNY--------------#
import requests
from bs4 import BeautifulSoup

#---------------PROMĚNNÉ--------------#
url = "https://online.atletika.cz/vysledky/36101/20"
my_name = "Tomáš Mirvald"

#---------------FUNKCE----------------#

def nacti_stranku(url):
    """Načte HTML stránky a vrátí objekt BeautifulSoup"""
    response = requests.get(url)
    response.raise_for_status()
    return BeautifulSoup(response.text, "html.parser")

def vypis_h2(soup):
    """Najde všechny <h2> nadpisy a vypíše je přehledně"""
    h2_tags = soup.find_all("h2")
    print("=== Všechny <h2> nadpisy na stránce ===")
    for i, h2 in enumerate(h2_tags, start=1):
        print(f"{i}. {h2.get_text(strip=True)}")

def najdi_jmeno(soup, jmeno):
    """Najde <span> s daným jménem a vypíše nadřazený řádek tabulky"""
    span_with_name = soup.find("span", string=lambda text: text and jmeno in text)
    
    if span_with_name:
        parent_tr = span_with_name.find_parent("tr")
        print(f"\n=== Řádek tabulky obsahující jméno '{jmeno}' ===")
        print(parent_tr.get_text(separator=' | ', strip=True))
    else:
        print(f"Text '{jmeno}' nebyl na stránce nalezen.")

#---------------MAIN------------------#

def main():
    soup = nacti_stranku(url)
    vypis_h2(soup)
    najdi_jmeno(soup, my_name)

if __name__ == "__main__":
    main()

