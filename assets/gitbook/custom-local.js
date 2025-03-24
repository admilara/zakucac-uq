<script>
function adjustGraphWidth(wideGraph, bookBody) {
    if (!wideGraph || !bookBody) return;
    const availableWidth = bookBody.offsetWidth;
    wideGraph.style.maxWidth = availableWidth + "px";
    wideGraph.style.width = availableWidth + "px";
    console.log("[GRAPH DEBUG] Width adjusted to:", availableWidth);
}

function waitForIframeAndShowGraph() {
    const maxAttempts = 30;
    let attempts = 0;

    function trySetup() {
        const wideGraph = document.querySelector(".wide-graph");
        const iframe = wideGraph?.querySelector("iframe");
        const bookBody = document.querySelector(".book-body");

        if (!wideGraph || !iframe || !bookBody) {
            if (attempts++ < maxAttempts) {
                console.log("[GRAPH DEBUG] Waiting... attempt", attempts);
                return setTimeout(trySetup, 200);
            } else {
                console.warn("[GRAPH DEBUG] Gave up waiting for iframe.");
                return;
            }
        }

        wideGraph.style.visibility = "hidden";

        iframe.onload = function () {
            console.log("[GRAPH DEBUG] iframe onload triggered");
            adjustGraphWidth(wideGraph, bookBody);
            wideGraph.style.visibility = "visible";
        };

        // Fallback in case iframe is cached and onload doesn't fire
        setTimeout(() => {
            if (wideGraph.style.visibility !== "visible") {
                console.log("[GRAPH DEBUG] Fallback showing iframe");
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
        console.log("[GRAPH DEBUG] GitBook navigation detected");
        waitForIframeAndShowGraph();
    });
}

// ✅ Also handle first-time full page load
window.addEventListener("load", function () {
    console.log("[GRAPH DEBUG] window.load triggered");
    waitForIframeAndShowGraph();
});
</script>