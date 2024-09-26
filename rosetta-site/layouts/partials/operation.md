{{ range .implementations }}
  ## {{ .language.human_name }}

  ```{{ .language.syntax_highlighting }} {filename="{{.file_name}}"}
  {{ .code }}
  ```

{{ end }}
