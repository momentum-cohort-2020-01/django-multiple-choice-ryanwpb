document.querySelector("code").addEventListener("click", async event => {
  if (!navigator.clipboard) {
    // Clipboard API not available
    return;
  }
  const text = event.target.innerText;
  try {
    await navigator.clipboard.writeText(text);
    event.target.textContent = "Copied to clipboard";
  } catch (err) {
    console.error("Failed to copy!", err);
  }
});

// Fetch Request here...
let searchForm = document.querySelector("#search-form");

searchForm.addEventListener("submit", function(e) {
  e.preventDefault();
  let searchTerm = document.querySelector("#search").value;
  fetch(`/search/?q=${searchTerm}`)
    .then(response => {
      return response.json();
    })
    .then(data => {
      document.querySelector(".container").innerHTML = "";
      console.log(data.results);
      for (const [id, snippet] of Object.entries(data.results)) {
        let snippetHtml = `<a class="snippet-link" href="/snippets/${id}">
        <div class="snippet">
          <h4 class="snippet-title" id="${id}">${snippet.title}</h4>
          <p class="">${snippet.description}</p>
<pre>
<code id="snip${id}">
</code>
</pre>
        </div>
      </a>`;
        document.querySelector(".container").innerHTML += snippetHtml;
        document.querySelector(`#snip${id}`).textContent = snippet.code_block;
      }
      // reloadHighlight();
      document.querySelectorAll("pre > code").forEach(function(el) {
        hljs.highlightBlock(el);
      });
    });
});

function reloadHighlight() {
  const script = document.querySelector("#highlight");
  script.remove();
  const newScript = document.createElement("script");
  newScript.id = "highlight";
  newScript.src =
    "//cdnjs.cloudflare.com/ajax/libs/highlight.js/9.18.1/highlight.min.js";
  document.querySelector("head").appendChild(newScript);
}
