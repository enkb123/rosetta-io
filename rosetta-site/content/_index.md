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
{{< cards cols="2">}}
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

{{< _.inline >}}
  {{range $.Site.Data.test_cases }}
    <h3>{{ .group_name }}</h3>
    {{ $group_slug := .group_slug }}
    <div class="hextra-cards hx-mt-4 hx-gap-4 hx-grid not-prose" style="--hextra-cards-grid-cols: 2;">
      {{ range .test_cases }}
        {{- partial "shortcodes/card" (dict
          "title"       .title
          "link"        (printf "/operations/%s/%s" $group_slug .script_name)
          "subtitle"    .doc_str_first_line
        ) -}}
      {{ end}}
    </div>
  {{ end}}
{{< /_.inline >}}
