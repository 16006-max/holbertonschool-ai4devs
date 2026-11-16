# Risk Assessment - Legacy jQuery (v1.x Core)

| Risk | Severity | Notes |
| :--- | :--- | :--- |
| **Cross-Site Scripting (XSS) in HTML Parsing** | High | Legacy `jQuery.htmlPrefilter()` and `$()` string parsing allow malicious script injection when untrusted HTML strings are passed (e.g., CVE-2020-11022, CVE-2020-11023). |
| **Prototype Pollution in `jQuery.extend()`** | High | Deep merging untrusted objects containing `__proto__` or `constructor` keys allows attackers to pollute `Object.prototype` across the entire application (CVE-2019-11358). |
| **Memory Leaks via Detached DOM Elements** | High | Internal `jQuery.cache` and expando properties retain references to DOM nodes and event handlers if elements are removed via native `innerHTML` or `removeChild()` instead of `.remove()`. |
| **Tight Coupling Across Internal Subsystems** | Medium | Core DOM manipulation, event delegation, animations, and AJAX modules share mutable internal state, preventing tree-shaking and making isolated refactoring risky. |
| **Non-Standard `jQuery.Deferred` Error Handling** | Medium | Pre-3.0 `Deferred` objects swallow or inconsistently propagate synchronous exceptions compared to standard Promises/A+, leading to silent failures in async workflows. |
| **Global Namespace Pollution (`window.$` / `window.jQuery`)** | Medium | Relying on global variables creates collision risks with other legacy libraries or multiple jQuery versions on the same page unless `noConflict()` is strictly enforced. |
| **Dead Code from IE6–8 Browser Workarounds** | Low | Extensive `jQuery.support` feature-detection hacks for obsolete browsers inflate bundle size and increase cognitive load for maintainers. |
| **Lack of Modern Automated Regression Coverage** | Low | Legacy QUnit browser-based test suites lack modern CI/CD integration, headless coverage metrics, and automated security fuzzing. |
