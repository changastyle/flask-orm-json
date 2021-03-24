$scope.arrProductos = [];
$scope.findUsuarios = function () {
	$scope.cargandoUsuarios = false;
	$.ajax({
		url: "../../findUsuarios",
		data: {},
		beforeSend: function (xhr) {
			$scope.cargandoUsuarios = true;
		},
		success: function (resultado, textStatus, jqXHR) {
			$scope.arrUsuarios = resultado;
			$scope.cargandoUsuarios = false;
			$scope.$evalAsync();
		},
	});
};
