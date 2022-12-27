document.addEventListener(
  "DOMContentLoaded",
  function () {
    documentReady();
  },
  false
);

function documentReady() {
  setupCodeBlocks();
  setupScrollToTop();
  fixContentHeight();
  setAnchorTop();
  window.addEventListener("resize", fixContentHeight);
  document
    .querySelector("button.navbar-toggler")
    .addEventListener("click", () => setTimeout(fixContentHeight, 500));
}
