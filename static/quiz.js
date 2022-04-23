function updateQuizLogs(selectedOption) {
    console.log("here")
    let question = window.location.href.split("/").pop()
    $.ajax({
        type: "POST",
        url: "/updateQuiz",
        dataType: "json",
        contentType: "application/json; charset=utf-8",
        data: JSON.stringify({selection: selectedOption, page: question}),
        success: function (result) {
            console.log("success::", result)
            populateDropDowns()
        },
        error: function (request, status, error) {
            console.log("Error");
            console.log(request)
            console.log(status)
            console.log(error)
        }
    });
}


$(document).ready(function () {
    if (question.type === 'mcq') {
        let selectedOption = 0;
        $('.mcq .choice:nth-child(1)').attr('selected', 'true');

        $('.choice').click(function (e) {
            selectedOption = $(this).index();
            deselectAll();
            console.log(selectedOption);
            updateQuizLogs(selectedOption)
            $(`.mcq .choice:nth-child(${selectedOption + 1})`).attr('selected', 'true');
        });

        function deselectAll() {
            for (let i = 0; i < question.options.length; i++) {
                $(`.mcq .choice`).removeAttr('selected');
            }
        }
    } else if (question.type === 'arrange') {
        let options = question.options;
        let order = [...Array(options.length).keys()]

        for (let option of options) {
            $('.arrange').append(`<div class="arrange-option">${option}</div>`)
        }
    }
});
