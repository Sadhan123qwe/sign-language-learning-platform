# 🚀 Signlingo Deployment Guide

## Recommended Platform: Streamlit Community Cloud (Free)

---

## ⚠️ Critical Issues to Fix Before Deploying

### 1. Fix `requirements.txt` (REQUIRED)
Replace your existing `requirements.txt` with the cleaned version provided.
The original had a broken last line (`Pillowpython -m streamlit run signlingo.py`).

Also, use `opencv-contrib-python-headless` instead of `opencv-contrib-python` —
the headless version works on servers that have no display (like cloud VMs).

### 2. ML Model Files (REQUIRED)
Your `asl_detection_models/` folder with `model1.p`, `model2.p`, `model3.p` **must** be
committed to your GitHub repository.

> ⚠️ If model files are large (>50MB each), use **Git LFS**:
> ```bash
> git lfs install
> git lfs track "*.p"
> git add .gitattributes
> ```

### 3. Protect `_secret_auth_.json` (IMPORTANT)
This file contains user credentials. **Never push real credentials to a public repo.**

**Option A – Keep the file but sanitize it for GitHub:**
Replace the real file with a blank template before pushing:
```json
[]
```
New users can register through the app's built-in signup.

**Option B – Use Streamlit Secrets (recommended):**
In `Signlingo.py`, replace the file reads with:
```python
import streamlit as st
import json
user_data = json.loads(st.secrets["auth_users"])
```
Then in Streamlit Cloud dashboard → App Settings → Secrets, add:
```toml
auth_users = '[{"username":"...","name":"...","email":"...","password":"..."}]'
```

### 4. SQLite Persistence
Streamlit Community Cloud has an **ephemeral filesystem** — `signlingo.db` resets on every reboot.

**Quick fix:** Add this at the top of `Signlingo.py` to copy the DB to a writable temp path:
```python
import shutil, os
DB_PATH = "/tmp/signlingo.db"
if not os.path.exists(DB_PATH):
    shutil.copy("signlingo.db", DB_PATH)
conn = sqlite3.connect(DB_PATH)
```

**Long-term fix:** Migrate to [Supabase](https://supabase.com) (free PostgreSQL) or
[PlanetScale](https://planetscale.com) for persistent storage.

---

## 📋 Step-by-Step Deployment

### Step 1 – Prepare Your Repository

```bash
# Make sure your repo has this structure:
signlingo/
├── .streamlit/
│   └── config.toml          ← use the provided one
├── asl_detection_models/
│   ├── model1.p
│   ├── model2.p
│   └── model3.p
├── pages/
│   ├── 1_Your_Profile_👨🏻‍💼.py
│   ├── 2_Learn Alphabets_📚.py
│   ├── 3_Learn Words_🧠.py
│   ├── 4_Quiz Time_📝.py
│   └── 5_Practice Zone_🎓.py
├── _secret_auth_.json       ← use empty [] for public repos
├── components.py
├── model.py
├── requirements.txt         ← use the cleaned version provided
├── Signlingo.py
├── styles.py
├── urls.py
├── video_urls.txt
└── .gitignore               ← use the provided one
```

### Step 2 – Push to GitHub

```bash
git init
git add .
git commit -m "Initial commit - Signlingo ASL app"
git remote add origin https://github.com/YOUR_USERNAME/signlingo.git
git push -u origin main
```

### Step 3 – Deploy on Streamlit Community Cloud

1. Go to **[share.streamlit.io](https://share.streamlit.io)**
2. Sign in with your GitHub account
3. Click **"New app"**
4. Fill in:
   - **Repository:** `YOUR_USERNAME/signlingo`
   - **Branch:** `main`
   - **Main file path:** `Signlingo.py`
5. Click **"Deploy!"**
6. Wait ~5 minutes for the build to complete ☕

### Step 4 – Configure Secrets (if using Option B above)

In your deployed app dashboard:
1. Click **"⋮" → Settings → Secrets**
2. Add your auth data in TOML format
3. Save and reboot the app

---

## 🔧 Alternative Platforms

### Railway
1. Sign up at [railway.app](https://railway.app)
2. New Project → Deploy from GitHub repo
3. Add env variable: `PORT=8501`
4. Add start command: `streamlit run Signlingo.py --server.port $PORT --server.address 0.0.0.0`

### Render
1. Sign up at [render.com](https://render.com)
2. New → Web Service → Connect GitHub repo
3. Build command: `pip install -r requirements.txt`
4. Start command: `streamlit run Signlingo.py --server.port $PORT --server.address 0.0.0.0`
5. Free tier has limited RAM — may struggle with MediaPipe + OpenCV

---

## 🐛 Common Deployment Errors

| Error | Fix |
|-------|-----|
| `ModuleNotFoundError: cv2` | Use `opencv-contrib-python-headless` in requirements |
| `No module named mediapipe` | Pin version: `mediapipe==0.10.13` |
| Model file not found | Ensure `asl_detection_models/` is committed to git |
| App crashes on webcam access | Browser webcam access requires HTTPS — Streamlit Cloud provides this automatically |
| DB resets on redeploy | Use `/tmp/` path for SQLite or migrate to cloud DB |

---

## ✅ Pre-Deploy Checklist

- [ ] `requirements.txt` uses `opencv-contrib-python-headless`
- [ ] `asl_detection_models/*.p` files are in the repo
- [ ] All `pages/*.py` files are in the repo
- [ ] `_secret_auth_.json` has no real passwords (or is in Secrets)
- [ ] `.streamlit/config.toml` is committed
- [ ] `.gitignore` excludes `signlingo.db` and `secrets.toml`
- [ ] Tested locally with `streamlit run Signlingo.py`
