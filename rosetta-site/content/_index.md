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
{{< cards >}}
  {{< _.inline >}}
    {{ range $.Site.Data.languages }}
      {{ partial "shortcodes/card" (dict
        "title"       .human_name
        "icon"        (printf "language-%s" .icon_id)
      ) }}
    {{ end}}
  {{< /_.inline >}}
{{< /cards >}}

## Operations

{{< cards >}}
  {{< _.inline >}}
    {{ range $.Site.Data.test_cases }}
      {{ partial "shortcodes/card" (dict
        "title"       .script_name
        "link"        (printf "/IO_Operations/%s" .script_name)
        "subtitle"    .doc_str_first_line
      ) }}
    {{ end}}
  {{< /_.inline >}}
{{< /cards >}}
