Run the video player removal script on all HTML files in src/:

```
python3 scripts/remove_video_player.py src
```

This removes the following from single-file HTML files:
1. Embedded JWPlayer video player sections (sjwc 패턴, course-fixed-content-video div)
2. JWPlayer CSS rules (.jwplayer, .jw-* selectors) from inline `<style>` blocks
3. Empty `<style data-jwplayer-id=...></style>` tags

Report the results to the user.
