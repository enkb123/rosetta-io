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

<style>
.running-the-program {
  padding: 0 1rem;
}

.language-console {
  .gp {
    font-weight: bold;
  }
}

h4 {
  font-size: 1rem !important;
  margin-bottom: -1rem !important;
}

hr {
  margin-top: 2rem;
  margin-bottom: .5rem;
  &:last-of-type {
    display: none;
  }
}
</style>
