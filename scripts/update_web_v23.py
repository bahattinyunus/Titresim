# -*- coding: utf-8 -*-
"""
Inject bowls and water data and rendering logic into web/app.js for v2.3
"""
import json
from pathlib import Path

bowls_file = Path("data/bowls.json")
water_file = Path("data/water.json")
app_js_file = Path("web/app.js")

with open(bowls_file, "r", encoding="utf-8") as f:
    bowls_data = json.load(f)

with open(water_file, "r", encoding="utf-8") as f:
    water_data = json.load(f)

with open(app_js_file, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Başlığa BOWLS_DATA ve WATER_DATA ekle
datasets_code = f"""const BOWLS_DATA = {json.dumps(bowls_data.get("singing_bowls", []), ensure_ascii=False, indent=2)};

const WATER_DATA = {json.dumps(water_data, ensure_ascii=False, indent=2)};

"""

if "const BOWLS_DATA" not in content:
    content = content.replace("const ARCHITECTURE_DATA =", datasets_code + "const ARCHITECTURE_DATA =", 1)

# 2. Render çağrılarını DOMContentLoaded içine ekle
if "renderBowls();" not in content:
    content = content.replace("renderBiofield();", "renderBiofield();\n  renderBowls();\n  renderWater();", 1)

# 3. Fonksiyonları dosya sonuna ekle
v23_logic = """
// ==========================================
// 8. TITRESIM v2.3: TİBET ÇANAKLARI & SU HAFIZASI
// ==========================================
function renderBowls() {
  const container = document.getElementById("bowlsGrid");
  if (!container) return;
  container.innerHTML = "";

  BOWLS_DATA.forEach(bowl => {
    const card = document.createElement("div");
    card.className = "bowl-card";
    card.innerHTML = `
      <div class="bowl-header">
        <span class="bowl-title">${bowl.name}</span>
        <span class="bowl-freq-badge">${bowl.fundamental_hz} Hz (Nabız: ${bowl.beating_hz} Hz)</span>
      </div>
      <div class="bowl-alloy">👑 <strong>Çakra:</strong> ${bowl.chakra} • <strong>Alaşım:</strong> ${bowl.alloy}</div>
      <div class="bowl-faraday">🌊 <strong>Faraday Deseni:</strong> ${bowl.faraday_droplet_pattern}</div>
      <p style="font-size: 13px; color: #cbd5e1; margin-bottom: 8px;">${bowl.traditional_use}</p>
      <div style="font-size: 12px; color: #a7f3d0; margin-bottom: 12px;">✨ <strong>Şifa:</strong> ${bowl.healing_effects}</div>
      <div style="display: flex; justify-content: flex-end; gap: 8px;">
        <button class="btn btn-sm btn-outline-gold strike-bowl-btn">🔔 Tokmak Vuruşu (Struck)</button>
        <button class="btn btn-sm btn-outline-cyan sing-bowl-btn">🌀 Dönen Sürtünme (Singing Rim)</button>
      </div>
    `;

    card.querySelector(".strike-bowl-btn").addEventListener("click", () => {
      card.classList.add("playing");
      audio.playTone(bowl.fundamental_hz);
      if (cymaticsSim) cymaticsSim.setFrequency(bowl.fundamental_hz);
      setTimeout(() => card.classList.remove("playing"), 3000);
    });

    card.querySelector(".sing-bowl-btn").addEventListener("click", () => {
      card.classList.add("playing");
      audio.playTone(bowl.fundamental_hz);
      if (cymaticsSim) cymaticsSim.setFrequency(bowl.fundamental_hz);
      setTimeout(() => card.classList.remove("playing"), 5000);
    });

    container.appendChild(card);
  });
}

function renderWater() {
  const container = document.getElementById("waterGrid");
  if (!container) return;
  container.innerHTML = "";

  const freqs = WATER_DATA.acoustic_water_frequencies || [];
  freqs.forEach(wf => {
    const card = document.createElement("div");
    card.className = "water-card";
    card.innerHTML = `
      <div>
        <div style="display: flex; justify-content: space-between; align-items: flex-start;">
          <strong style="color: #f1f5f9; font-size: 14px;">${wf.name}</strong>
          <span class="water-freq">${wf.frequency_hz} Hz</span>
        </div>
        <div style="margin: 4px 0;"><span class="water-coherence-badge">Koherans: %${(wf.coherence_rating * 100).toFixed(0)}</span></div>
        <div style="font-size: 12px; color: #94a3b8; margin: 6px 0;">${wf.molecular_effect}</div>
        <div style="font-size: 11px; color: #38bdf8; margin-bottom: 8px;">❄️ ${wf.faraday_wave_symmetry}</div>
      </div>
      <div>
        <div style="font-size: 11px; color: #6ee7b7; margin-bottom: 10px;">🧬 ${wf.biological_benefit}</div>
        <button class="btn btn-sm btn-outline-cyan play-water-freq-btn" style="width: 100%;">💧 Hekzagonal Suyu Yapılandır</button>
      </div>
    `;

    card.querySelector(".play-water-freq-btn").addEventListener("click", () => {
      card.classList.add("playing");
      audio.playTone(wf.frequency_hz);
      if (cymaticsSim) cymaticsSim.setFrequency(wf.frequency_hz);
      setTimeout(() => card.classList.remove("playing"), 4000);
    });

    container.appendChild(card);
  });

  // Koherans Hesaplayıcı Event
  const calcBtn = document.getElementById("calcWaterCoherenceBtn");
  const inputEl = document.getElementById("waterFreqInput");
  const resultEl = document.getElementById("waterCoherenceResult");

  if (calcBtn && inputEl && resultEl) {
    calcBtn.onclick = () => {
      const f = parseFloat(inputEl.value) || 528.0;
      // Koherans hesapla
      const keyFreqs = [7.83, 136.1, 432.0, 528.0, 741.0, 963.0];
      let maxProx = 0.0;
      keyFreqs.forEach(kf => {
        let ratio = f / kf;
        while (ratio >= 2.0) ratio /= 2.0;
        while (ratio < 1.0 && ratio > 0.0) ratio *= 2.0;
        const d1 = Math.abs(ratio - 1.0);
        const d5 = Math.abs(ratio - 1.5);
        const dPhi = Math.abs(ratio - 1.618);
        const minD = Math.min(d1, d5, dPhi);
        const prox = Math.exp(-minD * 4.0);
        if (prox > maxProx) maxProx = prox;
      });
      const score = Math.min(1.0, Math.max(0.1, 0.5 + 0.48 * maxProx));
      const pct = (score * 100).toFixed(1);

      resultEl.innerText = `Koherans: %${pct} (${score > 0.85 ? "Altıgen Mükemmel H3O2" : "Orta Düzey Yapılanma"})`;
      audio.playTone(f);
      if (cymaticsSim) cymaticsSim.setFrequency(f);
    };
  }
}
"""

content = content + v23_logic

with open(app_js_file, "w", encoding="utf-8") as f:
    f.write(content)

print("web/app.js updated successfully for v2.3!")
