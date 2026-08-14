# Qian Li's Technical Blog

This public repository is the umbrella GitHub Pages site for Qian Li's
technical publications.

- Technical essays are published directly from this repository.
- Tire & Rubber Intelligence remains a separate project site at
  `/tire-and-rubber-weekly-intelligence-report/`.
- Shared navigation and visual styling connect the two sites without combining
  their private editorial workflows.

Only publication-ready files belong here. Working notes and private assets are
maintained in the separate Industrial AI workspace. A single named note is
copied into this repository whenever the author chooses to publish or update
it.

The human author reviews the local Git changes, commits, and pushes them. GitHub
Pages then publishes from the `main` branch and repository root.

## Preview both public sites locally

From PowerShell in this repository, run:

```powershell
powershell -ExecutionPolicy Bypass -File .\tools\start_preview.ps1
```

The relative command works only after PowerShell has been changed into this
repository. Alternatively, open the repository's `tools` folder in File
Explorer and double-click `start_preview.cmd`.

One local server previews both repositories:

- Technical Thoughts: `http://127.0.0.1:4000/`
- Tire & Rubber Intelligence:
  `http://127.0.0.1:4000/tire-and-rubber-weekly-intelligence-report/`

The navigation stays local. Save a homepage, article, report, layout, or CSS
change and refresh the browser. Press `Ctrl+C` to stop. No commit, push, deploy,
or story-index change occurs.
