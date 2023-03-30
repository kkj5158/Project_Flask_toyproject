window.addEventListener('load', () => {
  const forms = document.getElementsByClassName('validation-form');

  Array.prototype.filter.call(forms, (form) => {
    form.addEventListener('submit', function (event) {
      if (form.checkValidity() === false) {
        event.preventDefault();
        event.stopPropagation();
      }

      form.classList.add('was-validated');
    }, false);
  });
}, false);

//비밀번호랑 비밀번호확인이랑 같지 않을때

var password = document.getElementById("password")
  , passwordChk = document.getElementById("passwordChk");

function passwordChecking() {
  if (password.value != passwordChk.value) { // 만일 두 인풋 필드값이 같지 않을 경우
    // setCustomValidity의 값을 지정해 무조건 경고 표시가 나게 하고
    passwordChk.setCustomValidity("비밀번호가 일치하지않습니다.");
  }
  else {
    passwordChk.setCustomValidity('');
  }
}
password.onchange = passwordChecking;


//join.py로 입력한 데이터 보내기

function posting(){
  // alert('확인')

  let id = $("#id").val()
  let password = $('#password').val()
  let email = $('#email').val()
  let address = $('#address').val()
  let phone = $('#phone').val()
  let name = $('#name').val()

  let formData = new FormData();

  formData.append("id_give", id);
  formData.append("password_give", password);
  formData.append("email_give", email);
  formData.append("address_give", address);
  formData.append("phone_give", phone);
  formData.append("name", name);


  // alert("데이터전송1")

  // localhost:5000/login/join
  // ./->
  
  fetch('./join/register', { method: "POST", body: formData }).then((res) => res.json()).then((data) => {
    alert(data['msg'])

    window.location.href = '../'

})

  // alert("데이터전송2")


}