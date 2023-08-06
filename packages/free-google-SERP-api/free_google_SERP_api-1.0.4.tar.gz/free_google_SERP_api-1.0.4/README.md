# Extraer datos de las SERP de Google free_google_SERP_api

free_google_SERP_api es una API para extraer datos de los resultados de Google

## ⚠ Aviso
Los motores de búsqueda como Google no permiten ningún tipo de acceso automatizado a su servicio, pero desde un punto de vista legal no se conoce ningún caso ni ley infringida. Google no emprende acciones legales contra el scraping, probablemente por razones de autoprotección.
La API se ha configurado para no abusar del motor de búsqueda de Google.

## Créditos
El código de esta librería ha sido creado por [txetxu](https://twitter.com/Txtetxu1) y adaptado por [Dídac Anton](https://twitter.com/seo_torch) para implementar las preguntas frecuentes, el knowledge panel, etc. 

## Contribución
Todo el mundo es libre de descargar y editar el código a sus anchas, estas son las mejoras que tengo en mente ahora:
* Detección de Local Pack y obtención de datos de los negocios
* Detección del snippet de YouTUbe y obtención de los datos de los videos
* Arreglar que las imágenes sean un pixel de 1x1 (Probablemente es una forma que tiene Google de limitar el scraping)

## Instalación
```
pip install free_google_SERP_api 
```

## Uso
El objetivo de ``free_google_SERP_api`` es proporcionar una API sencilla y fácil de usar para obtener información de los resultados de Google en diferentes idiomas.
En el ejemplo que hay a continuación se usa ``es`` para obtener los datos de una búsqueda en español, pero puede ser remplazado por cualquier valor de estos:
af, ach, ak, am, ar, az, be, bem, bg, bh, bn, br, bs, ca, chr, ckb,  co, crs, cs, cy, da, de, ee, el, en, eo, es, es-419, et, eu, fa, fi,  fo, fr, fy, ga, gaa, gd, gl, gn, gu, ha, haw, hi, hr, ht, hu, hy, ia,  id, ig, is, it, iw, ja, jw, ka, kg, kk, km, kn, ko, kri, ku, ky, la,  lg, ln, lo, loz, lt, lua, lv, mfe, mg, mi, mk, ml, mn, mo, mr, ms, mt, ne, nl, nn, no, nso, ny, nyn, oc, om, or, pa, pcm, pl, ps, pt-BR,  pt-PT, qu, rm, rn, ro, ru, rw, sd, sh, si, sk, sl, sn, so, sq, sr,  sr-ME, st, su, sv, sw, ta, te, tg, th, ti, tk, tl, tn, to, tr, tt,  tum, tw, ug, uk, ur, uz, vi, wo, xh, xx-bork, xx-elmer, xx-hacker,  xx-klingon, xx-pirate, yi, yo, zh-CN, zh-TW, zu.  


### Importación del paquete
```python
import free_google_SERP_api
```

### Obtención de los resultados de ls búsqueda ``Python`` en español
```python
import free_google_SERP_api

data = free_google_SERP_api.get_serps("python", 'es')

print(data)

# Resultado:
[
    {
        "serps_results": [
            {
                "title": "Python - Wikipedia, la enciclopedia libre",
                "link": "https://es.wikipedia.org/wiki/Python",
                "text": "Python es un lenguaje de programación multiparadigma. Esto significa que más que forzar a los programadores a adoptar un estilo particular de programación, ...",
                "bold": "python",
                "image": ""
            },
            {
                "title": "¿Qué es Python? | Guía de Python para principiantes de la nube",
                "link": "https://aws.amazon.com/es/what-is/python/",
                "text": "Python es un lenguaje de programación ampliamente utilizado en las aplicaciones web, el desarrollo de software, la ciencia de datos y el machine learning ...",
                "bold": "python",
                "image": ""
            },
            {
                "title": "Python: qué es y por qué deberías aprender a utilizarlo",
                "link": "https://www.becas-santander.com/es/blog/python-que-es.html",
                "text": "9 abr 2021 — Python es un lenguaje sencillo de leer y escribir debido a su alta similitud con el lenguaje humano. Además, se trata de un lenguaje ...",
                "bold": "python",
                "image": ""
            },
            {
                "title": "Aprende Python: Home",
                "link": "https://aprendepython.es/",
                "text": "Curso gratuito para aprender el lenguaje de programación Python con un enfoque práctico, incluyendo ejercicios y cobertura para distintos niveles de ...",
                "bold": "python",
                "image": ""
            },
            {
                "title": "python - Official Image - Docker Hub",
                "link": "https://hub.docker.com/_/python",
                "text": "Python is an interpreted, interactive, object-oriented, open-source programming language.",
                "bold": "python",
                "image": ""
            }
        ]
    },
    {
        "people_also_ask": [
            "¿Qué beneficios nos ofrece Python?",
            "¿Qué es y para qué sirve el Python?",
            "¿Qué tan bueno es aprender Python?",
            "¿Qué trabajos usan Python?",
            "¿Que se aprende en Python?",
            "¿Qué es Python y porque debes aprender ahora?",
            "¿Qué se puede hacer con Python?",
            "¿Cuánto tiempo se necesita para aprender Python?",
            "¿Qué es Python y por qué usarlo?",
            "¿Qué fácil es Python?",
            "¿Dónde se usa Python?"
        ]
    },
    {
        "images_snippet": {
            "has_images_snippet": true,
            "images_list": [
                {
                    "url": "data:image/gif;base64,R0lGODlhAQABAIAAAP///////yH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==",
                    "alt": "Resultado de imagen de python"
                },
                {
                    "url": "data:image/gif;base64,R0lGODlhAQABAIAAAP///////yH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==",
                    "alt": "Resultado de imagen de python"
                },
                {
                    "url": "data:image/gif;base64,R0lGODlhAQABAIAAAP///////yH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==",
                    "alt": "Resultado de imagen de python"
                },
                {
                    "url": "data:image/gif;base64,R0lGODlhAQABAIAAAP///////yH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==",
                    "alt": "Resultado de imagen de python"
                },
                {
                    "url": "data:image/gif;base64,R0lGODlhAQABAID/AMDAwAAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw==",
                    "alt": "Resultado de imagen de python"
                }
            ]
        }
    },
    {
        "has_knowledge_panel": true
    }
]
```

## Actualizaciones
Iré actualizando el repositorio cuando tenga tiempo. EL objetivo es poder ofrecer una API de calidad y gratis a todos los desarrolladores
Si quieres echarme una mano en este proyecto [contáctame por Twitter](https://twitter.com/seo_torch)  