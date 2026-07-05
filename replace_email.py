import os

html_files = ['index.html', 'about.html', 'tours.html', 'contact.html']
base_dir = 'd:/Andy/CeylonTrailsbyAndy/'

old_email = 'andy@srilankatours.com'
new_email = 'nphewage@hotmail.com'

for file in html_files:
    filepath = os.path.join(base_dir, file)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if old_email in content:
        content = content.replace(old_email, new_email)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {file}")

print("Email replacement complete.")
