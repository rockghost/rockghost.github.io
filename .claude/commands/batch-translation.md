You are a batch processing orchestrator. Your job is to run a series of slash commands on all HTML files in `src/` in a specific order.

## Execution Order

Run each step completely (all files) before moving to the next step:

### Step 1: Remove datetime suffixes
Run the datetime suffix removal script on all HTML files in src/:
```
bash scripts/remove-datetime-suffix.sh
```
Wait for completion and report results before proceeding.

### Step 2: Prettify HTML
Run BeautifulSoup prettify on all HTML files to ensure proper line breaks for the Read tool:
```
python3 scripts/prettify_html.py src
```
Wait for completion and report results before proceeding.

### Step 3: Remove video players
Run the video player removal script on all HTML files in src/:
```
python3 scripts/remove_video_player.py src
```
Wait for completion and report results before proceeding.

### Step 4: Create index (ONE TIME ONLY)
This step runs exactly ONCE — do NOT loop over files.
Use the `Skill` tool to invoke the `create-index` skill. This creates src/index.html as a course navigation page with an iframe viewer by:
1. Reading an HTML file in src/ to extract the sidebar menu structure
2. Listing all HTML files in src/ (excluding index.html)
3. Creating src/index.html with sidebar navigation, iframe viewer, and keyboard navigation

Wait for completion and report results before proceeding.

### Step 5: Remove sidebar menus
Run the sidebar menu removal script on all HTML files in src/:
```
python3 scripts/remove-sidebar-menu.py
```
Wait for completion and report results before proceeding.

### Step 6: Extract inline assets
Run the inline asset extraction script on all HTML files in src/:
```
python3 scripts/extract_inline_assets.py src
```
Wait for completion and report results before proceeding.

### Step 7: Extract inline styles
Run the inline style extraction script to extract `<style>` blocks into external CSS files:
```
python3 scripts/extract_inline_styles.py src
```
This is required before translation — without it, HTML files contain huge minified CSS blocks that exceed the Read tool's token limit, making translation agents unable to read the files.

Wait for completion and report results before proceeding.

### Step 8: Translate to Korean
Use the `Skill` tool to invoke the `translate-to-korean` skill. This translates all English content in HTML files under src/ into Korean using sub-agents with concurrency limit of 4.

Wait for completion and report results.

## Final Report

After all steps complete, provide a summary:
- Results from each step
- Any errors or warnings encountered
- Total files processed
