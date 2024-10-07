# Creates markdown files for each test an lists the languages

import json
import re
from collections import defaultdict
from pathlib import Path
import shlex

from test_helpers import LocalRunner, ScriptRunner, collect_pytest_cases, dedent, script_test_case_mark
from test_suite import LANGUAGES

sorted_languages = sorted(LANGUAGES, key=lambda lang: lang.human_name)

def slugify(text: str) -> str:
    text = text.lower()
    text = text.replace(' ', '-')
    text = re.sub(r'[^a-z0-9-]', '', text)
    return text


def save_data(name: str, data: dict):
    with open(f'rosetta-site/data/{name}.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def load_data(name: str):
    with open(f'rosetta-site/data/{name}.json', 'r', encoding='utf-8') as f:
        return json.load(f)


save_data('languages', [language.as_json() for language in sorted_languages])


pytest_cases_by_script_name = { script_test_case_mark(pytest_case)['script_name']: pytest_case
                                for pytest_case in collect_pytest_cases() }


def test_case_data(pytest_case):
    mark = script_test_case_mark(pytest_case)

    description = dedent(pytest_case.function.__doc__)
    summary, description = description.strip().split('\n', maxsplit=1)
    description = description.strip()

    files = []
    for file_name, content in mark.get('files', {}).items():
        files.append(dict(
            name=file_name,
            ext=file_name.split('.')[-1],
            content=content
        ))

    cli_args = " ".join(shlex.quote(arg) for arg in mark.get('cli_args', []))

    assertion = None
    if 'assertion' in mark:
        assertion = dict([mark['assertion']])

    implementations = []
    for language in sorted_languages:
        script_path = language.script_path(mark['script_name'])
        additional_path = Path(str(script_path) + ".md")

        # checks that this case is implemented for the specific language
        if script_path.exists():
            additional_md_path = None
            if additional_path.exists():
                additional_md_path = additional_path.read_text(encoding="utf-8").strip()

            runner = ScriptRunner(mark['script_name'], language, mark)

            implementations.append(dict(
                file_name=script_path.name,
                code=script_path.read_text(encoding="utf-8").strip(),
                additional_md=additional_md_path,
                language=language.as_json(),
                command=runner.basic_command(),
            ))

    return mark | dict(
        title=mark.get('title', mark['script_name']),
        summary=summary,
        description=description,
        cli_args=cli_args,
        files=files,
        assertion=assertion,
        implementations=implementations,
    )


all_test_cases_data = [test_case_data(pytest_case) for pytest_case in pytest_cases_by_script_name.values()]

test_cases_by_group = defaultdict(list)

for test_case in all_test_cases_data:
    test_cases_by_group[test_case['group']].append(test_case)

groups = []
for group_name, test_cases in test_cases_by_group.items():
    sorted_test_cases = sorted(test_cases, key=lambda test_case: test_case['title'])

    groups.append({
        'group_name': group_name,
        'group_slug': slugify(group_name),
        'test_cases': sorted_test_cases,
    })

save_data('test_cases', groups)


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
