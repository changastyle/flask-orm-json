$scope.getInstalacionSegunURL = function (url, forzar) {
	$scope.cargando = false;

	console.log("URL2:" + url)
	$.ajax({
		url: "getInstalacionSegunURL/" + url,
		beforeSend: function (xhr) {
			$scope.cargandoInstalacion = true;
		},
		success: function (resultado, textStatus, jqXHR) {
			$scope.instalacion = resultado;
			$scope.cargandoInstalacion = false;

			$scope.$evalAsync();
		},
	});
};
$scope.damePaginasSegunUsuario = function () {
	$scope.cargando = false;

	$.ajax({
		url: "damePaginasSegunUsuario",
		beforeSend: function (xhr) {
			$scope.cargandoPaginas = true;
		},
		success: function (resultado, textStatus, jqXHR) {
			$scope.arrPaginas = resultado;
			$scope.cargandoPaginas = false;

			$scope.$evalAsync();
		},
	});
};

[% include('fn/resize-listener.js') %]
[% include('fn/fn-desplazamiento-lateral-menus-mid.js') %]
[% include('fn/promos-fn.js') %]