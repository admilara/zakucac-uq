// Plot frames (.wide-graph): grow to the height of the embedded plot file, so plots are not
// squeezed into a scroll box. Width/centring is CSS (style.css + custom-local.css).
// Runs on first load and after every GitBook in-page navigation.

function fitIframeHeight(iframe) {
    try {
        const doc = iframe.contentDocument || iframe.contentWindow.document;
        if (!doc || !doc.body) return;
        if (!doc.getElementById("uq-frame-style")) {
            // Match the site's typography for the plot files' own headings (figures untouched).
            const s = doc.createElement("style");
            s.id = "uq-frame-style";
            s.textContent =
                'body{margin:0;padding:14px 14px 6px;font-family:"IBM Plex Sans",system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;color:#18202b}' +
                'h1,h2,h3{font-size:1rem;font-weight:600;margin:4px 0 10px;line-height:1.3}';
            doc.head.appendChild(s);
        }
        iframe.style.height = doc.documentElement.scrollHeight + "px";
    } catch (e) { /* cross-origin: keep the height set in the page */ }
}

function setupGraphs() {
    const graphs = document.querySelectorAll(".wide-graph");
    if (!graphs.length) return;

    graphs.forEach(function (wideGraph) {
        const iframe = wideGraph.querySelector("iframe");
        if (!iframe || iframe.dataset.uqBound) return;
        iframe.dataset.uqBound = "1";
        iframe.addEventListener("load", function () {
            fitIframeHeight(iframe);
            // Plotly lays out after load; settle the height once more.
            setTimeout(function () { fitIframeHeight(iframe); }, 600);
        });
        // Already loaded (cached) before we attached the listener.
        if (iframe.contentDocument && iframe.contentDocument.readyState === "complete") fitIframeHeight(iframe);
    });
}

function wrapTables() {
    // Wide tables scroll sideways on small screens instead of overflowing the page.
    document.querySelectorAll(".markdown-section table").forEach(function (t) {
        if (t.parentElement.classList.contains("table-wrap")) return;
        const w = document.createElement("div");
        w.className = "table-wrap";
        t.parentNode.insertBefore(w, t);
        w.appendChild(t);
    });
}

function onPage() {
    wrapTables();
    setupGraphs();
}

// Plot heights change with frame width (Plotly is responsive), so re-fit after resizing.
let resizeTimer;
window.addEventListener("resize", function () {
    clearTimeout(resizeTimer);
    resizeTimer = setTimeout(function () {
        document.querySelectorAll(".wide-graph iframe").forEach(fitIframeHeight);
    }, 250);
});

// GitBook in-page navigation (gitbook.js must already be loaded; footer.html loads this after it).
if (typeof gitbook !== "undefined" && gitbook.events && gitbook.events.bind) {
    gitbook.events.bind("page.change", onPage);
}

if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", onPage);
} else {
    onPage();
}
window.addEventListener("load", setupGraphs);
