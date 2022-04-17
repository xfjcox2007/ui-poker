$(function(){

	let list = $("#list")
	data.content.forEach(p => {
		let text = p.text
		p.highlight.forEach(t => {
			text = text.replace(t, "<u><b>$&</b></u>")
		})
		$("<li><h5></h5></li>").find("h5").html(text).end().appendTo(list)
	})

})
