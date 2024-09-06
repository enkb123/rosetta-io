# Creates markdown files for each test an lists the languages

from pathlib import Path
import shutil
import os

from test_helpers import collect_pytest_cases, dedent, format_code, script_name_of_test_case
from test_suite import LANGUAGES

docs_path = Path('./rosetta-site/content/IO_Operations/')
shutil.rmtree(docs_path, ignore_errors=True) #deletes the directory so it can be remade
os.makedirs(docs_path)

pytest_cases_by_script_name = { script_name_of_test_case(pytest_case): pytest_case
                                for pytest_case in collect_pytest_cases() }

for script_name, pytest_case in pytest_cases_by_script_name.items():
    script_name = script_name_of_test_case(pytest_case)
    doc_str = dedent(pytest_case.function.__doc__)

    with open(docs_path / f"{script_name}.md", "w", encoding="utf-8") as f:
        f.write(format_code(
            """
            +++
            title = ''
            draft = true
            +++

            # {script_name}

            {doc_str}

            """,
            script_name=script_name,
            doc_str=doc_str
        ))

        for language in LANGUAGES:
            script_path = language.script_path(script_name)

            # checks that this case is implemented for the specific language
            if script_path.exists():
                code = script_path.read_text(encoding="utf-8").strip()

                f.write(format_code(
                    """
                    ## {language_name}

                    `{file_name}`

                    ```{syntax}
                    {code}
                    ```

                    """,
                    language_name=language.human_name,
                    file_name=script_path.name,
                    syntax=language.syntax_highlighting,
                    code=code
                ))
