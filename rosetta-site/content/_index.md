+++
title = 'Rosetta I/O'
draft = false
type = 'default'
+++

## About

Rosetta I/O provides working, tested examples of how popular languages/runtimes handle basic I/O and common serialization formats.

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
          "subtitle"    .summary
        ) -}}
      {{ end}}
    </div>
  {{ end}}
{{< /_.inline >}}
