# Creates markdown files for each test an lists the languages

from pathlib import Path
import shutil
import json
import os

from test_helpers import collect_pytest_cases, dedent, format_code, script_name_of_test_case
from test_suite import LANGUAGES

docs_path = Path('./rosetta-site/content/IO_Operations/docs/')
shutil.rmtree(docs_path, ignore_errors=True) #deletes the directory so it can be remade
os.makedirs(docs_path)

pytest_cases_by_script_name = { script_name_of_test_case(pytest_case): pytest_case
                                for pytest_case in collect_pytest_cases() }

index_path = Path('./rosetta-site/content/_index.md')
shutil.rmtree(index_path, ignore_errors=True) #deletes the _index.md file so it can be remade

with open(index_path, "w", encoding = "utf-8") as index_page:
    index_page.write(format_code(
        """
        +++
        title = 'Rosetta I/O'
        draft = false
        type = 'default'
        +++

        ## About

        The purpose of this project is to provide working examples of how
        popular languages handle basic I/O and common serialization formats. The
        covered languages are listed below. For each example under IO
        operations, the language's handling of the operation is shown.

        The name `rosetta-io` is an hommage to [Rosetta
        Code](https://rosettacode.org/wiki/Rosetta_Code) but is not affiliated.

        ## Languages covered
        {{{{< cards >}}}}
        {languages_cards}
        {{{{< /cards >}}}}

        ## Operations

        {{{{< cards >}}}}
        """,
        languages_cards="\n".join(format_code(
            """
            {{{{< card icon="language-{language_id}" title=\"{language_name}\" >}}}}
            """,
            language_name=language.human_name,
            language_id=language.name.lower(),
        ) for language in LANGUAGES
        )
    ))


    for _, pytest_case in sorted(pytest_cases_by_script_name.items()):
        script_name = script_name_of_test_case(pytest_case)
        doc_str = dedent(pytest_case.function.__doc__)

        index_page.write(format_code(
            """
            {{{{< card  link="/IO_Operations/docs/{script_name}" title="{script_name}" subtitle={doc_str_json} >}}}}
            """,
            script_name=script_name,
            doc_str_json=json.dumps(doc_str.strip().split('\n', maxsplit=1)[0])
        ))

        with open(docs_path / f"{script_name}.md", "w", encoding="utf-8") as operation_page:
            operation_page.write(format_code(
                """
                +++
                title = ''
                draft = false
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

                    operation_page.write(format_code(
                        """
                        ## {language_name}

                        ```{syntax} {{filename="{file_name}"}}
                        {code}
                        ```

                        """,
                        language_name=language.human_name,
                        file_name=script_path.name,
                        syntax=language.syntax_highlighting,
                        code=code
                    ))

    index_page.write(format_code(
        """
        {{{{< /cards >}}}}
        """
    ))
