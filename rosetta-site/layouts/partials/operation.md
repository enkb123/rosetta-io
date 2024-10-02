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
### {{ .language.human_name }}

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

{{ end }}
