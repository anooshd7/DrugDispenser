const firebaseConfig = {
  
};

// initialize firebase
firebase.initializeApp(firebaseConfig);

// reference your database
var contactFormDB = firebase.database().ref("Form");

document.getElementById("Form").addEventListener("submit", submitForm);

function submitForm(e) {
  e.preventDefault();

  var name = getElementVal("name");
  var drug1 = getElementVal("drug1");
  var drug2 = getElementVal("drug2");

  saveMessages(name, drug1, drug2);

  //   enable alert
  document.querySelector(".alert").style.display = "block";

  //   remove the alert
  setTimeout(() => {
    document.querySelector(".alert").style.display = "none";
  }, 4000);

  //   reset the form
  document.getElementById("Form").reset();
}

const saveMessages = (name, drug1, drug2) => {
  var newContactForm = contactFormDB.push();

  newContactForm.set({
    name: name,
    drug1: drug1,
    drug2: drug2,
  });
};

const getElementVal = (id) => {
  return document.getElementById(id).value;
};
