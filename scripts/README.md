# Scripts

Automation scripts for Dumbledore bot operations.

## Scripts

### `renew_fps.py`

Auto-renewal script for FPS.ms free tier servers. Uses Selenium to click the "Add 24 hours" button on the panel.

**Usage:**
```bash
FPS_SERVER_URL=https://panel.fps.ms/server/xxxxx python scripts/renew_fps.py
```

**GitHub Actions:**
Runs automatically every 25 hours via `.github/workflows/renew.yml`.

Set `FPS_SERVER_URL` in repo variables (Settings → Secrets and variables → Actions → Variables).
