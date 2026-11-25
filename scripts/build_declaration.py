"""Build the editable ParkPilot AI Use Declaration from its Markdown source.

Usage: python scripts/build_declaration.py
Requires: python-docx
"""
from pathlib import Path
import re
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "docs" / "AI_Use_Declaration.md"
OUTPUT = ROOT / "docs" / "AI_Use_Declaration.docx"


def add_inline(p, value):
    for i, span in enumerate(re.split(r"\*\*(.*?)\*\*", value)):
        if not span:
            continue
        p.add_run(span).bold = i % 2 == 1


def build():
    doc = Document()
    section = doc.sections[0]
    section.top_margin = Inches(0.70)
    section.bottom_margin = Inches(0.70)
    section.left_margin = Inches(0.80)
    section.right_margin = Inches(0.80)
    styles = doc.styles
    styles['Normal'].font.name = 'Aptos'
    styles['Normal'].font.size = Pt(10)
    styles['Normal'].paragraph_format.space_after = Pt(5)
    for line in SOURCE.read_text(encoding='utf-8').splitlines():
        line = line.rstrip()
        if not line:
            continue
        if line.startswith('# '):
            para = doc.add_heading(line[2:], 0)
            para.alignment = WD_ALIGN_PARAGRAPH.LEFT
            for run in para.runs:
                run.font.color.rgb = RGBColor(24, 48, 84)
            continue
        if line.startswith('## '):
            para = doc.add_heading(line[3:], 2)
            para.paragraph_format.space_before = Pt(8)
            for run in para.runs:
                run.font.color.rgb = RGBColor(24, 48, 84)
            continue
        if line.startswith('- '):
            para = doc.add_paragraph(style='List Bullet')
            add_inline(para, line[2:])
            continue
        para = doc.add_paragraph()
        add_inline(para, line.replace('  ', ' '))
    doc.core_properties.title = 'ParkPilot — AI Use Declaration'
    doc.core_properties.subject = 'AIF1303 AI Fundamentals final project'
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    doc.save(OUTPUT)
    print('Created:', OUTPUT)

if __name__ == '__main__':
    build()
