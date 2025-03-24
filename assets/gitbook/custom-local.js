function adjustGraphWidth(wideGraph, bookBody) {
    if (!wideGraph || !bookBody) return;
    const availableWidth = bookBody.offsetWidth;
    wideGraph.style.maxWidth = availableWidth + "px";
    wideGraph.style.width = availableWidth + "px";
}

function waitForIframeAndShowGraph() {
    if (!document.querySelector(".wide-graph")) {
        console.log("[GRAPH DEBUG] No graph on this page. Skipping Setup.");
        return;
    }
    
    const maxAttempts = 30;
    let attempts = 0;

    function trySetup() {
        const wideGraph = document.querySelector(".wide-graph");
        const iframe = wideGraph?.querySelector("iframe");
        const bookBody = document.querySelector(".book-body");

        if (!wideGraph || !iframe || !bookBody) {
            if (attempts++ < maxAttempts) {
                return setTimeout(trySetup, 200);
            } else {
                return;
            }
        }

        wideGraph.style.visibility = "hidden";

        iframe.onload = function () {
            adjustGraphWidth(wideGraph, bookBody);
            wideGraph.style.visibility = "visible";
        };

        // Fallback in case iframe is cached and onload doesn't fire
        setTimeout(() => {
            if (wideGraph.style.visibility !== "visible") {
                adjustGraphWidth(wideGraph, bookBody);
                wideGraph.style.visibility = "visible";
            }
        }, 1200);

        // Adjust on resize
        window.addEventListener("resize", () => adjustGraphWidth(wideGraph, bookBody));

        // Observe sidebar changes
        const sidebar = document.querySelector(".book-summary");
        if (sidebar) {
            const observer = new MutationObserver(() => adjustGraphWidth(wideGraph, bookBody));
            observer.observe(sidebar, { attributes: true, childList: true, subtree: true });
        }
    }

    trySetup();
}

// ✅ Hook into GitBook navigation
if (typeof gitbook !== "undefined") {
    gitbook.events.bind("page.change", function () {
        waitForIframeAndShowGraph();
    });
}

// ✅ Also handle first-time full page load
window.addEventListener("load", function () {
    waitForIframeAndShowGraph();
});
