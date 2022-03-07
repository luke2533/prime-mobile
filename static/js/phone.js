// var color = document.getElementById("phone-color").innerText;
// document.getElementById("phone-color").style.background = color;

var color_1 = $("#color-1").text();
$("#color-1").css("background-color", color_1);

var color_2 = $("#color-2").text();
$("#color-2").css("background-color", color_2);

var color_3 = $("#color-3").text();
$("#color-3").css("background-color", color_3);

var color_4 = $("#color-4").text();
$("#color-4").css("background-color", color_4);

$(".hide").hide()

// --------

// $(".phone-form").click(function() {
//     var phone = JSON.stringify({
//         color: this.dataset.color,
//         storage: parseInt(this.dataset.storage),
//         price: parseFloat(this.dataset.price),
//     });
//     console.log(phone)
// });