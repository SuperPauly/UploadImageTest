let uploadForm = document.getElementById("upload");
uploadForm.addEventListener("click", (e) => {
	e.preventDefault();
	const request = new Request(
		"up",
		{ headers: { 'X-CSRFToken': csrftoken } }
	);
	fetch(request, {
		method: 'POST',
		mode: 'same-origin'  // Do not send CSRF token to another domain.
	}).then(function (response) {
		console.log(response)
	});
});