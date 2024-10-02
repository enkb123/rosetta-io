{{ $siteData := .siteData }}

> {{ .summary }}

{{ .description }}

{{ $assertion := .assertion }}

{{ if .files }}
## Setup

### Inputs
{{ range .files }}
  ```{{ .ext }} {filename="{{.name}}"}
  {{ .content }}
  ```
{{ end }}

{{ end }}


## Implementations

{{ range .implementations }}
<div class="implementation">

### {{ .language.human_name }}

<div class="language-icon">
  {{index $siteData.icons (printf "language-%s" .language.icon_id)}}
</div>

```{{ .language.syntax_highlighting }} {filename="{{.file_name}}"}
{{ .code }}
```

```console {filename="running the program"}
$ {{ .command }}
{{ with $assertion -}}
  {{ if .stdout_match -}}
    {{ .stdout_match }}
  {{ else if .json -}}
    {{ .json | jsonify }}
  {{ end -}}
{{ end -}}
```
</div>
{{ end }}
