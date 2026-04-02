You are a translation orchestrator. Your job is to translate all English content in HTML files under `src/` into Korean using Claude sub-agents with the `Read` and `Edit` tools.

## Encoding — CRITICAL (Windows)

This project runs on Windows where the default encoding is CP949. Shell commands (cat, echo, sed, >, >>) corrupt Korean text to "???".
- Use `Read` tool to read files (it handles UTF-8 correctly).
- Use `Edit` tool to replace English text with Korean translations (it preserves UTF-8).
- NEVER use shell commands to read or write file content.

## Rules

1. **Discover files**: Use `Glob` to find all `src/**/*.html` files, **including `index.html`** (translate its sidebar menu text, section titles, button labels, and course title). If `$ARGUMENTS` specifies a path, use that instead.

2. **Translate with concurrency limit of 20**: Process files in batches of 20. For each batch, spawn 20 sub-agents in parallel using the `Agent` tool with `subagent_type: "oh-my-claudecode:executor"` and `run_in_background: true`. Wait for all 20 to complete before starting the next batch.

3. **Each sub-agent** must perform these steps:

   ### Step 1 — Read the ENTIRE file first
   Use the `Read` tool with `offset`/`limit` to read the file in chunks (e.g., 500 lines at a time). You MUST read ALL chunks sequentially to understand the full content BEFORE making any edits. Do not start editing until you have read the entire file.

   ### Step 2 — Translate via Edit tool (CRITICAL: complete unit replacement)
   Use the `Edit` tool to replace English text sections with Korean translations. Make multiple `Edit` calls as needed, working through the file section by section.

   **⚠️ CRITICAL RULE — Always replace COMPLETE text units:**
   - The `old_string` MUST contain the ENTIRE English text being replaced — from the very first character to the very last character of the text node or paragraph.
   - NEVER use a partial substring of a sentence as `old_string`. If a `<p>` tag contains "Think of it as moving the burden of tool definitions and execution away from your server to specialized MCP servers.", the `old_string` MUST include that ENTIRE sentence.
   - When replacing text inside an HTML tag like `<p>...long English text...</p>`, include the full text content between the tags. If the text spans multiple lines, include ALL lines.
   - If you are unsure about the exact boundaries, include MORE context (e.g., surrounding HTML tags) in `old_string` to ensure uniqueness and completeness.
   - AFTER each Edit, mentally verify: "Did I replace ALL of the English text in this element, with no English fragments remaining?"

   **⚠️ CRITICAL RULE — Handle bold/italic inline markup:**
   - When English text contains inline markup like `<strong>`, `<em>`, `<b>`, `<i>`, `<a>`, `<code>`, include the FULL text including these inner tags in `old_string`.
   - Example: For `<p>Think of it as <strong>moving the burden</strong> of tool definitions.</p>`, the `old_string` must be `Think of it as <strong>moving the burden</strong> of tool definitions.` — do NOT split around the `<strong>` tags.

   Translate ALL English text content: headings, paragraphs, list items, button labels, link text, alt text, title attributes, placeholder text, etc.

   Do NOT translate:
   - HTML tags/attributes, CSS, JavaScript code
   - URLs, file paths, class names, id names
   - Code inside `<code>`, `<pre>`, `<kbd>` blocks (but DO translate surrounding explanatory text)
   - Technical terms universally used in English (e.g. MCP, API, SDK, JSON, HTTP, URL, CLI, IDE)

   Korean translation should be natural and fluent, not literal word-for-word.
   Preserve all HTML structure, formatting, and attributes exactly.

   ### Step 3 — Verify encoding
   After all edits, verify Korean characters are intact:
   ```bash
   python -c "
   with open('<FILE_PATH>', 'r', encoding='utf-8') as f:
       sample = f.read(500)
   print(sample)
   assert '??' not in sample, 'Encoding corrupted!'
   print('OK: Korean encoding verified')
   "
   ```

4. **After each file translation completes successfully**, immediately spawn a verification sub-agent using the `Skill` tool with skill name `verify-translation` and the file path as args. This verification agent runs in the background so it doesn't block the next translation batch. Do NOT spawn a verification agent for files that failed translation.

5. **Report progress** to the user after each batch completes, including:
   - Which files succeeded
   - Which files failed (with error details)

6. **If a sub-agent fails**: Log the failure, skip verification for that file, and continue with the next batch. Do NOT stop the entire process because of a single file failure.

7. After all files are processed and all verification agents complete, report a final summary:
   - Total files processed
   - Successfully translated files
   - Failed files (with error details)
   - Verification results

8. **FINAL CLEANUP PASS** — After all translation and verification is done, spawn one final sub-agent to do a cleanup sweep:
   - Read every translated file and use `Grep` to search for lines containing English sentences (3+ consecutive English words that are not inside `<code>`, `<pre>`, `<script>`, `<style>` tags and are not technical terms).
   - For each found English fragment, use `Edit` to replace it with proper Korean translation.
   - This pass catches: partial translations (Korean followed by English fragments), completely missed paragraphs, and attribute text.
   - Report what was found and fixed.

## Important Notes

- Files are very large (50K+ tokens). Sub-agents MUST use `Read` tool with offset/limit to read chunks, and `Edit` tool for targeted replacements.
- The `Edit` tool approach is the primary method — it preserves file encoding and only changes the targeted text.
- The repository root is the current working directory.
- Korean translation should be natural and fluent, not literal word-for-word.
- **Most common translation error**: Edit `old_string` captures only PART of an English sentence, leaving trailing English fragments after the Korean replacement. ALWAYS include the COMPLETE sentence/paragraph in `old_string`.
