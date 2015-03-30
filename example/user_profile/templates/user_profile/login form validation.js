function c(){
    var f = document.forms["mf"];
    var a = f["input_login"].value;
    var b = f["input_password"].value;
    if (a == null || b == null || a == "" || b == "") {
        document.getElementById("back_end_error_message").hidden = true;
        document.getElementById("jsalert").hidden = false;
        return false;
    }
}
function h() {
    try {
        document.getElementById("back_end_error_message").hidden = true;
        document.getElementById("jsalert").hidden = true;
    } catch(e) {

    }
}