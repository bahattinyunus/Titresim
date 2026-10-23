# -*- coding: utf-8 -*-
"""
Inject organs and phonetics data, along with rendering logic, into web/app.js
"""
import json
from pathlib import Path

organs_file = Path("data/organs.json")
phonetics_file = Path("data/phonetics.json")
app_js_file = Path("web/app.js")

with open(organs_file, "r", encoding="utf-8") as f:
    organs_data = json.load(f)

with open(phonetics_file, "r", encoding="utf-8") as f:
    phonetics_data = json.load(f)

with open(app_js_file, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Başlığa ORGANS_DATA ve PHONETICS_DATA ekle (CHAKRAS_DATA'nın hemen önüne)
datasets_code = f"""const ORGANS_DATA = {json.dumps(organs_data, ensure_ascii=False, indent=2)};

const PHONETICS_DATA = {json.dumps(phonetics_data, ensure_ascii=False, indent=2)};

"""

if "const ORGANS_DATA" not in content:
    content = content.replace("const CHAKRAS_DATA = [", datasets_code + "const CHAKRAS_DATA = [", 1)

# 2. Render ve Event Listener fonksiyonlarını son satırın arkasına ekle
rendering_logic = """
// ==========================================
// 6. TITRESIM v2.1: ORGAN, NEFES & VOKAL RENDER
// ==========================================
function renderOrgans() {
  const container = document.getElementById("organsGrid");
  if (!container) return;
  container.innerHTML = "";

  const scanBtn = document.getElementById("fullBodyScanBtn");
  if (scanBtn) {
    scanBtn.onclick = () => {
      scanBtn.disabled = true;
      scanBtn.innerText = "🧬 Tüm Beden Taranıyor (10 Organ)...";
      let oIdx = 0;

      const playNextOrgan = () => {
        if (oIdx >= ORGANS_DATA.length) {
          scanBtn.disabled = false;
          scanBtn.innerText = "Tam Beden Organ Taraması Başlat (10 Organ)";
          audio.stopTone();
          return;
        }
        const org = ORGANS_DATA[oIdx];
        audio.playTone(org.frequency);
        if (cymaticsSim) cymaticsSim.setFrequency(org.frequency);

        document.querySelectorAll(".organ-card").forEach(c => c.classList.remove("playing"));
        const activeCard = document.querySelector(`[data-organ-id="${org.id}"]`);
        if (activeCard) activeCard.classList.add("playing");

        oIdx++;
        setTimeout(playNextOrgan, 3000);
      };

      playNextOrgan();
    };
  }

  ORGANS_DATA.forEach(org => {
    const card = document.createElement("div");
    card.className = "organ-card";
    card.setAttribute("data-organ-id", org.id);
    card.innerHTML = `
      <div class="organ-header">
        <span class="organ-title">${org.name}</span>
        <span class="organ-freq-badge">${org.frequency} Hz</span>
      </div>
      <div class="organ-desc">${org.description}</div>
      <div class="organ-effects">✨ <strong>Şifa:</strong> ${org.effects} • <em>Çakra: ${org.associated_chakra}</em></div>
      <div style="display: flex; justify-content: space-between; align-items: center;">
        <span style="font-size: 11px; color: #94a3b8;">Protokol: ${org.healing_protocol}</span>
        <button class="btn btn-sm btn-outline play-organ-btn">Frekansı Çal</button>
      </div>
    `;

    card.querySelector(".play-organ-btn").addEventListener("click", () => {
      document.querySelectorAll(".organ-card").forEach(c => c.classList.remove("playing"));
      card.classList.add("playing");
      audio.playTone(org.frequency);
      if (cymaticsSim) cymaticsSim.setFrequency(org.frequency);
    });

    container.appendChild(card);
  });
}

const BREATH_PATTERNS = {
  coherence: { title: "0.10 Hz Kardiyak Koherans Nefesi", desc: "5.5s Alış, 5.5s Veriş ile vagal fren uyarımı ve maksimum HRV.", inhale: 5.5, holdIn: 0, exhale: 5.5, holdOut: 0 },
  box: { title: "Kutu Nefesi (Box Breathing)", desc: "4s Alış, 4s Tutuş, 4s Veriş, 4s Boş Tutuş ile panik bastırma.", inhale: 4.0, holdIn: 4.0, exhale: 4.0, holdOut: 4.0 },
  "4-7-8": { title: "4-7-8 Dr. Weil Uyku Nefesi", desc: "4s Burundan Alış, 7s Tutuş, 8s Ağızdan Veriş ile derin uyku.", inhale: 4.0, holdIn: 7.0, exhale: 8.0, holdOut: 0 },
  relax: { title: "Yumuşak Gevşeme Nefesi (1:1.5)", desc: "4s Alış, 6s Yavaş Veriş ile kas gevşemesi ve tansiyon düşüşü.", inhale: 4.0, holdIn: 0, exhale: 6.0, holdOut: 0 }
};

let activeBreathPattern = "coherence";
let breathTimer = null;
let breathTimeLeft = 0;

function setupBreathGuide() {
  const pTitle = document.getElementById("breathPatternTitle");
  const pDesc = document.getElementById("breathPatternDesc");
  const cText = document.getElementById("breathCircleText");
  const cTimer = document.getElementById("breathCircleTimer");
  const circle = document.getElementById("breathCircle");
  const startBtn = document.getElementById("startBreathBtn");
  const stopBtn = document.getElementById("stopBreathBtn");

  document.querySelectorAll(".breath-mode-btn").forEach(btn => {
    btn.addEventListener("click", () => {
      document.querySelectorAll(".breath-mode-btn").forEach(b => b.classList.remove("active"));
      btn.classList.add("active");
      activeBreathPattern = btn.getAttribute("data-pattern");
      const p = BREATH_PATTERNS[activeBreathPattern];
      if (pTitle) pTitle.innerText = p.title;
      if (pDesc) pDesc.innerText = p.desc;
      stopBreathingSession();
    });
  });

  function stopBreathingSession() {
    if (breathTimer) {
      clearInterval(breathTimer);
      breathTimer = null;
    }
    if (circle) {
      circle.style.transform = "scale(1.0)";
      circle.className = "breath-circle";
    }
    if (cText) cText.innerText = "HAZIR";
    if (cTimer) cTimer.innerText = "0.0s";
    if (startBtn) startBtn.classList.remove("hidden");
    if (stopBtn) stopBtn.classList.add("hidden");
    audio.stopTone();
  }

  if (stopBtn) stopBtn.onclick = stopBreathingSession;

  if (startBtn) {
    startBtn.onclick = () => {
      startBtn.classList.add("hidden");
      stopBtn.classList.remove("hidden");

      const p = BREATH_PATTERNS[activeBreathPattern];
      let currentPhase = "inhale"; // inhale, holdIn, exhale, holdOut
      let phaseTime = p.inhale;

      audio.playTone(216.0);

      const runPhase = () => {
        circle.className = `breath-circle ${currentPhase}`;
        if (currentPhase === "inhale") {
          cText.innerText = "NEFES AL";
          circle.style.transform = "scale(1.35)";
          audio.playTone(260.0);
        } else if (currentPhase === "holdIn") {
          cText.innerText = "NEFESİ TUT";
          audio.playTone(280.0);
        } else if (currentPhase === "exhale") {
          cText.innerText = "NEFES VER";
          circle.style.transform = "scale(0.85)";
          audio.playTone(200.0);
        } else if (currentPhase === "holdOut") {
          cText.innerText = "DİNLEN / TUT";
          audio.playTone(180.0);
        }
      };

      runPhase();
      let stepCountdown = phaseTime;

      breathTimer = setInterval(() => {
        stepCountdown -= 0.1;
        cTimer.innerText = `${Math.max(0, stepCountdown).toFixed(1)}s`;

        if (stepCountdown <= 0) {
          // Sıradaki faza geç
          if (currentPhase === "inhale") {
            if (p.holdIn > 0) { currentPhase = "holdIn"; phaseTime = p.holdIn; }
            else { currentPhase = "exhale"; phaseTime = p.exhale; }
          } else if (currentPhase === "holdIn") {
            currentPhase = "exhale"; phaseTime = p.exhale;
          } else if (currentPhase === "exhale") {
            if (p.holdOut > 0) { currentPhase = "holdOut"; phaseTime = p.holdOut; }
            else { currentPhase = "inhale"; phaseTime = p.inhale; }
          } else if (currentPhase === "holdOut") {
            currentPhase = "inhale"; phaseTime = p.inhale;
          }
          stepCountdown = phaseTime;
          runPhase();
        }
      }, 100);
    };
  }
}

function renderPhonetics() {
  const container = document.getElementById("vocalChantsList");
  if (!container) return;
  container.innerHTML = "";

  PHONETICS_DATA.forEach(chant => {
    const card = document.createElement("div");
    card.className = "chant-card";
    card.innerHTML = `
      <div class="chant-header">
        <span class="chant-title">${chant.name}</span>
        <span class="organ-freq-badge">${chant.base_pitch_hz} Hz</span>
      </div>
      <div style="font-size: 12px; color: #fde68a;">Gelenek: ${chant.tradition} • Mahreç: ${chant.mahref}</div>
      <div class="organ-desc mt-1">${chant.description}</div>
      <div class="formants-row">
        ${chant.formants.map((f, i) => `<span class="formant-pill">F${i+1}: ${f} Hz</span>`).join("")}
      </div>
      <div class="chant-no-effect">🧪 <strong>Biyoakustik Etki:</strong> ${chant.nitric_oxide_effect}</div>
      <div style="display: flex; justify-content: flex-end;">
        <button class="btn btn-sm btn-outline-gold play-chant-btn">🕊️ Vokal Formantını Dinle</button>
      </div>
    `;

    card.querySelector(".play-chant-btn").addEventListener("click", () => {
      document.querySelectorAll(".chant-card").forEach(c => c.classList.remove("playing"));
      card.classList.add("playing");
      audio.playTone(chant.base_pitch_hz);
      if (cymaticsSim) cymaticsSim.setFrequency(chant.base_pitch_hz);
    });

    container.appendChild(card);
  });
}
"""

if "function renderOrgans()" not in content:
    content += rendering_logic

# DOMContentLoaded içine fonksiyon çağrılarını ekle
if "renderOrgans();" not in content:
    content = content.replace("renderChakras();", "renderChakras();\n  renderOrgans();\n  setupBreathGuide();\n  renderPhonetics();")

with open(app_js_file, "w", encoding="utf-8") as f:
    f.write(content)

print("web/app.js başarıyla v2.1 geliştirmeleriyle güncellendi!")
