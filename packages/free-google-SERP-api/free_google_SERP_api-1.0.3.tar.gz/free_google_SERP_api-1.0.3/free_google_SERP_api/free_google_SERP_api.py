import requests
import json
import urllib.parse
import pandas as pd
import numpy as np
from requests_html import HTMLSession
import faqs_google_results

def _get_source(url: str):
    try:
        session = HTMLSession()
        response = session.get(url)

        if response.status_code == 200:
            return response
        elif response.status_code == 429:
            print(
                'Error: Too many requests. Google te ha bloqueado temporalmente. Vuelve a intentarlo más tarde.')
            exit()
        else:
            print('Error:' + response)
            exit()
    except requests.exceptions.RequestException as e:
        print(e)

def _get_results(query: str, lang:str):

    query = urllib.parse.quote_plus(query)
    lang = urllib.parse.quote_plus(lang)
    response = _get_source(
        "https://www.google.es/search?q=" + query+"&gl="+lang)

    return response

def _parse_search_results(response, query, lang):

    # La clase del div que contiene cada resultado, es decir<div class="tF2Cxc">
    css_identifier_result = ".tF2Cxc"
    # El elemento que contiene el título, es decir, <h3 class="...
    css_identifier_title = "h3"
    # La clase del div que contiene el ancla, es decir <div class="yuRUbf"><a ...
    css_identifier_link = ".yuRUbf a"
    # La clase del elemento principal que contiene el fragmento.<span>
    css_identifier_text = ".VwiC3b"
    # La clase del elemento que contiene el fragmento.<span><em>
    css_identifier_bold = ".VwiC3b span em"
    # La clase del elemento que contiene la imagen
    css_identifier_image = ".LicuJb img"
    # La clase del elemento que contiene el knowledge panel
    css_identifier_knowledge_panel = ".TQc1id"
    # La clase del elemento que contiene las imágenes destacadas
    css_identifier_images = ".kno-fiu"

    try:
        results = response.html.find(css_identifier_result)

        output = []
        serps_results = []
        people_also_ask_list = []
        snippet_images_list = []

        for result in results:

            if result.find(css_identifier_text, first=True):
                text = result.find(css_identifier_text, first=True).text
            else:
                text = ''

            if result.find(css_identifier_title, first=True):
                title = result.find(css_identifier_title, first=True).text
            else:
                title = ''

            if result.find(css_identifier_link, first=True):
                link = result.find(css_identifier_link,
                                   first=True).attrs['href']
            else:
                link = ''

            # Extract bold text
            if result.find(css_identifier_bold, first=True):
                bold = result.find(css_identifier_bold,
                                   first=True).text.lower()
            else:
                bold = ''

            if result.find(css_identifier_image, first=True):
                image = result.find(css_identifier_image,
                                    first=True).attrs['src']
            else:
                image = ''

            item = {
                'title': title,
                'link': link,
                'text': text,
                'bold': bold,
                'image': image
            }

            serps_results.append(item)

        paas = faqs_google_results.get_related_questions(query, lang, 10)
        for paa in paas:
            people_also_ask_list.append(paa)

        if response.html.find(css_identifier_images, first=True):
            has_images_snippet = True
            snippet_images = response.html.find(css_identifier_images + " img")
            for snippet_image in snippet_images:
                snippet_images_list.append({
                    "url":snippet_image.attrs['src'],
                    "alt":snippet_image.attrs['alt']
                })

            if (has_images_snippet):
                images_snippet = {
                    "has_images_snippet": has_images_snippet,
                    "images_list": snippet_images_list
                }
            else:
                images_snippet = {
                    "has_images_snippet": has_images_snippet,
                }

        if response.html.find(css_identifier_knowledge_panel, first=True):
            has_knowledge_panel = True
        else:
            has_knowledge_panel = False

        output.append({
            "serps_results": serps_results
        })
       
        output.append({
            "people_also_ask": people_also_ask_list
        })
        output.append({
            "images_snippet": images_snippet
        })
        output.append({
            "has_knowledge_panel": has_knowledge_panel
        })

        return output
    except requests.exceptions.RequestException as e:
        print(e)


def get_serps(query: str,lang="es"):
    response = _get_results(query, lang)
    results = _parse_search_results(response, query, lang)


    if results:
        return results


