// 랭킹 끌고와서 그리기

$(document).ready(function () {
  fetch("/ranking")
    .then((res) => res.json())
    .then((data) => {
      // console.log(data);
      data.forEach((artist) => {
        let name = artist["name"];
        let rank = artist["ranking"];
        let fan = artist["fan"];
        let image_url = artist["image_url"];
        let average_point = artist["score"];
        let artist_id_num = artist["id"];

        $("#artists-ranking").append(`<tr>
                    <td><img src=${image_url} valign="middle"></td>
                    <th scope="row" valign="middle">${rank}</th>
                    <td class="namebox" id="${artist_id_num}" valign="middle">${name}</td>
                    <td valign="middle">${fan}명</td>
                    <td valign="middle">${average_point}점</td>
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

    const ourl = new URL(url)

    // console.log(ourl.origin)

    moveurl = ourl.origin + "/" + "artist?" + "artist_id_num=" + artist_id_num;

    // console.log(moveurl)

    window.location.href = moveurl;
  });
});
