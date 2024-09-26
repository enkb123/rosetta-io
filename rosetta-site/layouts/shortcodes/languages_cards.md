{{ range $.Site.Data.languages }}
  {{- partial "shortcodes/card" (dict
    "title"       .human_name
    "icon"        (printf "language-%s" .icon_id)
  ) -}}
{{ end }}
