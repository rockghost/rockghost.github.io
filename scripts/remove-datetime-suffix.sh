#!/bin/bash
# src/ 디렉토리의 HTML 파일명에서 날짜/시간 접미사를 제거
# 예: "Filename (2026. 3. 31. 오전 10：51：50).html" -> "Filename.html"

cd "$(dirname "$0")/../src" || exit 1

for f in *'('*')'*.html; do
  [ -e "$f" ] || continue
  newname=$(echo "$f" | sed 's/ ([^)]*)//')
  echo "\"$f\" -> \"$newname\""
  mv "$f" "$newname"
done
