{{ $siteData := .siteData }}

> {{ .summary }}

{{ .description }}

{{ $assertion := .assertion }}

{{ if .files }}

<h4>Input file</h4>

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


{{ default "" .additional_md }}


{{ if .code }}
```{{ .language.syntax_highlighting }} {filename="{{.file_name}}"}
{{ .code }}
```

<div class="running-the-program">
  <h4>Running the program</h4>

```console
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
</div>
{{ end }}

---
{{ end }}
