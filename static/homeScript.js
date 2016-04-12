window.onload = function(){
    checkKeyDeadlines();
};

//Check if date of key deadlines has passed and update HTML and progress bar as required
function checkKeyDeadlines() {

    //If changing dates also change in HTML
    var keyDeadlines = [{event: "Deadline for abstracts", textDate: "16 Jan 2017"},
        {event: "Notification of acceptance", textDate: "15 Feb 2017"},
        {event: "Submission of full papers", textDate: "30 Jun 2017"},
        {event: "Registration closes", textDate: "1 Aug 2017"}];
    var months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];
    var currentDate = new Date();
    var day = currentDate.getDate();
    var month = currentDate.getMonth();
    var year = currentDate.getFullYear();
    var lastDeadline = -1;
    var lastDeadlineChanged = false;
    var newHTML = "<tr>";

    for (var index =  0; index < keyDeadlines.length; index++) {

        lastDeadlineChanged = false;

        var newDate = keyDeadlines[index].textDate.split(" ");

        if (newDate[2] < year) {
            lastDeadline = index;
            lastDeadlineChanged = true;
        }

        else if (newDate[2] == year) {
            if (months.indexOf(newDate[1]) < month) {
                lastDeadline = index;
                lastDeadlineChanged = true;
            }

            else if (months.indexOf(newDate[1]) == month) {
                if (newDate[0] < day) {
                    lastDeadline = index;
                    lastDeadlineChanged = true;
                }

            }

        }

        if(lastDeadlineChanged){
            newHTML += "<td><del>" + keyDeadlines[index].event + "</del><br><del>" + keyDeadlines[index].textDate + "</del></td>";
        }
        else{
            newHTML += "<td><p>" + keyDeadlines[index].event + "<br>" + keyDeadlines[index].textDate + "</p></td>";
        }

    }

    var newProgress = (lastDeadline + 1) * (100 / keyDeadlines.length);
    $("#datesProgress").css('width', newProgress +'%').attr('aria-valuenow', newProgress);

    newHTML += "</tr>";
    $("#keyDeadlinesTable").html(newHTML);

}


//Set the side navbar to stick when a certain point in the page is reached
$(function () {

    var sidebarNav = $("#sidebarNav");

    $('#sidebar').height(sidebarNav.height());

    sidebarNav.affix({
        offset: {top: (sidebarNav.offset().top - ($(window).height() / 3))}
    });
});

