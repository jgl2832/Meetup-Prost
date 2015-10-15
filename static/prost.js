function useLocation(query) {
	var showPosition = function (position) {
		var form = document.createElement('form');
		form.setAttribute("method", "post");
		form.setAttribute("action", "/"+query+"/");

		params = {'lat': position.coords.latitude, 'lon': position.coords.longitude, "useGeo": true}

		for(var key in params) {
			if(params.hasOwnProperty(key)) {
				var hiddenField = document.createElement('input');
				hiddenField.setAttribute("type", "hidden");
				hiddenField.setAttribute("name", key);
				hiddenField.setAttribute("value", params[key]);
				form.appendChild(hiddenField);
			}
		}
		document.body.appendChild(form);
		form.submit();
	};

	if (navigator.geolocation) {
		navigator.geolocation.getCurrentPosition(showPosition);
	}
}


