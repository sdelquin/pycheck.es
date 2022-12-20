document.addEventListener(
  "DOMContentLoaded",
  function () {
    documentReady();
  },
  false
);

function documentReady() {
  setupCodeBlocks();
  fixContentHeight();
  setAnchorTop();
  window.addEventListener("resize", fixContentHeight);
  document
    .querySelector("button.navbar-toggler")
    .addEventListener("click", () => setTimeout(fixContentHeight, 500));
}

function setupCodeBlocks() {
  document.querySelectorAll("div.code").forEach((el) => {
    el.innerHTML = el.innerHTML.trim();
    hljs.highlightElement(el);
    if (el.classList.contains("linenumbers")) {
      hljs.lineNumbersBlock(el);
    }
  });
}

function fixContentHeight() {
  let header = document.querySelector("header");
  let footer = document.querySelector("footer");
  let content = document.querySelector("div.content");
  const headerHeight = header.offsetHeight;
  console.log(headerHeight);
  const footerHeight = footer.offsetHeight;
  const contentHeight = window.innerHeight - headerHeight - footerHeight;
  content.style.minHeight = `${contentHeight}px`;
}

function setAnchorTop() {
  let header = document.querySelector("header");
  const headerHeight = header.offsetHeight;
  const finalGap = headerHeight + 20;
  document.querySelectorAll("a.anchor").forEach((el) => {
    el.style.top = `-${finalGap}px`;
  });
}
