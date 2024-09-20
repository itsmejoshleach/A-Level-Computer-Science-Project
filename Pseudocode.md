# Pseudocode

```

class webgui:
endclass webgui

class invoice:
  define func create:
    parsetemplate(html_template_path, form_input_data)
  end func create

  define func export:
    self.convertpdf()
    self.savepdf()
  end func export

endclass invoice

```