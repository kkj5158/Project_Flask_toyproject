$(document).ready(function () {
  show_comment();
});
function save_comment() {


  let comment = $("#comment").val();
  let artist_id = $("#artist_id").text();

  // alert(artist_id)

  let formData = new FormData();

  formData.append("comment_give", comment);
  formData.append("artist_id", artist_id);

  // localhost:5000/artist/gusetbook 
  
  fetch("./guestbook", { method: "POST", body: formData })
    .then((res) => res.json())
    .then((data) => {
      //console.log(data)
      alert(data["msg"]);
      
      window.location.reload();
    });
}
function show_comment() {
  fetch("./guestbook")
    .then((res) => res.json())
    .then((data) => {
      let rows = data["result"];
      $("#comment-list").empty();
      rows.forEach((a) => {
        let comment = a["comment"];

        let temp_html = `<div class="card">
                          <div class="card-body">
                            <blockquote class="blockquote mb-0">
                              <p>${comment}</p>
                            </blockquote>
                          </div>
                        </div>`;
        $("#comment-list").append(temp_html);
      });
    });
}
