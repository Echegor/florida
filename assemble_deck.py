import deck_css
import deck_slides_1_10
import deck_slides_11_20
import deck_slides_21_30
import deck_js

print("Assembling full index.html...")

parts = [
    deck_css.get_head(),
    deck_slides_1_10.get_slides(),
    deck_slides_11_20.get_slides(),
    deck_slides_21_30.get_slides(),
    deck_js.get_footer_and_js()
]

full_html = "".join(parts)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(full_html)

print(f"Successfully generated index.html ({len(full_html)} bytes, {len(full_html.splitlines())} lines)")
