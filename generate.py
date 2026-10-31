# -*- coding: utf-8 -*-
"""
Генератор HTML-страницы с информацией об организации.
Кейс-задача № 5 практики в ООО «Регионстройпроект».
"""

ORG_NAME = "ООО «Регионстройпроект»"

ORG_INFO = {
    "Полное наименование": "Общество с ограниченной ответственностью «Регионстройпроект»",
    "Сокращённое наименование": "ООО «Регионстройпроект»",
    "ИНН": "7000004671",
    "ОГРН": "1237000002007",
    "Юридический адрес": "634062, Томская область, г. о. город Томск, г. Томск, ул. Беринга, д. 4/1, кв. 75",
    "Основная деятельность": "Инженерные изыскания и проектирование зданий и сооружений",
    "Телефон": "+7 (8722) 00-00-00",
    "E-mail": "info@regionstroyproject.ru",
    "Сайт": "www.regionstroyproject.ru",
}

# Основной шрифт компании (по фирменному стилю — Arial)
MAIN_FONT = "Arial, sans-serif"

# 5 альтернативных шрифтов
ALT_FONTS = [
    ("Times New Roman, serif", "Times New Roman — классический шрифт с засечками"),
    ("Georgia, serif", "Georgia — гуманистический шрифт с засечками"),
    ("Verdana, sans-serif", "Verdana — широкий шрифт без засечек"),
    ("Trebuchet MS, sans-serif", "Trebuchet MS — гуманистический шрифт без засечек"),
    ("Courier New, monospace", "Courier New — моноширинный шрифт"),
]


def build_info_rows() -> str:
    """Формирует строки таблицы с информацией об организации."""
    rows = []
    for key, value in ORG_INFO.items():
        rows.append(
            f"        <tr><th>{key}</th><td>{value}</td></tr>"
        )
    return "\n".join(rows)


def build_font_samples() -> str:
    """Формирует блок с 5 вариантами шрифтов."""
    blocks = []
    for i, (font_family, description) in enumerate(ALT_FONTS, start=1):
        blocks.append(
            f'        <div class="font-sample" style="font-family: {font_family};">\n'
            f'            <span class="font-num">Вариант {i}</span> — {description}\n'
            f'        </div>'
        )
    return "\n".join(blocks)


def build_html() -> str:
    """Собирает итоговую HTML-страницу."""
    info_rows = build_info_rows()
    font_samples = build_font_samples()

    return f"""<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{ORG_NAME}</title>
    <style>
        body {{
            font-family: {MAIN_FONT};
            margin: 0;
            padding: 40px 20px;
            background: #f4f6f8;
            color: #222;
            line-height: 1.6;
        }}
        .container {{
            max-width: 900px;
            margin: 0 auto;
            background: #ffffff;
            padding: 40px 50px;
            border-radius: 8px;
            box-shadow: 0 2px 12px rgba(0, 0, 0, 0.08);
        }}
        header {{
            border-bottom: 3px solid #1a3d6d;
            padding-bottom: 16px;
            margin-bottom: 24px;
        }}
        h1 {{
            color: #1a3d6d;
            margin: 0 0 8px 0;
            font-size: 28px;
        }}
        .subtitle {{
            color: #666;
            font-size: 14px;
            margin: 0;
        }}
        h2 {{
            color: #1a3d6d;
            margin-top: 32px;
            font-size: 20px;
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
            margin-top: 12px;
        }}
        th, td {{
            text-align: left;
            padding: 10px 14px;
            border-bottom: 1px solid #e0e4e8;
            vertical-align: top;
        }}
        th {{
            width: 35%;
            background: #f0f3f7;
            font-weight: 600;
            color: #1a3d6d;
        }}
        .font-sample {{
            padding: 10px 14px;
            margin: 8px 0;
            background: #f8f9fb;
            border-left: 4px solid #1a3d6d;
            font-size: 16px;
        }}
        .font-num {{
            display: inline-block;
            min-width: 90px;
            font-weight: 600;
            color: #1a3d6d;
            font-family: {MAIN_FONT};
        }}
        footer {{
            margin-top: 40px;
            padding-top: 16px;
            border-top: 1px solid #e0e4e8;
            font-size: 12px;
            color: #888;
            text-align: center;
        }}
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>{ORG_NAME}</h1>
            <p class="subtitle">Информационная страница организации</p>
        </header>

        <h2>Сведения об организации</h2>
        <table>
{info_rows}
        </table>

        <h2>Основной шрифт компании</h2>
        <p>
            В качестве основного шрифта используется <strong>Arial</strong> —
            он обеспечивает деловой вид документации, хорошую читаемость
            и корректно отображается во всех браузерах и операционных системах.
        </p>

        <h2>Альтернативные варианты шрифтов</h2>
{font_samples}

        <footer>
            Сгенерировано программой generate.py — кейс-задача № 5
        </footer>
    </div>
</body>
</html>
"""


def main() -> None:
    html = build_html()
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("Готово: index.html сгенерирован.")
    print(f"Размер: {len(html)} символов.")


if __name__ == "__main__":
    main()