function processPost(title, date, body) {
    document.getElementById("blogPosts").innerHTML +=
        "<h1 class='text-center blogTitle'>" + title + "</h1>" +
        "<h4 class='date'>" + date + "</h4>" +
        "<p class='text-sm-left'>" + body + "</p>"+ "<hr>";

}
