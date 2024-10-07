> {{ .summary }}

{{ .description }}

{{ range .implementations }}
## {{ .language.human_name }}

```{{ .language.syntax_highlighting }} {filename="{{.file_name}}"}
{{ .code }}
```
{{ .additional_md }}
{{ end }}
