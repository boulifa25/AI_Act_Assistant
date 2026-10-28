"""Découpage du texte de l'AI Act en suivant sa structure juridique.

Unités : considérants, articles (avec chapitre/section), annexes.
Les unités trop longues sont redécoupées par paragraphe en conservant leurs métadonnées.
"""
import re
from dataclasses import dataclass

MAX_CHARS = 1800

RE_CHAPITRE = re.compile(r"^CHAPITRE\s+([IVXLC]+)$")
RE_ARTICLE = re.compile(r"^Article\s+(premier|\d+)$")
RE_ANNEXE = re.compile(r"^ANNEXE\s+([IVXLC]+)$")
RE_CONSIDERANT = re.compile(r"^\((\d+)\)$|^\((\d+)\)\s+(.*)$")
RE_PARAGRAPHE = re.compile(r"^(\d+\.|[a-z]\)|\d+\))(\s|$)")
END_PREAMBULE = "ONT ADOPTÉ LE PRÉSENT RÈGLEMENT"


@dataclass
class Chunk:
    article: str
    titre: str | None
    chapitre: str | None
    contenu: str


def _split_long(text: str, max_chars: int = MAX_CHARS) -> list[str]:
    """Redécoupe aux frontières de paragraphes numérotés ("1.", "a)") puis de lignes."""
    lines = text.split("\n")
    blocks: list[str] = []
    current: list[str] = []
    for line in lines:
        if RE_PARAGRAPHE.match(line) and current:
            blocks.append("\n".join(current))
            current = []
        current.append(line)
    if current:
        blocks.append("\n".join(current))

    parts: list[str] = []
    buf = ""
    for block in blocks:
        if len(block) > max_chars:  # bloc unique trop long : on coupe par lignes
            for line in block.split("\n"):
                if buf and len(buf) + len(line) + 1 > max_chars:
                    parts.append(buf)
                    buf = ""
                buf = f"{buf}\n{line}" if buf else line
        elif buf and len(buf) + len(block) + 1 > max_chars:
            parts.append(buf)
            buf = block
        else:
            buf = f"{buf}\n{block}" if buf else block
    if buf:
        parts.append(buf)
    return parts


def _emit(unit: dict, out: list[Chunk]) -> None:
    body = "\n".join(unit["lines"]).strip()
    if not body:
        return
    for part in _split_long(body):
        out.append(Chunk(unit["article"], unit["titre"], unit["chapitre"], part))


def chunk_text(text: str) -> list[Chunk]:
    lines = text.split("\n")
    chunks: list[Chunk] = []
    unit: dict | None = None
    chapitre: str | None = None
    in_preambule = True
    i = 0

    while i < len(lines):
        line = lines[i]
        nxt = lines[i + 1] if i + 1 < len(lines) else ""

        if in_preambule:
            if line.startswith(END_PREAMBULE):
                if unit:
                    _emit(unit, chunks)
                unit = None
                in_preambule = False
            elif m := RE_CONSIDERANT.match(line):
                if unit:
                    _emit(unit, chunks)
                num = m.group(1) or m.group(2)
                unit = {"article": f"Considérant {num}", "titre": None,
                        "chapitre": "Considérants", "lines": [m.group(3)] if m.group(3) else []}
            elif unit:
                unit["lines"].append(line)
            i += 1
            continue

        if m := RE_CHAPITRE.match(line):
            if unit:
                _emit(unit, chunks)
                unit = None
            titre_chapitre = re.sub(r"\bia\b", "IA", nxt.capitalize()) if nxt.isupper() else nxt
            chapitre = f"Chapitre {m.group(1)} — {titre_chapitre}"
            i += 2
            continue

        if m := RE_ARTICLE.match(line):
            if unit:
                _emit(unit, chunks)
            num = "1" if m.group(1) == "premier" else m.group(1)
            unit = {"article": num, "titre": nxt, "chapitre": chapitre, "lines": []}
            i += 2
            continue

        if m := RE_ANNEXE.match(line):
            if unit:
                _emit(unit, chunks)
            chapitre = "Annexes"
            unit = {"article": f"Annexe {m.group(1)}", "titre": nxt, "chapitre": chapitre, "lines": []}
            i += 2
            continue

        # Les titres de section restent dans le texte de l'unité précédente : on les ignore.
        if re.match(r"^SECTION\s+\d+$", line):
            i += 2
            continue

        if unit:
            unit["lines"].append(line)
        i += 1

    if unit:
        _emit(unit, chunks)
    return chunks


if __name__ == "__main__":
    import sys
    from collections import Counter

    from app.ingestion.parse import extract_text

    text = extract_text(sys.argv[1] if len(sys.argv) > 1 else "data/ai_act_fr.pdf")
    chunks = chunk_text(text)
    arts = [c.article for c in chunks if c.article.isdigit()]
    print(f"{len(chunks)} chunks")
    print(f"articles distincts : {len(set(arts))} (attendu : 113)")
    print(f"considérants : {len({c.article for c in chunks if c.article.startswith('Considérant')})} (attendu : 180)")
    print(f"annexes : {sorted({c.article for c in chunks if c.article.startswith('Annexe')})}")
    missing = sorted(set(range(1, 114)) - {int(a) for a in arts})
    print(f"articles manquants : {missing}")
    print(f"taille max : {max(len(c.contenu) for c in chunks)}")
    for c in chunks:
        if c.article == "5":
            print(f"\n--- Article 5 | {c.titre} | {c.chapitre}\n{c.contenu[:400]}")
            break
