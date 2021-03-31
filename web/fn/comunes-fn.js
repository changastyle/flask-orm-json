$scope.getInstalacionSegunURL = function (url, forzar) {
	$scope.cargando = false;

	$.ajax({
		url: "getInstalacionSegunURL/gInst",
		data: {
			url: url,
		},
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
