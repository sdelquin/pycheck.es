document.addEventListener(
  "DOMContentLoaded",
  function () {
    documentReady();
  },
  false
);

function documentReady() {
  document.querySelectorAll("div.code").forEach((el) => {
    el.innerHTML = el.innerHTML.trim();
    hljs.highlightElement(el);
    if (el.classList.contains("linenumbers")) {
      hljs.lineNumbersBlock(el);
    }
  });
}
