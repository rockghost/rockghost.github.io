Run the datetime suffix removal script on all HTML files in src/:

```
bash scripts/remove-datetime-suffix.sh
```

This removes date/time suffixes from HTML filenames in src/:
- Pattern: "Filename (2026. 3. 31. 오전 10：51：50).html" -> "Filename.html"
- Removes the ` (날짜시간)` portion from the end of each filename

Report the results to the user.
