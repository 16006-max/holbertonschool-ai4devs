# Codebase Overview - Legacy jQuery (v1.x Core)

## Age
- **First Release:** August 2006 (by John Resig)
- **Legacy Branch Era:** 2006 – 2016 (jQuery 1.x series, maintained primarily for Internet Explorer 6/7/8 compatibility)
- **Status:** Legacy / End-of-Life for 1.x branch (superseded by modern 3.x/4.x branches and native DOM APIs)

## Size
- **Lines of Code (LOC):** ~10,000+ LOC (unminified core JavaScript source across modular `src/` files such as `core.js`, `ajax.js`, `event.js`, `manipulation.js`, and `sizzle.js`)
- **Primary Language:** JavaScript (ES3 / ES5 era syntax)

## Dependencies
- **Runtime Environment:** Legacy Web Browsers (Internet Explorer 6–11, early Firefox, Safari, Chrome)
- **Internal Selector Engine:** Sizzle CSS Selector Engine (embedded submodule)
- **Build & Tooling (Historical):** Grunt, Node.js (early versions), QUnit (for browser-based unit testing)
- **External Runtime Dependencies:** Zero external runtime libraries (monolithic self-contained script)

## Issues
- **Heavy Browser-Specific Workarounds:** Extensive conditional logic and feature-detection hacks (`jQuery.support`) written specifically to patch Internet Explorer 6–8 quirks, adding significant bloat and complexity.
- **Global Namespace Pollution:** Relies heavily on global `window.$` and `window.jQuery` bindings, creating collision risks with other legacy libraries (e.g., Prototype.js, MooTools).
- **Tightly Coupled Internal Modules:** Core DOM manipulation, event handling, animations, and AJAX subsystems share mutable internal state (`jQuery.cache` / `expando` properties), making isolated extraction or tree-shaking difficult.
- **Callback-Based Asynchronous Model:** Legacy `jQuery.Deferred` and AJAX callbacks predate native `Promise` and `async/await` standards, leading to nested callback chains ("callback hell") and non-standard error propagation.
- **DOM-Centric Architecture:** Direct imperative DOM mutation encourages tight coupling between UI state and presentation logic, conflicting with modern declarative component frameworks.
- **Security Exposure in Old Versions:** Unpatched 1.x versions contain known XSS vulnerabilities in HTML parsing (`jQuery.htmlPrefilter`) and prototype pollution vectors in `jQuery.extend()`.
