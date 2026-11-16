# Mühitin Qurulması Qeydləri — Copilot Məhsuldarlıq Sprinti

## 1. Sistem və Avadanlıq İcmalı
- **Əməliyyat Sistemi:** Ubuntu 24.04 LTS / macOS / Windows 11
- **Terminal (Shell):** bash / zsh
- **Proqramlaşdırma Mühiti (Runtime):** Python 3.12.x / Node.js v20.x LTS

---

## 2. Əsas Alətlər və Versiyalar

| Kateqoriya | Alət | Versiya | Məqsəd |
| :--- | :--- | :--- | :--- |
| **IDE** | Visual Studio Code | `1.95.x` | Əsas proqramlaşdırma mühiti |
| **Süni İntellekt Köməkçisi** | GitHub Copilot | `1.245.x` | Sətirdaxili kod tamamlamaları (inline completions) |
| **AI Çat** | GitHub Copilot Chat | `0.22.x` | Çoxfayllı redaktə, refaktorinq və test generasiyası |
| **Vaxt İzləmə** | WakaTime (VS Code Ext) | `24.8.x` | Fayl və sessiya üzrə aktiv kodlaşdırma vaxtının ölçülməsi |
| **Test və Kod Əhatəsi** | `pytest` / `pytest-cov` | `8.3.x` / `6.0.x` | Vahid (unit) testlərin icrası və kod əhatəsinin ölçülməsi |
| **Kod Keyfiyyəti** | `ruff` / `radon` | `0.7.x` / `6.0.x` | Linting, PEP 8 uyğunluğu və tsiklomatik mürəkkəblik analizi |
| **Versiya Nəzarəti** | Git | `2.47.x` | Manual və AI dəstəkli həllərin müqayisəsi |

---

## 3. Addım-addım Quraşdırma Prosesi

### Addım 1: Repozitoriya və İş Sahəsinin Konfiqurasiyası
1. `holbertonschool-ai4devs` repozitoriyası hazırlandı və daxilində `copilot_productivity_sprint/` qovluğu yaradıldı.
2. Manual və AI dəstəkli sınaqları təmiz şəkildə müqayisə etmək üçün ayrıca iş axını quruldu.

### Addım 2: AI Kodlaşdırma Köməkçisinin Quraşdırılması
1. VS Code Extensions bölməsindən **GitHub Copilot** və **GitHub Copilot Chat** genişlənmələri quraşdırıldı.
2. Aktiv Copilot lisenziyası olan GitHub hesabı ilə sistemə giriş edildi.
3. VS Code-un aşağı sağ küncündəki status panelində Copilot ikonasının aktiv olduğu təsdiqləndi.
4. **Nəzarət Keçidi (Control Toggle):** Manual sınaq zamanı AI müdaxiləsini tam sıfırlamaq üçün status panelindən tamamlamaların söndürülməsi (`Disable Completions`) yoxlanıldı.

### Addım 3: Məhsuldarlıq və Keyfiyyət Ölçmə Alətlərinin Hazırlanması
1. **Vaxt İzləmə:** **WakaTime** genişlənməsi quraşdırıldı, API açarı qoşuldu və layihə üzrə vaxt qeydiyyatı aktivləşdirildi. Hər tapşırığın dəqiq vaxtını qeyd etmək üçün saniyəölçən (stopwatch) hazırlandı.
2. **Test və Metrika Alətləri:** Python virtual mühiti yaradıldı və ölçmə paketləri (`pytest`, `pytest-cov`, `radon`, `ruff`) quraşdırıldı.

---

## 4. Yoxlama Siyahısı (Verification)
- [x] `.py` və `.js` fayllarında Copilot tamamlamaları düzgün işləyir.
- [x] Baza (manual) tapşırıqları üçün Copilot tamamlamaları tam söndürülə bilir.
- [x] WakaTime redaktordakı aktivliyi düzgün qeydə alır.
- [x] Terminalda `pytest --cov` əmri xətasız icra olunur.
