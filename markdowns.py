# Creates markdown files for each test an lists the languages

import json

from test_helpers import collect_pytest_cases, dedent, script_name_of_test_case
from test_suite import LANGUAGES


def save_data(name: str, data: dict):
    with open(f'rosetta-site/data/{name}.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def load_data(name: str):
    with open(f'rosetta-site/data/{name}.json', 'r', encoding='utf-8') as f:
        return json.load(f)


save_data('languages', [language.as_json() for language in LANGUAGES])


pytest_cases_by_script_name = { script_name_of_test_case(pytest_case): pytest_case
                                for pytest_case in collect_pytest_cases() }


def test_case_data(pytest_case):
    script_name = script_name_of_test_case(pytest_case)
    doc_str = dedent(pytest_case.function.__doc__)
    doc_str_first_line = doc_str.strip().split('\n', maxsplit=1)[0]

    implementations = []
    for language in LANGUAGES:
        script_path = language.script_path(script_name)

        # checks that this case is implemented for the specific language
        if script_path.exists():
            implementations.append(dict(
                file_name=script_path.name,
                code=script_path.read_text(encoding="utf-8").strip(),
                language=language.as_json(),
            ))

    return dict(
        script_name=script_name,
        doc_str=doc_str,
        doc_str_first_line=doc_str_first_line,
        implementations=implementations,
    )


all_test_cases_data = [test_case_data(pytest_case) for pytest_case in collect_pytest_cases()]

save_data('test_cases', all_test_cases_data)




def default_icon(icon_id: str):
    # The the 2nd <image> tag acts as a fallback in case the plain icon doesn't exist
    return f"""
        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" aria-hidden="true">
            <image href="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/{icon_id}/{icon_id}-plain.svg"    x="0" y="0" width="24" height="24"/>
            <image href="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/{icon_id}/{icon_id}-original.svg" x="0" y="0" width="24" height="24"/>
        </svg>
    """.strip()


default_icons = {
    f"language-{language.icon_id}":  default_icon(language.icon_id)
    for language in LANGUAGES
}

icons = default_icons | load_data('icons-custom')

save_data('icons', icons)
