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

      $(document).ready(function() {
        $(document).on("click", ".namebox", function(){
            // alert('클릭됨');

            var artist_id_num = $(this).attr("id");
            // alert(artist_id_num);

            var url = $(location).attr('href'); 

            // console.log(url)

            url = url + 'artist?' + 'artist_id_num=' + artist_id_num

            // console.log(url)

            window.location.href = url







        });
    });