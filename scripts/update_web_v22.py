# -*- coding: utf-8 -*-
"""
Inject architecture and biofield data, along with rendering logic, into web/app.js for v2.2
"""
import json
from pathlib import Path

arch_file = Path("data/architecture.json")
bio_file = Path("data/biofield.json")
app_js_file = Path("web/app.js")

with open(arch_file, "r", encoding="utf-8") as f:
    arch_data = json.load(f)

with open(bio_file, "r", encoding="utf-8") as f:
    bio_data = json.load(f)

with open(app_js_file, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Başlığa ARCHITECTURE_DATA ve BIOFIELD_DATA ekle
datasets_code = f"""const ARCHITECTURE_DATA = {json.dumps(arch_data.get("sacred_spaces", []), ensure_ascii=False, indent=2)};

const BIOFIELD_DATA = {json.dumps(bio_data, ensure_ascii=False, indent=2)};

"""

if "const ARCHITECTURE_DATA" not in content:
    content = content.replace("const ORGANS_DATA =", datasets_code + "const ORGANS_DATA =", 1)

# 2. Render çağrılarını DOMContentLoaded içine ekle
if "renderArchitecture();" not in content:
    content = content.replace("renderPhonetics();", "renderPhonetics();\n  renderArchitecture();\n  renderBiofield();", 1)

# 3. Fonksiyonları dosya sonuna ekle
v22_logic = """
// ==========================================
// 7. TITRESIM v2.2: KUTSAL MİMARİ & BİYOALAN
// ==========================================
function renderArchitecture() {
  const container = document.getElementById("architectureGrid");
  if (!container) return;
  container.innerHTML = "";

  ARCHITECTURE_DATA.forEach(sp => {
    const card = document.createElement("div");
    card.className = "architecture-card";
    card.innerHTML = `
      <div class="arch-header">
        <span class="arch-title">${sp.name}</span>
        <span class="arch-badge">RT60: ${sp.rt60_sec}s</span>
      </div>
      <div class="arch-meta">Mimar: ${sp.architect} • Hacim: ${Number(sp.volume_m3).toLocaleString()} m³</div>
      <div class="arch-res-info">
        🏺 <strong>Akustik Rezonatör:</strong> ${sp.resonators_count > 0 ? `${sp.resonators_count} adet ${sp.resonator_type} (${sp.resonator_frequency_hz} Hz)` : `${sp.resonator_type} (${sp.resonator_frequency_hz} Hz)`}
      </div>
      <p style="font-size: 13px; color: #cbd5e1; margin-bottom: 12px; line-height: 1.5;">${sp.description}</p>
      <div style="display: flex; justify-content: flex-end; gap: 8px;">
        <button class="btn btn-sm btn-outline-cyan play-arch-freq-btn">Mekân Frekansını Çal (${sp.resonator_frequency_hz} Hz)</button>
      </div>
    `;

    card.querySelector(".play-arch-freq-btn").addEventListener("click", () => {
      audio.playTone(sp.resonator_frequency_hz);
      if (cymaticsSim) cymaticsSim.setFrequency(sp.resonator_frequency_hz);
    });

    container.appendChild(card);
  });
}

function renderBiofield() {
  const container = document.getElementById("forksGrid");
  if (!container) return;
  container.innerHTML = "";

  const forks = BIOFIELD_DATA.tuning_forks || [];
  forks.forEach(fork => {
    const card = document.createElement("div");
    card.className = "fork-card";
    card.innerHTML = `
      <div>
        <div style="display: flex; justify-content: space-between; align-items: flex-start;">
          <strong style="color: #f1f5f9; font-size: 14px;">${fork.name}</strong>
          <span class="fork-freq">${fork.frequency} Hz</span>
        </div>
        <div style="font-size: 11px; color: #eab308; margin-top: 2px;">${fork.biofield_layer}</div>
        <div class="fork-desc">${fork.clinical_effects}</div>
      </div>
      <div>
        <div style="font-size: 11px; color: #64748b; margin-bottom: 8px;">Doku: ${fork.target_tissue}</div>
        <button class="btn btn-sm btn-outline strike-fork-btn" style="width: 100%;">🔱 Tokmakla Vur (Strike)</button>
      </div>
    `;

    card.querySelector(".strike-fork-btn").addEventListener("click", () => {
      card.classList.add("playing");
      audio.playTone(fork.frequency);
      if (cymaticsSim) cymaticsSim.setFrequency(fork.frequency);
      setTimeout(() => card.classList.remove("playing"), 3000);
    });

    container.appendChild(card);
  });
}

function playTeslaVortex(root) {
  const triads = (BIOFIELD_DATA.tesla_369_vortex && BIOFIELD_DATA.tesla_369_vortex.triads) || [];
  const triad = triads.find(t => t.root === root) || triads[2];
  if (!triad) return;

  // 3 frekansı sırayla veya akor şeklinde deneyimle
  audio.playTone(triad.frequencies[1]); // Merkez frekansı çal
  if (cymaticsSim) cymaticsSim.setFrequency(triad.frequencies[1]);

  alert(`⚡ Tesla Triad ${root} (${triad.name}) Aktif!\nFrekanslar: ${triad.frequencies.join(" Hz, ")} Hz\nEtki: ${triad.effects}`);
}

function playFibonacciScale() {
  const phi = 1.61803398875;
  const base = 432.0;
  audio.playTone(base);
  if (cymaticsSim) cymaticsSim.setFrequency(base);
  alert(`🌀 Fibonacci Altın Oran (Phi: ${phi}) Akordu Başlatıldı!\nTaban: ${base} Hz (Verdi A4). Fraktal spiralleşen biyo-harmonikler.`);
}
"""

content = content + v22_logic

with open(app_js_file, "w", encoding="utf-8") as f:
    f.write(content)

print("web/app.js updated successfully for v2.2!")
