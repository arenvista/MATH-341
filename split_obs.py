import os
import re
import urllib.parse
from pathlib import Path

# ===== SETTINGS =====
SOURCE_FOLDER = r"/home/sybil/Documents/School/2026-Spring/MATH-341/Notes-MATH(341)/LecFormated"
OUTPUT_FOLDER = r"/home/sybil/Documents/School/2026-Spring/MATH-341/Notes-MATH(341)/Atomized"
HEADING_LEVEL = 1  # 1 = #, 2 = ##, 3 = ### etc.
USE_WIKI_LINKS = True  # Set to True if using Obsidian/Logseq: [[Filename]]
# ====================

def split_headers(SOURCE_FOLDER, OUTPUT_FOLDER, HEADING_LEVEL, USE_WIKI_LINKS): 
    heading_pattern = re.compile(rf"^{'#' * HEADING_LEVEL} (.+)", re.MULTILINE)

    source_path = Path(SOURCE_FOLDER)
    output_path = Path(OUTPUT_FOLDER)
    output_path.mkdir(parents=True, exist_ok=True)

    for file_path in source_path.glob("*.md"):
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        matches = list(heading_pattern.finditer(content))
        
        # If no headings found, skip to the next file
        if not matches:
            continue

        modified_original = ""
        last_index = 0

        for i, match in enumerate(matches):
            title = match.group(1).strip()
            start = match.end()
            end = matches[i + 1].start() if i + 1 < len(matches) else len(content)
            section_content = content[start:end].strip()

            safe_title = re.sub(r'[\\/*?:"<>|]', "", title)
            new_file_name = f"{file_path.stem} - {safe_title}.md"
            new_file_path = output_path / new_file_name

            # --- Link Generation ---
            if USE_WIKI_LINKS:
                link_to_new = f"[[{new_file_path.stem}]]"
                link_to_orig = f"[[{file_path.stem}]]"
            else:
                # Generate standard relative markdown links, URL-encoding spaces
                rel_path_to_new = urllib.parse.quote(os.path.relpath(new_file_path, file_path.parent))
                rel_path_to_orig = urllib.parse.quote(os.path.relpath(file_path, output_path))
                link_to_new = f"[{title}]({rel_path_to_new})"
                link_to_orig = f"[{file_path.stem}]({rel_path_to_orig})"

            # --- Write New File ---
            with open(new_file_path, "w", encoding="utf-8") as new_file:
                new_file.write(f"# {title}\n\n*Original Note: {link_to_orig}*\n\n{section_content}\n")

            # --- Update Original Content ---
            # Append text before this heading
            modified_original += content[last_index:match.start()]
            # Append the heading itself and the link replacing the extracted content
            modified_original += f"{match.group(0)}\n\n*Extracted to: {link_to_new}*\n\n"
            
            last_index = end

        # Append any remaining text from the very end of the file
        modified_original += content[last_index:]

        # --- Overwrite Original File ---
        with open(file_path, "a", encoding="utf-8") as f:
            f.write("# Extractions -------------\n")
            f.write(modified_original)

    print("Done splitting files and creating bidirectional links.")

if __name__ == "__main__":
    SOURCE_FOLDER = r"/home/sybil/Documents/School/2026-Spring/MATH-341/Notes-MATH(341)/LecFormated"
    OUTPUT_FOLDER = r"/home/sybil/Documents/School/2026-Spring/MATH-341/Notes-MATH(341)/Atomized/H1"
    HEADING_LEVEL = 1  
    split_headers(SOURCE_FOLDER, OUTPUT_FOLDER, HEADING_LEVEL, USE_WIKI_LINKS)
    SOURCE_FOLDER = r"/home/sybil/Documents/School/2026-Spring/MATH-341/Notes-MATH(341)/Atomized/H1"
    OUTPUT_FOLDER = r"/home/sybil/Documents/School/2026-Spring/MATH-341/Notes-MATH(341)/Atomized/H2"
    HEADING_LEVEL = 2  
    split_headers(SOURCE_FOLDER, OUTPUT_FOLDER, HEADING_LEVEL, USE_WIKI_LINKS)
