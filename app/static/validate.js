function checkPassword() {
    var prev = document.getElementById('password').value;
      var rePass = document.getElementById('confirmPassword').value;
      if (prev !== rePass) {
      document.getElementById('confirmPassword').style.color  = 'red'
     
    }
    else {
        document.getElementById('confirmPassword').style.color  = 'black'
        
    }
  }