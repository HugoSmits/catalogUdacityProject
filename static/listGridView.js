// Get the elements with class="enumerate_column"
var elements = document.getElementsByClassName("enumerate_restaurant_column");
var elements1 = document.getElementsByClassName("enumerate_menu_column");

// Declare a loop variable
var i;
var k;

// List View
function listViewRestaurant() {
  for (i = 0; i < elements.length; i++) {
    elements[i].style.width = "100%";
  }
}

// Grid View
function gridViewRestaurant() {
  for (i = 0; i < elements.length; i++) {
    elements[i].style.width = "33%";
  }
}

// List View
function listViewMenu() {
  for (k = 0; k < elements1.length; k++) {
    elements1[k].style.width = "100%";
  }
}

// Grid View
function gridViewMenu() {
  for (k = 0; k < elements1.length; k++) {
    elements1[k].style.width = "33%";
  }
}