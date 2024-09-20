# Let's adjust the CSS by ensuring all rules are scoped under the div with id="custom_theme".
# We'll prefix all selectors with "#custom_theme" where necessary.

input_css_path = './final.css'
output_css_path = './final-scoped.css'

with open(input_css_path, 'r') as file:
    css_content = file.read()

# Prefix every rule with #custom_theme if it's not already scoped
scoped_css = ""
inside_block = False
for line in css_content.splitlines():
    stripped_line = line.strip()
    
    # Check if the line starts with a CSS selector (and is not already scoped by #custom_theme)
    if stripped_line and not stripped_line.startswith('@') and not stripped_line.startswith('#custom_theme') and not inside_block:
        if stripped_line.endswith('{'):
            scoped_css += f"#custom_theme {line}\n"
            inside_block = True
        else:
            scoped_css += line + "\n"
    else:
        scoped_css += line + "\n"
    
    if inside_block and stripped_line.endswith('}'):
        inside_block = False

# Save the scoped CSS file
with open(output_css_path, 'w') as scoped_file:
    scoped_file.write(scoped_css)

output_css_path  # Return the path to the newly scoped CSS file
