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
### {{ .language.human_name }}


{{ default "" .additional_md }}


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

---
{{ end }}
