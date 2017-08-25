
var clockID;
var yourTimeZoneFrom = +1.00; //time zone value where you are at

var d = new Date();  
//get the timezone offset from local time in minutes
var tzDifference = yourTimeZoneFrom * 60 + d.getTimezoneOffset();
//convert the offset to milliseconds, add to targetTime, and make a new Date
var offset = tzDifference * 60  * 1000;

function UpdateClock() {
    var tDate = new Date(new Date().getTime()+offset);
    var in_hours = tDate.getHours()
    var in_minutes=tDate.getMinutes();
    var in_seconds= tDate.getSeconds();

var in_date = tDate.getDate();
var in_year = tDate.getFullYear();
var in_month   = (tDate.getMonth() + 1);

 



    if(in_minutes < 10)
        in_minutes = '0'+in_minutes;
    if(in_seconds<10)   
        in_seconds = '0'+in_seconds;
    if(in_hours<10) 
        in_hours = '0'+in_hours;

   document.getElementById('date_time').innerHTML = "  " 

+ in_date  + "-" 
+ in_month + "-" 
+ in_year + " " 
                   + in_hours + ":" 
                   + in_minutes + ":" 
                   + in_seconds;

}
function StartClock() {
   clockID = setInterval(UpdateClock, 500);
}

function KillClock() {
  clearTimeout(clockID);
}
window.onload=function() {
  StartClock();
}