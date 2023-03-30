

// document.querySelector('.img__btn').addEventListener('click', function () {
//   document.querySelector('.cont').classList.toggle('s--signup');
// });




// !!! 로그아웃 버튼과의 연결필요. 

// 로그아웃은 내가 가지고 있는 토큰만 쿠키에서 없애면 됩니다.
function logout() {
  $.removeCookie('mytoken');
  alert('로그아웃!')
  window.location.href = '/login'
}



// ['쿠키'라는 개념에 대해 알아봅시다]
// 로그인을 구현하면, 반드시 쿠키라는 개념을 사용합니다.
// 페이지에 관계없이 브라우저에 임시로 저장되는 정보입니다. 키:밸류 형태(딕셔너리 형태)로 저장됩니다.
// 쿠키가 있기 때문에, 한번 로그인하면 네이버에서 다시 로그인할 필요가 없는 것입니다.
// 브라우저를 닫으면 자동 삭제되게 하거나, 일정 시간이 지나면 삭제되게 할 수 있습니다.
function login() {

  // alert("로그인 시도")

  $.ajax({
    type: "POST",
    url: "./login",
    data: { id_give: $('#userid').val(), pw_give: $('#userpw').val() },
    success: function (response) {
      if (response['result'] == 'success') {
        // alert("진입")
        // 로그인이 정상적으로 되면, 토큰을 받아옵니다.
        // 이 토큰을 mytoken이라는 키 값으로 쿠키에 저장합니다.
        $.cookie('mytoken', response['token']);

        alert('로그인 완료!')
        window.location.href = '../rank'
      } else {
        // 로그인이 안되면 에러메시지를 띄웁니다.
        alert(response['msg'])
      }
    }
  })
}

