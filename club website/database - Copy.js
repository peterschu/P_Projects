// rules_version = '2';
// service cloud.firestore {
//   match /databases/{database}/documents {
//     match /{document=**} {
//       allow read, write: if
//           request.time < timestamp.date(2020, 3, 21);
//     }
//   }
// }}
var database = firebase.database();
const addMember = document.getElementById('addMember');
var rootRef = database.ref('Users');

addMember.addEventListener('click', e => {
  //Variables for storing data from the HTML
    var email = document.getElementById('email').value;
    var first_name = document.getElementById('firstName').value;
    var last_name = document.getElementById('lastName').value;
    var gradyear = document.getElementById('gradYear').value;
    var major = document.getElementById('major').value;
    var member_status = document.getElementById('memberStatus').value;
  //Uses the variables to place into firebase with the tag firtstname + lastname
    rootRef.child(first_name + " " + last_name).set({
      Email: email,
      Name: first_name + " " + last_name,
      Grad_Year: gradyear,
      Major: major,
      Member_Status: member_status
    });
  })

rootRef.orderByChild('First_Name')

const createBtn = (text = 'Empty') => {
  const btn = document.createElement('button');
  btn.innerText = text;
  document.getElementById("addButton").appendChild(btn).className ="ghostFormat";
}




// const Search = document.getElementById('Search');
//
function Search() {
  var firstSearch = document.getElementById('firstSearch').value;
  var lastSearch = document.getElementById('lastSearch').value;

  rootRef.orderByChild("Name").equalTo(firstSearch + " " + lastSearch).on('value', snapshot => {
    var Users = snapshot.val();
    console.log(Users);
    console.log(Users.Email);
    createBtn(snapshot.val().Email);
  });
}

// Search.addEventListener('click', e => {
//   rootRef.orderByChild('First_Name').equalTo("lemon").on('value', snapshot => {
//       console.log(snapshot.val());
//
//     });
//   })

  // function snapshot(data){
  //   console.log(data.val());
  // }
  //
  // function errData(err) {
  //   console.log("Error!");
  //   console.log(err);
  // }
