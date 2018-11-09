from salon.models import *

price_list = {
"Женский педикюр":[
["Обработка пальчиков",  "1000"],
["Покрытие гель-лак",  "800"],
["Покрытие гель-лак French",  "1000"],
["Снятие лака",  "250"],
["Удаление мозоли",  "300/400"]],
"Мужской маникюр":[
["Классический",  "900"],
["Аппаратный",  "1000"],
["Форма ногтей",  "250"],
["Полировка ногтей",  "250"]],
"Мужской педикюр": [
["Классический",  "2200"],
["Аппаратный",  "2300"]],
"Стрижки и укладки (девушки)":[
["Стрижка с укладкой (короткие)", "1950"],
["Стрижка с укладкой (средняя длина)", "2350"],
["Стрижка с укладкой (длинные)", "2850"],
["Стрижка одним срезом",  "1500"],
["Стрижка челки",  "500"],
["Коррекция стрижки (короткие)", "700"],
["Коррекция стрижки (средняя длина)", "850"],
["Коррекция стрижки (длинные)", "1100"],
["Укладка волос (короткие)", "850"],
["Укладка волос (средняя длина)", "1350"],
["Укладка волос (длинные)", "1600"],
["Укладка на брашинг (средняя длина)", "1950"],
["Укладка на брашинг (длинные)", "2550"],
["Укладка горячими инструментами (средняя длина)", "1900"],
["Укладка горячими инструментами (длинные)", "2950"]],
"Стрижки и укладки (мужчины)":[
["Стрижка машинкой",  "900"],
["Стрижка ножницами",  "1800/2150"],
["Укладка",  "600"],
["Коррекция бороды / усов",  "1200"]],
"Стрижки и укладки (дополнительно)":[
["Стрижка детская (до 7 лет)", "1000"],
["Вечерняя/Свадебная укладка (средняя длина)", "5000"],
["Вечерняя/Свадебная укладка (длинные)", "7500"],
["Репетиция укладки",  "50% от стоимости работы"],
["Косоплетение",  "от  1000"]],
"Окрашивание":[
["Прикорневое окрашивание (до 2 см)", "4000"],
["Окрашивание в один тон на короткие волосы",  "5000"],
["Окрашивание в один тон на волосы средней длины",  "5500"],
["Окрашивание в один тон на длинные волосы",  "6000"],
["Тонирование на короткие волосы",  "4000"],
["Тонирование на волосы средней длины",  "5000"],
["Тонирование на длинные волосы",  "6000"],
["Блондирование",  "3000"],
["Мелирование на короткие волосы",  "3000"],
["Мелирование на волосы средней длины",  "3500"],
["Мелирование на длинные волосы",  "4500"],
["Частичное мелирование на короткие волосы",  "1500"],
["Частичное мелирование на волосы средней длины",  "2000"],
["Частичное мелирование на длинные волосы",  "2500"],
["Декапирование на короткие волосы",  "2000"],
["Декапирование на волосы средней длины",  "3000"],
["Декапирование на длинные волосы",  "4000"],
["Сложное окрашивание1 на короткие волосы",  "6000"],
["Сложное окрашивание на волосы средней длины",  "5000"],
["Сложное окрашивание на длинные волосы",  "7000"],
["Дополнительная надбавка за длину/густоту волос",  "1000"]],
"Уходы":[
["Уход JOICO K-PAK на короткие волосы",  "1500"],
["Уход JOICO K-PAK на среднюю длину волос",  "2000"],
["Уход JOICO K-PAK на длинные волосы",  "2500"],
["Уход REDKEN на короткие волосы",  "1500"],
["Уход REDKEN на среднюю длину волос",  "2000"],
["Уход REDKEN на длинные волосы",  "2500"],
["Уход Essence Shots (ботокс) на короткие волосы",  "3000"],
["Уход Essence Shots (ботокс) среднюю длину волос",  "4000"],
["Уход Essence Shots (ботокс) длинные волосы",  "5000"]],
"Макияж":[
["Дневной макияж",  "2000"],
["Вечерний макияж",  "2500"],
["Естественный макияж",  "1500"],
["Smoky eyes",   "2500"],
["Антивозрастной макияж",  "2500"],
["Свадебный макияж",  "2500"],
["Макияж для фотосессий",  "3000"],
["Накладные ресницы",  "500"]],
"Брови и ресницы":[
["Коррекция бровей",  "от 400"],
["Придание формы",  "600"],
["Окрашивание бровей краской",  "400"],
["Окрашивание бровей хной",  "850"],
["Окрашивание ресниц краской",  "500"]],
"Эстетическая косметология":[
["Чистка Т зоны (1ч. 2омин.)", "2200"],
["Чистка лица + уход (2 ч.)", "3600/4100"],
["Уход по типу кожи (1ч. зомин.)", "2700/4000"],
["Массаж скульптурный (45 мин.)", "2000"],
["Массаж скульптурный по маске",  "2000"],
["Массаж классический (30 мин.)", "1500"],
["Массаж головы (15 мин.)", "900"],
["Маска миолифтинг",  "900"]],
"Кабинет депиляции":[
["Подмышечные впадины (воск)", "от 700"],
["Подмышечные впадины (сахар)", "от 800"],
["Бикини глубокое (воск)", "от 1800"],
["Бикини глубокое (сахар)", "от 2100"],
["Бикини классическое (воск)", "от 1200"],
["Бикини классическое (сахар)", "от 1500"],
["Стринги (воск)", "от 1600"],
["Стринги (сахар)", "от 1800"],
["Ноги полностью (воск)", "от 1700"],
["Ноги полностью (сахар)", "от 2000"],
["Ноги до колен (воск)", "от 800"],
["Ноги до колен (сахар)", "от 1000"],
["Ноги выше колен (воск)", "от 800"],
["Ноги выше колен (сахар)", "от 1000"],
["Руки (воск)", "от 700"],
["Руки (сахар)", "от 800"],
["Над верхней губой (воск)", "от 200"],
["Нос",  "от 200"]],
"Продукция для женщин":[
["Шампунь Redken color extend magnetic (300mll)", "1440"],
["Кондиционер  Redken color extend magnetic (250mll)", "1800"],
["Шампунь  Redken color extend magnetic (500mll)", "2100"],
["Кондиционер  Redken color extend magnetic (500mll)", "2700"],
["Шампунь Redken Extreme (300mll)", "1440"],
["Кондиционер Redken Extreme (250mll)", "1800"],
["Шампунь Redken Extreme (500mll)", "2100"],
["Кондиционер Redken Extreme (500mll)", "2700"],
["Шампунь Redken All Soft (300mll)", "1440"],
["Кондиционер Redken All Soft (250mll)", "1800"],
["Шампунь Redken All Soft (500mll)", "2100"],
["Кондиционер Redken All Soft (500mll)", "2700"],
["Шампунь Redken Highe-rise volume (500mll)", "2100"],
["Кондиционер Redken Highe-rise volume (500mll)", "2700"],
["Шампунь Redken Diamond oil glow dry (500mll)", "2100"],
["Кондиционер Redken Diamond oil glow dry (500mll)", "2700"],
["Шампунь Redken Frizz dismiss (500mll)", "2100"],
["Кондиционер Redken Frizz dismiss (500mll)", "2700"],
["Шампунь Redken Blonde idol (300mll)", "1440"],
["Маска Redken Blonde idol (250mll)", "2290"],
["Спрей Redken супер сильной фиксации (400mll)", "860"],
["Спрей Redken мгновенной фиксации (4ооп11)", "1300"],
["Мультифункциональный спрей Redken (1501111)", "2770"],
["Масло Redken Diamond oil glow dry (100mll)", "2460"],
["Масло Redken All soft комплексный уход (90mll)", "1260"],
["Шампунь JOICO К-РАК для окрашенных волос (300mll)", "1730"],
["Кондиционер JOICO К-РАК для окрашенных волос (300mll)", "1850"],
["Шампунь JOICO Endure violet для осветленных и седых волос",  "1650"],
["Кондиционер JOICO Endure violet для осветленных и седых волос",  "1750"],
["Шампунь JOICO Body luxe для пышности и объёма (300mll)", "1570"],
["Кондиционер JOICO Body luxe для пышности и объёма (300mll)", "1600"],
["Эликсир JOICO Body luxe для пышности и объёма (2001111)", "1600"],
["Шампунь JOICO Blonde life безупречный блонд (300mll)", "1750"],
["Кондиционер JOICO Blonde life безупречный блонд (250mll)", "1820"],
["Маска JOICO Blonde life бриллиантовый блонд (1501111)", "2540"]],
"Продукция для мужчин":[
["Шампунь Redken Clear brew с пивными дрожжами (250mll)", "1310"],
["Шампунь Redken Go clean для нормальных и сухих волос (300mll)", "1310"],
["Шампунь Redken Mint clean тонизирующий (300mll)", "1330"],
["Крем для завершения укладки Redken get groomed (150mll)", "1220"],
["Воск для укладки волос Redken Maneuver (100mll)", "1220"]]
}

def add_price(prices=price_list):
    for cat_name in prices:
        _: object
        for item in prices[cat_name]:
            cat = Category.objects.get(title=cat_name)
            price = PriceItem()
            price.category = cat
            price.price = item[1]
            price.title = item[0]
            price.save()
def calculate_delay(common_delay=1):
    category_items = Category.objects.all()
    if not len(category_items):
        return []
    delay_step = common_delay / len(category_items)
    return [(category,
             "{0}s".format(round((delay_step * category.pk), 3)),
             PriceItem.objects.filter(category=category))
            for category in category_items]
