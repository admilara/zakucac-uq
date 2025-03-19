<script>
  function resizeIframe(iframe) {
      iframe.style.height = iframe.contentWindow.document.body.scrollHeight + 'px';
  }

  document.addEventListener("DOMContentLoaded", function () {
      var iframe = document.querySelector(".wide-graph iframe");
      if (iframe) {
          iframe.onload = function () {
              resizeIframe(iframe);
          };
      }
  });
</script>