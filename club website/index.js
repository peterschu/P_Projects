firebase.auth().onAuthStateChanged(function(firebaseUser) {
  if (firebaseUser) {
    // User is signed in.
    if((window.location) =="file:///C:/Users/peter/Desktop/CPP/club%20website/scheyloggingIn.html"){window.location.href = "ScheyLoggedIn.html";}

  }
else{
  console.log("Login failed");
  if((window.location) =="file:///C:/Users/peter/Desktop/CPP/club%20website/ScheyLoggedIn.html"){window.location.href = "scheyloggingIn.html";}
}
});

const loginBtn = document.getElementById('login_button');
loginBtn.addEventListener('click', e => {
    //Get email and pass
    const email = document.getElementById("UserID").value;
    const pass = document.getElementById("PassID").value;
    firebase.auth().setPersistence(firebase.auth.Auth.Persistence.SESSION)
  .then(function() {
    // Existing and future Auth states are now persisted in the current
    // session only. Closing the window would clear any existing state even
    // if a user forgets to sign out.
    // ...
    // New sign-in will be persisted with session persistence.
    return firebase.auth().signInWithEmailAndPassword(email, pass);
  })
  .catch(function(error) {
    // Handle Errors here.
    var errorCode = error.code;
    var errorMessage = error.message;
    window.alert("Error :" + errorMessage);
  });
})

function logout(){
  firebase.auth().signOut();
}
