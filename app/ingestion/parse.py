"""PDF -> texte brut, sans en-têtes/pieds de page du Journal officiel."""
import re
import sys

import fitz  # PyMuPDF

# Lignes répétées sur chaque page du JO : "FR", "JO L du 12.7.2024", "ELI: http://...", "16/144"
NOISE = re.compile(
    r"^(FR|JO L.*|ELI\s*:.*|\d+/\d+|Journal officiel de l.Union européenne)$"
)


# Corps du texte en 9,6 pt ; notes de bas de page en 8,5 pt. Les numéros de considérants
# sont aussi en petite police : une note se reconnaît donc à sa taille ET à sa position,
# sous la dernière ligne du corps de la page.
BODY_FONT_SIZE = 9.0


def _page_lines(page: fitz.Page) -> list[str]:
    rows = []  # (y, texte, taille max)
    for block in page.get_text("dict")["blocks"]:
        for pdf_line in block.get("lines", []):
            text = "".join(s["text"] for s in pdf_line["spans"]).strip()
            if text and not NOISE.match(text):
                size = max(s["size"] for s in pdf_line["spans"])
                rows.append((pdf_line["bbox"][1], text, size))
    body_bottom = max((y for y, _, size in rows if size >= BODY_FONT_SIZE), default=0)
    return [text for y, text, size in rows if size >= BODY_FONT_SIZE or y <= body_bottom]


def extract_text(pdf_path: str) -> str:
    with fitz.open(pdf_path) as doc:
        return "\n".join(line for page in doc for line in _page_lines(page))


if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else "data/ai_act_fr.pdf"
    text = extract_text(path)
    out = path.rsplit(".", 1)[0] + ".txt"
    with open(out, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"{len(text):,} caractères -> {out}")
