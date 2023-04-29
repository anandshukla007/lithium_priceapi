from django.shortcuts import render
import requests
from django.http import JsonResponse
from bs4 import BeautifulSoup


def get_price(request):
    url = "https://www.metal.com/Lithium-ion-Battery/202303240001"

    try:
        getprice = requests.get(url)
        getprice.raise_for_status()  # Raise exception for non-2xx status codes
        soup = BeautifulSoup(getprice.content, "html.parser")
        price_element = soup.find("span", class_="priceDown___2TbRQ")
        price = price_element.text if price_element else "Price not found"

        return JsonResponse({"Current Price": price})
    except requests.exceptions.RequestException as e:
        return JsonResponse({"error": "Error retrieving price: " + str(e)})

