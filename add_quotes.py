import re

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Regex to find review cards and modify their content
    # We want to match:
    # <p class="text-slate-600 italic mb-8 flex-grow">Text</p>
    
    # Put literal quotes back around the paragraph text
    p_pattern = r'(<p class="text-slate-600 italic mb-8 flex-grow">)(.*?)(</p>)'
    # The regex won't double quote if we do a quick check, but since we stripped them, they don't have it.
    
    # We just need to make sure we don't double quote if we run it twice accidentally.
    def replace_func(match):
        text = match.group(2)
        if not text.startswith('"') and not text.endswith('"'):
            text = '"' + text + '"'
        return match.group(1) + text + match.group(3)
        
    content = re.sub(p_pattern, replace_func, content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Processed {filepath}")

process_file('d:/Project/andy-tours/index.html')
process_file('d:/Project/andy-tours/about.html')
