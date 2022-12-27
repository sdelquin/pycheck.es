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
  const finalGap = headerHeight + 10;
  document.querySelectorAll("a.anchor").forEach((el) => {
    el.style.top = `-${finalGap}px`;
  });
}

function setupScrollToTop() {
  //Get the button
  let mybutton = document.getElementById("btn-back-to-top");

  // When the user scrolls down 20px from the top of the document, show the button
  window.onscroll = function () {
    scrollFunction();
  };

  function scrollFunction() {
    if (
      document.body.scrollTop > 20 ||
      document.documentElement.scrollTop > 20
    ) {
      mybutton.style.display = "block";
    } else {
      mybutton.style.display = "none";
    }
  }
  // When the user clicks on the button, scroll to the top of the document
  mybutton.addEventListener("click", backToTop);

  function backToTop() {
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
  }
}
