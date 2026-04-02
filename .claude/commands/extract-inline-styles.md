Run the inline style extraction script on all HTML files in src/:

```
python3 scripts/extract_inline_styles.py src
```

This extracts inline `<style>` blocks from HTML files into external CSS files:
1. Shared styles (identical across 2+ files) -> src/assets/shared-{n}.css (deduplicated)
2. Per-page unique styles -> src/assets/css/{page-name}.css (merged per file)
3. Replaces `<style>...</style>` in HTML with `<link rel="stylesheet" href="...">`

This is required before translation — without it, HTML files contain huge minified CSS blocks (up to 75KB per line) that exceed the Read tool's token limit.

Report the results to the user.
