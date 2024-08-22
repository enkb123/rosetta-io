#Creates markdown files for each test an lists the languages

from test_suite import LANGUAGES
import os

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

mypath = './docs/'
os.makedirs(mypath, exist_ok=True)

for case in TEST_CASES:
    with open(mypath + case + '.md', "a") as f:
        f.write ("# " + case + "\n\n")

        for language in LANGUAGES:
            opening_path = language.name + "/" + language.script_file_name(case)
            if language.script_local_file_exists(case): #checks that this case is implemented for the specific language
                f.write("## " + language.human_name + "\n\n")

                f.write("`" + language.script_file_name(case)+ "`\n\n")

                e = open(opening_path, "r")
                code = e.read()
                text = language.syntax_highlighting +  "\n" + code + "\n"
                f.write("```" + text + "```\n\n")
