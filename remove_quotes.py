import re

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Regex to find review cards and modify their content
    # We want to match:
    # <div class="review-card ...">
    #    <svg ...>...</svg>
    #    <p class="text-slate-600 italic mb-8 flex-grow">"Text"</p>
    
    # 1. Remove the SVG tag
    svg_pattern = r'<svg class="w-8 h-8 flex-shrink-0 text-brand-primary mb-6".*?</svg>\s*'
    content = re.sub(svg_pattern, '', content)

    # 2. Remove literal quotes from the paragraph text
    # It looks like: <p class="text-slate-600 italic mb-8 flex-grow">"Traveling with..."</p>
    p_pattern = r'(<p class="text-slate-600 italic mb-8 flex-grow">)"(.*?)"(</p>)'
    content = re.sub(p_pattern, r'\1\2\3', content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Processed {filepath}")

process_file('d:/Project/andy-tours/index.html')
process_file('d:/Project/andy-tours/about.html')
