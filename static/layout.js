function populateDropDowns() {
    // read local JSON file in javascript
    $("#navbarDropdownMenuLinkContainer").empty();
    $("#navbarDropdownMenuLinkQuizContainer").empty();

    fetch("/fetchData")
        .then(function (response) {
            return response.json()
        })
        .then(function (data) {
            let quiz = data["quiz"]
            Object.keys(quiz).forEach(key => {
                $('#navbarDropdownMenuLinkQuizContainer').append(`<a class="dropdown-item ${quiz[key]['status']}" href="/quiz/${key}" >Question -  ${key}</a>`)
            })

            let learning = data["learningProgress"]
            console.log(learning)
            Object.keys(learning).forEach(key => {
                $('#navbarDropdownMenuLinkContainer').append(`<a class="dropdown-item" href="/learn/${key}">${learning[key]["topic"]}</a>`)
            })
        })

}

$(document).ready(function () {
    populateDropDowns()
});
