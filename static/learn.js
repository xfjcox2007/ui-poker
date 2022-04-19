function toHtml(p){
	let text = p.text
	p.highlight.forEach(t => {
		text = text.replace(t, "<u><b>$&</b></u>")
	})
	return text
}
