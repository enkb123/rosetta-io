# Creates markdown files for each test an lists the languages

import json

from test_helpers import Language, collect_pytest_cases, dedent, script_name_of_test_case
from test_suite import LANGUAGES

pytest_cases_by_script_name = { script_name_of_test_case(pytest_case): pytest_case
                                for pytest_case in collect_pytest_cases() }


def implementation_for(script_path: str, language: Language):
    return dict(
        file_name=script_path.name,
        code = script_path.read_text(encoding="utf-8").strip(),
        language=language.as_json(),
    )

def all_implementations_for(script_name: str):
    for language in LANGUAGES:
        script_path = language.script_path(script_name)

        # checks that this case is implemented for the specific language
        if script_path.exists():
            yield implementation_for(script_path, language)

def test_cases_data():
    for _, pytest_case in sorted(pytest_cases_by_script_name.items()):
        script_name = script_name_of_test_case(pytest_case)
        doc_str = dedent(pytest_case.function.__doc__)
        doc_str_json = json.dumps(doc_str.strip().split('\n', maxsplit=1)[0])

        implementations = [*all_implementations_for(script_name)]

        yield dict(
            script_name=script_name,
            doc_str=doc_str,
            doc_str_json=doc_str_json,
            implementations=implementations,
        )

with open('rosetta-site/data/languages.json', 'w', encoding='utf-8') as f:
    json.dump([language.as_json() for language in LANGUAGES], f, ensure_ascii=False, indent=4)

with open('rosetta-site/data/test_cases.json', 'w', encoding='utf-8') as f:
    json.dump([*test_cases_data()], f, ensure_ascii=False, indent=4)
