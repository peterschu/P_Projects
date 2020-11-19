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
    var first_name = { a: document.getElementById('firstName').value};
    stringFormating(first_name);
    var last_name = { a: document.getElementById('lastName').value};
    stringFormating(last_name);
    var gradyear = document.getElementById('gradYear').value;
    var major = document.getElementById('major').value;
    var member_status = document.getElementById('memberStatus').value;
  //Uses the variables to place into firebase with the tag firtstname + lastname
    var data = {
      Email: email,
      Name: first_name.a + " " + last_name.a,
      Grad_Year: gradyear,
      Major: major,
      Member_Status: member_status
    }
    rootRef.push(data);
  })


//creates buttons the user will click on in order to pull found user info
const createBtn = (text = 'Empty') => {
  const btn = document.createElement('button');
  btn.id = text;
  btn.innerText = text;
  btn.setAttribute("onclick", "writeDataIn(this.id)");
  document.getElementById("addButton").appendChild(btn).className = "findButton newButton";
}

function errorBtn () {
  const btn = document.createElement('button');
  btn.innerText = "Could not find the user(s) entered.";
  document.getElementById("addButton").appendChild(btn).className = "errBtn newButton";
}




//beggining of the search function to take user input from HTML
function Search() {
  var classname = "findButton newButton";
  removeElementsByClass(classname);
  var classname = "errBtn newButton";
  removeElementsByClass(classname);
  rootRef.on('value', gotData, errData);
}

//recieves the data from the database
function gotData(data){
  var firstSearch = {a: document.getElementById('firstSearch').value};
  stringFormating(firstSearch);
  var lastSearch = {a: document.getElementById('lastSearch').value};
  stringFormating(lastSearch);
  var fullName = firstSearch.a + " " + lastSearch.a;
  var children = data.val();
  var none = true;
  var keys = Object.keys(children)
  for (var i = 0; i < keys.length; i++) {
    var k = keys[i];
    name = children[k].Name;
    if (name == fullName ) {
      none = false;
      createBtn(children[k].Email);
    }//end of if
  }//end of for
if (none == true) {
  errorBtn();
} //end of if
}//end of function gotData

function errData(err) {
  console.log("Error");
  console.log(err);
}

function removeElementsByClass(className){
    var elements = document.getElementsByClassName(className);
    while(elements.length > 0){
        elements[0].parentNode.removeChild(elements[0]);
    }
  }

function writeDataIn(clicked_id){
  rootRef.on('value', snapshot => {
    console.log(clicked_id);
    var data = snapshot.val();
    var children = data;
    var keys = Object.keys(children)

    for (var i = 0; i < keys.length; i++) {
      var k = keys[i];
      email = children[k].Email;
      if (email == clicked_id ) {
          var name = children[k].Name
          var gradyear = children[k].Grad_Year
          var major = children[k].Major
          var member_status = children[k].Member_Status
          document.getElementById('foundEmail').value = email;
          document.getElementById('foundName').value = name;
          document.getElementById('foundGrad').value = gradyear;
          document.getElementById('foundMajor').value = major;
          document.getElementById('foundStatus').value = member_status;
          return;
      }
    }
  });
}

function stringFormating(word) {
  word.a = word.a.trim();
  word.a = word.a.toLowerCase();
  word.a = word.a.charAt(0).toUpperCase() + word.a.slice(1);
}
