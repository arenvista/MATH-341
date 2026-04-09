import os
import sys
from pathlib import Path

from openai import OpenAI

MODEL = "gpt-5"

SYSTEM_PROMPT = """You are an expert technical editor and formatter.

Read the provided contents and run: clean, split into sections by header, title unnamed theorems, sections etc. 

Formatting Rules:
- Use $$ $$ for display math.
- Use $ $ if better formatted inline.
- Use Markdown blockquote callouts (e.g., > [!thm] Title) when appropriate. 
- Focus on generating named headers and subheaders

The environment supports the following callout types:
/* --- THEOREM (Blue) --- */
.callout[data-callout="thm"] 
/* --- LEMMA (Teal/Cyan) --- */
.callout[data-callout="lem"] 
/* --- COROLLARY (Purple) --- */
.callout[data-callout="cor"] 
/* --- DEFINITION (Green) --- */
.callout[data-callout="def"] {
/* --- PROOF (Gray/Subtle) --- */
.callout[data-callout="pf"] {
/* --- CASE (Orange) --- */
/* Used for specific scenarios, use cases, or 'Case 1' in proofs */
.callout[data-callout="case"] 
/* --- QUESTION (Yellow/Gold) --- */
/* Used for inquiries, open problems, or FAQs */
.callout[data-callout="?"] 
/* --- IMPORTANT (Red) --- */
/* Used for critical warnings, key takeaways, or risks */
.callout[data-callout="imp"]

Output ONLY the formatted markdown text. Do not include introductory conversational filler.
"""


def get_client() -> OpenAI:
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("Error: OPENAI_API_KEY not set.")
        sys.exit(1)
    return OpenAI(api_key=api_key)


def format_code(client: OpenAI, text_content: str) -> str:
    response = client.responses.create(
        model=MODEL,  # Assuming MODEL is defined (e.g., "gpt-5")
        input=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": text_content},
        ],
        reasoning={"effort": "high"},
        text={"verbosity": "high"},  # Options: "low", "medium", "high"
    )
    return response.output_text.strip()


def process_directory(source_dir: Path, target_dir: Path) -> None:
    client = get_client()

    # Changed from *.py to *.md to process Markdown files
    for file_path in source_dir.rglob("*.md"):
        relative = file_path.relative_to(source_dir)
        output_path = target_dir / relative

        print(f"Formatting: {file_path}")

        output_path.parent.mkdir(parents=True, exist_ok=True)

        original_text = file_path.read_text(encoding="utf-8")

        try:
            formatted = format_code(client, original_text)
            output_path.write_text(formatted, encoding="utf-8")
        except Exception as e:
            print(f"Failed: {file_path} -> {e}")


def main() -> None:
    if len(sys.argv) != 3:
        print("Usage: uv run format_dir.py <source_dir> <target_dir>")
        sys.exit(1)

    source = Path(sys.argv[1]).resolve()
    target = Path(sys.argv[2]).resolve()

    if not source.exists():
        print(f"Source directory does not exist: {source}")
        sys.exit(1)

    process_directory(source, target)
    print("Done.")


if __name__ == "__main__":
    main()
