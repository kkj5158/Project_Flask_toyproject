// 랭킹 끌고와서 그리기

$(document).ready(function () {
  fetch("/ranking")
    .then((res) => res.json())
    .then((data) => {
      data.forEach((artist) => {
        let name = artist["name"];
        let rank = artist["rank"];
        let fan = artist["fan"];
        let image_url = artist["image_url"];
        let average_point = artist["average_point"];
        let artist_id_num = artist["artist_id_num"];

        $("#artists-ranking").append(`<tr>
                    <td><img src=${image_url}></td>
                    <th scope="row">${rank}</th>
                    <td class="namebox" id="${artist_id_num}">${name}</td>
                    <td>${fan}</td>
                    <td>${average_point}</td>
                    </tr>`);
      });
    });
});

// 클릭시에 아티스트 팬명록 페이지로의 이동

$(document).ready(function () {
  $(document).on("click", ".namebox", function () {
    // alert('클릭됨');

    var artist_id_num = $(this).attr("id");
    // alert(artist_id_num);

    var url = $(location).attr("href");

    // console.log(url)

    url = url + "artist?" + "artist_id_num=" + artist_id_num;

    // console.log(url)

    window.location.href = url;
  });
});

function includeNavbar() {
  var z, i, elmnt, file, xhttp;
  z = document.getElementsByTagName("*");
  for (i = 0; i < z.length; i++) {
    elmnt = z[i];
    /*search for elements with a certain atrribute:*/
    file = elmnt.getAttribute("w3-include-html");
    if (file) {
      /* Make an HTTP request using the attribute value as the file name: */
      xhttp = new XMLHttpRequest();
      xhttp.onreadystatechange = function () {
        if (this.readyState == 4) {
          if (this.status == 200) {
            elmnt.innerHTML = this.responseText;
          }
          if (this.status == 404) {
            elmnt.innerHTML = "Page not found.";
          }
          /* Remove the attribute, and call this function once more: */
          elmnt.removeAttribute("w3-include-html");
          includeHTML();
        }
      };
      xhttp.open("GET", file, true);
      xhttp.send();
      /* Exit the function: */
      return;
    }
  }
}
