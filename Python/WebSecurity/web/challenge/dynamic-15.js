/*
 * Make titles dynamic
 *
 * P.s.: {{flag}}
 *
 */

const colors = ["black", "red", "green", "blue"];
var color_index = 0;

function change_titles_color() {
  color_index = (color_index + 1) % colors.length;
  for (let el of document.getElementsByTagName("h1")) {
    el.style.color = colors[color_index];
  }
  window.setTimeout(change_titles_color, 800);
}

window.setTimeout(change_titles_color, 800);
