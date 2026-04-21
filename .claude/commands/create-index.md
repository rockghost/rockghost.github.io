Create an index.html file for src/ that serves as a course navigation page with an iframe viewer.

Steps:
1. Read one of the HTML files in src/ to extract the left sidebar menu structure (look for `section-title` and `lesson-row` elements)
2. List all HTML files in src/ (excluding index.html) to determine which lessons have files
3. Create src/index.html following the same template as ../claude-course/Claude 101/index.html:
   - Left sidebar with course title, section headings, and lesson links
   - Lessons with matching HTML files get `<a class="lesson">` links with `target="viewer"`
   - Lessons without files get `<span class="no-file">` (greyed out)
   - Right side iframe viewer with Prev/Next navigation and sidebar toggle
   - Keyboard navigation (arrow keys)
   - Auto-load first available lesson

Report the results to the user.
