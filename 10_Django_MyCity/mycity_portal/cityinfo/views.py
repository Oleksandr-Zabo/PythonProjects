from django.shortcuts import render

from .models import Gallery

import os
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from django.conf import settings


def fetch_links(url, max_items=8):
    try:
        req = Request(url, headers={"User-Agent": "Mozilla/5.0"})
        html = urlopen(req, timeout=10).read().decode("utf-8", "ignore")
        soup = BeautifulSoup(html, "html.parser")

        items = []
        
        # Find the main content area - try different selectors for the central content
        main_content = soup.find("main") or soup.find("div", class_="content") or soup.find("div", id="content") or soup.find("article")
        
        # If no main content found, fall back to body but exclude navigation
        if not main_content:
            main_content = soup.body
        
        # Remove navigation elements if they exist
        if main_content:
            for nav in main_content.find_all(["nav", "aside", "header", "footer"]):
                nav.decompose()
        
        # Extract links from the central content area
        if main_content:
            for a in main_content.find_all("a", href=True):
                href = a.get("href")
                text = a.get_text(strip=True)
                
                # Skip empty links, navigation links, and pagination
                if not text or not href:
                    continue
                if href.startswith("#") or "javascript:" in href:
                    continue
                if text.lower() in ["читати", "далі", "more", "read"]:
                    continue
                if "?" in href and "p=" in href:  # skip pagination
                    continue
                
                # Convert relative URLs to absolute
                if href.startswith("/"):
                    href = settings.PRIMARY_CITY_SITE + href
                
                items.append({"title": text, "href": href, "img": None})
                if len(items) >= max_items:
                    break

        # If no items found in main content, try alternative approach
        if not items:
            # Look for news/article items specifically
            for article in soup.find_all(["article", "div"], class_=lambda x: x and ("news" in str(x).lower() or "post" in str(x).lower())):
                for a in article.find_all("a", href=True):
                    href = a.get("href")
                    text = a.get_text(strip=True)
                    if text and href and not href.startswith("#"):
                        if href.startswith("/"):
                            href = settings.PRIMARY_CITY_SITE + href
                        items.append({"title": text, "href": href, "img": None})
                        if len(items) >= max_items:
                            break
                if len(items) >= max_items:
                    break

        # Attach images (best-effort) - look for images near the links
        if main_content:
            images = main_content.find_all("img", src=True)
            for i, img in enumerate(images):
                if i < len(items):
                    src = img.get("src")
                    if src.startswith("//"):
                        src = "https:" + src
                    elif src.startswith("/"):
                        src = settings.PRIMARY_CITY_SITE + src
                    items[i]["img"] = src

        return items
    except Exception:
        # fallback: return a small placeholder
        return [{"title": "Не вдалося завантажити дані", "href": None, "img": None}]


SECTION_TEMPLATE = "cityinfo/section.html"


def home(request):
    context = {
        "title": "Шаргородська громада",
        "section_name": "Головна",
        "hero_title": "Шаргородська громада",
        "hero_subtitle": "Вінницька область, Жмеринський район",
        "highlights": [
            "Офіційна інформація міської ради",
            "Актуальні новини громади",
            "Контакти основних міських служб",
        ],
    }
    return render(request, "cityinfo/home.html", context)


def news(request, extra=None):
    url = settings.PRIMARY_CITY_SITE + "/news/"
    items = fetch_links(url, max_items=10)
    context = {"title": "Новини міста", "section_name": "Новини", "items": items}
    return render(request, SECTION_TEMPLATE, context)


def management(request, extra=None):
    # Керівний склад - fetch from individual leadership pages
    leadership_urls = settings.LEADERSHIP_URLS
    
    items = []
    for url in leadership_urls:
        try:
            req = Request(url, headers={"User-Agent": "Mozilla/5.0"})
            html = urlopen(req, timeout=10).read().decode("utf-8", "ignore")
            soup = BeautifulSoup(html, "html.parser")
            
            # Find the main content area
            main_content = soup.find("main") or soup.find("div", class_="content") or soup.find("div", id="content") or soup.body
            
            if main_content:
                # Try to extract the title/name from the page
                title_tag = main_content.find("h1") or main_content.find("h2")
                if title_tag:
                    title = title_tag.get_text(strip=True)
                else:
                    # Use URL as fallback title
                    title = url.split("/")[-2].replace("-", " ").title()
                
                items.append({"title": title, "href": url, "img": None})
                
                if len(items) >= 12:
                    break
        except Exception:
            continue
    
    context = {"title": "Керівний склад", "section_name": "Керівний склад", "items": items}
    return render(request, SECTION_TEMPLATE, context)


def facts(request, extra=None):
    items = [
        {"title": "Шаргород має багатовікову історію, яка пов'язана з...", "href": None, "img": None},
        {"title": ''' 

          Вінницька обласна рада рішенням №449 на 14 сесії 5 скликання вирішила, що Шаргородський історико-культурний центр духовності та злагоди заслуговує на те, щоб ввійти в сімку чудес Вінниччини. І це не випадково, адже Шаргородський костел св. Флоріана, чоловічий Свято-Миколаївський монастир та синагога дійсно заслуговують на увагу. Вони відіграли велику роль в соціокультурному становищі міста.

     Шаргород (першочергово Шарогрудек) – це унікальне місце на теренах східної Європи, адже тут, на крихітній території і в такій кількості зосереджено сліди існування різних культур, де реально існував міжконфесійний та міжнаціональний мир протягом багатьох століть. Такий уклад життя, який завжди був  у Шаргороді – це ідеальна модель для світосистеми.

     Шаргород – улюбенець століть. На нього турки говорили «кучук - Стамбул» (маленький Стамбул). Задля придбання місцини для нього засновник Ян Замойський здійснює обмін села Прага під Варшавою. Місто мало свій герб, магдебурзьке право і право обов’язкових торгів три рази на рік.

     Ці чудові пам’ятки зосереджені в радіусі 400 метрів, утворюючи так званий історико-культурний Центр духовності та злагоди.

       \n\n- в 1840 році в Шаргородській бурсі з семи літ навчався український поет Степан Васильович Руданський;

       \n- великий український письменник Михайло Коцюбинський 1870 роках навчався в Шаргороді, саме тут було помічено талант маленького Михайлика вчителем, який зайшовши до вчительської, сказав: «будемо мати свого літератора» і не помилився;

        \n- трохи згодом тут же навчався український композитор, майстер хорового мистецтва Микола Дмитрович Леонтович, автор славнозвісного «Щедрика».''',
         "href": None, "img": None},
    ]
    context = {"title": "Факти", "section_name": "Факти", "items": items}
    return render(request, SECTION_TEMPLATE, context)


def landmarks(request, extra=None):
    url = settings.PRIMARY_CITY_SITE + "/" + settings.LEADERSHIP_PAGE_SLUG
    items = fetch_links(url, max_items=12)
    context = {"title": "Видатне місто", "section_name": "Видатне місто", "items": items}
    return render(request, SECTION_TEMPLATE, context)


def people(request, extra=None):
    url = settings.SHARGOROD_NET_SITE + "/category/mystetstvo/"
    items = fetch_links(url, max_items=10)

    # local presentation images placed under cityinfo/static/cityinfo/Names
    local_images = []
    static_names_dir = os.path.join(os.path.dirname(__file__), "static", "cityinfo", "Names")
    if os.path.isdir(static_names_dir):
        fnames = sorted([f for f in os.listdir(static_names_dir) if f.lower().endswith((".png", ".jpg", ".jpeg", ".webp"))])
        # normalize STATIC_URL to start with '/'
        static_prefix = settings.STATIC_URL
        if not static_prefix.startswith("/"):
            static_prefix = "/" + static_prefix
        if not static_prefix.endswith("/"):
            static_prefix += "/"
        for f in fnames:
            # build static URL with leading slash
            local_images.append(static_prefix + f"cityinfo/Names/{f}")

    context = {"title": "Видатні люди", "section_name": "Видатні люди", "items": items, "local_images": local_images}
    return render(request, SECTION_TEMPLATE, context)


def photos(request, extra=None):
    # album with many images - collect <img> sources
    url = settings.PRIMARY_CITY_SITE + "/" + settings.ALBUM_PAGE_SLUG
    try:
        req = Request(url, headers={"User-Agent": "Mozilla/5.0"})
        html = urlopen(req, timeout=10).read().decode("utf-8", "ignore")
        soup = BeautifulSoup(html, "html.parser")
        
        # Find gallery container
        gallery = soup.find("div", class_="row gallery")
        
        items = []
        if gallery:
            # Find all album_img links
            for a in gallery.find_all("a", class_="album_img")[:18]:
                # Extract background-image URL from style attribute
                style = a.get("style", "")
                if "background-image:" in style:
                    # Extract URL from background-image: url(...)
                    import re
                    match = re.search(r'url\(([^)]+)\)', style)
                    if match:
                        img_url = match.group(1).strip('"\'')
                        items.append({"title": "Фото", "href": a.get("href"), "img": img_url})
        else:
            # Fallback: try to find any images in main content
            main_content = soup.find("main") or soup.find("div", class_="content") or soup.find("div", id="content") or soup.body
            if main_content:
                for img in main_content.find_all("img", src=True)[:18]:
                    src = img.get("src")
                    if src.startswith("//"):
                        src = "https:" + src
                    elif src.startswith("/"):
                        src = settings.PRIMARY_CITY_SITE + src
                    items.append({"title": "Фото", "href": None, "img": src})
    except Exception:
        items = [{"title": "Не вдалося завантажити фото", "href": None, "img": None}]

    context = {"title": "Фотогалерея", "section_name": "Фото", "items": items}
    return render(request, SECTION_TEMPLATE, context)


def history(request, extra=None):
    # General history page
    items = [
        {"title": "Шаргород має багатовікову історію, яка пов'язана з...", "href": None, "img": None},
        {"title": ''' - через місто не раз проїздили відомі люди: турецький мандрівник Евлій Челиба, французький дипломат Ульріх фон Вердум, які залишили нариси про велич міста; \n- в 1769 році Яків Франк був в Шаргороді, багато жителів піддалося франкістському впливу, особливо, коли Франк показував різні чудеса: літав в повітрі, викликав душі мертвих, змушував бика проповідувати півгодинну проповідь на тему книги Зо Хап, зсунув з місця на базарній площі великий камінь і т.d.;

     \n- з замку Яна Замойського великий гетьман Богдан Хмельницький писав листи до російських послів В.Стрєшньова і М.Бредіхіна;

     \n- Шаргород, другий після Кам’янця місто воєводства дуже подобався туркам і вони називали його «кучук-Стамбул», що означає «маленький Стамбул»;

     \n- тут був схоплений, катований і страчений на міських воротах славетний полковник Морозенко, пісня про якого «Ой, Морозе, Морозенку, ти славний козаче, за тобою, Морозенку, вся Вкраїна плаче…» ;

     \n- француз Моро де Бразе, який найнявся до російської армії бригадиром, залишив записки, які потім були перекладені і підготовлені до видання самим О.С. Пушкіним, проїзжаючи через Шаргород писав : « … город был некогда весьма обширен и имел знатную торговлю …»;

     \n- власником міста в який час був відомий Князь Роман Сангушко;

    \n- в 1840 році в Шаргородській бурсі з семи літ навчався український поет Степан Васильович Руданський;

    \n- великий український письменник Михайло Коцюбинський 1870 роках навчався в Шаргороді, саме тут було помічено талант маленького Михайлика вчителем, який зайшовши до вчительської, сказав: «будемо мати свого літератора» і не помилився;

     \n- трохи згодом тут же навчався український композитор, майстер хорового мистецтва Микола Дмитрович Леонтович, автор славнозвісного «Щедрика».''', "href": None, "img": None},
    ]
    context = {"title": "Історія міста", "section_name": "Історія", "items": items}
    return render(request, SECTION_TEMPLATE, context)


def history_people(request):
    items = [
        {"title": "Видатні мешканці: художники, діячі культури та науки.", "href": None, "img": None},
    ]
    context = {"title": "Історія — Відомі люди", "section_name": "Історія — Відомі люди", "items": items}
    return render(request, SECTION_TEMPLATE, context)


def history_photos(request):
    # small gallery placeholder — reuse photos parser on album
    return photos(request)


def services(request, extra=None):
    items = [
        {"title": "Єдина довідка міської ради: +38 (000) 000-00-01", "href": None, "img": None},
        {"title": "ЦНАП: +38 (000) 000-00-02", "href": None, "img": None},
        {"title": "Чергова служба ЖКГ: +38 (000) 000-00-03", "href": None, "img": None},
    ]
    context = {"title": "Контакти", "section_name": "Контактні телефони", "items": items}
    return render(request, SECTION_TEMPLATE, context)


def gallery_db(request):
    """Display gallery images from database"""
    images = Gallery.objects.filter(is_active=True)
    items = [{"title": img.title, "href": None, "img": img.image.url} for img in images]
    if not items:
        items = [{"title": "Галереї скоро поповніються...", "href": None, "img": None}]
    
    context = {"title": "Галереї", "section_name": "Галереї із БД", "items": items, "local_images": []}
    return render(request, SECTION_TEMPLATE, context)


def custom_404(request, exception=None):
    # simple 404 handler (render template)
    return render(request, "cityinfo/404.html", {"section_name": "Сторінка не знайдена"}, status=404)