#Creates markdown files for each test an lists the languages

import shutil
from test_suite import LANGUAGES
import os
from pathlib import Path

TEST_CASES = [
    "arguments",
    "decode",
    "encode",
    "json_array",
    "json_control_chars",
    "json_numbers",
    "json_object_array",
    "json_object_with_array_values",
    "json_stdout_object",
    "null_char",
    "read_file",
    "read_json_file",
    "stdin",
    "streaming_pipe_in_and_out",
    "streaming_pipe_in",
    "streaming_stdin",
    "write_file"
]



docs_path = Path('./docs/')
shutil.rmtree(docs_path, ignore_errors=True) #deletes the directory so it can be remade
os.makedirs(docs_path)

for test_case in TEST_CASES:
    with open(docs_path / f"{test_case}.md", "w") as f:
        f.write ("# " + test_case + "\n\n")

        for language in LANGUAGES:
            opening_path = language.script_local_file(test_case)
            if language.script_local_file(test_case).exists(): #checks that this case is implemented for the specific language
                f.write("## " + language.human_name + "\n\n")

                f.write(f"`{language.script_file_name(test_case)}`\n\n")

                e = open(opening_path, "r")
                code = e.read()
                text = language.syntax_highlighting +  "\n" + code + "\n"
                f.write("```" + text + "```\n\n")
