Run the inline asset extraction script on all HTML files in src/:

```
python3 scripts/extract_inline_assets.py src
```

This extracts inline base64-encoded assets from single-file HTML files:
1. Shared assets (fonts, favicon, logo) -> src/assets/ (deduplicated across all files)
2. Per-page content images -> src/assets/images/ (unique per file)
3. Replaces data: URIs in HTML with relative file paths

Report the results to the user.
