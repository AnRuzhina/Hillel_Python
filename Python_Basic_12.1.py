# Очистити текст від html-тегів

import re


def delete_html_tags(html_file, result_file='cleaned.txt'):
    with open(html_file, 'r', encoding='utf-8') as file:
        html_content = file.read()

    cleaned_text = re.sub(r'<[^>]+>', '', html_content)

    with open(result_file, 'w', encoding='utf-8') as output_file:
        output_file.write('\n'.join([line for line in cleaned_text.splitlines() if line.strip()]))

    print(f"Текст очищено від HTML-тегів і записано у файл '{result_file}'.")


delete_html_tags('draft.html')
